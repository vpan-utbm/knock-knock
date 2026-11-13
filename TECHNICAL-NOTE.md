# HumanProof — Technical note

*Draft 0.1, 13 November 2026 — by **Human After All**. Written with the help of an AI.*
*Companion to the [manifesto](MANIFESTO.md). It is meant to be broken: please say where it fails.*

---

## 1. Goal

A verifier receives a text and wants to know one thing: **a human finger, on a genuine keyboard, typed this text, now,
for me.** It must learn nothing else: not who the human is, not which keyboard, not how they type.

**Non-goals.** Proving who *thought* the words (a human may retype a machine's text, and is then answerable for it).
Proving identity (only by the user's choice, §6). Being mandatory (manifesto, principle 5).

## 2. Parties and trust

| Party | Trusted for | Not trusted for |
| --- | --- | --- |
| **Keyboard secure element (SE)** | holding keys, measuring liveness, keeping the text buffer, signing | nothing beyond its own boundary |
| **Host computer** | carrying messages | anything: it may be fully compromised, run an AI, alter or inject text |
| **Verifier** (a service, a mailbox, a form) | issuing challenges, checking proofs | learning biometrics or linking users |
| **Manufacturer** | certifying genuine keyboards, publishing revocations | seeing any text or proof |

## 3. Threat model

The adversary **controls the host entirely**, reads and alters all traffic, owns many keyboards, can run software at
scale, and can pay for some hardware attacks. Out of scope: coercion of the typist, and the typist choosing to retype
someone else's text (by design, §1).

What the design must make **expensive** rather than impossible (manifesto, §5): robotic fingers, replayed human
keystrokes, keys extracted from a chip in a laboratory.

## 4. Protocol

**4.1 Challenge.** The verifier sends `c = (nonce[16 bytes], verifier_origin, expiry)`. The host forwards it to the
keyboard. The keyboard shows that a signing session is open (an LED, ideally the origin on a small display).

**4.2 Typing.** While the session is open, the SE does three things, inside its boundary:

1. it keeps **its own text buffer**, applying a minimal, public editing model (characters, backspace, arrows, line
   breaks) and a **declared layout**, so the signed text is what the keys produced, not what the host claims;
2. it extracts **liveness features** for each press (rhythm and irregularity, contact point, force and travel curve,
   temperature, conductivity, micro-tremor), feeds them to a classifier, and **discards them** at the end of the session;
3. it marks the session **non-certifiable** if anything enters the buffer without a key press (paste, injected text).

**4.3 Signature.** On a physical "sign" key, the SE returns:

```
payload = { v: 1,
            text_hash: SHA-256(normalised buffer),
            layout: "fr-azerty" | ... | "raw-hid",
            challenge: c,
            verdict: "human" | "unsure" }
proof   = Sign_attestation(payload)        // COSE_Sign1, CBOR-encoded
```

No timings, no features, no device identifier, **no global counter**: freshness comes from the verifier's nonce, and a
counter shared across services would let them link proofs.

**4.4 Verification.** The verifier checks the signature against the manufacturers' published keys, that `c` is its own
unexpired nonce (once only), that `SHA-256(normalised text)` equals `text_hash`, and the revocation list. The result is
`human`, `unsure` (never "robot": principle 4), or invalid.

## 5. The attestation key: two options

The manifesto asks for two things at once: a key **born in the chip** that never leaves it, and **anonymity in a crowd**
of at least 100,000 keyboards. A group signature gives both; a FIDO-style batch key is simpler but gives up the first.

| | **A. Batch key (FIDO2 style)** | **B. Group signature (DAA / EPID style)** |
| --- | --- | --- |
| How | one private key injected into every keyboard of a batch | each keyboard's own key is born in the chip and joined to a group; signatures do not reveal which member |
| Anonymity | the batch | the whole group |
| One key extracted | the whole batch must be revoked | that one keyboard can be revoked |
| Maturity | standard, cheap secure elements support it | used in TPMs (DAA) and Intel EPID; fewer off-the-shelf chips |

**Proposal: A for the prototype, B as the target.**

## 6. Identity, only by choice

A user who wants to sign in their own name adds, per service, a separate key pair created in the SE (as with a passkey).
The proof then carries two signatures: the anonymous attestation ("a human typed") and the per-service key ("Alice on
this service"). Two services cannot link the keys.

## 7. Carrying the proof

- **Web forms and APIs:** the proof travels next to the text; the challenge comes from the page that receives it.
- **Documents and media:** as a C2PA assertion, so that existing provenance tools can display "typed by a human".
- **Email and messaging:** an attached proof; the recipient's challenge needs a round trip, or a published per-recipient
  nonce (open problem).

## 8. A prototype that anyone could build

A QMK or ZMK keyboard with **Hall-effect switches** (they already measure travel continuously), force sensors, and a
secure element such as the ATECC608B (ECDSA P-256, option A). Honest limit: on such a board the keyboard firmware runs
outside the secure element, so a compromised firmware can inject keys. The prototype proves the flow and the user
experience, not the security. The real product needs the scan matrix, the buffer and the classifier inside the
secure boundary, as payment-terminal keypads already do.

## 9. Open problems

1. **Editing.** Real writing is not linear: mouse clicks, selections, editing the middle of a paragraph, autocorrect.
   The minimal editing model of §4.2 does not cover them. Which model is rich enough and still verifiable?
2. **Layouts and input methods.** Dead keys, AltGr, input methods for Chinese or Japanese. Sign raw key codes and
   let the verifier replay them? That leaks more than a hash.
3. **Robots and replays.** How expensive must a robotic finger be before it stops mattering? This is the arms race
   the manifesto admits.
4. **Who decides "human"?** The classifier, its thresholds and its error rates (ISO/IEC 30107 measures both kinds of
   error) must be public and testable, or the verdict is an act of faith.
5. **Accessibility.** The path for those who cannot type (principle 5) needs its own design, not a footnote.
6. **Trusting what you sign.** The host may display a different text from the one in the SE buffer. A small display
   on the keyboard, or a read-back, may be needed.

## 10. Prior art

Signing keystrokes: Intel (US 2014/0115662 A1, priority 2008, abandoned), Lawrence Livermore National Laboratory
(US 12,476,822 B2, 2025), *Suppressing Bot Traffic with Accurate Human Attestation* (ACM, 2010), *Privacy-Preserving
Proof of Human Authorship via Zero-Knowledge Process Attestation* (arXiv 2603.00179, 2026). Hardware pieces: payment
keypads, Apple's Magic Keyboard with Touch ID, C2PA cameras, FIDO batch attestation, TPM Direct Anonymous Attestation.

What we have not found is the assembly: **liveness sensors in the keys, bound to the signature of the typed text and a
recipient's challenge.** If it exists, where is it? Tell us, and we will cite it.

---

*Text licensed under CC BY 4.0. Comments, objections and corrections: open an issue on this repository.*
