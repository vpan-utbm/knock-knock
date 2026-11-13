# HumanProof — Manifesto

> ## I write, therefore I am.

*For a keyboard that knows a human typed, without ever saying who.*

13 November 2026 — by **Human After All**

*Written with the help of an AI, and that is precisely why this keyboard is needed.*

---

## 1. The observation

Soon, no one online will be able to tell a human from a machine.

Language models write as we do, imitating our style, our punctuation, our mistakes. CAPTCHAs are falling one
after another. Behavioural signals (typing rhythm, mouse movements) are measured **on the machine of the very
person being judged**: if that machine lies, they lie with it. A measurement taken on the adversary's side
proves nothing.

What we need is proof that the imitator cannot forge.

## 2. The principle

Proof of humanity does not say **who drafted** a text. It says **that a human typed it and stands behind it**.

This is the logic of a signature at the bottom of a contract: the lawyer drafted it, the one who signs is
bound by it. Whether a human copies out what a machine whispered to them changes nothing: they are the one
writing it, they are the one answerable for it.

And every certified text costs a human gesture. A machine on its own can no longer act at scale.

## 3. The proposal: a keyboard that attests

A digital fingerprint, left by the finger on what it writes.

1. **Liveness sensors in the keys.** Rhythm and its irregularity, where the finger lands (never quite in the
   centre), the force and travel curve of each press, the temperature, conductivity and micro-tremor of the
   finger. Any one signal can be imitated; all of them together, in real time, far less easily. This is the
   liveness detection that fingerprint readers already perform (ISO/IEC 30107), extended to typing.
2. **A key born in the keyboard's chip**, which never leaves it, certified by the manufacturer.
3. **The keyboard itself signs what it typed**: the hash of the text, the "human finger" verdict, a counter
   and a challenge sent by the recipient. If the computer alters a single character, the signature no longer
   verifies. Pasted text is not certified. An old signature cannot be replayed.
4. **Anyone can verify it**, using the manufacturer's certificate chain: "typed by a human, on a genuine
   keyboard".

The computer merely carries the message. It can neither lie about the measurement nor tamper with the text.

## 4. The seven principles

Poorly designed proof of humanity becomes a surveillance tool. This one rests on seven non-negotiable
principles.

1. **Biometrics never leave the keyboard.** Only the signed verdict does. The measurements are sensitive data:
   they are born and die in the chip.
2. **Anonymous by default.** Attestation keys are shared across batches (at least 100,000 keyboards, as with
   FIDO2): it proves "a genuine keyboard", never "this keyboard".
3. **Identity only by choice.** Those who wish to sign in their own name add a separate key for each service,
   which cannot be linked from one service to another.
4. **A refusal is never an accusation.** Cold fingers, gloves, tremors, disability: the keyboard says
   "not sure", never "robot".
5. **Never mandatory.** A signed text carries more weight; an unsigned text still counts. No one is shut out
   because they dictate, write with their eyes or use an adapted keyboard.
6. **Open.** A public signature and verification format that any manufacturer can produce and anyone can
   verify, without going through a platform.
7. **Proof of humanity is not a right.** Knowing that a human typed a text gives them no authority over the
   machine of the person reading it. Decisions never travel through a channel where one could be impersonated.

## 5. What it proves, and what it does not

**Proven:** a human finger, on a genuine keyboard, typed this text, at this moment, for this recipient.

**Not proven:**
- who drafted the words;
- who the human is, unless they choose to say.

**The limits, stated plainly:**
- A robotic arm with a heated finger, or human keystrokes recorded and replayed: this will be an arms race,
  as with CAPTCHAs. The aim is not the impossible; it is to make cheating expensive.
- A key extracted from a chip in a laboratory can sign whatever it likes: revocation lists are needed.
- The keyboard does not know letters, only keys (AZERTY, QWERTY, dead keys, input methods for Asian
  languages): it must know the layout, or sign the raw key codes.

## 6. Beyond the keyboard

The principle holds for every input device: **each sensor signs what it captured itself, with its own liveness
detection**, and the seven principles apply unchanged.

