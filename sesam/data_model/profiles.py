import json 
import random 
from preference_item import *


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


class Profile : 
    def __init__(self,
                 versioning, 
                 preferences):
        """Constructor for Profile Object

        Args:
            versioning (string): url pointing to the specifications of the used version of the SESAM ontology
            preferences (Preferences): cultural preferences of the user represented by this Profile
        """
        self.identifier = random.randint(500,999)
        self.versioning = versioning 
        self.timestamp = datetime.now().isoformat()
        self.preferences = preferences 

    def export_json(self, path):
        """export a profile in JSON format

        Args:
            path (string): filepath to location of exported profile
        """
        profile_dict = {
            "identifier":self.identifier, 
            "versioning":self.versioning, 
            "timestamp":self.timestamp, 
            "preferences" : {
                "categories" : [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                 "rating":item.rating, "timestamp": item.timestamp} for item in self.preferences.categories], 
                "audiences": [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                 "rating":item.rating, "timestamp": item.timestamp} for item in self.preferences.audiences], 
                "areas" : [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                 "rating":item.rating, "timestamp": item.timestamp} for item in self.preferences.areas], 
                "culturalProducts":[{"identifier":item.identifier, "name":item.name, "type": item.type, "rating": item.rating,
                                      "timestamp":item.timestamp} for item in self.preferences.culturalProducts], 
                "culturalOperators": [{"identifier":item.identifier, "name":item.name, "rating": item.rating,
                                      "timestamp":item.timestamp} for item in self.preferences.culturalOperators],
                "culturalCreators": [{"identifier":item.identifier, "name":item.name, "rating": item.rating,
                                      "timestamp":item.timestamp} for item in self.preferences.culturalCreators]
            }
        }


        with open(path, "w", encoding='utf-8') as f_save:
            json.dump(profile_dict, f_save, ensure_ascii=False, indent=4)
    
    def to_string(self): 
        """makes readable string of Profile object

        Returns:
            string: string representing the Profile Object
        """

        profile_dict = {
            "identifier":self.identifier, 
            "versioning":self.versioning, 
            "timestamp":self.timestamp, 
            "preferences" : {
                "categories" : [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                 "rating":item.rating, "timestamp": item.timestamp} for item in self.preferences.categories], 
                "audiences": [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                 "rating":item.rating, "timestamp": item.timestamp} for item in self.preferences.audiences], 
                "areas" : [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                 "rating":item.rating, "timestamp": item.timestamp} for item in self.preferences.areas], 
                "culturalProducts":[{"identifier":item.identifier, "name":item.name, "type": item.type, "rating": item.rating,
                                      "timestamp":item.timestamp} for item in self.preferences.culturalProducts], 
                "culturalOperators": [{"identifier":item.identifier, "name":item.name, "rating": item.rating,
                                      "timestamp":item.timestamp} for item in self.preferences.culturalOperators],
                "culturalCreators": [{"identifier":item.identifier, "name":item.name, "rating": item.rating,
                                      "timestamp":item.timestamp} for item in self.preferences.culturalCreators]
            }
        }
        return json.dumps(profile_dict, indent=4, ensure_ascii=False)
    

    
    def generate_random(n_categories, 
                        n_audiences, 
                        n_areas, 
                        n_culturalProducts, 
                        n_culturalOperators, 
                        n_culturalCreators):
        """generates a random Profile using a set of predefined possibilities for cultural preferences

        Args:
            n_categories (int): number of preferences in the "categories" field to be included in Profile
            n_audiences (int): number of preferences in the "audiences" field to be included in Profile
            n_areas (int): number of preferences in the "areas" field to be included in Profile
            n_culturalProducts (int): number of preferences in the "culturalProducts" field to be included in Profile
            n_culturalOperators (int): number of preferences in the "culturalOperators" field to be included in Profile
            n_culturalCreators (int): number of preferences in the "culturalCreators" field to be included in Profile

        Returns:
            _type_: _description_
        """
        # 1. generation random de chaque élément 
        categories = []
        for i in range(n_categories):
            categories.append(Category.select_random(category_termSet_path))
        audiences = []
        for i in range(n_audiences):
            audiences.append(Audience.select_random(audience_termSet_path))
        areas = []
        for i in range(n_areas):
            areas.append(Area.select_random(location_termSet_path))
        culturalProducts = []
        for i in range(n_culturalProducts): 
            culturalProducts.append(CulturalProduct.select_random(events_examples_path))
        culturalOperators = []
        for i in range(n_culturalOperators):
            culturalOperators.append(CulturalOperator.select_random(operators_examples_path))
        culturalCreators = []
        for i in range(n_culturalCreators):
            culturalCreators.append(CulturalCreator.select_random(creators_examples_path))
        # 2. initier un objet Preferences 
        pref = Preferences(categories, audiences, areas, culturalProducts, culturalOperators, culturalCreators)
        # 3. initier un objet Profile avec preferences dedans
        return Profile(versioning_url, pref)
    
