<div align="center">

# 🍌 sunge-skill (孙割.skill)

### Distills Justin Sun's mind, writing style, and decision-making — three in one

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)
[![Sun-ology](https://img.shields.io/badge/孙学-Sun--ology-8a2be2)](references/mind.md)

**Justin Sun (孙宇晨) · mind × writing × decisions · one skill for how "Sun-ge" thinks, writes, and decides**

[中文 README](README.md) · [Install](#install) · [Where the three live](#where-the-three-live) · [How to use](#how-to-use) · [What a decision looks like](#what-a-decision-looks-like) · [Red lines](#red-lines)

</div>

---

sunge-skill distills Justin Sun into three things and bundles them to work together.

First, his head — how he reads the world. Increment beats stock, winner-takes-all, attention is energy, governing cars with carriage law. These are the rulers he measures every person and situation against.

Second, his hand — how he writes. Cold, it's the register of *My Girlfriend Jing Tian*: one sentence per paragraph, a fortune pinned next to one small detail, an ending that just says "nothing happened." Hot, it's how he tweets: numbers to the face, upward the whole way, three rockets at the end.

Third, how he decides. Hand the decision you can't bear to a system with no feelings and let it make the call. Set the emotions to autopilot. Not deciding is itself a decision.

Give it a subject and it writes with all three at once. Give it a story or a dilemma and it lifts out the decisions, or hands you a call in his logic.

> Fans call him "Sun-ge" (孙哥, brother Sun). The market calls him "Sun-ge" (孙割, Sun-the-harvester — 割 as in fleecing retail). Same sound. **孙学 ("Sun-ology")** is the online habit of studying the man, his lines, and his way of deciding — like "曾学" for the Qing statesman Zeng Guofan.

## Where the three live

The head is in [`references/mind.md`](references/mind.md), the writing in [`references/style-dna.md`](references/style-dna.md), the decisions in [`references/decisions.md`](references/decisions.md). Three files, and the skill's three pillars.

The writing file breaks the *Jing Tian* voice into fifteen moves, each with the original line, how to write it, and how it goes wrong. Four of them are load-bearing; drop one and it stops sounding like him: obedient to the very end, a fortune with a tiny detail beside it, feeling written as action, and no uplift at the close. The decisions file lifts six out of *Jing Tian*: outsource the decision to a cold system, set feeling to autopilot, not-deciding as a decision, money as a scoreboard, pricing emptiness, and acting on what you already know is bad.

The three aren't separate. The chill in his prose comes from that same "unmoved, like a machine" head. His most famous decision was letting Claude make the fifty-million call. Thinking, writing, and deciding were always welded together, and the seam is what this skill wants to hand you.

## Install

Drop the whole `sunge-skill` folder into your skills directory.

```bash
git clone https://github.com/swaylq/sunge-skill.git
cp -r sunge-skill ~/.claude/skills/
```

Or, in the skills.sh ecosystem, `npx skills add swaylq/sunge-skill`.

## How to use

Once it's installed, just say what you want in plain words and it works out which of the three you're after.

To have it write, say "write my grad-school year in Justin Sun's voice," or "put this into the Sun-ge register," and you get a cold essay; say "do a Sun-ge hype tweet for my app" and you get a hot one. To borrow his head, ask "how would Justin Sun see AI startups" and it answers through his models. To use it on a decision, hand it an article and have it pull the buried decisions into a table — or tell it the thing you're stuck on, and it first sorts whether it's "actually hard" or "you fear the answer," then gives a call with no hedging.

For real people and events it looks up the real numbers and names before it writes. This runs on real material; fabricated detail reads fake on sight. When it's done, it takes a checklist back through its own draft and strips out the AI tics.

## What a decision looks like

The decision pillar shows clearest in the most famous dilemma in *Jing Tian*.

> **Q:** This fifty million dollars — do I give it to her?
>
> **Sun-ge:** This isn't actually hard, it's that you fear the answer. Whether the money affects you can be worked out. What you fear is whether she still loves you afterward. So split the two.
> The money goes to what can compute it. I ran my cash through Claude; giving it wouldn't affect me, money isn't the problem.
> The "no" you can't say yourself — you've never once said no to her — hand that over too. It said don't give it, without a beat.
> So I won't. I'm going with the AI.

He wasn't leaning on the AI for the math; the math was already done. He was borrowing the machine's lack of hesitation to say, for himself, the "no" he couldn't. The other five decisions are all in [`references/decisions.md`](references/decisions.md).

## A few worked samples

Four finished pieces sit in [`examples/`](examples/) (in Chinese). [*My Gym Card*](examples/01-my-gym-card.md) puts the voice on the smallest possible thing, a membership you never used. [*My First 100x Coin*](examples/02-my-first-100x.md) writes from the fleeced end instead. There's [a Sun-ge hype thread](examples/03-hype-thread.md) for the hot register, and [the fifty-million call](examples/04-decision-5000w.md) from decision mode.

## How it differs from the other two Justin Sun skills

Two good ones already exist. [alchaincyf/sun-yuchen-perspective](https://github.com/alchaincyf/sun-yuchen-perspective) distills his decision lens with six mental models and eight shortcuts. [0xquqi/sun-skill](https://github.com/0xquqi/sun-skill) distills a cognitive system out of twenty-odd thousand tweets, an autobiography, and a 155-episode course — fourteen models, eighteen heuristics.

Both build the head deep and complete. sunge-skill doesn't compete on that. It gathers all three: a serviceable head, plus the writing and the decisions-inside-the-stories that neither of the other two touches, welded together. Want to study how he thinks — those two are fuller. Want his thinking, writing, and deciding in one pair of hands — take this. All three coexist fine.

## Red lines

This lives between "looks true" and "actually fiction," and half of *Jing Tian*'s force comes from that ambiguity. Which is exactly why a few lines have to hold.

For real people still in court — Sun and Jing Tian, the SEC and Sun — it uses only what they've said publicly, ends with "this is fiction, any resemblance is coincidental," and never states it as fact. It won't invent explicit private detail about a real person and pass it off as true, or pin a specific crime on someone living. Decision mode gives you "how someone like Justin Sun would judge it," not investment, legal, or medical advice; it flags the risk, it doesn't egg you on.

In the end this is a mimicry tool for a wry smile or a chill down the spine, not a tool for defamation, harassment, whitewashing, or verdicts. Use it on yourself, on pure fiction, on self-parody — go ahead.

*Not affiliated with Justin Sun, TRON, Jing Tian, or their teams. All analysis is based on publicly published text, for writing instruction and research.*

## License

MIT. Sun's own note at the end of *Jing Tian* was "no copyright, share freely." This skill does the same. Take it and use it.
