# Higgsfield 提示词状态机架构

## 目录

1. 核心模型
2. 推荐顺序
3. 字段规范
4. 镜头模板
5. 生成单元容量
6. 参考权限
7. 表演与物理语言

## 1. 核心模型

把提示词视为四类指令：

```text
STATE       固定状态：人物、场景、道具、当前伤势和位置
TRANSITION  状态转换：动作、反应、切镜、离场
INVARIANT   持续不变量：身份、光线、悬浮高度、景深、禁区
FINAL STATE 终止状态：尾帧构图、姿态、道具、焦点和下一镜入口
```

每条重要要求必须能归入其中一类。无法归类的形容词通常是低优先级修辞。

## 2. 推荐顺序

```text
[OUTPUT CONTRACT]
[REFERENCE AUTHORITY]
[IDENTITY / LOCATION / PROP LOCKS]
[INITIAL CONTINUITY STATE]
[DRAMATIC PURPOSE]
[GLOBAL CINEMATIC PROTOCOL]
[ACTION BLOCKS / SHOTS]
[POSITIVE LOCKS]
[CONTINUITY]
[FINAL FRAME]
[AUDIO]
[NEGATIVES]
```

精确参考和不可变状态应前置。全局风格保持紧凑，不要让导演名与画质词压过身份和动作。

## 3. 字段规范

### OUTPUT CONTRACT

```text
Duration:
Aspect ratio:
Mode: R2V | I2V | T2V | storyboard
Generation-unit limit:
Timing policy: exact | ordered | adaptive
Number of shots/blocks:
Dialogue policy:
```

### REFERENCE AUTHORITY

为每个参考资产写：

```text
asset_id
asset_type
controls
does_not_control
priority
override
```

### IDENTITY LOCK

```text
permanent identity
face/hair/skin/build
wardrobe
current temporary state
wide-shot recognition: silhouette + color block + posture
close-shot recognition: facial identity + hair + skin + wardrobe detail
```

### LOCATION HOLD

```text
architecture
entry/far end/left/right/floors
foreground/midground/background
motivated light sources
fixed props
forbidden additions
```

### PROP LOCK

```text
owner
hand or attachment point
geometry and dimensions
material and optical behavior
mass and contact behavior
allowed transformation
safe contact zone
forbidden variants
```

## 4. 镜头模板

```text
SHOT [N] — [single visual responsibility]

CAMERA:
[shot size], [lens feel], [height], [distance], [axis/direction],
[one primary camera behavior], [focus behavior].

START STATE:
[position, pose, eye-line, expression residue, prop state].

TRIGGER:
[visible or audible cause].

ACTION CHAIN:
[force/gesture] → [contact or perception] → [inertial/reaction change]
→ [new spatial or emotional state].

PERFORMANCE:
[eyes] → [breath] → [brow/mouth/jaw] → [body] → [line if any].

END STATE:
[exact pose, position, gaze, prop and focus state].

AUDIO:
[foreground sync] + [midground action] + [room/environment bed].
```

多人动作再附：

```text
initiator → receiver → visible response → position change → end relationship
```

## 5. 生成单元容量

- 一个镜头默认只承担一个主要视觉问题。
- 一个镜头默认最多：一个主要空间动作、一个情绪转折、一个主要运镜。
- 一个短生成单元默认最多：一个地点、一个主要因果链、一个明确尾帧。
- 对白、剧烈动作、复杂道具变形和多人反应同时出现时，优先拆段。
- 在动作完成、台词完成或稳定姿态处切分。
- 使用目标模型的真实最大窗口；未知时标记 `NEEDS_REVIEW`，不要假设固定 15 秒。

## 6. 参考权限

默认优先级：

```text
用户本轮明确修正
> 用户指定的主参考资产
> 当前连续性圣经
> 旧提示词描述
> 风格推断
```

不同类型参考互不越权：

- 人物图不控制镜头动作。
- 场景图不自动覆盖人物服装。
- 道具图不自动决定持有者和所在手。
- 运镜参考视频不自动复制其中人物、地点和受保护内容。
- 音频参考只控制音色/节奏时，不自动引入原视频对白。

## 7. 表演与物理语言

抽象情绪必须转译为至少两个可见通道：

```text
eye-line
breath/chest
brow/eyelid
mouth/jaw
head/shoulder
hand pressure
center of gravity
```

物理动作按顺序写：

```text
施力 → 接触 → 质量/惯性反应 → 环境反馈 → 结束状态
```

镜头离场必须声明：相机跟随还是锁定、焦点是否保持、空镜保持多久、下一镜如何接入。
