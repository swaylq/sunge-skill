#!/usr/bin/env python3
"""孙割.skill 结构自测 —— 零第三方依赖，CI 与本地都能跑。

检查这个 skill 是不是完整、自洽、可安装。不评判文风好坏（那是人的活），
只保证骨架没缺、frontmatter 合法、样本齐全。用法：

    python3 tools/self_test.py

有问题时逐条打印并以非零码退出。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
issues: list[str] = []


def need(rel: str) -> Path | None:
    p = ROOT / rel
    if not p.exists():
        issues.append(f"缺文件：{rel}")
        return None
    if p.is_file() and p.stat().st_size == 0:
        issues.append(f"空文件：{rel}")
    return p


REQUIRED = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "ROADMAP.md",
    "prompts/xiaozuowen.md",
    "prompts/hype.md",
    "prompts/decision.md",
    "references/mind.md",
    "references/style-dna.md",
    "references/decisions.md",
    "references/anti-cringe.md",
    "references/voice-and-facts.md",
    "references/jingtian-essay.md",
]
for rel in REQUIRED:
    need(rel)


def frontmatter(md: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
    if not m:
        return {}
    out: dict[str, str] = {}
    key = None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if km and not line.startswith(" "):
            key = km.group(1)
            out[key] = km.group(2)
        elif key:
            out[key] += "\n" + line
    return out


skill = ROOT / "SKILL.md"
if skill.exists():
    fm = frontmatter(skill.read_text(encoding="utf-8"))
    if fm.get("name", "").strip() != "sunge-skill":
        issues.append("SKILL.md frontmatter：name 应为 sunge-skill")
    desc = fm.get("description", "")
    if len(desc.strip()) < 60:
        issues.append("SKILL.md frontmatter：description 太短或缺失")
    if "触发词" not in desc:
        issues.append("SKILL.md frontmatter：description 里应包含触发词")
    if "allowed-tools" not in fm:
        issues.append("SKILL.md frontmatter：缺 allowed-tools")

# 样本：至少 3 篇，且冷篇（小作文体）带免责声明
examples = sorted((ROOT / "examples").glob("*.md")) if (ROOT / "examples").exists() else []
if len(examples) < 3:
    issues.append(f"examples/ 至少要 3 篇样本，现有 {len(examples)}")
for ex in examples:
    text = ex.read_text(encoding="utf-8")
    # 只有冷小作文体样本硬性要求「纯属虚构」免责声明；发推体/决策体不强制
    if "小作文体" in text and "虚构" not in text:
        issues.append(f"{ex.name}：小作文体样本应带「纯属虚构」免责声明")

# style-dna 应确实列出 15 个写法
sd = ROOT / "references/style-dna.md"
if sd.exists():
    n = len(re.findall(r"^## \d+\.", sd.read_text(encoding="utf-8"), re.M))
    if n < 15:
        issues.append(f"style-dna.md：应有 15 个编号写法，实测 {n}")

if issues:
    print(f"✗ {len(issues)} 个问题：")
    for i in issues:
        print("  -", i)
    sys.exit(1)

print("✓ 孙割.skill 结构自测通过：骨架完整、frontmatter 合法、样本齐全、15 个写法在位。")
