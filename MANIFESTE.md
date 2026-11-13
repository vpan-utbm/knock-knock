# HumanProof — Manifeste

> ## J'écris, donc je suis.

*Pour un clavier qui sait qu'un humain a tapé, sans jamais dire qui.*

13 novembre 2026 — par **Human After All**

*Écrit avec l'aide d'une IA, et c'est justement pour ça qu'il faut ce clavier.*

---

## 1. Le constat

Bientôt, plus personne ne saura distinguer en ligne l'humain de la machine.

Les modèles de langage écrivent comme nous, imitent notre style, notre ponctuation, nos fautes. Les captchas
tombent les uns après les autres. Les signaux de comportement (le rythme de frappe, les mouvements de souris)
sont mesurés **sur la machine de celui qu'on veut juger** : si cette machine ment, ils mentent avec elle. Une
mesure faite chez l'adversaire ne prouve rien.

Il faut une preuve que l'imitateur ne peut pas fabriquer.

## 2. Le principe

Une preuve d'humanité ne dit pas **qui a rédigé** un texte. Elle dit **qu'un humain l'a tapé et en répond**.

C'est la logique de la signature au bas d'un contrat : l'avocat l'a rédigé, celui qui signe s'engage. Qu'un
humain recopie ce qu'une machine lui a soufflé ne change rien : c'est lui qui l'écrit, c'est lui qui en répond.

Et chaque texte certifié coûte un geste humain. Une machine seule ne peut plus agir à la chaîne.

## 3. La proposition : le clavier qui atteste

Une empreinte digitale numérique, posée par le doigt sur ce qu'il écrit.

1. **Des capteurs de vivant dans les touches.** La cadence et son irrégularité, le point d'appui (jamais
   exactement au centre), la force et la courbe d'enfoncement, la température, la conductivité et le
   micro-tremblement du doigt. Un signal seul s'imite ; tous ensemble, en temps réel, beaucoup plus
   difficilement. C'est la détection du vivant que les lecteurs d'empreintes pratiquent déjà
   (ISO/IEC 30107), étendue à la frappe.
2. **Une clé née dans la puce du clavier**, qui n'en sort jamais, certifiée par le fabricant.
3. **Le clavier signe lui-même ce qu'il a tapé** : l'empreinte (le hash) du texte, le verdict « doigt
   humain » et un défi envoyé par le destinataire. Si l'ordinateur retouche un seul caractère, la signature
   ne vérifie plus. Un copier-coller n'est pas certifié. Le défi, neuf à chaque fois, empêche de rejouer une
   signature ancienne ; pas de compteur, qui permettrait de relier les textes d'une même personne.
4. **N'importe qui vérifie**, avec la chaîne de certificats du fabricant : « tapé par un humain, sur un
   clavier authentique ».

L'ordinateur ne fait que transporter. Il ne peut ni mentir sur la mesure, ni falsifier le texte.

## 4. Les sept principes

Une preuve d'humanité mal conçue devient un outil de surveillance. Celle-ci tient à sept principes, non
négociables.

1. **La biométrie ne quitte jamais le clavier.** Seul le verdict signé en sort. Les mesures sont des données
   sensibles : elles naissent et meurent dans la puce.
