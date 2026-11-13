# HumanProof — Technical note

*Draft 0.2, 13 November 2026 — by **Human After All**. Written with the help of an AI.*
*Companion to the [manifesto](MANIFESTO.md). It is meant to be broken: please say where it fails.*

---

## 1. Goal

A verifier receives a text and wants to know one thing: **a human finger, on a genuine keyboard, typed this text, now,
for me.** It must learn nothing else: not who the human is, not which keyboard, not how they type.

**Non-goals.** Proving who *thought* the words (a human may retype a machine's text, and is then answerable for it).
Proving identity (only by the user's choice, §7). Being mandatory (manifesto, principle 5).

## 2. Parties and trust

| Party | Trusted for | Not trusted for |
| --- | --- | --- |
| **Keyboard secure element (SE)** | holding keys, measuring liveness, chaining the typed segments, signing | nothing beyond its own boundary |
| **Host computer** | carrying messages | anything: it may be fully compromised, run an AI, alter or inject text |
| **Verifier** (a service, a mailbox, a form) | issuing challenges, checking proofs | learning biometrics or linking users |
| **Manufacturer** | certifying genuine keyboards, publishing revocations | seeing any text or proof; deciding alone what counts as "human" (§6) |
| **Accredited test laboratory** | testing the liveness classifier, publishing its error rates (§6) | any online role: it never sees a text or a proof |

## 3. Threat model

The adversary **controls the host entirely**, reads and alters all traffic, owns many keyboards, can run software at
scale, and can pay for some hardware attacks. Out of scope: coercion of the typist, and the typist choosing to retype
someone else's text (by design, §1).

What the design must make **expensive** rather than impossible (manifesto, §5): robotic fingers, replayed human
keystrokes, keys extracted from a chip in a laboratory.

## 4. Protocol

**4.1 Challenge.** The verifier sends `c = (nonce[16 bytes], verifier_origin, expiry)`. The host forwards it to the
keyboard. A light on the keyboard is on while a session is open, like a webcam's. No screen is needed: the typist
signs what they typed themselves, so they already know the text (unlike a bank's signature pad, where one signs a
document written by someone else).

**4.2 Typing, in segments.** Real writing is not linear: one types, clicks elsewhere, fixes a word, comes back. The SE
does not try to follow the document. It cuts what the keys produce into **segments**: a segment is a run of typed text,
closed by a navigation key (arrows, Home, End, Page Up/Down), a pause longer than a threshold, or the end of the
session. Backspaces inside a run are applied to it. For each segment, inside its boundary, the SE:

1. turns key codes into text with a **declared layout**, so the segment is what the keys produced, not what the host
   claims;
2. extends a **hash chain**: `h_0 = H(c)`, then `h_i = H(h_(i-1) || H(segment_i))`, so that the order in which the
   segments were typed is sealed;
3. extracts **liveness features** for each press (rhythm and irregularity, contact point, force and travel curve,
   temperature, conductivity, micro-tremor), feeds them to the certified classifier (§6), and **discards them** at the end
   of the session.

Text that reaches the document without a key press (paste, injection, autocorrect) belongs to no segment.

**4.3 Signature.** On a physical "sign" key, the SE returns:

```
payload = { v: 2,
            chain: h_n,  segments: n,
            layout: "fr-azerty" | ... | "raw-hid",
            challenge: c,
            verdict: "human" | "unsure",
            cert_level: <the classifier's certification, §6> }
proof   = Sign_attestation(payload)        // COSE_Sign1, CBOR-encoded
```

Alongside the proof, the host sends the final text, the hash of each segment, and where each surviving segment sits in
the final text. **The text of deleted segments is never sent**, only their hash: what you typed and then erased stays
yours.

No timings, no features, no device identifier, **no global counter**: freshness comes from the verifier's nonce, and a
counter shared across services would let them link proofs.

**4.4 Verification.** The verifier checks the signature against the manufacturers' published keys and the revocation
list, that `c` is its own unexpired nonce (once only), and recomputes the chain from the segment hashes. Then it reads the
final text against the segments and reports a **provenance map**:

- **intact**: this passage is a typed segment, unchanged;
- **altered**: a typed segment no longer matches, at this exact place;
- **not typed**: this passage belongs to no segment;
- plus the share of the final text covered by intact segments, and the order in which the passages were typed.

This is what defeats the **"ransom note" attack**: a compromised host that deletes words from an honest text to change
its meaning ("I am **not** guilty") breaks a segment exactly where it cuts. The verdict is `human` or `unsure` (never
"robot": principle 4), or invalid.

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

## 6. Who decides "human"?

The liveness classifier sits in the manufacturer's chip. Whoever sets its threshold decides who passes for human: that is
a power, and it must not belong to the manufacturer alone.

- **Independent certification.** Classifiers are tested by **accredited independent laboratories**, against
  ISO/IEC 30107-3 (presentation attack detection: robots, replays, fake fingers) and ISO/IEC 19795-1 (error rates). This
  already exists for fingerprint and face sensors: the FIDO Alliance runs a Biometric Component Certification programme
  with labs it accredits, and caps the false-reject rate. Typing liveness would be a new modality in an existing scheme.
- **Published numbers.** Thresholds, false-reject rate (humans told "unsure") and attack-acceptance rate are public
  for each certified model.
- **The verifier chooses.** The proof carries the certification level; each verifier decides which levels it accepts.
- **Offline only.** The laboratory certifies models, never sees a text or a proof, and has no server to call: nothing
  to track.

## 7. Identity, only by choice

A user who wants to sign in their own name adds, per service, a separate key pair created in the SE (as with a passkey).
The proof then carries two signatures: the anonymous attestation ("a human typed") and the per-service key ("Alice on
this service"). Two services cannot link the keys.

## 8. Carrying the proof

- **Web forms and APIs:** the proof travels next to the text; the challenge comes from the page that receives it.
- **Documents and media:** as a C2PA assertion, so that existing provenance tools can display "typed by a human".
- **Email and messaging:** an attached proof; the recipient's challenge needs a round trip, or a published per-recipient
  nonce (open problem).

## 9. A prototype that anyone could build

A QMK or ZMK keyboard with **Hall-effect switches** (they already measure travel continuously), force sensors, and a
secure element such as the ATECC608B (ECDSA P-256, option A). Honest limit: on such a board the keyboard firmware runs
outside the secure element, so a compromised firmware can inject keys. The prototype proves the flow and the user
experience, not the security. The real product needs the scan matrix, the buffer and the classifier inside the
secure boundary, as payment-terminal keypads already do.

## 10. A precedent: signature pads in banks

Banks already collect handwritten signatures on electronic pads that record pressure, movement and speed. Two of their
ideas carry over, one does not.

- **Bind before capture.** The pad's software hashes the document before the pen touches the pad, and any change to
  the document invalidates the signature (Wacom Signature SDK). This is our recipient's challenge.
- **Open formats matter.** Court experts can often read a pad's biometric data only with its vendor's own tool: an
  argument for principle 6.
- **Not the biometric escrow.** In Italy, the *firma grafometrica* encrypts the biometric data for a trusted third
  party, opened only by order of a judge; the data-protection authority accepted the scheme in 2013. We do not copy
  it: the biometrics would leave the keyboard (principle 1) and the escrow would become a target. But it shows that
  the law already knows how to frame biometric signatures.

## 11. Open problems

1. **Segment size.** Long segments catch more tampering but break on honest edits; short ones survive edits but let a
   host reorder words. Which closing rules (pause threshold, keys) balance the two? And segment boundaries reveal
   where one paused: a coarse timing leak.
2. **Layouts and input methods.** Dead keys, AltGr, input methods for Chinese or Japanese. Sign raw key codes and
   let the verifier replay them? That leaks more than a hash.
3. **Robots and replays.** How expensive must a robotic finger be before it stops mattering? This is the arms race
   the manifesto admits.
4. **Autocorrect and predictive text.** Host-side corrections create "not typed" passages. Should they be marked as
   such, or should correction move into the keyboard?
5. **Accessibility.** The path for those who cannot type (principle 5) needs its own design, not a footnote.
6. **Redirected proofs.** A compromised host can send a genuinely typed text to a different recipient than the one the
   typist believes. The light shows that a session is open, not for whom. Accepted for now: each redirected text
   still costs a human gesture, so it cannot scale.

## 12. Prior art

Signing keystrokes: Intel (US 2014/0115662 A1, priority 2008, abandoned), Lawrence Livermore National Laboratory
(US 12,476,822 B2, 2025), *Suppressing Bot Traffic with Accurate Human Attestation* (ACM, 2010), *Privacy-Preserving
Proof of Human Authorship via Zero-Knowledge Process Attestation* (arXiv 2603.00179, 2026). Hardware pieces: payment
keypads, bank signature pads, Apple's Magic Keyboard with Touch ID, C2PA cameras, FIDO batch attestation and
biometric certification, TPM Direct Anonymous Attestation.

What we have not found is the assembly: **liveness sensors in the keys, bound to the signature of the typed text and a
recipient's challenge.** If it exists, where is it? Tell us, and we will cite it.

---

*Text licensed under CC BY 4.0. Comments, objections and corrections: open an issue on this repository.*
