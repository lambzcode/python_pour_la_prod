# Projet : création d'une webapp Streamlit d'analyse de données

**Groupe** : 3-5 personnes par groupe
**Deadline** : 1er décembre à 23h59

---

## Contexte

Vous travaillez pour l'entreprise **RailInsight**, jeune pousse spécialisée dans l'analyse de données de mobilité ferroviaire.

La SNCF publie en open data un jeu de données mensuel détaillant la régularité de ses circulations TGV : nombre de trains prévus, annulations, retards au départ et à l'arrivée, et répartition des causes de retard (infrastructure, matériel roulant, gestion du trafic, affluence voyageurs, causes externes, etc.), liaison par liaison.

RailInsight a décroché un contrat avec un grand quotidien national : produire une application web interactive et accessible au grand public, permettant d'explorer la ponctualité du réseau TGV français et de comprendre les causes structurelles des retards. L'article qui accompagnera la sortie de l'application devra s'appuyer sur des insights chiffrés et visuels que seule votre analyse pourra fournir.

RailInsight compte sur vous pour que cette application web soit représentative du niveau technique de ses (meilleurs) employés. En effet, elle rendra également public le code source de cette application web, qui devra donc répondre à un ensemble de critères, des bonnes pratiques de code à la qualité du travail d'équipe (visible sur Git).

## Objectif

L'objectif de ce projet est de mettre en pratique les concepts et compétences vus en cours sur le développement Python pour la production, et de créer puis déployer une application web incluant une partie analyse de données.

Vous allez vous concentrer sur la structure du projet Git, la gestion de l'environnement Python avec `uv` ou `poetry`, la programmation orientée objet, la programmation d'une webapp Streamlit, le type hinting, la gestion des logs, le respect des normes PEP 8, la gestion des exceptions, la sécurité, les tests unitaires avec pytest, le test coverage, la documentation avec Sphinx, et la mise en place d'un pipeline CI/CD avec GitHub Actions.

## Process à suivre

### 1. Construire votre Dream team
Retrouvez vos collègues de travail émérites.

### 2. Récupérer la matière première
Téléchargez le jeu de données "Régularité mensuelle TGV" mis à disposition par la SNCF :
https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-tgv-aqst/information/

