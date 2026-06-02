# twc-skills

> Fork/adaptation notice: this project is adapted from the original
> `nature-skills`/scientific-writing skill framework and has been rebuilt for
> IEEE Transactions on Wireless Communications (TWC) workflows. The current
> version adds TWC-specific guidance for wireless federated learning, AirComp,
> RIS/IRS, cell-free MIMO, resource allocation, semantic communications, paper
> reading, manuscript writing, polishing, figures, reviewer responses, and
> paper-to-PPT workflows.
>
> 改造说明：本项目是在原有 `nature-skills` / 科研写作 skill 框架基础上改造而来，
> 当前版本面向 IEEE TWC 与无线通信论文工作流，重点覆盖无线联邦学习、AirComp、
> RIS/IRS、cell-free MIMO、资源分配、语义通信、论文阅读、写作润色、图表、审稿
> 回复与论文转 PPT。

## TWC Corpus Upgrade

This release includes a local-corpus upgrade based on 50 user-provided TWC papers.
The repository does not store the paper PDFs or full paper text. It stores only
public-safe structural observations, such as section patterns, figure/table
patterns, domain tags, and aggregate statistics, so the skills can better follow
TWC-style system modelling, problem formulation, simulation evidence, and
wireless-communications presentation logic.

我们基于 50 篇用户提供的 TWC 论文做结构化归纳。仓库不保存论文 PDF 或全文，
只保留公开安全的结构观察，例如章节模式、图表模式、领域标签和统计信息，用于让
skill 更贴近 TWC 的系统模型、问题建模、仿真实验和无线通信论文表达习惯。

## Installation

`twc-skills` is a repository of reusable instruction bundles centred on `SKILL.md`.
Each `skills/twc-*` directory is one installable unit. Copy the whole folder, not
only `SKILL.md`, because many skills depend on `references/`, assets, scripts, or
README context.

### 1. Codex

Codex can use these folders directly as local skills. This is the simplest installation path.

**Clone the repo**

```bash
git clone https://github.com/Yuankun-Xia/twc-skills.git
cd twc-skills
```

**Install one skill**

```bash
mkdir -p ~/.codex/skills
cp -R skills/twc-reader ~/.codex/skills/
```

**Install all current skills**

```bash
mkdir -p ~/.codex/skills
for d in skills/twc-*; do
  cp -R "$d" ~/.codex/skills/
done
```

**Update after pulling new changes**

```bash
git pull
for d in skills/twc-*; do
  cp -R "$d" ~/.codex/skills/
done
```

**Finish**

- Restart Codex so newly added skills are picked up.
- Then ask naturally, for example: `Translate this paper into a full markdown reader.` or
  `Make this paper into a Chinese journal-club PPT.`

If you prefer not to use the terminal, copying the `skills/twc-*` folder(s) into
`~/.codex/skills/` manually works as well. For a longer walkthrough, see
[`install.md`](install.md).

### 2. Claude Code

**Primary method: Plugin marketplace installation**

This repository is published as a Claude Code plugin, making installation simple.

```bash
# Add the marketplace (one-time)
/plugin marketplace add https://github.com/Yuankun-Xia/twc-skills

# Install the plugin
/plugin install twc-skills

# Reload to apply
/reload-plugins
```

All nine skills are available automatically after reload. No manual wrapper setup needed.

**Alternative: subagent wrapper**

If you prefer manual control over individual skills, create a user-level subagent:

```bash
mkdir -p ~/.claude/agents
cp skills/twc-reader/SKILL.md ~/.claude/agents/twc-reader.md
```

Then open `~/.claude/agents/twc-reader.md` and make sure the frontmatter is valid
for Claude Code subagents:

```yaml
---
name: twc-reader
description: Full-paper bilingual, figure-aware, source-grounded Markdown reader for journal or conference papers. Use proactively when the user asks to translate an entire paper or generate a complete markdown reader.
---
```

After that, start a new Claude Code session or open `/agents`, and invoke it naturally or explicitly:

```text
Use the twc-reader subagent to turn this PDF into a full markdown reader.
```

If you prefer commands instead of subagents, create a project or user command under
`.claude/commands/` or `~/.claude/commands/` and paste or adapt the corresponding
`SKILL.md` content there.

Official Claude Code docs:

- [Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
