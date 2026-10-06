## Tips pour le projet

* Générer une clé SSH pour votre accès à github (settings -> clé ssh)
* Une personne crée le projet sur github et les autres font un `git clone` sur leur machine
* Pour la programmation orientée objet, par exemple créer une classe `dataset` avec des méthodes pour l'analyse des données, le cleaning des données, l'affichage sur la webapp, etc.
* Créez vos branches pour ajouter des fonctionnalités avec `git switch -c nom_de_ma_branche`
* Faites vos développements, git add, git commit puis git push
* Créez une `pull request` via l'interface de git pour que vos camarades puissent relire vos changement
* Pour le déploiement, si vous passez par streamlit cloud, vous n'avez pas besoin de build une image docker (ça reste un bon exercice cependant, vous pouvez le tester si vous avez un vps)
* Vous pouvez croiser les données avec d'autres dataset open source (positions des gares, nombre de passagers par ligne, tarifs des trajets, etc.) :warning: ne pas rajouter trop de données, se limiter à de la visualisation :warning:
* Ne mettez pas tout votre code streamlit dans un seul fichier: créez des pages ou des composants streamlit que vous importez dans le script principal
* L'API sncf à l'adresse https://ressources.data.sncf.com/explore/dataset/regularite-mensuelle-tgv-aqst/api/ peut être requêtée depuis streamlit cloud (permet de faire des filtres, group_by, tri, etc. directement depuis l'api)
* Dans le README, justifiez certains choix que vous avez faits: nettoyage des données, analyses, hypothèses,...