"""Writes docs/index.html (French) and docs/en.html (English) of the HumanProof page from one template.
Usage: python -I tools/gen_pages.py <repository folder>"""
import html
import re
import sys

REPO = "https://github.com/vpan-utbm/knock-knock"
SITE = "https://vpan-utbm.github.io/knock-knock"

FR = dict(
    lang="fr", page="", banner="banner-fr.png", here="Français", other="en.html", other_lang="en", other_label="English",
    title="HumanProof — J’écris, donc je suis",
    description="Manifeste pour un clavier qui sait qu’un humain a tapé, sans jamais dire qui.",
    kicker="Les Tables de la Loi",
    tagline="J’écris, donc je suis.",
    subtitle="Pour un clavier qui sait qu’un humain a tapé, sans jamais dire qui.",
    slogan="Ne prouvez pas qui vous êtes. Prouvez que vous êtes là.",
    laws_label="Les sept lois",
    laws=[
        ("La biométrie ne quitte jamais le clavier.", "Seul le verdict signé en sort ; les mesures naissent et meurent dans la puce."),
        ("Anonyme par défaut.", "On prouve « un vrai clavier », jamais « ce clavier-là »."),
        ("L’identité seulement par choix.", "Une clé distincte par service, impossible à relier d’un service à l’autre."),
        ("Un refus n’est jamais une accusation.", "Doigts froids, tremblements, handicap : « pas sûr », jamais « robot »."),
        ("Jamais obligatoire.", "Personne n’est exclu parce qu’il dicte, écrit avec les yeux ou tape autrement."),
        ("Ouvert.", "Un format public, que tout fabricant produit et que chacun vérifie, sans plateforme."),
        ("Une preuve d’humanité n’est pas un droit.", "Elle ne donne aucune autorité sur la machine de celui qui lit."),
    ],
    h_preamble="Préambule",
    preamble=[
        "Bientôt, plus personne ne saura distinguer en ligne l’humain de la machine. Les machines écrivent comme "
        "nous, imitent notre style, notre ponctuation, nos fautes. Les captchas tombent les uns après les autres.",
        "Les signaux de comportement, le rythme de frappe ou les mouvements de souris, sont mesurés sur la machine "
        "de celui qu’on veut juger : si elle ment, ils mentent avec elle. Une mesure faite chez l’imitateur ne "
        "prouve rien.",
    ],
    h_keyboard="Le Clavier qui atteste",
    steles=[
        ("Les capteurs du vivant", "La cadence, le point d’appui, la force, la température et le "
         "micro-tremblement du doigt. Un signal s’imite ; tous ensemble, bien moins."),
        ("La clé scellée", "Née dans la puce du clavier, elle n’en sort jamais, et le fabricant la certifie."),
        ("Le sceau du texte", "Le clavier signe ce qu’il a tapé, avec un défi du destinataire. Une lettre "
         "changée, et la signature tombe. Un copier-coller n’est pas certifié."),
    ],
    gloss="Ce n’est pas la preuve de qui a rédigé, c’est la preuve qu’un humain a tapé et en répond, comme une "
          "signature au bas d’un contrat. Une empreinte digitale sur ce que l’on écrit.",
    map_caption="Ce que voit le destinataire : chaque passage, et d’où il vient.",
    map=[
        ("typed", "Tapé à la main", "Madame, Monsieur, suite à notre échange du 12 novembre, je vous confirme "
         "mon accord sur les points 1 à 3."),
        ("pasted", "Collé, non tapé", "« Le prestataire livre sous trente jours à compter de la signature. »"),
        ("altered", "Tapé, puis modifié hors du clavier", "Je suis d’accord sur le point 4."),
    ],
    map_note="« Non tapé » décrit, n’accuse jamais : une citation se colle.",
    h_beyond="Au-delà du clavier",
    beyond="Souris, caméra, micro : chaque capteur peut signer ce qu’il capte, avec sa propre détection du vivant. "
           "Leur limite commune : ce qu’on rejoue devant le capteur, un écran ou un haut-parleur, passe pour du réel. "
           "Le clavier y échappe mieux, il faut un doigt sur la touche. On commence donc par lui.",
    h_call="L’Appel",
    call="Le courrier électronique est né en 1982 sans preuve d’expéditeur ; il a fallu attendre 2007, et des milliards "
         "de spams, pour l’ajouter. Ne refaisons pas l’erreur avec l’IA : prouvons qu’un humain est là avant d’ouvrir "
         "les vannes. "
         "Toutes les tentatives passées sont tombées sur la vie privée. Si la preuve d’humanité devient obligatoire, "
         "qu’elle le devienne sous cette forme, et pas sous une autre.",
    decree=[("Fabricants", "construisez-le."), ("Plateformes", "acceptez l’anonymat."),
            ("Législateurs", "protégez ceux qui ne peuvent pas taper.")],
    maxim="Les idées appartiennent à ceux qui les réalisent.",
    date="Donné sur la montagne, le treizième jour de novembre MMXXVI",
    aveu="Écrit avec l’aide d’une IA, et c’est justement pour ça qu’il faut ce clavier.",
    full=("Le manifeste complet", f"{REPO}/blob/main/MANIFESTE.md"),
    source=("Le dépôt", REPO),
    fine="Texte sous licence CC BY 4.0, polices sous licence SIL OFL 1.1. Cette page n’a aucun script, aucun "
         "cookie, et ne charge rien d’ailleurs.",
)