2. **Anonyme par défaut.** Chaque clavier garde sa propre clé, mais signe au nom d'un groupe d'au moins
   100 000 claviers (une signature de groupe, comme l'attestation anonyme des puces TPM des ordinateurs) : on
   prouve « un vrai clavier », jamais « ce clavier-là ». Une clé volée se révoque seule, sans toucher aux autres.
3. **L'identité seulement par choix.** Celui qui veut signer de son nom ajoute une clé distincte par service,
   impossible à relier d'un service à l'autre.
4. **Un refus n'est jamais une accusation.** Doigts froids, gants, tremblements, handicap : le clavier dit
   « pas sûr », jamais « robot ».
5. **Jamais obligatoire.** Un texte signé vaut davantage ; un texte non signé vaut toujours. Personne n'est
   exclu parce qu'il dicte, écrit avec les yeux ou utilise un clavier adapté.
6. **Ouvert.** Un format de signature et de vérification public, que tout fabricant peut produire et que
   chacun peut vérifier, sans passer par une plateforme.
7. **Une preuve d'humanité n'est pas un droit.** Savoir qu'un humain a tapé un texte ne lui donne aucune
   autorité sur la machine de celui qui le lit. La décision ne passe jamais par le canal où l'on pourrait se
   faire imiter.

## 5. Ce que cela prouve, et ce que cela ne prouve pas

**Prouvé :** un doigt humain, sur un clavier authentique, a tapé ce texte-là, à ce moment-là, pour ce
destinataire-là.

**Et passage par passage.** Sur n'importe quel texte, une lettre, un mémoire, un contrat, le destinataire voit
ce qui a été tapé à la main, ce qui a été collé, et ce qui a été modifié hors du clavier, à l'endroit exact.
On n'interdit rien, on montre. « Non tapé » décrit, n'accuse jamais : une citation se colle.

**Pas prouvé :**
- qui a rédigé les mots ;
- qui est l'humain, sauf s'il le choisit.

**Les limites, dites franchement :**
- Un bras robot avec un doigt chauffé, une frappe humaine enregistrée puis rejouée : ce sera une course aux
  armements, comme pour les captchas. Le but n'est pas l'impossible, c'est de rendre la triche chère.
- Une clé arrachée à une puce en laboratoire signe ce qu'elle veut : il faut des listes de révocation.
- Le clavier ne connaît pas les lettres, seulement les touches (AZERTY, QWERTY, touches mortes, saisie des
  langues asiatiques) : il doit connaître la disposition, ou signer les codes bruts.

## 6. Au-delà du clavier

Le principe vaut pour tout périphérique d'entrée : **chaque capteur signe ce qu'il a lui-même capté, avec sa propre
détection du vivant**, et les sept principes s'y appliquent tels quels.

| Périphérique | Signe du vivant | Ce qui existe | Le piège |
| --- | --- | --- | --- |
| Clavier | la cadence, le point d'appui, la force, la température du doigt | des brevets sur la signature des frappes, rien d'assemblé | le bras robot, coûteux et lent |
| Souris | le tremblement physiologique de la main (8 à 12 Hz, présent chez tout humain), les micro-corrections | l'analyse du comportement de la souris, côté logiciel, donc falsifiable | un robot qui ajoute un faux tremblement |
| Caméra | la profondeur, la vraie lumière sur le capteur | la signature à la prise de vue (C2PA) sur certains appareils photo et smartphones | filmer un écran : on signe fidèlement la photo d'un faux |
| Micro | le souffle, l'impact des consonnes près du micro, l'acoustique de la pièce | la recherche contre l'usurpation de la voix | diffuser une voix de synthèse par un haut-parleur |

Leur limite commune s'appelle le **trou analogique** : ce qu'on peut rejouer devant un capteur passe pour du réel.
Une caméra signe aussi bien la photo d'un écran que celle d'un visage ; un micro enregistre aussi bien un
haut-parleur qu'une gorge. Le clavier y échappe mieux, parce qu'il faut un doigt physique sur la touche. C'est
pourquoi ce manifeste commence par lui : c'est le plus facile à prouver, et le premier à construire.

**La boîte noire des agents.** Demain, des agents d'IA conduiront des systèmes critiques, un réseau électrique,
un hôpital, une salle de marché, sous la surveillance d'humains. Un agent n'a pas de doigt : dans le journal
des actions, la preuve dira quelle commande un humain a tapée, et laquelle vient de l'agent. Le jour d'un
accident, on saura qui a fait quoi. Pas qui est responsable : un « oui » tapé sans lire reste un « oui » ; mais
l'enquête partira de faits, pas de suppositions. C'est aussi ce que l'Europe exige : l'AI Act impose un contrôle
humain effectif des IA à haut risque (article 14, à partir de décembre 2027). Encore faudra-t-il le prouver.

## 7. Pourquoi maintenant

L'idée n'est pas neuve, et ses morceaux existent déjà.

- **Signer les frappes** : Intel l'a proposé dès 2008 (puce de la carte mère qui signe l'activité du
  clavier ; demande abandonnée). Un laboratoire américain a obtenu en 2025 un brevet sur la signature d'un
  texte d'origine humaine. Des chercheurs ont décrit dès 2010 un clavier de confiance contre les bots.
- **Les pièces matérielles** : les claviers de terminal de paiement chiffrent chaque touche dans leur propre
  puce ; certains claviers sont déjà appairés par cryptographie à la puce sécurisée de l'ordinateur ; des
  trackpads et des claviers mesurent la force ; des appareils photo signent leurs images à la prise de vue
  (C2PA).

Ce qui manque, c'est l'assemblage : **des capteurs de vivant dans les touches, liés à la signature du texte
tapé.**

Les tentatives passées ont toutes échoué au même endroit : la vie privée. Le numéro de série du Pentium III
(1999), l'informatique « de confiance » de Palladium (2002-2005), le Web Environment Integrity de Google
(2023) : tous retirés sous la protestation. Elles certifiaient la machine, ou traçaient l'utilisateur.