| Device | Sign of life | What exists | The trap |
| --- | --- | --- | --- |
| Keyboard | rhythm, where the finger lands, force, finger temperature | patents on signing keystrokes, nothing assembled | a robotic arm, costly and slow |
| Mouse | the hand's physiological tremor (8 to 12 Hz, present in every human), micro-corrections | mouse-behaviour analysis, in software, hence forgeable | a robot adding a fake tremor |
| Camera | depth, real light on the sensor | signing at the moment of capture (C2PA) on some cameras and smartphones | filming a screen: the photo of a fake is faithfully signed |
| Microphone | breath, the pop of consonants close to the mic, the acoustics of the room | research against voice spoofing | playing a synthetic voice through a loudspeaker |

Their common limit is known as the **analogue hole**: whatever can be replayed in front of a sensor passes for
real. A camera signs the photo of a screen as readily as that of a face; a microphone records a loudspeaker as
readily as a throat. The keyboard escapes it better, because a physical finger must press the key. That is why
this manifesto starts there: it is the easiest to prove, and the first to build.

## 7. Why now

The idea is not new, and its pieces already exist.

- **Signing keystrokes**: Intel proposed it as early as 2008 (a motherboard chip signing keyboard activity;
  application abandoned). An American laboratory was granted a patent in 2025 on signing text of human origin.
  Researchers described a trustworthy keyboard against bots as early as 2010.
- **The hardware**: payment terminal keypads encrypt every key in their own chip; some keyboards are already
  cryptographically paired with the computer's secure chip; trackpads and keyboards measure force; cameras
  sign their images at the moment of capture (C2PA).

What is missing is the assembly: **liveness sensors in the keys, bound to the signature of the typed text.**

Past attempts all failed at the same point: privacy. The Pentium III serial number (1999), Palladium's
"trusted computing" (2002–2005), Google's Web Environment Integrity (2023): all withdrawn amid protest. They
certified the machine, or tracked the user.

Two things have changed:
- **The need has exploded.** Before language models, CAPTCHAs were enough. Not any more.
- **Obligation is coming.** It is already arriving de facto, through platforms: apps refuse uncertified
  devices without any law having required it. And it is arriving through legislation: age verification in
  France, labelling of AI-generated content in Europe.

If proof of humanity becomes mandatory, the only question is **in what form**: an anonymous attestation that
keeps biometrics inside the keyboard, or a unique identifier that tracks every text. That choice is being made
now, as the first designs appear. A privacy-respecting design that exists before the law has every chance of
becoming the standard. Otherwise, we inherit whichever comes first.

France has shown it can be done: in imposing age verification, it required a double-anonymity option. An
obligation can respect privacy, if someone insists on it from the start.

## 8. The call

To the makers of keyboards, computers and chips: build it, and honour these seven principles.

To platforms: accept anonymous proof, never demand identity.

To legislators: if you ever make it mandatory, mandate anonymity by default, biometrics kept on the device,
and a path for those who cannot type.

This manifesto claims nothing. **Ideas belong to those who bring them to life.**

---

## References

- Intel, *Mechanism for Detecting Human Presence Using Authenticated Input Activity Timestamps*,
  US 2014/0115662 A1, priority 2008, abandoned: https://patents.google.com/patent/US20140115662
- Lawrence Livermore National Laboratory, *Differentiation between human-generated and AI-generated text*,
  US 12,476,822 B2, 18/11/2025:
  https://ipo.llnl.gov/technologies/it-and-communications/system-cryptographically-distinguish-between-human-generated
- *Suppressing Bot Traffic with Accurate Human Attestation* (ACM):
  https://dl.acm.org/doi/pdf/10.1145/1851276.1851287
- *Privacy-Preserving Proof of Human Authorship via Zero-Knowledge Process Attestation* (arXiv, 2026):
  https://arxiv.org/html/2603.00179
- Apple, *Keyless keyboard with force sensing and haptic feedback*, US 11,500,538 (2022):
  https://patents.justia.com/patent/11500538
- Apple Platform Security, *Magic Keyboard with Touch ID*:
  https://support.apple.com/guide/security/magic-keyboard-with-touch-id-secf60513daa/web
- ISO/IEC 30107, presentation attack detection (liveness detection in biometrics).
- FIDO Alliance, batch attestation of authenticators.