EN = dict(
    lang="en-GB", page="en.html", banner="banner-en.png", here="English", other="index.html", other_lang="fr",
    other_label="Français",
    title="HumanProof — I write, therefore I am",
    description="A manifesto for a keyboard that knows a human typed, without ever saying who.",
    kicker="The Tables of the Law",
    tagline="I write, therefore I am.",
    subtitle="For a keyboard that knows a human typed, without ever saying who.",
    slogan="Don’t prove who you are. Prove that you are there.",
    laws_label="The seven laws",
    laws=[
        ("Biometrics never leave the keyboard.", "Only the signed verdict does; the measurements are born and die in the chip."),
        ("Anonymous by default.", "It proves “a genuine keyboard”, never “this keyboard”."),
        ("Identity only by choice.", "A separate key for each service, impossible to link from one to another."),
        ("A refusal is never an accusation.", "Cold fingers, tremors, disability: “not sure”, never “robot”."),
        ("Never mandatory.", "No one is shut out for dictating, writing with their eyes or typing differently."),
        ("Open.", "A public format that any manufacturer can produce and anyone can verify, without a platform."),
        ("Proof of humanity is not a right.", "It grants no authority over the reader’s machine."),
    ],
    h_preamble="Preamble",
    preamble=[
        "Soon, no one online will be able to tell a human from a machine. Machines write as we do, imitating our "
        "style, our punctuation, our mistakes. CAPTCHAs are falling one after another.",
        "Behavioural signals, typing rhythm or mouse movements, are measured on the machine of the very person "
        "being judged: if it lies, they lie with it. A measurement taken on the imitator’s side proves nothing.",
    ],
    h_keyboard="The Keyboard that Attests",
    steles=[
        ("Liveness sensors", "Rhythm, where the finger lands, force, temperature and the finger’s "
         "micro-tremor. One signal can be imitated; all of them together, far less easily."),
        ("The sealed key", "Born in the keyboard’s chip, it never leaves it, and the manufacturer certifies it."),
        ("The seal of the text", "The keyboard signs what it typed, with a challenge from the recipient. "
         "Change one letter and the signature fails. Pasted text is not certified."),
    ],
    gloss="It is not proof of who drafted the words; it is proof that a human typed them and stands behind them, "
          "like a signature at the bottom of a contract. A fingerprint on what we write.",
    map_caption="What the recipient sees: every passage, and where it came from.",
    map=[
        ("typed", "Typed by hand", "Dear Sir or Madam, further to our conversation of 12 November, I confirm "
         "my agreement on points 1 to 3."),
        ("pasted", "Pasted, not typed", "“The supplier delivers within thirty days of signature.”"),
        ("altered", "Typed, then changed outside the keyboard", "I agree on point 4."),
    ],
    map_note="“Not typed” describes, never accuses: a quotation is pasted.",
    h_beyond="Beyond the keyboard",
    beyond="Mouse, camera, microphone: each sensor can sign what it captures, with its own liveness detection. "
           "Their common limit: whatever is replayed in front of the sensor, a screen or a loudspeaker, passes for real. "
           "The keyboard escapes it better: a finger must press the key. So we start there.",
    h_call="The Call",
    call="E-mail was born in 1982 with no proof of sender; it took until 2007, and billions of spam messages, to add "
         "one. Let us not repeat the mistake with AI: prove that a human is there before opening the floodgates. "
         "Every past attempt foundered on privacy. If proof of humanity becomes mandatory, let it be in this form "
         "and no other.",
    decree=[("Manufacturers", "build it."), ("Platforms", "accept anonymity."),
            ("Legislators", "protect those who cannot type.")],
    maxim="Ideas belong to those who bring them to life.",
    date="Given upon the mountain, this thirteenth day of November, MMXXVI",
    aveu="Written with the help of an AI, and that is precisely why this keyboard is needed.",
    full=("The full manifesto", f"{REPO}/blob/main/MANIFESTO.md"),
    source=("The repository", REPO),
    fine="Text licensed under CC BY 4.0, fonts under the SIL OFL 1.1. This page has no script, no cookie, and "
         "loads nothing from elsewhere.",
)

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII"]