Deux choses ont changé :
- **Le besoin a explosé.** Avant les modèles de langage, les captchas suffisaient. Plus maintenant.
- **L'obligation arrive.** Elle arrive déjà de fait, par les plateformes : des applications refusent les
  appareils non certifiés, sans qu'aucune loi ne l'ait voté. Et elle arrive par la loi : la vérification
  d'âge en France, le marquage des contenus générés par l'IA en Europe.

On ne freine pas l'IA : on protège l'humain. Le marquage des textes produits par l'IA demande la bonne
volonté de tous ses fabricants, et il suffit d'un seul qui refuse : un modèle libre ou un acteur hostile ne
marquera rien, et une simple reformulation efface souvent la marque. La preuve d'humanité ne demande rien à
personne du côté de l'IA : elle vit dans le clavier de celui qui tape, et elle tient même si toutes les IA du
monde restent libres et sans marque.

L'histoire a déjà donné la leçon. Le courrier électronique est né en 1982 sans aucun moyen de prouver qui
l'envoie. La preuve n'est arrivée qu'en 2007 (DKIM), puis en 2015 (DMARC), après des milliards de spams et
d'hameçonnages. Aujourd'hui, tout le monde se tourne vers plus d'IA, et presque personne vers la preuve qu'un
humain est là. Un jour, on se retournera et on se dira : on aurait dû prouver qu'il y avait un humain avant
d'ouvrir les vannes.

Si la preuve d'humanité devient obligatoire, la seule question est **sous quelle forme** : une attestation
anonyme qui garde la biométrie dans le clavier, ou un identifiant unique qui trace chaque texte. Ce choix se
fait maintenant, quand les premiers modèles sortent. Un modèle respectueux qui existe avant la loi a toutes
les chances de devenir la norme. Sinon, on hérite du premier qui passe.

La France a montré que c'est possible : en imposant la vérification d'âge, elle a exigé une option en double
anonymat. Une obligation peut respecter la vie privée, si quelqu'un l'exige dès le départ.

## 8. L'appel

Aux fabricants de claviers, d'ordinateurs et de puces : construisez-le, en respectant ces sept principes.

Aux plateformes : acceptez une preuve anonyme, jamais une identité exigée.

Aux législateurs : si vous l'imposez un jour, imposez aussi l'anonymat par défaut, la biométrie gardée dans
l'appareil et une voie pour ceux qui ne peuvent pas taper.

Ce manifeste ne revendique rien. **Les idées appartiennent à ceux qui les réalisent.**

---

## Références

- Intel, *Mechanism for Detecting Human Presence Using Authenticated Input Activity Timestamps*,
  US 2014/0115662 A1, priorité 2008, abandonnée : https://patents.google.com/patent/US20140115662
- Lawrence Livermore National Laboratory, *Differentiation between human-generated and AI-generated text*,
  US 12,476,822 B2, 18/11/2025 :
  https://ipo.llnl.gov/technologies/it-and-communications/system-cryptographically-distinguish-between-human-generated
- *Suppressing Bot Traffic with Accurate Human Attestation* (ACM) :
  https://dl.acm.org/doi/pdf/10.1145/1851276.1851287
- *Privacy-Preserving Proof of Human Authorship via Zero-Knowledge Process Attestation* (arXiv, 2026) :
  https://arxiv.org/html/2603.00179
- Apple, *Keyless keyboard with force sensing and haptic feedback*, US 11,500,538 (2022) :
  https://patents.justia.com/patent/11500538
- Apple Platform Security, *Magic Keyboard with Touch ID* :
  https://support.apple.com/guide/security/magic-keyboard-with-touch-id-secf60513daa/web
- ISO/IEC 30107, détection des attaques par présentation (détection du vivant en biométrie).
- Règlement (UE) 2024/1689 sur l'intelligence artificielle (AI Act), article 14 (contrôle humain) et
  article 50 (marquage des contenus générés par l'IA) :
  https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- V. S. Sadasivan et al., *Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under
  Various Attacks*, Transactions on Machine Learning Research (TMLR), 2025, la reformulation contre le
  marquage : https://openreview.net/forum?id=OOgsAZdFOt (prépublication : https://arxiv.org/abs/2303.11156)
- J. Postel, *Simple Mail Transfer Protocol*, RFC 821 (1982) : https://www.rfc-editor.org/rfc/rfc821
- *DomainKeys Identified Mail (DKIM) Signatures*, RFC 4871 (2007) : https://www.rfc-editor.org/rfc/rfc4871
- *Domain-based Message Authentication, Reporting, and Conformance (DMARC)*, RFC 7489 (2015) :
  https://www.rfc-editor.org/rfc/rfc7489
- FIDO Alliance, attestation des authentificateurs par lots.
- Trusted Computing Group, *Direct Anonymous Attestation* (attestation anonyme des puces TPM 2.0).
