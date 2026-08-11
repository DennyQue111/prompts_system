# 手绘逐帧动画 · 运动质感

**用途**：视频生成（Seedance 等），注入传统 2D 手绘动画的逐帧运动质感——非 3D CG 的无限平滑插值，而是每一帧都像独立手稿连续播放的「手作感」。
**类型**：视频动画风格（非静帧风格），只控制运动/时间/轮廓行为，不涉及色调、材质、构图。
**效果**：消解 CG 的数学完美感，保留手绘的微小跳动与不均匀，产生二维动画的「画出来的」运动质感。

---

## 技术拆解

### 帧节奏 / 定时

```
hand-drawn frame-by-frame animation motion texture,
slight freeze-frame pause between keyframes — traditional 2D animation "on-twos" rhythm (12 distinct drawings per second),
not 3D CG infinitely smooth interpolation,
motion reads as individually drawn pages played in sequence
```

- 拍二节奏：每秒 12 张不同画面，非 24fps 全帧连续
- 关键帧之间有轻微的定格/停顿感
- 运动的本质是「手稿序列播放」而非「数学插值计算」

### 轮廓线行为

```
contour lines exhibit extremely subtle variation between consecutive frames —
each frame's outlines are slightly different, as if redrawn by hand,
lines "breathe" with micro-boil — not jittery, not flickering, but alive
```

- 连续帧之间轮廓线有极细微变化，像逐帧重描
- 线条有「呼吸感」——微小的线煮（line boil），不死板不抖动不过度
- 这是区别于 3D 渲染最关键的特征：3D 每帧轮廓完全一致

### 缓动曲线特征

```
avoid perfect mathematical easing curves (no bezier-smooth acceleration/deceleration),
preserve hand-drawn micro "jitter" and unevenness in all motion trajectories,
each movement feels authored frame-by-frame rather than algorithmically interpolated
```

- 拒绝完美的贝塞尔缓动——任何加速/减速都保留手调的不均匀
- 运动轨迹有微小的「人手偏差」——不是错误，是质感
- 每个位移、旋转、缩放都像动画师逐帧调的

### 运动模糊策略

```
minimal to no motion blur — traditional 2D animation relies on clear key poses,
not photographic motion blur,
if blur exists, it appears as hand-drawn smears (stretched in-betweens), not Gaussian/vector blur
```

- 几乎不出现运动模糊（传统 2D 动画靠关键张清晰传递动作）
- 如有模糊，是手绘 smear frame（拉伸中割），非高斯/向量模糊
- 画面在运动中也保持清晰可读的轮廓

### 整体感觉

```
the final output reads like traditional 2D animation — not cel-shaded 3D, not rotoscoped,
each frame appears to be a separately drawn image,
the slight imperfections in timing, line consistency, and trajectory uniformity 
are the signature texture of hand-crafted animation
```

- 不是 cel-shaded 3D（3D 渲染后加描边）
- 不是 rotoscope（实拍转描）
- 每一帧都像独立手绘画面的集合

---

## 使用方式

### 注入位置

在 shot seedance 提示词的「动作」段落之后插入。已有「运动质感说明」段的直接追加以下内容。

### 标准注入块

直接复制到视频提示词中：

```
运动质感说明：所有动作呈现手绘逐帧动画的运动质感——关键帧之间有轻微的定格感，类似传统2D动画的拍二节奏，非3D CG的无限平滑插值。轮廓线在连续帧之间有极细微的变化，像一张张单独绘制的手稿连续播放。运动避免完美的数学缓动曲线，保留手绘的微小"跳动"与不均匀感。
```

### 强化版（更偏传统动画感）

如需更强的手绘感（画面更接近吉卜力/早期 MADHOUSE 时代质感），替换为：

```
运动质感说明：所有动作呈现手绘逐帧动画的运动质感——关键帧之间有轻微的定格感，类似传统2D动画的拍二节奏（每秒12张），非3D CG的无限平滑插值。轮廓线在连续帧之间有极细微的变化，像一张张单独绘制的手稿连续播放。运动避免完美的数学缓动曲线，保留手绘的微小"跳动"与不均匀感。运动模糊最小化——如有模糊，仅以手绘smear frame（拉伸中割）形式出现，不使用高斯或向量模糊。整体运动质感应接近传统赛璐珞动画的制作痕迹，而非现代数字插值产物的完美平滑。
```

---

## 负面约束

对应注入在视频提示词的「负面约束」段：

```
禁止3D CG般完美平滑的插值运动；禁止每一帧轮廓完全一致、无任何手绘抖动；禁止过度运动模糊；禁止数学缓动曲线式的均匀加速/减速；禁止出于运动模糊导致的轮廓模糊或形状变形；禁止24fps全帧连续平滑感（应保持拍二节奏的轻微定格）；禁止cel-shaded 3D渲染感（3D模型描边伪装2D）
```

---

## 适用场景

| 适用 | 不适用 |
|------|--------|
| 2D 动画风格短片 | 写实/电影感真人视频 |
| 手绘感角色动画 | 3D CG 动画 |
| 传统动画美学追求 | 高帧率游戏过场动画 |
| GIF/循环动画 | 纪录片/实拍风格 |

---

## 与图像 style-profile 的关系

- 本文件只控制**运动的时间行为**，不控制画面风格（色调/材质/构图/渲染方式）
- 画面风格仍由参考图 + 图像 style-profile（如 `made-in-abyss-technical.md`）负责
- 两者正交叠加：图像 style-profile 管「每一帧长什么样」，本文件管「帧与帧之间怎么过渡」
- 在 Seedance 工作流中：参考图锁定视觉 → 动作描述锁定物理 → 本文件锁定运动质感

---

## 效果检测清单

视频生成后，按以下清单检查运动质感是否达标：

- [ ] 连续两帧之间轮廓线不 100% 一致（有微呼吸感）
- [ ] 运动不出现 3D 数学缓动完美曲线
- [ ] 关键帧切换有轻微「定格」感，非连续平滑滑动
- [ ] 无过度运动模糊（画面在运动中轮廓仍然清晰）
- [ ] 整体观看体验接近传统 2D 手绘动画，非 cel-shaded 3D
- [ ] 线条在运动中不出现像素闪烁/摩尔纹（那是 3D 渲染 bug，不是手绘感）