def page(t):
    def e(s):
        if t["lang"] == "fr":  # French spacing: never break a line before : ; ! ? » or after «
            s = re.sub(r" ([:;!?»])", lambda m: " " + m.group(1), s).replace("« ", "« ")
        return html.escape(s)

    laws = "\n".join(
        f'            <li><span class="num" aria-hidden="true">{ROMAN[i]}</span>'
        f'<span class="law"><span class="visually-hidden">{ROMAN[i]}. </span>{e(t["laws"][i][0])}</span>'
        f'<span class="gloss-line">{e(t["laws"][i][1])}</span></li>' for i in range(7))
    steles = "\n".join(f'            <div class="stele"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["steles"])
    passages = "\n".join(
        f'            <p class="pm pm-{k}"><span class="pm-tag">{e(tag)}</span> {e(txt)}</p>' for k, tag, txt in t["map"])
    decree = "\n".join(f"            <dt>{e(a)}</dt><dd>{e(b)}</dd>" for a, b in t["decree"])
    preamble = "\n".join(
        f'          <p{" class=\"lettrine\"" if i == 0 else ""}>{e(p)}</p>' for i, p in enumerate(t["preamble"]))
    slogan_a, slogan_b = t["slogan"].split(". ", 1)
    langs = (f'<span aria-current="page">{e(t["here"])}</span>&nbsp;· '
             f'<a href="{t["other"]}" hreflang="{t["other_lang"]}" lang="{t["other_lang"]}">{e(t["other_label"])}</a>')
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; font-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'">
  <meta name="referrer" content="no-referrer">
  <meta name="color-scheme" content="light">
  <title>{e(t['title'])}</title>
  <meta name="description" content="{e(t['description'])}">
  <meta property="og:title" content="{e(t['title'])}">
  <meta property="og:description" content="{e(t['description'])}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE}/{t['page']}">
  <meta property="og:image" content="{SITE}/{t['banner']}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="alternate" hreflang="{t['other_lang']}" href="{t['other']}">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="sky">
    <nav class="lang">{langs}</nav>
    <h1>HumanProof</h1>
    <p class="tagline">{e(t['tagline'])}</p>
  </header>

  <main class="tables">
    <div class="tablet tablet-law">
      <div class="field">
        <div class="crown">
          <p class="kicker">{e(t['kicker'])}</p>
          <p class="subtitle">{e(t['subtitle'])}</p>
        </div>
        <section class="laws" aria-labelledby="h-laws">
          <h2 id="h-laws">{e(t['laws_label'])}</h2>
          <ol>
{laws}
          </ol>
        </section>
      </div>
    </div>

    <div class="tablet tablet-word">
      <div class="field">
        <div class="crown">
          <p class="slogan"><span>{e(slogan_a)}.</span> <span>{e(slogan_b)}</span></p>
        </div>
        <section aria-labelledby="h-preamble">
          <h2 id="h-preamble">{e(t['h_preamble'])}</h2>
{preamble}
        </section>
        <section aria-labelledby="h-keyboard">
          <h2 id="h-keyboard">{e(t['h_keyboard'])}</h2>
          <div class="steles">
{steles}
          </div>
          <p class="gloss">{e(t['gloss'])}</p>
          <figure class="proofmap">
            <figcaption>{e(t['map_caption'])}</figcaption>
{passages}
            <p class="pm-note">{e(t['map_note'])}</p>
          </figure>
        </section>
        <section aria-labelledby="h-beyond">
          <h2 id="h-beyond">{e(t['h_beyond'])}</h2>
          <p>{e(t['beyond'])}</p>
        </section>
        <section aria-labelledby="h-call">
          <h2 id="h-call">{e(t['h_call'])}</h2>
          <p>{e(t['call'])}</p>
          <dl class="decree">
{decree}
          </dl>
        </section>
        <div class="colophon">
          <p class="maxim">{e(t['maxim'])}</p>
          <p class="signature">Human After All</p>
          <div class="seal" aria-hidden="true">HP</div>
          <p class="date">{e(t['date'])}</p>
          <p class="aveu">{e(t['aveu'])}</p>
        </div>
      </div>
    </div>
  </main>

  <footer class="foot">
    <p class="links"><a href="{e(t['full'][1])}">{e(t['full'][0])}</a>&nbsp;· <a href="{e(t['source'][1])}">{e(t['source'][0])}</a>&nbsp;· {langs}</p>
    <p class="fine">{e(t['fine'])}</p>
  </footer>
</body>
</html>
"""


root = sys.argv[1]
for name, t in (("index.html", FR), ("en.html", EN)):
    with open(f"{root}/docs/{name}", "w", encoding="utf-8", newline="\n") as f:
        f.write(page(t))
print("ok")
