# HumanProof — The objections

*The questions we will be asked, and our answers, limits included. For the detail: the [manifesto](MANIFESTO.md) and
the [technical note](TECHNICAL-NOTE.md).*

---

## 1. "This already exists."

Pieces of it do, and the manifesto cites them. Intel proposed as early as 2008 that a motherboard chip sign keyboard
activity (patent application abandoned). An American laboratory, LLNL, was granted a patent in 2025 on signing text of
human origin (US 12,476,822 B2). Researchers described a trustworthy keyboard against bots as early as 2010. Payment
terminal keypads encrypt every key in their own chip, and some keyboards are already cryptographically paired with the
computer's secure chip.

What we have not found is the assembly: **liveness sensors in the keys, bound to the signature of the typed text, with
a challenge from the recipient**, and the seven principles that stop it becoming a surveillance tool. Where is that
patent? If you know of it, tell us: we will cite it.

## 2. "You can just retype an AI's text."

Yes, and that is by design. HumanProof does not prove **who thought** the words; it proves **that a human typed them
and stands behind them**, like a signature at the bottom of a contract the lawyer drafted. The manifesto says so from
§2, and is its own example: written with the help of an AI, then typed, read and signed by a human.

What it changes: every certified text costs a human gesture. A machine alone can no longer turn out thousands of
"human" texts on a production line.

## 3. "This is Google's Web Environment Integrity."

No, and the difference is precise. Web Environment Integrity (proposed in 2023, dropped by Google on 2 November 2023
after a strong backlash) had **the user's software** certified: the browser and the operating system. A site could have
refused a modified browser, an ad blocker, a free operating system.

Here the computer is **never attested**: the technical note treats it as fully hostile (§2 and §3). Only the
keyboard's chip attests a single fact about a single text: a human finger typed it. It says nothing about your browser,
your system or your software, and gives no authority over the reader's machine (law VII).

What we concede: nothing technical stops a platform from requiring this proof one day. "Never mandatory" (law V) is a
demand on platforms and legislators, not a guarantee of the protocol. That is exactly why an anonymous form must exist
**before** the obligation arrives: otherwise we inherit whichever comes first.

## 4. "It's DRM for humans."

DRM forbids you from doing something on your own device. This keyboard forbids nothing: you type as before, you paste,
you correct, you send an unsigned text, which still counts (law V). It attests only when asked, and the proof follows
the text, not the user. The format is open: any manufacturer can produce it, anyone can verify it, without going through
a platform (law VI).

## 5. "Watermarking AI text is enough."

Watermarking (a mark hidden in the choice of words) needs the goodwill of **every** AI maker. A single refusal is
enough: an open model or a hostile actor will mark nothing. And a study published in 2025 (Sadasivan et al., TMLR)
shows that paraphrasing by another AI often erases the mark, and that human text can even be made to pass for AI text.

Proof of humanity asks nothing of anyone on the AI side. We are not slowing AI down; we are protecting the human. The
two can coexist: watermarking flags AI when it cooperates, proof of humanity works even when it does not.

## 6. "The manufacturer holds the key: it can cheat."

The risk is real, and the technical note deals with it in three points:
- **The key.** The target is for each keyboard to have its own key, born in its chip, joined to a group signature of at
  least 100,000 keyboards: the proof says "a genuine keyboard", never "this keyboard", and a stolen key can be revoked
  on its own. A key shared by batch, simpler, is for the prototype only.
- **Who decides you are human.** The liveness threshold must not belong to the manufacturer alone. Classifiers are
  tested by **accredited independent laboratories** (ISO/IEC 30107-3 and 19795-1), as fingerprint sensors are today.
  Thresholds and error rates are published, and each recipient chooses the levels it accepts.
- **What it sees.** Neither the manufacturer nor the laboratory ever sees a text or a proof.

The limit, stated plainly: you have to trust the chip, as we already do with a payment terminal.

## 7. "A robot can press the keys."

Yes: a robotic arm with a heated finger, or human keystrokes recorded and replayed. It will be an arms race, as with
CAPTCHAs. The aim is not the impossible; it is to make cheating **expensive and slow**: a robot typing one text at a
time does not replace a bot farm.

## 8. "What if my computer is compromised?"

That is the case the design is built for. The computer merely carries the message: if it changes a single character of
the typed text, the signature breaks at the exact place of the change. Nor can it pass off pasted or injected text as
typed.

One limit remains open (technical note, §12): a compromised computer can send a genuinely typed text to a different
recipient than the one you think. The keyboard's light shows that a session is open, not for whom. Each redirected text
still costs a human gesture: it does not scale.

## 9. "What about what I paste, quotations?"

Nothing is forbidden; everything is shown. The recipient sees, passage by passage, what was typed, what was pasted and
what was changed outside the keyboard. "Not typed" describes, never accuses: a quotation is pasted.

## 10. "What about those who cannot type?"

No one is shut out because they dictate, write with their eyes or use an adapted keyboard: an unsigned text still
counts (law V), and a refusal from the keyboard says "not sure", never "robot" (law IV). The manifesto asks legislators,
if they ever make the proof mandatory, to mandate a path for those who cannot type as well.

What we concede: that path has not been designed yet. It deserves its own work, not a footnote (technical note, §12).

## 11. "Why not World ID?"

World ID scans your iris to prove you are a unique person. An iris cannot be changed: if it leaks, it leaks for ever.
And you have to stand in front of the company's device, the Orb, to be enrolled.

HumanProof needs no enrolment and no registry: biometrics are born and die in the keyboard's chip, and only the verdict
leaves it (law I). Don't prove who you are; prove that you are there.

What we concede: HumanProof does not prove uniqueness. One person with ten keyboards can sign with all ten. It proves a
human gesture, not "one person, one account".

## 12. "Who are you?"

Human After All is the name signing the manifesto: one person, not a company, with nothing to sell. The repository sits
under the GitHub account `vpan-utbm`, with no attempt to hide it. The manifesto was written with the help of an AI, then
typed, read and signed by a human.

It claims nothing: no patent, no product. Ideas belong to those who bring them to life.
