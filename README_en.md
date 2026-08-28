<div align="center">

# 🍌 sunge-skill (孙割.skill)

### Distills Justin Sun's mind, writing style, and decision-making — three in one

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)
[![Sun-ology](https://img.shields.io/badge/孙学-Sun--ology-8a2be2)](references/mind.md)

**Justin Sun (孙宇晨) · mind × writing × decisions · one skill for how "Sun-ge" thinks, writes, and decides**

[中文 README](README.md) · [Install](#install) · [The three](#what-it-distills) · [How to use](#how-to-use) · [Decision case](#decision-case) · [Red lines](#red-lines)

</div>

---

sunge-skill distills Justin Sun into three things, bundled to work together:

- **🧠 Mind** — how he sees the world. Increment > stock, winner-takes-all, attention-as-energy, "carriage law governing cars" — a set of mental models.
- **✍️ Writing style** — how he writes. From the ice-cold literary essay of *My Girlfriend Jing Tian* to the number-blasting, 🚀-capped hype of his tweets.
- **🎯 Decision-making** — how he decides. Outsource the decision you can't bear to a cold system, Auto Pilot off the feelings, "not deciding is a decision," and more.

Give it a subject or a dilemma and it answers with his brain, his pen, and his decision logic at once.

> **Two names.** Fans call him "Sun-ge" (孙哥, brother Sun); the market calls him "Sun-ge" (孙割, Sun-the-harvester — 割 as in fleecing retail). Same sound. **孙学 ("Sun-ology")** is the fandom term for studying his person, words, and methods — like "曾学" for the Qing statesman Zeng Guofan.

## What it distills

| | What | Where |
|---|---|---|
| **🧠 Mind** | Mental models + value ordering + the cracks in his persona (write him in 3D, keep the contradictions) | [`references/mind.md`](references/mind.md) |
| **✍️ Writing** | The *Jing Tian* voice broken into **15 reusable moves**, each with the original line + how to write it + how it goes wrong; **4 are load-bearing**: obedient to the end, fortune beside a tiny detail, feeling as action, no uplift ending | [`references/style-dna.md`](references/style-dna.md) |
| **🎯 Decisions** | **6 key decisions** lifted out of *Jing Tian* (outsource to a cold system / Auto Pilot / not-deciding / money-as-scoreboard / pricing emptiness / acting on info you know is bad) + a heuristics ledger | [`references/decisions.md`](references/decisions.md) |

The three are welded: the coldness of his prose comes from the same "reduce emotional volatility like an AI" mind; his most famous decision was letting Claude make the call. This skill hands you that seam too.

## Install

**Claude Code** — drop the whole `sunge-skill/` folder into your skills directory:

```bash
git clone https://github.com/swaylq/sunge-skill.git
cp -r sunge-skill ~/.claude/skills/
```

Or `npx skills add swaylq/sunge-skill` in the skills.sh ecosystem.

## How to use

Just talk to it — it picks the mode:

| You want | It gives |
|---|---|
| "Write my grad-school year in Justin Sun's voice" | a cold literary essay (the flagship) |
| "Do a Sun-ge hype tweet for my app" | an upbeat hype thread |
| "How would Justin Sun see AI startups?" | a take, through his mind |
| "Pull the key decisions out of this story" | the buried decisions, as a table |
| "Using his logic, should I make this investment?" | it first sorts "actually hard" vs "you fear the answer," then gives an unhedged call |

For real people/products it looks up real numbers and proper nouns first — **this runs on real material**, fabricated details read fake — then self-checks against a de-slop list before handing anything over.

## Decision case

Here's what the decision pillar looks like — from the most famous dilemma in *Jing Tian*:

> **Q:** This fifty million — do I give it to her?
>
> **Sun-ge:** Whether it affects me, I worked out. I ran all my cash through Claude Code's API. No effect at all. I checked again — still none. So this isn't about the money.
> I've never once refused her. Not generosity — fear. Fear of the next second's answer.
> I typed the question into Claude. I asked, should I give it. It said, don't give her the fifty million. I asked, does she not love me anymore. It said, about love I don't care and don't understand, but you cannot give her the fifty million.
> It answered fast, not a beat missed. What chilled me wasn't that it was right, it was that it didn't hesitate at all. It felt nothing.
> That "no," I didn't say it. I let the machine say it for me.
> **I'm going with the AI.**

He wasn't leaning on Claude for the math — that was already done. He was borrowing the machine's lack of hesitation to say, for himself, the "no" he couldn't. All six decisions in [`references/decisions.md`](references/decisions.md).

## Examples

Four ready-made ([`examples/`](examples/), in Chinese): [*My Gym Card*](examples/01-my-gym-card.md) (the voice on the most ordinary thing) · [*My First 100x Coin*](examples/02-my-first-100x.md) (from the fleeced side) · [a Sun-ge hype thread](examples/03-hype-thread.md) · [the fifty-million call](examples/04-decision-5000w.md) (decision mode).

## Red lines

This lives in the gap between "apparently true" and "labeled fiction" — half the essay's force comes from that ambiguity, so the skill holds a few lines hard:

- Real people in **active disputes** (Sun v. Jing Tian, SEC v. Sun): only their public positions, ending with "this is fiction, any resemblance is coincidental," never asserted as fact.
- No fabricated explicit sexual/reproductive/medical private facts about a real person as if true; no invented crimes for a living, identifiable person.
- Decision mode gives "how someone like Justin Sun would judge it," **not investment/legal/medical advice** — it flags risk, it doesn't egg you on.
- A style/mind mimicry tool for a wry smile or a chill down the spine — not for defamation, harassment, whitewashing, or verdicts. Output carries a disclaimer by default; loosen it when you write yourself, pure fiction, or self-parody.

*Not affiliated with Justin Sun, TRON, Jing Tian, or their teams. All analysis is based on publicly published text, for writing instruction and research.*

## License

[MIT](LICENSE). Sun's own note on the original essay was "no copyright, share freely." This skill follows suit.