Le jeu de données contient, pour chaque mois et chaque liaison (gare de départ / gare d'arrivée), le nombre de circulations prévues, le nombre d'annulations, le nombre de trains en retard au départ et à l'arrivée, les retards moyens associés, ainsi que la répartition en pourcentage des causes de retard (causes externes, infrastructure, gestion du trafic, matériel roulant, gestion en gare, prise en charge des voyageurs).

### 3. Réfléchir avant de miner
Conscient que ce dataset permet de réaliser différentes analyses pertinentes, RailInsight vous laisse l'opportunité de choisir l'axe d'analyse que vous trouverez le plus intéressant à développer et mettre en avant.

Vous devez identifier une question/un thème qui définit le fil principal de votre étude, par exemple :
- Les liaisons les moins fiables du réseau, et cette instabilité s'aggrave-t-elle ou s'améliore-t-elle dans le temps ?
- Y a-t-il un lien entre la durée d'un trajet et sa probabilité d'être en retard ou annulé ?
- Les causes de retard varient-elles selon la saison (travaux l'été, intempéries l'hiver, affluence lors des vacances scolaires) ?
- Quelles gares de départ concentrent le plus de trains "responsables" de retards par rapport aux gares qui subissent des correspondances en cascade ?
- Peut-on regrouper les liaisons par "profil de ponctualité" (bonne régularité, retards chroniques mineurs, retards rares mais sévères, etc.) à l'aide d'un clustering ?
- Peut-on construire un score de fiabilité par liaison, combinant taux d'annulation et retard moyen, et le représenter sur une carte du réseau ?
- Un modèle simple peut-il prédire, à partir du mois et de la liaison, la probabilité qu'un trajet donné soit en retard de plus de 15 ou 30 minutes ?

Cette partie pourra se faire conjointement avec les séances de Charlotte.

### 4. Au charbon !
Réalisez votre étude en écrivant le code Python permettant d'analyser ces données et de répondre à vos questions :
- Sélectionner les variables d'intérêt
- Manipuler les données afin d'en extraire les statistiques et insights pertinents
- Visualiser ces résultats dans des visualisations appropriées et dynamiques (vous pouvez par exemple utiliser Plotly, ou une carte interactive de type pydeck/Folium pour représenter le réseau et les gares)

### 5. L'extérieur de la mine compte aussi
RailInsight ne vous paye pas seulement pour réaliser cette étude, mais attend également que vous rendiez ces résultats accessibles sous forme d'une webapp, avec un minimum de storytelling et d'interactivité, pour que le grand public puisse se l'approprier et comprendre les tenants et aboutissants de votre étude.

Vous devez donc créer une application web avec Streamlit, qui encapsulera votre analyse. N'hésitez pas à ajouter des widgets pour renforcer l'interactivité — par exemple, la possibilité de sélectionner une liaison, une période, ou une cause de retard pour faire évoluer les graphiques et la carte en conséquence.

RailInsight vous laisse libre cours à votre imagination, tant que cette application web en met plein la vue évidemment.

### 6. Donner les clefs de la mine
RailInsight sera pleinement satisfait lorsque votre webapp sera accessible au monde entier. La concurrence pourra ainsi en juger et lui donner une note (sur 20 !).

Pour cela, vous pouvez déployer votre application sur Streamlit Cloud, AWS, Azure, GCP, Heroku, ou sur un serveur à vous.

---

## Exigences techniques

Le repository Git devant être public sur GitHub pour le rayonnement de l'entreprise (et le vôtre !), un minimum de qualité est attendu.

### La gestion du projet

- **Structure du projet** : organisez votre projet en respectant une structure cohérente. Utilisez des packages et des modules pour diviser votre code en composants logiques. Vous pouvez utiliser Visual Studio Code si vous n'avez pas encore d'IDE préféré.
- **Environnement Python** : utilisez un gestionnaire d'environnement Python ou Poetry pour gérer les dépendances de votre projet. Choisissez bien votre version de Python. Assurez-vous d'avoir un fichier `requirements.txt` ou `pyproject.toml` correctement configuré.
- **Git** : initialisez un dépôt Git pour votre projet et suivez les meilleures pratiques de gestion de code avec des commits (assurez-vous de committer régulièrement), et dans la mesure du possible, des branches et des Pull Requests pour travailler en équipe. Assurez-vous d'inclure un fichier `README.md` qui explique comment installer, exécuter, déployer et utiliser votre application.
- **Optionnel** : créez éventuellement des tags de version pour marquer les versions stables de votre application.
- **Streamlit** : développez votre webapp avec une expérience utilisateur (UX) simple et intuitive, en laissant à l'utilisateur la possibilité d'interagir avec vos données pour bien comprendre le storytelling que vous lui racontez. Ce storytelling doit comporter des insights au travers de graphiques (charts, cartes, etc.) et doit répondre à votre problématique / question initiale.

### La programmation

- **Programmation orientée objet** : dans la mesure du possible, utilisez le paradigme orienté objet. Utilisez les principes de l'encapsulation et de l'héritage si approprié. Utilisez également les bonnes structures de données.
- **Type Hinting** : utilisez des annotations de type pour améliorer la lisibilité de votre code.
- **PEP 8** : assurez-vous que votre code respecte les normes PEP 8 pour la lisibilité et la cohérence du code. Utilisez un formateur (par exemple black).
- **Gestion des exceptions** : gérez les erreurs de manière appropriée en utilisant des exceptions personnalisées lorsque nécessaire. Par exemple en cas de saisie incorrecte de l'utilisateur (liaison inexistante, période hors plage disponible, etc.).
- **Logger** : utilisez le module `logging` pour enregistrer les actions de l'utilisateur et les événements importants dans un fichier de log. Créez un fichier de log pour le debug, et un autre pour les erreurs (ERROR et CRITICAL).
- **Sécurité** : assurez-vous (a minima) que les bibliothèques que vous utilisez sont connues et n'ont pas de vulnérabilités de sécurité évidentes. Si vous autorisez une entrée utilisateur, n'utilisez pas la fonction `eval`, évitez les mots de passe/tokens en clair dans le code, etc.

### Les tests

- **Tests unitaires** : écrivez des tests unitaires approfondis pour chaque composant de votre application en utilisant pytest. Vérifiez que la logique de votre application fonctionne correctement.
- **Test coverage** : utilisez un outil de test coverage (comme `pytest-cov`) pour mesurer la couverture de vos tests et assurez-vous d'avoir une couverture suffisante (90 % de couverture minimum).

### La documentation du projet

- **Commentaires** : assurez-vous d'inclure des commentaires pertinents dans votre code pour expliquer la logique complexe ou les décisions de conception importantes.
- **Docstrings** : utilisez des docstrings pour documenter vos classes, méthodes et fonctions de manière détaillée, en expliquant leur but, leurs paramètres et leurs valeurs de retour. Vous pouvez utiliser la convention qu'il vous plaira : Google, NumPy ou reStructuredText (reST).
- **Documentation** : créez une documentation claire et concise pour votre application en utilisant Sphinx. Documentez les classes, les méthodes, et expliquez comment installer et utiliser votre application.

### La CI

- **Pipeline CI/CD** : configurez un pipeline de CI avec GitHub Actions pour vérifier que PEP 8 est bien respecté, que les docstrings sur les fonctions/méthodes, classes, modules sont bien présentes, pour automatiser les tests et vérifier que le test coverage est supérieur à 90 % du code. Les tests unitaires doivent être exécutés automatiquement à chaque push sur une branche en review, et lors du merge de la branche en review sur master.
- **Optionnel** : inclure votre phase de déploiement de l'application dans votre CI/CD.

---

## Livraison du projet

Vous devez soumettre votre projet sous la forme d'un dépôt GitHub public, incluant :

- Code source Python bien structuré
- Documentation générée avec Sphinx
- Fichiers de logs
- Tests unitaires vérifiant le bon fonctionnement de l'application
- Le pipeline CI/CD
- Le lien vers votre webapp Streamlit déployée

Avant la deadline, envoyez le lien de votre projet GitHub à : lambert.fatoux@enpc.fr

## Évaluation

Votre projet sera évalué en fonction de la qualité du code, du respect des bonnes pratiques, de la couverture de tests, de la documentation, de la qualité visuelle de la webapp (graphiques, pertinence des insights, etc.) et du bon fonctionnement de l'application.

## Conseils

- N'hésitez pas à vous répartir le travail et à fusionner votre code sur Git avec des Pull Requests.
- Faites simple au début dans les fonctionnalités pour mettre en place le tout, puis itérez avec d'autres fonctionnalités plus complexes.
- Utilisez tout ce que vous voulez, Internet, ChatGPT, Codium, Copilot, etc. tant que vous maîtrisez votre code.

## Pour aller plus loin (bonus)

- **Utilisation d'une base de données** : comment pourriez-vous migrer votre système de stockage de données vers une base de données SQL ou NoSQL pour gérer un historique plus long (plusieurs années de données mensuelles) et améliorer les performances ?
- **Enrichissement des données** : pourriez-vous croiser ce jeu de données avec d'autres sources ouvertes (évènements locaux, distance kilométrique entre gares, données météo, vacances scolaires par zone) pour affiner votre analyse des causes de retard ?
- **Optimisation des performances** : comment pourriez-vous optimiser les performances de votre application, en particulier lors du filtrage et de l'agrégation de plusieurs années de données ?

*Liste non exhaustive. Libre à vous d'améliorer davantage votre web-app !*
