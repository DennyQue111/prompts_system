#!/usr/bin/env python3
"""Deterministic structural audit for Higgsfield-style cinematic prompts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SECTION_PATTERNS = {
    "output_contract": r"(?im)^\s*(?:duration|aspect ratio|mode|output contract)\s*:",
    "reference_authority": r"(?im)^\s*(?:references?|reference authority|参考(?:图|资产|权限))\s*:",
    "identity_lock": r"(?im)^\s*(?:characters?|identity hold|identity lock|character locked|人物锁定)\s*(?:\([^\n]*\))?\s*:",
    "location_hold": r"(?im)^\s*(?:location|environment|scene setup|location hold|场景锁定|环境)\s*(?:\([^\n]*\))?\s*:",
    "prop_lock": r"(?im)^\s*(?:props?|the [^\n:]+|prop lock|道具锁定)\s*(?:\([^\n]*\))?\s*:",
    "action": r"(?im)^\s*(?:action|multi-shot sequence|shots?|blocks?|分镜|动作)\b",
    "positive_locks": r"(?im)^\s*(?:positive locks?|strict|key rules?|硬规则|正向锁)\s*:",
    "continuity": r"(?im)^\s*(?:continuity|连续性)\s*:",
    "final_frame": r"(?im)^\s*(?:final frame|end state|最终帧|尾帧)\s*:",
    "audio": r"(?im)(?:^|\b)(?:audio(?:\s+bed(?:\s*\([^\n)]*\))?)?|dialogue|音频|对白)\s*:",
    "negatives": r"(?im)^\s*(?:negative(?:s| prompt)?|负面(?:提示词|约束)?)\s*:",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def find_first(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else None


def detect_metadata(text: str) -> dict[str, Any]:
    duration = find_first(r"\bDuration\s*:\s*([0-9]+(?:\.[0-9]+)?)\s*(?:seconds?|s)\b", text)
    aspect_ratio = find_first(r"\bAspect\s+ratio\s*:\s*([0-9.]+\s*:\s*[0-9.]+)", text)
    mode = find_first(r"\bMode\s*:\s*([A-Za-z0-9_-]+)", text)
    fps_values = sorted({int(value) for value in re.findall(r"(?i)\b(24|25|30|48|50|60|120)\s*fps\b", text)})
    declared_blocks = find_first(r"\b([0-9]+)\s+blocks?\b", text)
    declared_shots = find_first(r"\b([0-9]+)\s+(?:shots?|cuts?)\b", text)
    return {
        "duration_seconds": float(duration) if duration else None,
        "aspect_ratio": aspect_ratio.replace(" ", "") if aspect_ratio else None,
        "mode": mode,
        "fps_values": fps_values,
        "declared_blocks": int(declared_blocks) if declared_blocks else None,
        "declared_shots": int(declared_shots) if declared_shots else None,
    }


def extract_numbered_units(text: str) -> dict[str, list[int]]:
    blocks = sorted({int(value) for value in re.findall(r"(?im)^\s*(?:\[\s*)?BLOCK\s+([0-9]+)\b", text)})
    shots = sorted({int(value) for value in re.findall(r"(?im)^\s*(?:\[\s*)?SHOT\s+([0-9]+)\b", text)})
    cuts = len(re.findall(r"(?im)^\s*\[?CUT\]?\s*$", text))
    return {"blocks": blocks, "shots": shots, "explicit_cut_markers": cuts}


def extract_timed_ranges(text: str) -> list[dict[str, Any]]:
    ranges: list[dict[str, Any]] = []
    pattern = re.compile(
        r"(?im)^\s*(?:\[\s*)?(BLOCK|SHOT|CUT)\s*([0-9]+)?[^\n]*?"
        r"(?:\(|/|—|-)\s*([0-9]+(?:\.[0-9]+)?)\s*[–-]\s*([0-9]+(?:\.[0-9]+)?)\s*s"
    )
    for match in pattern.finditer(text):
        start = float(match.group(3))
        end = float(match.group(4))
        ranges.append({
            "kind": match.group(1).upper(),
            "id": int(match.group(2)) if match.group(2) else None,
            "start": start,
            "end": end,
            "duration": round(end - start, 3),
        })
    return ranges


def issue(code: str, severity: str, message: str, evidence: str) -> dict[str, str]:
    return {"code": code, "severity": severity, "message": message, "evidence": evidence}


def audit_text(text: str, source: Path, max_unit_seconds: float | None) -> dict[str, Any]:
    metadata = detect_metadata(text)
    units = extract_numbered_units(text)
    ranges = extract_timed_ranges(text)
    sections = {name: bool(re.search(pattern, text)) for name, pattern in SECTION_PATTERNS.items()}
    reference_tokens = sorted(set(re.findall(r"<<<[^>]+>>>|@[\w\u4e00-\u9fff]+\d+", text)))
    issues: list[dict[str, str]] = []

    if not sections["action"] and not units["blocks"] and not units["shots"]:
        issues.append(issue("STRUCT_NO_ACTION", "error", "No ACTION/SHOT/BLOCK structure detected.", "No action heading or numbered unit found."))
    for key, code, label in (
        ("continuity", "STRUCT_NO_CONTINUITY", "continuity handoff"),
        ("final_frame", "STRUCT_NO_FINAL_FRAME", "final-frame state"),
        ("audio", "STRUCT_NO_AUDIO", "audio policy"),
        ("positive_locks", "STRUCT_NO_POSITIVE_LOCKS", "positive locks"),
    ):
        if not sections[key]:
            issues.append(issue(code, "warning", f"No explicit {label} section detected.", f"section.{key}=false"))

    if reference_tokens and not sections["reference_authority"]:
        issues.append(issue(
            "REF_NO_AUTHORITY",
            "warning",
            "Reference tags exist, but their control boundaries are not declared.",
            f"Detected {len(reference_tokens)} unique reference tag(s).",
        ))

    if len(metadata["fps_values"]) > 1:
        issues.append(issue(
            "TECH_MULTI_FPS",
            "error",
            "Multiple delivery frame rates are declared.",
            f"fps_values={metadata['fps_values']}",
        ))

    lower = text.lower()
    if ("strongest possible handheld" in lower or "heavy aggressive handheld" in lower) and "no jitter" in lower:
        issues.append(issue(
            "CAMERA_HANDHELD_JITTER",
            "warning",
            "Organic handheld and unwanted digital jitter are not distinguished.",
            "Prompt contains strong handheld language and 'no jitter'.",
        ))
    if "heavy aggressive handheld throughout" in lower and ("mostly still" in lower or "camera stays locked" in lower or "camera is locked" in lower):
        if "exception" not in lower and "override" not in lower:
            issues.append(issue(
                "CAMERA_GLOBAL_LOCAL_CONFLICT",
                "error",
                "Global aggressive handheld conflicts with a locked/mostly-still local shot without an explicit override.",
                "Found global handheld rule and local still/locked rule.",
            ))
    if "no floating props" in lower and re.search(r"\b(float|floating|floats|hover|hovering|magnetic board)\b", lower):
        if "no unintended floating props" not in lower and "only" not in lower:
            issues.append(issue(
                "PHYSICS_FLOAT_EXCEPTION",
                "error",
                "A required floating/hovering object conflicts with 'No floating props'.",
                "Floating action and blanket negative both detected.",
            ))
    if "artificial lightning" in lower:
        issues.append(issue(
            "LIGHTING_TYPO",
            "warning",
            "Likely typo: 'artificial lightning' should be 'artificial lighting'.",
            "Exact phrase 'artificial lightning' detected.",
        ))
    if "pixel-for-pixel" in lower:
        issues.append(issue(
            "REF_PIXEL_PROMISE",
            "warning",
            "Pixel-for-pixel generative fidelity is not reliably enforceable; use a plate/composite for exact graphics.",
            "Exact phrase 'pixel-for-pixel' detected.",
        ))
    if "every person moving from frame one" in lower and re.search(r"\b(hold|stillness|locked|empty hall|empty space)\b", lower):
        issues.append(issue(
            "ACTING_MOVEMENT_HOLD",
            "warning",
            "Mandatory movement from frame one may conflict with held stillness or an empty-frame ending.",
            "Movement rule and hold/still/empty language both detected.",
        ))
    if "completely out of focus" in lower and ("rack focus" in lower or "autofocus" in lower):
        if "no rack focus" not in lower and "no autofocus" not in lower:
            issues.append(issue(
                "FOCUS_BACKGROUND_CONFLICT",
                "error",
                "Permanent background defocus conflicts with rack-focus/autofocus behavior.",
                "Both permanent defocus and focus-shift language detected.",
            ))
    positive_music = re.search(
        r"\b(?:background music|bgm|music starts|music plays|with (?:a )?music|score (?:starts|plays|swells|builds))\b",
        lower,
    )
    if "no music" in lower and positive_music:
        issues.append(issue(
            "AUDIO_MUSIC_CONFLICT",
            "error",
            "The prompt both forbids and requests music/score.",
            "'no music' plus music/BGM/score language detected.",
        ))

    actual_block_count = len(units["blocks"])
    if metadata["declared_blocks"] is not None and actual_block_count and metadata["declared_blocks"] != actual_block_count:
        issues.append(issue(
            "NUMBER_BLOCK_COUNT",
            "error",
            "Declared block count does not match detected block headings.",
            f"declared={metadata['declared_blocks']}, detected={actual_block_count}, ids={units['blocks']}",
        ))
    if units["blocks"]:
        expected = list(range(min(units["blocks"]), max(units["blocks"]) + 1))
        if units["blocks"] != expected:
            issues.append(issue(
                "NUMBER_BLOCK_GAP",
                "error",
                "Block numbering contains gaps.",
                f"ids={units['blocks']}, expected={expected}",
            ))
        referenced_ranges = re.findall(r"(?i)BLOCKS?\s+([0-9]+)\s*[–-]\s*([0-9]+)", text)
        max_defined = max(units["blocks"])
        for start_text, end_text in referenced_ranges:
            if int(end_text) > max_defined:
                issues.append(issue(
                    "NUMBER_BLOCK_REFERENCE",
                    "error",
                    "A block range references an undefined block.",
                    f"range={start_text}-{end_text}, max_defined={max_defined}",
                ))
                break

    if ranges:
        ordered = sorted(ranges, key=lambda item: item["start"])
        for previous, current in zip(ordered, ordered[1:]):
            if current["start"] < previous["end"] - 1e-6:
                issues.append(issue(
                    "TIME_OVERLAP",
                    "error",
                    "Timed blocks overlap.",
                    f"previous={previous}, current={current}",
                ))
                break
            if current["start"] > previous["end"] + 0.05:
                issues.append(issue(
                    "TIME_GAP",
                    "warning",
                    "Timed blocks contain an undeclared gap.",
                    f"previous_end={previous['end']}, current_start={current['start']}",
                ))
                break
        if metadata["duration_seconds"] is not None:
            final_end = max(item["end"] for item in ranges)
            if abs(final_end - metadata["duration_seconds"]) > 0.05:
                issues.append(issue(
                    "TIME_DURATION_MISMATCH",
                    "error",
                    "Timed blocks do not end at the declared duration.",
                    f"declared={metadata['duration_seconds']}, final_end={final_end}",
                ))
        if max_unit_seconds is not None:
            oversized = [item for item in ranges if item["duration"] > max_unit_seconds + 1e-6]
            if oversized:
                issues.append(issue(
                    "CAPACITY_UNIT_TOO_LONG",
                    "error",
                    "One or more timed units exceed the supplied generation-unit limit.",
                    f"limit={max_unit_seconds}, oversized={oversized}",
                ))

    segment_headings = list(re.finditer(r"(?im)^\s*(?:SHOT|BLOCK)\s+[0-9]+[^\n]*", text))
    dense_segments: list[dict[str, Any]] = []
    for index, heading in enumerate(segment_headings):
        end = segment_headings[index + 1].start() if index + 1 < len(segment_headings) else len(text)
        segment = text[heading.end():end]
        words = len(re.findall(r"\b\w+\b", segment))
        transitions = len(re.findall(r"(?i)\b(?:then|suddenly|immediately|finally|after|before|but then)\b|→", segment))
        if words > 550 or transitions > 14:
            dense_segments.append({"heading": heading.group(0).strip(), "words": words, "transition_markers": transitions})
    if dense_segments:
        issues.append(issue(
            "CAPACITY_DENSE_SEGMENT",
            "warning",
            "One or more shot/block descriptions are unusually dense and need semantic capacity review.",
            json.dumps(dense_segments[:8], ensure_ascii=False),
        ))

    severity_counts = {level: sum(1 for item in issues if item["severity"] == level) for level in ("error", "warning")}
    status = "REWRITE_REQUIRED" if severity_counts["error"] else ("NEEDS_REVIEW" if severity_counts["warning"] else "PASS")
    return {
        "schema_version": "higgsfield-prompt-audit.v1",
        "source": str(source.resolve()),
        "source_sha256": sha256_text(text),
        "status": status,
        "metadata": metadata,
        "metrics": {
            "characters": len(text),
            "words": len(re.findall(r"\b\w+\b", text)),
            "reference_token_count": len(reference_tokens),
            "reference_tokens": reference_tokens,
            "units": units,
            "timed_ranges": ranges,
        },
        "sections": sections,
        "severity_counts": severity_counts,
        "issues": issues,
        "semantic_review_required": [
            "reference-image fidelity and authority",
            "character/action causality",
            "physical feasibility and safe contact",
            "shot visibility and emotional readability",
            "final-frame continuity into the next generation unit",
        ],
    }


def build_bundle(audit: dict[str, Any], source: Path) -> dict[str, dict[str, Any]]:
    now = datetime.now(timezone.utc).isoformat()
    issues = audit["issues"]
    error_codes = [item["code"] for item in issues if item["severity"] == "error"]
    warning_codes = [item["code"] for item in issues if item["severity"] == "warning"]
    request_contract = {
        "schema_version": "higgsfield-prompt-request.v1",
        "created_at": now,
        "source": str(source.resolve()),
        "source_sha256": audit["source_sha256"],
        "detected_output": audit["metadata"],
        "scope": "audit existing cinematic prompt",
        "protected_boundaries": ["source file is read-only", "no external generation or upload"],
        "stop_rules": ["reference conflict requiring user choice", "unsafe overwrite", "unresolvable duration conflict"],
    }
    action_plan = {
        "schema_version": "higgsfield-prompt-action-plan.v1",
        "status": "repair" if error_codes else ("review" if warning_codes else "accept"),
        "actions": [
            {"action": "repair", "code": code, "reason": "deterministic audit error"} for code in error_codes
        ] + [
            {"action": "review", "code": code, "reason": "deterministic audit warning or semantic decision"} for code in warning_codes
        ] + [
            {"action": "semantic_review", "item": item} for item in audit["semantic_review_required"]
        ],
    }
    final_report = {
        "schema_version": "higgsfield-prompt-final-report.v1",
        "status": audit["status"],
        "error_codes": error_codes,
        "warning_codes": warning_codes,
        "deterministic_checks_complete": True,
        "semantic_review_complete": False,
        "completion_claim": "Structural audit only; generated video has not been tested.",
    }
    requirement_audit = {
        "schema_version": "higgsfield-prompt-requirement-audit.v1",
        "requirements": [
            {"requirement": name, "status": "present" if present else "missing", "evidence": f"inspection_report.sections.{name}"}
            for name, present in audit["sections"].items()
        ],
        "unverified": audit["semantic_review_required"],
    }
    return {
        "request_contract.json": request_contract,
        "inspection_report.json": audit,
        "action_plan.json": action_plan,
        "final_report.json": final_report,
        "requirement_audit.json": requirement_audit,
    }


def write_bundle(output_dir: Path, bundle: dict[str, dict[str, Any]], force: bool) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    targets = [output_dir / name for name in bundle]
    targets.append(output_dir / "manifest.json")
    existing = [str(path) for path in targets if path.exists()]
    if existing and not force:
        raise FileExistsError("Refusing to overwrite existing audit artifacts: " + ", ".join(existing))

    for name, payload in bundle.items():
        (output_dir / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "schema_version": "higgsfield-prompt-manifest.v1",
        "files": [
            {"path": name, "sha256": hashlib.sha256((output_dir / name).read_bytes()).hexdigest()}
            for name in bundle
        ],
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit a Higgsfield-style cinematic AI-video prompt and optionally write a JSON evidence bundle.")
    parser.add_argument("input", type=Path, help="UTF-8 prompt text file")
    parser.add_argument("--output-dir", type=Path, help="Write request/inspection/plan/manifest/final/audit JSON files")
    parser.add_argument("--max-unit-seconds", type=float, help="Optional active model generation-unit limit")
    parser.add_argument("--force", action="store_true", help="Overwrite existing audit artifacts in the exact output directory")
    parser.add_argument("--strict", action="store_true", help="Exit 2 when deterministic errors are found")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        print(json.dumps({"status": "BLOCKED", "error": f"Input file not found: {args.input}"}, ensure_ascii=False), file=sys.stderr)
        return 2
    try:
        text = args.input.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        print(json.dumps({"status": "BLOCKED", "error": f"Input is not valid UTF-8: {exc}"}, ensure_ascii=False), file=sys.stderr)
        return 2
    if not text.strip():
        print(json.dumps({"status": "BLOCKED", "error": "Input prompt is empty."}, ensure_ascii=False), file=sys.stderr)
        return 2

    audit = audit_text(text, args.input, args.max_unit_seconds)
    bundle = build_bundle(audit, args.input)
    if args.output_dir:
        try:
            write_bundle(args.output_dir, bundle, args.force)
        except OSError as exc:
            print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            return 2
    print(json.dumps(audit, ensure_ascii=False, indent=2))
    if args.strict and audit["severity_counts"]["error"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
