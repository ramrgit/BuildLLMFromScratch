# 4-Week Plan: Build an LLM from Scratch + Microsoft Foundry

**Target finish:** before the July 4 weekend (start Mon June 8 → done Fri July 3)
**Daily time:** ~2–3 hrs on weekday mornings after school drop-off
**Book:** *Build a Large Language Model (From Scratch)* — Sebastian Raschka (7 chapters + Appendix A PyTorch primer)
**Companion repo:** https://github.com/rasbt/LLMs-from-scratch
**Hardware:** local RTX 4070 (12 GB VRAM) for all book + local work; Foundry (serverless) for cloud familiarity

---

## The 3 anti-reset habits (the whole reason this plan works)

You lose progress to "start over" because you lose your *mental state* between sessions, not because the material is hard. These three habits fix that. Do them every single session.

1. **Two-line log note.** End every session by writing two lines in `PROGRESS.md`: where you stopped, what's next. Start every session by reading them. Resume in 30 seconds, not 30 minutes.
2. **Commit to git every session, even broken.** Your repo *is* your progress. You can never lose it to a distraction. Bonus: it becomes a resume artifact.
3. **The companion repo is your safety net, not your shortcut.** If you fall behind, read the chapter and run *his* code to stay on schedule, then re-type it yourself later. Never let "I haven't typed it yet" stop you moving forward in understanding.

**The daily unit (this is what survives interruption):**
- [ ] Read your two PROGRESS.md lines (1 min)
- [ ] Read the section in the book *first*, then retype + run the code
- [ ] `git commit` (even if broken)
- [ ] Write your two-line note for next time

> A successful day = one section read, typed, committed, noted. It does **not** have to be a whole chapter. That belief is the trap.

---

## One-time setup (do this first, ~30 min, Mon Week 1)

- [x] Create a project folder; `git init`; create `PROGRESS.md` and paste the template (bottom of this file)
- [x] Confirm PyTorch sees the GPU: `python -c "import torch; print(torch.cuda.is_available())"` → should print `True`
- [ ] Clone the companion repo: `git clone https://github.com/rasbt/LLMs-from-scratch`
- [x] Bookmark the free "Test Yourself" quiz PDF (Manning) — ~30 questions/chapter, great for self-checking
- [x] Set an Azure **budget alert** at $5 (Cost Management → Budgets) — free insurance before any Foundry work

---

## Week 1 (June 8–14): Foundations + first Foundry deployment

Goal by Friday: you can turn text into tokens, and you've made your first Foundry deployment.

- [x] **Mon** — Setup (above) + start **Ch 1** (Understanding LLMs). Mostly reading; light day on purpose.
- [x] **Tue** — Finish **Ch 1**. If PyTorch feels rusty, skim **Appendix A** (PyTorch primer) — don't skip if unsure; it pays off all month.
- [x] **Wed** — **Ch 2** (Working with text data): tokenization, byte-pair encoding. Hands-on and satisfying.
- [ ] **Thu** — **Ch 2** cont.: data loaders, input-target pairs, embeddings. Retype the data loader yourself.
- [ ] **Fri** — Finish **Ch 2** + do the Ch 2 exercises. You now have a working tokenizer/data pipeline.
- [ ] **Weekend block (~2 hr) — FOUNDRY #1:** sign in to ai.azure.com → deploy a serverless model (Haiku 4.5 or any cheap one) → call it from the **playground** AND from a **Python script** (endpoint + key). Confirm deployment type says *serverless / pay-as-you-go*, never a dedicated GPU SKU. Resume item banked.

---

## Week 2 (June 15–21): Attention — the heart of it

Goal by Friday: you understand attention deeply + have a RAG-on-Foundry mini-project.