class Preferences : 
    def __init__(self, 
                 categories, 
                 audiences, 
                 areas, 
                 culturalProducts, 
                 culturalOperators, 
                 culturalCreators
                 ):
        # Remark : all arguments have to be lists
        """Constructor for Preferences Object

        Args:
            categories (list): list of Category objects to be included in Preferences. 
            audiences (list): list of Audience objects to be included in Preferences. 
            areas (list): list of Area objects to be included in Preferences. 
            culturalProducts (list): list of CulturalProducts objects to be included in Preferences. 
            culturalOperators (list): list of CulturalOperators objects to be included in Preferences. 
            culturalCreators (list): list of CulturalCreators objects to be included in Preferences. 
        """
        self.categories = categories
        self.audiences = audiences
        self.areas = areas
        self.culturalProducts = culturalProducts
        self.culturalOperators = culturalOperators
        self.culturalCreators = culturalCreators


    def add_category(self, category_object): 
        """adds a Category Object to an existing Preference

        Args:
            category_object (Category): object to add
        """
        self.categories.append(category_object)
    
    def add_audiences(self, audience_object): 
        """adds an Audience Object to an existing Preference

        Args:
            audience_object (Audience): object to add
        """
        self.audiences.append(audience_object)

    def add_areas(self, area_object): 
        """adds an Area Object to an existing Preference

        Args:
            area_object (Area): object to add
        """
        self.areas.append(area_object)

    def add_culturalProduct(self, culturalProduct_object) : 
        """adds a CulturalProduct Object to an existing Preference

        Args:
            culturalProduct_object (CulturalProduct): object to add
        """
        self.culturalProducts.append(culturalProduct_object)

    def add_culturalOperator(self, culturalOperator_object) :
        """adds a CulturalOperator Object to an existing Preference

        Args:
            culturalOperator_object (CulturalOperator): object to add
        """
        self.culturalOperators.append(culturalOperator_object)
    
    def add_culturalCreator(self, culturalCreator_object) :
        """adds a CulturalCreator Object to an existing Preference

        Args:
            culturalCreator_object (CulturalCreator): object to add
        """
        self.culturalCreators.append(culturalCreator_object)

    def to_string(self, for_printing=False):
        """generates a json-format string of the Preferences object and all nested objects

        Args:
            for_printing (bool, optional): set to True to print result as well as return string. Defaults to False.

        Returns:
            String: string representation of Preferences object
        """
        preference_dict = {
            "categories" : [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                "rating":item.rating, "timestamp": item.timestamp} for item in self.categories], 
            "audiences": [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                "rating":item.rating, "timestamp": item.timestamp} for item in self.audiences], 
            "areas" : [{"name":item.name, "termCode":item.termCode, "inDefinedTermSet":item.inDefinedTermSet, 
                                "rating":item.rating, "timestamp": item.timestamp} for item in self.areas], 
            "culturalProducts":[{"identifier":item.identifier, "name":item.name, "type": item.type, "rating": item.rating,
                                    "timestamp":item.timestamp} for item in self.culturalProducts], 
            "culturalOperators": [{"identifier":item.identifier, "name":item.name, "rating": item.rating,
                                    "timestamp":item.timestamp} for item in self.culturalOperators],
            "culturalCreators": [{"identifier":item.identifier, "name":item.name, "rating": item.rating,
                                    "timestamp":item.timestamp} for item in self.culturalCreators]
        }
        s =  json.dumps(preference_dict, indent=4, ensure_ascii=False)
        if for_printing:
            print(s)
        return s