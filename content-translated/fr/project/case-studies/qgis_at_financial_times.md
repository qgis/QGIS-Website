---
HasBanner: false
archived: false
date: 2016-04-01
draft: false
featured: true
section: projet
sidebar: true
thumbnail: images/ft_europe_migration_balkan-route.png
title: Utilisation de QGIS au sein du Financial Times
type: case-study

---
{{<content-start >}}
# Utilisation de QGIS au sein du Financial Times
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2016</span>
</p>

## Entretien avec Steven Bernard (Éditeur Conception Interactive)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS** : Steven, Quel est le nom de l'équipe avec laquelle vous travaillez au FT ? Pouvez-vous nous donner des détails sur le contexte de ce que fait votre équipe au FT ?

**Steve** : Notre équipe est dans une période de transition en ce moment, nous avons un nouveau éditeur visualisation des données, Alan Smith OBE (anciennement ONS) qui est en train de tout changer en créant une équipe graphique unique. Traditionnellement nous avions une équipe graphique web et une équipe graphique impression. L'équipe impression était responsable de tous les graphiques du journal ainsi que de la création de leur version pour le web. Mon équipe ne s'occupait que du contenu spécifiquement web, ainsi que de travailler en étroite collaboration avec les producteurs/développeurs interactifs pour le développement de graphiques interactifs.

L'équipe nouvellement formée permettra une dissémination plus importante des expériences entre les différents médias.

Alan a introduit un flux de travail unique pour notre équipe, comprenant l'utilisation de d3 pour aider à créer un vocabulaire graphique plus étendu et pour réduire le temps nécessaire à la création d'illustrations.

![](../images/ft_europe_migration_balkan-route.png)

*Exemple : Flux de migration. Route des Balkans de l'Ouest.*

**QGIS** : Combien y a-t-il de collaborateurs dans votre équipe ?

**Steven** : En incluant les designers, développeurs, producteurs et statisticiens, nous avons une équipe de 24

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](../images/ft_nigeria-migration_animation.gif)

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](../images/ft_gotthard-tunnel.png)

*Exemple : Le tunnel routier et ferroviaire du Gotthard dans les Alpes suisses.*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS**: Comment avez-vous découvert QGIS?

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](../images/ft_blm-federal-land-map.png)

*Exemple : Domaines publics aux USA.*

**QGIS** : Quels autres outils utilisez-vous en dehors de QGIS et comment les combinez-vous ?

**Steven** : Si c'est pour une simple carte de localisation 95% du travail se fait dans QGIS, et le polissage final dans Adobe Illustrator.

Si je fait une carte topographique, alors le procédé est bien plus complexe. Je récupère les fichiers MNE avec Nasa Earth Explorer et les importent dans QGIS pour les recadrer à la taille voulue. J'importe ensuite le MNE recadré dans Blender pour faire un rendu 3D. Si j'utilise une image satellite sur le relief ombré je récupère une image BlueMarble à partir de la Nasa et l'importe aussi dans Blender. Le rendu exporté de Blender est alors importé dans QGIS pour être utilisé comme couche de base. Je le manipule avec Photoshop avant l'import si nécessaire. 

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

Un autre outil utile est Google My Maps qui permet aux reporteurs dans le monde de marquer des positions sur une carte que nous pouvons ensuite récupérer en tant que fichier kmz et les importer directement dans QGIS.

Le dernier outil que j'utilise est Adobe After Effects car je me suis mis récemment à animer mes cartes pour amener l'utilisateur en voyage. Comme dans la série récente Land Rush :
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS** : Utilisez-vous d'autres outils spatiaux ou SIG en dehors de QGIS, et si oui, lesquels ?

**Steven** : Tout en QGIS pour moi, mais comme mentionné auparavant certains de mes collègues utilisent aussi Map Publisher.

![](../images/ft_isis-air-strikes_febupdate.png)

*Exemples : Frappes en Syrie en février 2016.*

**QGIS** : Pouvez-vous décrire les points forts et les points faibles de QGIS en ce qui concerne les travaux que vous avez à faire ?

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

Dans les quinze jours j'étais convaincu que c'était faisable. Le point fort étant la possibilité de mettre en place des guides de styles pour tout, y compris pour les niveaux de zoom pour les cartes de villes.

J'ai un système en place où nous avons des sets de feuilles Google avec colonnes pour nom du marqueur, lat., long., icône, épaisseur-casse, taille-casse et si vous voulez que le marqueur soit visible ou non.

L'icône du marqueur est une boîte déroulante connectée à une table vLookUp qui remplie tous les détails pour ce marqueur.

Ainsi, tout ce que j'ai à faire est de télécharger le fichier csv, l'importer dans QGIS, lui appliquer un style et bingo, j'ai une carte prête à 95%.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](../images/ft_chinaMigration.png)

*Exemple : Attraction urbaine et migration interne en Chine.*

**QGIS** : Quels sont les concepts ou composantes que vous appréciez le plus dans QGIS ?

**Steven** : Il y a beaucoup de composantes que je classifierais comme essentielles ! Mais principalement Quick OSM et l'outil de géo-référencement m'ont fait gagner énormément de temps, ce qui est absolument essentiel lorsque les échéances sont serrées. Ce qui, travaillant pour un organisme de presse, arrive 90% du temps. 

![](../images/ft_china_henanGuangdong.png)

*Exemple : Attraction urbaine et migration interne en Chine. Vues de détail.*

**QGIS** : Quelles sont les composantes ou fonctionnalités de QGIS qui vous manquent le plus ? Avez-vous une liste des composantes manquantes qui vous serez très utiles si elles étaient implémentées ?

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

Pouvoir sauver en tant qu'image ayant une taille plus grande. À l'heure actuelle c'est la seule façon que j'ai pour créer un fichier MNE géo-référencé recadré pour l'import dans Blender. Mais il est limité à la taille de votre écran. Si j'ai un fichier MNE de 8 000 pixels dans QGIS j'aimerais pouvoir être capable d'exporter un recadrage ayant une taille plus grande que celle de mon écran, par exemple, pour être utilisé dans une vidéo HD.

**QGIS** : S'il vous manque des composantes dans QGIS qui vous aideraient - considéreriez-vous d'améliorer QGIS vous-même (en changeant le code de QGIS ou avec des extensions Python), ou considéreriez-vous employer un développeur QGIS pour implémenter les composantes manquantes pour vous ? Ou bien rechercheriez-vous d'autres outils pour combler ce manque ?

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](../images/ft_us_broadband_internet_subscription.png)

*Exemple : Pourcentage des ménages ayant une connexion internet haut débit aux USA.*

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS** : Merci de nous avoir reçu et du travail que vous faite pour promouvoir et documenter les flux de travail en QGIS !

![](../images/ft_potrait_steve_bernard.jpg)

*Portrait de  Steve Bernard. Éditeur Design Interactif chez Financial Times.*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

Interview réalisé par A. Neumann et T. Sutton, Avril 2016.

{{<content-end >}}