- [ ] **Mon** — **Ch 3** start: simplified self-attention. Go slow; this is THE chapter.
- [ ] **Tue** — **Ch 3**: self-attention with trainable weights. **Type the verbose from-scratch class by hand** — this is where it clicks.
- [ ] **Wed** — **Ch 3**: causal/masked attention + dropout.
- [ ] **Thu** — **Ch 3**: multi-head attention. Wire the dimensions by hand.
- [ ] **Fri** — Finish **Ch 3** + exercises. Don't skip the explicit version thinking it's throwaway — the understanding lives there.
- [ ] **Weekend block — FOUNDRY #2 (RAG tie-in):** reuse your local retrieval setup (you've done Gemma) but point the **generation** step at a Foundry-served model. Now you have a clean "RAG pipeline using Microsoft Foundry for inference" story. Experiment with chunk size + top-k to deepen RAG understanding.

---

## Week 3 (June 22–28): Build the full model + pretrain it

Goal by Friday: you've built and trained a GPT from scratch on your own GPU.

- [ ] **Mon** — **Ch 4** start: layer norm, GELU, feed-forward block.
- [ ] **Tue** — **Ch 4**: assemble the transformer block + full GPT architecture.
- [ ] **Wed** — **Ch 4**: the forward pass, generating (untrained) text + exercises. You now have a complete GPT.
- [ ] **Thu** — **Ch 5** start: training loop, loss/cross-entropy, the pretraining setup. RTX 4070 handles the book's small model fine.
- [ ] **Fri** — **Ch 5**: run training, **watch the loss come down on your own GPU.** Text generation strategies (temperature, top-k). The emotional payoff.
- [ ] **Weekend block:** finish **Ch 5** — loading pretrained GPT-2 weights into your model. Optional: rest, you're ahead.

---

## Week 4 (June 29–July 3): Fine-tuning — your stated goal

Goal by Friday: you've fine-tuned models two ways and used Foundry end-to-end.

- [ ] **Mon** — **Ch 6** (Fine-tuning for classification): dataset prep, adding a classification head.
- [ ] **Tue** — **Ch 6**: training the classifier + evaluating + exercises.
- [ ] **Wed** — **Ch 7** (Fine-tuning to follow instructions): instruction dataset formatting. This is the "never done it, want to learn it" goal.
- [ ] **Thu** — **Ch 7**: instruction fine-tuning training loop + evaluating responses. **Book complete.**
- [ ] **Fri** — **FOUNDRY #3 (optional, resume line):** one small managed fine-tune in Foundry to say you've used the platform's fine-tuning workflow. **⚠️ DELETE the serving endpoint immediately after testing** — this is the one place a real bill can appear.
- [ ] **July 4 weekend:** Done. You built an LLM from scratch (incl. fine-tuning) and used Foundry end-to-end. Celebrate.

---

## Stretch goal (only if ahead, or for early July): local QLoRA

Connects the book to modern practice. After the book's *full* fine-tuning, try **parameter-efficient** fine-tuning on the 4070:
- [ ] Install `transformers` + `peft` + `bitsandbytes` + `trl`
- [ ] QLoRA-fine-tune a small (1–3B) model in 4-bit on a tiny dataset
- [ ] Story upgrade: "hand-coded the training loop in PyTorch, then applied LoRA to fine-tune a real model on my own GPU"

---

## Cost guardrails (so you can experiment with zero anxiety)

- **Serverless only** for Foundry inference (per-token = pennies for experimenting)
- **Local vector store** (Chroma/FAISS) for RAG = $0
- **Delete-when-done** for any fine-tuned/dedicated endpoint — never leave one provisioned idle
- The golden rule: *avoid anything that bills hourly-while-idle.* That's the only thing that can hurt you.
- Realistic total spend across all Foundry exercises: a couple of dollars, likely under one.

---

## If life happens (triage rules)

- The **book is the priority** — it's the harder-to-resume, higher-value, deeper-resume-signal thing. Protect book sessions; let Foundry float to early July if needed.
- A missed weekday is **not** a crisis — the weekend block is your built-in buffer.
- Plans bend. The point isn't perfect adherence; it's that your two-line note + git commit mean you **never start over**. That single thing gets you to the finish line.

---

## PROGRESS.md template (paste into your project root)

```
# Progress Log

## Next session — START HERE
- Stopped at:
- Next:

## History
- 2026-06-08: Setup done. GPU confirmed. Next: Ch 1.
```