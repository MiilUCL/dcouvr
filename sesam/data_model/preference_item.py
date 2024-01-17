from datetime import datetime
import numpy as np
import pandas as pd
import random
import json

# GLOBAL VARIABLES
# links to termSets on the internet 
category_url = "https://miilucl.github.io/dcouvr/sesam_v0/termSets/DefinedTermSet_categories.csv"
location_url = "https://miilucl.github.io/dcouvr/sesam_v0/termSets/DefinedTermSet_location.csv"
audience_url = "https://miilucl.github.io/dcouvr/sesam_v0/termSets/DefinedTermSet_audience.csv"
# paths to termSets in local 
category_termSet_path = "source_data/DefinedTermSet_categories.csv"
audience_termSet_path = "source_data/DefinedTermSet_audience.csv"
location_termSet_path = "source_data/DefinedTermSet_location.csv"
# paths to events, creators, operators examples 
events_examples_path = "source_data/events_examples.json"
operators_examples_path = "source_data/operators_examples.json"
creators_examples_path = "source_data/creators_examples.json"
# current version to SESAM ontology (fake)
versioning_url = "https://miilucl.github.io/dcouvr/sesam_v0/profile_schema.html"



class Preference_Item :
    def __init__(self, 
                 rating, 
                 name
                 ):
        """Constructor for Preference_Item object

        Args:
            rating (int): integer between 1-5 : rating attributed by the user to the Preference Item 
            name (string): name of Preference Item
        """
        self.name = name
        self.rating = rating
        self.timestamp = datetime.now().isoformat()
    
    def to_string(self): 
        """returns the Preference Item in string format

        Returns:
            string: Preference Item in string format
        """
        #string in json format with all variables and nested variables
        return json.dumps(vars(self), indent=4, ensure_ascii=False)

class Category(Preference_Item):
    def __init__(self,
                 name, 
                 termCode, 
                 definedTermSet_url, 
                 rating):
        """Constructor for Category Object. Inherits from Preference_Item

        Args:
            name (string): name of Category Object
            termCode (string): termCode associated to name of object
            definedTermSet_url (string): url pointing to definedTermSet for Category
            rating (int): integer between 1-5 : rating attributed by the user to the Preference Item 
        """
        self.name = name
        self.termCode = termCode
        self.inDefinedTermSet = definedTermSet_url 
        self.rating = rating 
        self.timestamp = datetime.now().isoformat()
    
    def select_random(termSet_path):
        """selects a random Category object from the possible TermSet. Associates a random rating

        Args:
            termSet_path (string): path to file defining Category TermSet

        Returns:
            Category: randomly selected object
        """
        termSet = pd.read_csv(termSet_path, encoding="latin1")
        row = termSet.sample(1)
        rating = np.random.randint(1,6)
        return Category(row["name"].values[0], row["termCode"].values[0], category_url , rating)


class Audience(Preference_Item):
    def __init__(self,
                 name, 
                 termCode, 
                 definedTermSet_url, 
                 rating):
        """Constructor for Audience Object. Inherits from Preference_Item

        Args:
            name (string): name of Audience Object
            termCode (string): termCode associated to name of object
            definedTermSet_url (string): url pointing to definedTermSet for Audience
            rating (int): integer between 1-5 : rating attributed by the user to the Preference Item 
        """
        self.name = name
        self.termCode = termCode
        self.inDefinedTermSet = definedTermSet_url 
        self.rating = rating 
        self.timestamp = datetime.now().isoformat()
    
    def select_random(termSet_path): 
        """selects a random Audience object from the possible TermSet. Associates a random rating

        Args:
            termSet_path (string): path to file defining Audience TermSet

        Returns:
            Audience: randomly selected object
        """
        termSet = pd.read_csv(termSet_path, encoding="latin1")
        row = termSet.sample(1)
        rating = np.random.randint(1,6)
        return Audience(row["name"].values[0], row["termCode"].values[0], audience_url, rating)

