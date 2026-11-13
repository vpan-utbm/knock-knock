# HumanProof — Les objections

*Les questions qu'on nous posera, et nos réponses, limites comprises. Pour le détail : le [manifeste](MANIFESTE.md)
et la [note technique](TECHNICAL-NOTE.md) (en anglais).*

---

## 1. « Ça existe déjà. »

Des morceaux, oui, et le manifeste les cite. Intel a proposé dès 2008 qu'une puce de la carte mère signe l'activité du
clavier (demande de brevet abandonnée). Un laboratoire américain, le LLNL, a obtenu en 2025 un brevet sur la signature
d'un texte d'origine humaine (US 12,476,822 B2). Des chercheurs ont décrit un clavier de confiance contre les bots dès
2010. Les claviers de terminal de paiement chiffrent chaque touche dans leur propre puce, et certains claviers sont déjà
appairés par cryptographie à la puce sécurisée de l'ordinateur.

Ce que nous n'avons pas trouvé, c'est l'assemblage : **des capteurs de vivant dans les touches, liés à la signature du
texte tapé, avec un défi du destinataire**, et les sept principes qui l'empêchent de devenir un outil de surveillance.
Où est le brevet ? Si vous le connaissez, dites-le-nous : nous le citerons.

## 2. « Il suffit de retaper le texte d'une IA. »

Oui, et c'est voulu. HumanProof ne prouve pas **qui a pensé** les mots, il prouve **qu'un humain les a tapés et en
répond**, comme une signature au bas d'un contrat que l'avocat a rédigé. Le manifeste le dit dès le §2, et il en est
lui-même l'exemple : écrit avec l'aide d'une IA, puis tapé, relu et signé par un humain.

Ce que ça change : chaque texte certifié coûte un geste humain. Une machine seule ne peut plus produire à la chaîne
des milliers de textes « humains ».

## 3. « C'est le Web Environment Integrity de Google. »

Non, et la différence est précise. Le Web Environment Integrity (proposé en 2023, abandonné par Google le 2 novembre
2023 après une forte levée de boucliers) faisait certifier **le logiciel de l'utilisateur** : le navigateur et le
système. Un site aurait pu refuser un navigateur modifié, un bloqueur de publicité, un système libre.

Ici, l'ordinateur n'est **jamais certifié** : la note technique le traite comme entièrement hostile (§2 et §3). Seule
la puce du clavier atteste un seul fait sur un seul texte : un doigt humain l'a tapé. Elle ne dit rien de votre
navigateur, de votre système ni de vos logiciels, et ne donne aucune autorité sur la machine de celui qui lit (loi VII).

Ce qu'on reconnaît : rien de technique n'empêche une plateforme d'exiger cette preuve un jour. « Jamais obligatoire »
(loi V) est une exigence adressée aux plateformes et aux législateurs, pas une garantie du protocole. C'est justement
pour cela qu'il faut une forme anonyme **avant** que l'obligation arrive : sinon, on hérite de la première venue.

## 4. « C'est un DRM pour humains. »

Un DRM vous interdit de faire quelque chose sur votre propre appareil. Ce clavier n'interdit rien : on tape comme
avant, on colle, on corrige, on envoie un texte non signé, qui compte toujours (loi V). Il atteste seulement quand on
le lui demande, et la preuve suit le texte, pas l'utilisateur. Le format est ouvert : n'importe quel fabricant peut le
produire, n'importe qui peut le vérifier, sans passer par une plateforme (loi VI).

## 5. « Le marquage des textes de l'IA suffit. »

Le marquage (un filigrane caché dans le choix des mots) demande la bonne volonté de **tous** les fabricants d'IA. Il
suffit d'un seul qui refuse : un modèle libre ou un acteur hostile ne marquera rien. Et une étude publiée en 2025
(Sadasivan et al., TMLR) montre qu'une reformulation par une autre IA efface souvent la marque, et qu'on peut même
faire passer un texte humain pour un texte d'IA.

La preuve d'humanité ne demande rien à personne du côté de l'IA. On ne freine pas l'IA, on protège l'humain. Les deux
peuvent coexister : le marquage signale l'IA quand elle coopère, la preuve d'humanité marche même quand elle ne
coopère pas.

