# dcouvr
Repository of the DCouvr project

## Projet DCOUVR
Introduction 

### WP2 - Technologie 

#### Ontologie : SESAM_data_model

Dans le cadre du WP2 - Technologie, un modèle de données et une ontologie ont été développées pour décrire les profils de préférences culturelles des utilisateurs SESAM et pour représenter les différents types de données qui seront stockées dans les différentes bases de données gérées par SESAM.

Une description détaillée du modèle de données SESAM peut être consultée à ce *lien*

Le type d'objet qui représente un profil de préférences est `Profile` qui contient un objet `Preferences`. Ces deux classes sont définies dans le fichier `profile.py`. `Preferences` contient des listes d'objets de différents types, qui sont des sous-classes de `Preference_Item`. La classe `Preference_Item` ainsi que ses six sous-classes sont définis dans le fichier `preference_item.py`.

Les autres types d'objets hébergés par les bases de données SESAM sont définis par les classes `Event`, `Operator` et `Creator` dans le fichier `db_SESAM_objects.py`. Ces classes décrivent des objets de manière conforme aux schémas de données du projet [https://schema.org](schema.org). 

Chacune des classes ci-dessus implémente une fonction permettant d'exporter les instances au format .json. 

**Génération d'un profil utilisateur aléatoire**

La fonction `Profile.generate_random()` permet de générer un profil utilisateur conforme à l'ontologie en sélectionnant aléatoirement des préférences culturelles parmi les répertoires d'exemples du dossier [*WP2-techno/SESAM_data_model/data/*](WP2-techno/SESAM_data_model/data). 

Les arguments à passer à la fonction correspondent au nombre d'items de préférences à associer à chaque propriété du profil de préférence. 
Un profil peut être obtenu et exporté au format .json de la manière suivante : 

```python 
profile = Profile.generate_random(2, 1, 1, 5, 1, 2) # ces nombres sont arbitraires
save_path = "/your_local_path/example.json"
profile.export_json(save_path)
```


**Validator**

Le fichier `validator.py` est utilisé pour vérifier qu'un objet au format .json est conforme au modèle de données de SESAM. 

La fonction `main()` utilise le package `jsonschema` pour valider la conformié du fichier json passé en argument selon les schémas définis dans le dossier *data/validation_schemas/*  

Le fichier `validator.py` peut être appelé en ligne de commande de la manière suivante : 
> `python validator.py "path_to_json_to_be_validated.json"`


### WP5 - Baromètre