class Area(Preference_Item) :
    def __init__(self,
                 name, 
                 termCode, 
                 definedTermSet_url, 
                 rating):
        """Constructor for Audience Object. Inherits from Preference_Item

        Args:
            name (string): name of Audience Object
            termCode (string): termCode associated to name of object
            definedTermSet_url (string): url pointing to definedTermSet for Audience
            rating (int): integer between 1-5 : rating attributed by the user to the Preference Item 
        """
        self.name = name
        self.termCode = termCode
        self.inDefinedTermSet = definedTermSet_url 
        self.rating = rating 
        self.timestamp = datetime.now().isoformat()
    
    def select_random(termSet_path): 
        """selects a random Area object from the possible TermSet. Associates a random rating

        Args:
            termSet_path (string): path to file defining Area TermSet

        Returns:
            Area: randomly selected object
        """
        termSet = pd.read_csv(termSet_path, encoding="latin1")
        row = termSet.sample(1)
        rating = np.random.randint(1,6)
        return Area(row["name"].values[0], row["termCode"].values[0], location_url, rating)


class CulturalProduct(Preference_Item):
    def __init__(self,  
                 name,
                 identifier, 
                 type, 
                 rating):
        """Constructor for CulturalProduct. Inherits from Preference_Item

        Args:
            name (string): name of CulturalProduct
            identifier (int): identifier of Cultural Product in SESAM CulturalProduct DB
            type (string): schema.org type of Cultural Product 
            rating (integer): integer between 1-5 : rating attributed by the user to the Preference Item
        """
        self.identifier = identifier 
        self.name = name
        self.type = type
        self.rating = rating
        self.timestamp = datetime.now().isoformat()
    
    def select_random(example_events_paths): 
        """generate a CulturalProduct object by randomly selecting an Event in the event examples file

        Args:
            example_events_paths (string): path to event examples file

        Returns:
            CulturalProduct: generated CulturalProduct object
        """
        with open(example_events_paths, "r", encoding='utf-8') as f_events:
            events = json.load(f_events)["events"]
        ev = random.sample(events, 1)[0]
        rating = np.random.randint(1,6)
        return CulturalProduct(ev["name"], ev["identifier"], ev["@type"], rating)

class CulturalOperator(Preference_Item) :
    def __init__(self, 
                 name,
                 identifier,
                 rating):
        """Constructor for CulturalOperator. Inherits from Preference_Item

        Args:
            name (string): name of CulturalOperator
            identifier (int): identifier of Cultural Operator in SESAM CulturalOperator DB
            type (string): schema.org type of Cultural Operator
            rating (integer): integer between 1-5 : rating attributed by the user to the Preference Item
        """
        self.identifier = identifier
        super().__init__(rating, name)

    
    def select_random(example_operators_paths):
        """generate a CulturalOperator object by randomly selecting an Operator in the operator examples file

        Args:
            example_operators_paths (string): path to operator examples file

        Returns:
            CulturalOperator: generated CulturalOperator object
        """
        with open(example_operators_paths, "r", encoding='utf-8') as f_operators:
            operators = json.load(f_operators)["operators"]
        op = random.sample(operators, 1)[0]
        rating = np.random.randint(1,6)
        return CulturalOperator(op["name"], op["identifier"], rating)

class CulturalCreator(Preference_Item):
    def __init__(self, 
                 name,
                 identifier, 
                 rating):
        """Constructor for CulturalCreator. Inherits from Preference_Item

        Args:
            name (string): name of CulturalCreator
            identifier (int): identifier of Cultural Creator in SESAM CulturalCreator DB
            type (string): schema.org type of Cultural Creator
            rating (integer): integer between 1-5 : rating attributed by the user to the Preference Item
        """
        self.identifier = identifier
        super().__init__(rating, name)

    def select_random(example_creators_paths): 
        """generate a CulturalCreator object by randomly selecting a Creator in the creator examples file

        Args:
            example_creator_paths (string): path to event examples file

        Returns:
            CulturalProduct: generated CulturalProduct object
        """
        with open(example_creators_paths, "r", encoding='utf-8') as f_creators:
            creators = json.load(f_creators)["creators"]
        cr = random.sample(creators, 1)[0]
        rating = np.random.randint(1,6)
        return CulturalCreator(cr["name"], cr["identifier"], rating)