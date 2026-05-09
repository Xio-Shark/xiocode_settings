---
name: "jupyter-notebook"
description: "Use when the user asks to create or edit Jupyter notebooks (`.ipynb`). Prefer `scripts/new_notebook.py` for clean scaffolding."
---


# Jupyter Notebook Skill

## Rules
- 优先从模板和 `scripts/new_notebook.py` 起步，避免手写 notebook JSON。
- 编辑现有 notebook 时保持原意，做小步可运行的结构化改进。
- 能运行就做一次从上到下验证，不能运行就明确说明验证缺口。

Create clean, reproducible Jupyter notebooks for two primary modes:
- Experiments / exploratory analysis
- Tutorials / teaching walkthroughs

## When to use
- Create a new `.ipynb` notebook from scratch.
- Convert rough notes or scripts into a structured notebook.
- Refactor an existing notebook to be more reproducible and skimmable.
- Build experiments or tutorials that will be read or re-run by other people.

## Workflow
1. 判断 notebook 类型：`experiment` 或 `tutorial`。
2. 优先用 `scripts/new_notebook.py` 从模板起稿，避免手写 JSON。
3. 每个 cell 只做一步；markdown 只解释目的、输入和预期结果。
4. 编辑已有 notebook 时做定点修改，除非叙事顺序明显更好，否则不要大规模重排。
5. 能运行就全量执行验证；不能运行就明确验证缺口。

## Templates and helper script
- Templates: `assets/experiment-template.ipynb` and `assets/tutorial-template.ipynb`
- Helper script: `scripts/new_notebook.py`

## Temp and output conventions
- Use `tmp/jupyter-notebook/` for intermediate files; delete when done.
- Write final artifacts under `output/jupyter-notebook/` when working in this repo.
- Use stable, descriptive filenames (for example, `ablation-temperature.ipynb`).

## Reference map
- `references/experiment-patterns.md`: experiment structure and heuristics.
- `references/tutorial-patterns.md`: tutorial structure and teaching flow.
- `references/notebook-structure.md`: notebook JSON shape and safe editing rules.
- `references/quality-checklist.md`: final validation checklist.