## 6. « Le fabricant tient la clé : il peut tricher. »

Le risque est réel, et la note technique le traite en trois points :
- **La clé.** À terme, chaque clavier a sa propre clé, née dans sa puce, jointe à une signature de groupe d'au moins
  100 000 claviers : la preuve dit « un vrai clavier », jamais « ce clavier », et une clé volée se révoque seule. Une
  clé partagée par lots, plus simple, ne sert qu'au prototype.
- **Qui décide qu'on est humain.** Le seuil du détecteur de vivant ne doit pas appartenir au seul fabricant. Les
  détecteurs sont testés par des **laboratoires indépendants accrédités** (normes ISO/IEC 30107-3 et 19795-1), comme
  les capteurs d'empreintes aujourd'hui. Les seuils et les taux d'erreur sont publiés, et chaque destinataire choisit
  les niveaux qu'il accepte.
- **Ce qu'il voit.** Ni le fabricant ni le laboratoire ne voient jamais un texte ou une preuve.

La limite, dite franchement : il faut faire confiance à la puce, comme on le fait déjà pour un terminal de paiement.

## 7. « Un robot peut appuyer sur les touches. »

Oui : un bras robotisé avec un doigt chauffé, ou des frappes humaines enregistrées puis rejouées. Ce sera une course,
comme pour les captchas. Le but n'est pas l'impossible, c'est de rendre la triche **chère et lente** : un robot qui
tape un texte à la fois ne remplace pas une ferme de bots.

## 8. « Et si mon ordinateur est piraté ? »

C'est le cas prévu. L'ordinateur ne fait que transporter le message : s'il change un seul caractère du texte tapé, la
signature tombe à l'endroit exact du changement. Il ne peut pas non plus faire passer un texte collé ou injecté pour un
texte tapé.

Une limite reste ouverte (note technique, §12) : un ordinateur piraté peut envoyer un texte vraiment tapé à un autre
destinataire que celui qu'on croit. Le voyant du clavier montre qu'une session est ouverte, pas pour qui. Chaque texte
détourné coûte quand même un geste humain : ça ne passe pas à l'échelle.

## 9. « Et ce qu'on colle, les citations ? »

Rien n'est interdit, tout est montré. Le destinataire voit, passage par passage, ce qui a été tapé, ce qui a été collé
et ce qui a été modifié hors du clavier. « Non tapé » décrit, n'accuse jamais : une citation se colle.

## 10. « Et ceux qui ne peuvent pas taper ? »

Personne n'est exclu parce qu'il dicte, écrit avec les yeux ou utilise un clavier adapté : un texte non signé compte
toujours (loi V), et un refus du clavier dit « pas sûr », jamais « robot » (loi IV). Le manifeste demande aux
législateurs, s'ils imposent un jour la preuve, d'imposer aussi une voie pour ceux qui ne peuvent pas taper.

Ce qu'on reconnaît : cette voie n'est pas encore conçue. Elle mérite son propre travail, pas une note de bas de page
(note technique, §12).

## 11. « Pourquoi pas World ID ? »

World ID scanne l'iris pour prouver qu'on est une personne unique. Un iris ne se change pas : s'il fuit, c'est pour
toujours. Et il faut passer devant l'appareil de l'entreprise, l'Orb, pour être inscrit.

HumanProof ne demande ni enregistrement ni registre : la biométrie naît et meurt dans la puce du clavier, seul le
verdict en sort (loi I). On ne prouve pas qui vous êtes, on prouve que vous êtes là.

Ce qu'on reconnaît : HumanProof ne prouve pas l'unicité. Une personne avec dix claviers peut signer avec les dix.
Il prouve un geste humain, pas « une personne, un compte ».

## 12. « Qui êtes-vous ? »

Human After All est la signature du manifeste : une personne, pas une entreprise, rien à vendre. Le dépôt est sous le
compte GitHub `vpan-utbm`, sans chercher à le cacher. Le manifeste a été écrit avec l'aide d'une IA, puis tapé, relu et
signé par un humain.

Il ne revendique rien : aucun brevet, aucun produit. Les idées appartiennent à ceux qui les réalisent.
