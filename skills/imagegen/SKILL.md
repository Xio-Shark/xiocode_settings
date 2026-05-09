---
name: "imagegen"
description: "Use when the user wants image generation or image editing via the OpenAI Image API."
---


# Image Generation Skill

## Rules
- 只处理图片生成和图片编辑，不处理视频或语音任务。
- 优先使用 `scripts/image_gen.py`，不要临时重写一套图片调用脚本。
- 缺少 `OPENAI_API_KEY` 时只指导本地配置，不要求用户在聊天里粘贴密钥。

Generates or edits images for the current project (e.g., website assets, game assets, UI mockups, product mockups, wireframes, logo design, photorealistic images, infographics). Defaults to `gpt-image-1.5` and the OpenAI Image API, and prefers the bundled CLI for deterministic, reproducible runs.

## When to use
- Generate a new image (concept art, product shot, cover, website hero)
- Edit an existing image (inpainting, masked edits, lighting or weather transformations, background replacement, object removal, compositing, transparent background)
- Batch runs (many prompts, or many variants across prompts)

## Workflow
1. 判断任务是 generate、edit 还是 batch。
2. 收集必要输入：prompt、文本约束、输入图/蒙版、必须保持不变的元素。
3. 批量任务写临时 JSONL；编辑任务要明确 invariants。
4. 把 prompt 压成短 spec 后运行 `scripts/image_gen.py`。
5. 检查输出是否满足主体、构图、文本准确性和约束；每次只改单一变量迭代。

## Temp and output conventions
- Use `tmp/imagegen/` for intermediate files (for example JSONL batches); delete when done.
- Write final artifacts under `output/imagegen/` when working in this repo.
- Use `--out` or `--out-dir` to control output paths; keep filenames stable and descriptive.

## Environment
`OPENAI_API_KEY` is required for live calls. If missing, ask the user to configure it locally and confirm when ready.

## Defaults
- Use `gpt-image-1.5` unless the user explicitly asks for `gpt-image-1-mini` or explicitly prefers a cheaper/faster model.
- Assume the user wants a new image unless they explicitly ask for an edit.
- 编辑时必须写清楚“只改什么，保持什么不变”。
- 结果不满足约束时，只做小步 prompt/mask 迭代。

## Prompt augmentation
把用户要求整理成短 spec，只补充用户已隐含表达的构图、用途和约束，不凭空增加新视觉元素。完整 taxonomy、模板和示例都放在引用文件里。

## Reference map
- `references/cli.md`: commands, flags, and batch recipes
- `references/image-api.md`: API parameters and model knobs
- `references/prompting.md`: prompt-augmentation rules
- `references/sample-prompts.md`: taxonomy, examples, and copyable specs
- `references/codex-network.md`: environment and network troubleshooting
