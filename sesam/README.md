# WP2 - Technologie : sesam

## Ontologie : data_model

Dans le cadre du WP2 - Technologie, un modèle de données et une ontologie ont été développées pour décrire les profils de préférences culturelles des utilisateurs SESAM et pour représenter les différents types de données qui seront stockées dans les différentes bases de données gérées par SESAM.

Le dossier [*../docs/sesam/sesam_v0/diagrammes*](../docs/sesam/sesam_v0/diagrammes) contient des schémas de classes permettant d'avoir un aperçu du modèle de données. Ces schémas sont visibles au format .png et .svg et les versions au format .xml peuvent être ouvertes et modifiées dans [draw.io](*https://app.diagrams.net/*).

En ouvrant les fichiers .html dans un navigateur internet, des versions interactives des objets définis par le modèle de données peuvent également être consultées dans le dossier [*../docs/sesam/sesam_v0/interactive_visualization*](../docs/sesam/sesam_v0/interactive_visualization/).

Le type d'objet qui représente un profil de préférences est `Profile` qui contient un objet `Preferences`. Ces deux classes d'objets sont définies au format *jsonschema* dans le fichier [*../docs/sesam/sesam_v0/jsonschema/profile_schema.json*](../docs/sesam/sesam_v0/jsonschema/profile_schema.json). `Preferences` contient des listes d'objets de différents types, qui sont des sous-classes de `Preference_Item`. La classe `Preference_Item` ainsi que ses six sous-classes sont également définis au format *jsonschema* dans le fichier [*profile_schema.json*](../docs/sesam/sesam_v0/jsonschema/profile_schema.json).

Les autres types d'objets hébergés par les bases de données SESAM sont définis par les classes `Event`, `Operator` et `Creator`. Ces classes sont définies au format *jsonschema*  dans les fichier [*../docs/sesam/sesam_v0/jsonschema/event_schema.json*](../docs/sesam/sesam_v0/jsonschema/event_schema.json), [*../docs/sesam/sesam_v0/jsonschema/operator_schema.json*](../docs/sesam/sesam_v0/jsonschema/operator_schema.json) et [*../docs/sesam/sesam_v0/jsonschema/creator_schema.json*](../docs/sesam/sesam_v0/jsonschema/creator_schema.json) respectivement et décrivent des objets de manière conforme aux schémas de données du projet [schema.org](https://www.schema.org). 


**Génération d'un profil utilisateur aléatoire**

Tous les objets introduits ci-dessus peuvent également être construits, générés aléatoirement et manipulés en utilisant les classes et fonctions définies dans les fichiers `profiles.py`, `preference_item.py` et `schema_objects.py`. Chacune des classes implémente notamment une fonction permettant d'exporter les instances créées au format .json. 

La fonction `Profile.generate_random()` permet de générer un profil utilisateur conforme à l'ontologie en sélectionnant aléatoirement des préférences culturelles parmi les répertoires d'exemples du dossier [*data_model/source_data/*](data_model/source_data/). 

Les arguments à passer à la fonction correspondent au nombre d'items de préférences à associer à chaque propriété du profil de préférence. 
Un profil peut être obtenu et exporté au format .json de la manière suivante : 

```python 
profile = Profile.generate_random(2, 1, 1, 5, 1, 2) # arbitrary numbers
save_path = "/your_local_path/example.json"
profile.export_json(save_path)
```


**Validator**

Le dossier [*data_model/validator*](data_model/validator/) contient des outils qui permettent de valider qu'un objet au format .json est confomrme au modèle de données de SESAM. 

La fonction `main()` du fichier `validator.py` utilise le package `jsonschema` pour valider la conformié du fichier json passé en argument selon les schémas définis dans le dossier *data/validation_schemas/*  

Le fichier `validator.py` peut être appelé en ligne de commande de la manière suivante : 
> `python validator.py "path_to_json_to_be_validated.json"`

Les fichiers décrivant les schémas de référence pour chacun des types d'objets de l'ontologie SESAM sont dans le dossier [*data_model/validator/validation_schemas*](data_model/validator/validation_schemas/).


**Représentation interactive du modèle de données**

A partir des fichiers .json au format *jsonschema* il est possible de générer automatiquement les pages html de visualisation contenues dans le dossier [*interactive_visualization*](../docs/sesam/sesam_v0/interactive_visualization/) en utilisant le package python `json-schema-for-humans` dont la documentation est disponible [ici](https://pypi.org/project/json-schema-for-humans/0.3.1/). 

La commande à entrer dans une interface en ligne de commande est la suivante 

> `generate-schema-doc "path_to_folder_with_input_files" "path_to_output_folder"`