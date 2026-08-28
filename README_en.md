<div align="center">

# 🍌 sunge-skill (孙割.skill)

### Write in Justin Sun's voice — the one from *My Girlfriend Jing Tian*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)
[![Sun-ology](https://img.shields.io/badge/孙学-Sun--ology-8a2be2)](references/decisions.md)

**Justin Sun writing style · the "Sun-ge" essay voice · Chinese literary mimicry · 孙学 decision extraction**

[中文 README](README.md) · [Install](#install) · [See what it writes](#see-what-it-writes) · [The 15 moves](#what-it-actually-distilled) · [Decision extraction](#孙学-decision-extraction)

</div>

---

On 2026-08-27, Justin Sun (孙宇晨) published a short essay, *My Girlfriend Jing Tian* (《我的女友景甜》). It went viral across the Chinese internet overnight.

The style is strange. Sentences as cold as a court ruling, describing fifty million dollars in cash, a Gulfstream jet, a $6.2M banana, and a woman who makes the narrator call her "mom." Every paragraph is short. Every paragraph pushes down. It ends with no tears, no lesson, just one line — **nothing happened**.

Plenty of people tried to copy it and couldn't. It looks simple, but each sentence hides a precise move: pin a fortune next to a heartbreakingly small detail, write heartbreak as "my heartbeat was steady," keep the narrator obedient to the last word, and never, ever end on a moral.

sunge-skill breaks that voice into **15 reusable moves**. Give it a subject — a person, an event, a relationship, a gym membership you never used — and it hands you back a piece built from the same machinery.

> **The name.** Fans call him "Sun-ge" (孙哥, brother Sun). The market calls him "Sun-ge" (孙割, Sun-the-harvester — 割 as in fleecing retail investors). Same sound. This skill takes the writing; the name takes the joke.

## See what it writes

The same voice, turned on the most ordinary thing possible — **a gym membership you never used** ([full text, in Chinese](examples/01-my-gym-card.md)):

> The weight of one drop of sweat: fifty milligrams.
> The weight of a one-year card: five grams.
> This year, my card weighed more than my sweat.
> ...
> At year's end the app pushed a report. It said: this year you came 4 times, burned 620 kcal, about 1.2 hamburgers.
> It put "1.2 hamburgers" in bold.
> ...
> In January the card auto-renewed. The text came at 3 a.m.
> Nothing happened.

No adjective of feeling, no rhetorical question, no uplift. Just actions and numbers, and an ending that presses down. That's the voice.

Two more worked examples ship in [`examples/`](examples/): [*My First 100x Coin*](examples/02-my-first-100x.md) (told from the side of the fleeced) and a [hype-mode launch thread](examples/03-hype-thread.md) (his other, louder register).

## Install

**Claude Code** — drop the whole `sunge-skill/` folder into your skills directory:

```bash
git clone https://github.com/swaylq/sunge-skill.git
cp -r sunge-skill ~/.claude/skills/
```

Or `npx skills add swaylq/sunge-skill` in the skills.sh ecosystem.

## How to use

Just talk to it:

- "Write my grad-school year in Justin Sun's voice."
- "Do the *Jing Tian* essay style on me and my last job."
- "Turn 'a middle-aged man's first used Porsche' into the Sun-ge essay voice."

It first picks the register — **cold** (the literary essay, the default) or **hot** (the hype/tweet voice) — looks up real numbers and proper nouns when the subject is real, writes to the flow, then runs its own **de-slop checklist** before handing the piece to you.

## What it actually distilled

The core is the **15 moves** in [`references/style-dna.md`](references/style-dna.md), each with the original line from the essay, how to write it yourself, and what it looks like when it goes wrong. A few of the load-bearing ones:

| Move | In one line |
|---|---|
| **Weigh-in opening** | Put the priceless and the priced on one scale; harder the unit, the better |
| **One sentence, one paragraph** | Let the blank line do the feeling; delete the conjunctions |
| **The "okay" refrain** | The narrator never refuses; the "no" is said by someone else |
| **Fortune + tiny detail** | Every huge sum sits next to something small enough to hurt |
| **Feeling as action** | Where you'd emote, write a body doing something instead |
| **Staffed emptiness** | A whole entourage runs for someone who isn't there |
| **The cold-AI cameo** | Let a machine say the "no" the narrator can't |
| **No uplift ending** | Land on an object and "nothing happened" — never a moral |

**Four of them are load-bearing** — miss one and it's just an impression, not the voice: *obedient to the end, fortune beside a tiny detail, feeling written as action, no uplift at the end.*

### On removing the "AI smell"

LLMs have a set of habits that run exactly opposite to this voice: stacking adjectives, rhetorical questions, "however / in fact," and moralizing endings. [`references/anti-cringe.md`](references/anti-cringe.md) catalogs these failure modes, and the skill self-checks against it every time. That's the real difference from "ask some model to imitate Justin Sun" — this one fights the AI smell by default.

## 孙学 (Decision extraction)

The prose is the shell; the decisions are the core. On its surface *My Girlfriend Jing Tian* is about a relationship — underneath it are six decisions you can lift out on their own. The most famous:

> She asks for fifty million dollars. For the first time he says "let me think." He runs all his cash through Claude Code's API and confirms it wouldn't affect him at all. Money isn't the problem. He still can't decide. So he hands the decision itself to Claude, and Claude says: don't give her the fifty million.
>
> What chills him isn't that it's smart. It's that it doesn't hesitate for a second.

sunge-skill lifts these out into [`references/decisions.md`](references/decisions.md): **outsource the decision you can't bear to a cold system** (what he lacks isn't compute, it's the machine's resolve), **Auto Pilot / switch feeling off**, **not deciding is a decision — the priciest one**, **money as a scoreboard**, **pricing emptiness**, **acting on info you know is bad**. Each with: what he did → the logic → how you'd use it → the flip side.

Two uses beyond writing: **extract** — hand it an essay, an experience, a news story, and it pulls the buried decisions into a table (decisions only, no character judgment); **borrow the logic** — hand it your own dilemma and it first sorts whether it's "actually hard" or "you fear the answer," then gives an unhedged call in his style — while telling you honestly that this is what *his* logic would answer, not what's right for you (he's the cautionary tale of living by it).

## How it differs from the other two Justin Sun skills

Two good Justin Sun skills already exist, and both distill his **mind** — his mental models and decision heuristics, so the AI can *think* like him:

- [alchaincyf/sun-yuchen-perspective](https://github.com/alchaincyf/sun-yuchen-perspective)
- [0xquqi/sun-skill](https://github.com/0xquqi/sun-skill)

sunge-skill distills his **hand** — first the *prose* (the cold literary register neither of the other two covers), then the *decisions as they live inside his stories*. Its decision extraction is different in kind: the other two hand you a complete, abstract framework of ~18 heuristics; sunge-skill lifts decisions out **one at a time, with the scene attached** ("Claude decides the fifty million" is a live one), so what he *writes* and how he *decides* end up welded together. Install all three and you get his mind, his pen, and the seam between them.

## Red lines

This voice lives in the gap between "apparently true" and "labeled fiction" — half the essay's force comes from that ambiguity, so the skill holds a few lines hard:

- For real people in **active disputes** (Sun v. Jing Tian, SEC v. Sun), it uses only their public positions and ends with "this is fiction, any resemblance is coincidental" — never asserted as fact.
- It won't fabricate explicit sexual, reproductive, or medical private facts about a real person as if true, and won't invent specific crimes for a living, identifiable person.
- This is a **style tool** — for a wry smile or a chill down the spine — not a tool for defamation, harassment, whitewashing, or verdicts. Output carries a disclaimer by default; loosen it freely when you're writing yourself, pure fiction, or self-parody.

*Not affiliated with Justin Sun, TRON, Jing Tian, or their teams. All style analysis is based on publicly published text, for writing instruction and research.*

## License

[MIT](LICENSE). Sun's own note on the original essay was "no copyright, share freely." This skill follows suit — take it and write something.
