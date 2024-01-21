from helper_functions import make_DefinedTerm_keywords_block, make_DefinedTerm_audience_block, make_DefinedTerm_location_block
import json
import random 

# GLOBAL VARIABLES
# links to termSets on the internet 
category_url = "https://miilucl.github.io/dcouvr/sesam/sesam_v0/termSets/DefinedTermSet_categories.csv"
location_url = "https://miilucl.github.io/dcouvr/sesam/sesam_v0/termSets/DefinedTermSet_location.csv"
audience_url = "https://miilucl.github.io/dcouvr/sesam/sesam_v0/termSets/DefinedTermSet_audience.csv"
class DB_SESAM_Object: 
    def __init__(self,
                 name,  
                 keywords):
        """Initialize a DB_SESAM_Object

        Args:
            name (string): name of the object
            keywords (list): list of strings corresponding to keywords associated to object
        """
        # keywords est un vecteur
        self.name = name
        self.keywords =  [make_DefinedTerm_keywords_block(category_url, c) for c in keywords] # c quoi category url ? 
    
    def add_category(self, new_keywords):
        """add keyword to existing DB_SESAM_Object

        Args:
            new_keywords (string): name of additionnal keyword (from DefinedTermSet)
        """
        self.keywords.append(make_DefinedTerm_keywords_block(category_url, new_keywords)) 
    
    def export_to_schema_org_compliant_json(self, path, for_printing=False):
        """generate json representation of the object, compliant with schema.org
        data model specs    

        Args:
            path (string): path to .json file where the object should be save
            for_printing (bool, optional): set to True to print result. Defaults to False.
        """
        d = {}
        obj_dict = vars(self)
        if self.__class__.__name__=="Operator": 
            t = "Organization"
        elif self.__class__.__name__=="Event":
            t = "Event"
        else : 
            t = self.type
            del obj_dict["type"]
        d["@context"] = "https://schema.org"
        d["@type"] = t
        for key in obj_dict:
            d[key] = obj_dict[key]
        if for_printing:
            print(json.dumps(d, ensure_ascii=False, indent=4))
        else :
            with open(path, "w", encoding="utf-8") as f_save:
                json.dump(d, f_save, ensure_ascii=False, indent=4)

class Event(DB_SESAM_Object): 
    def __init__(self,
                 name, 
                 keywords, 
                 audience, 
                 name_location, 
                 organizer_id, 
                 organizer_name, 
                 description, 
                 startDate,
                 endDate,
                 sameAs):
        """Constructor of Event Object (inherits from DB_SESAM_Object)

        Args:
            name (string): name of Event
            keywords (list): list of strings that are keywords associated to Event. From DefinedTermSet
            audience (list): list of strings that are name of audience group associated to Event. From DefinedTermSet
            name_location (string): name of place/location associated to Event. From DefinedTermSet
            organizer_id (int): identifier of the Event's organizer (Operator object) in the SESAM Cultural Operator DB
            organizer_name (string): name of the Event's organizer (Operator object)
            description (string): description of the Event
            startDate (string): datetime string in isoformat : start date of event
            endDate (string): datetime string in isoformat : end date of event (where applicable)
            sameAs (string): url to the event's webpage
        """
        self.identifier = random.randint(10000, 19999)
        self.sameAs = sameAs 
        super().__init__(name, keywords) 
        self.location = make_DefinedTerm_location_block(location_url, name_location)
        self.audience = [make_DefinedTerm_audience_block(audience_url, aud) for aud in audience]
        self.organizer = {"@type":"Organization", "identifier":organizer_id, "name":organizer_name}
        self.startDate = startDate
        if endDate is not None : 
            self.endDate = endDate
        self.description = description

    def add_audience(self, new_audience):
        """add audience to existing DB_SESAM_Object

        Args:
            new_audience (string): name of additionnal audience (from DefinedTermSet)
        """
        self.audience.append(make_DefinedTerm_audience_block(category_url, new_audience))

class Operator(DB_SESAM_Object) : 
    def __init__(self, 
                 name, 
                 keywords, 
                 name_location,  
                 url):
        """Constructor of Operator Object (inherits from DB_SESAM_Object)

        Args:
            name (string): name of Operator
            keywords (list): list of strings that are keywords associated to Operator. From DefinedTermSet
            name_location (string): name of place/location associated to Operator. From DefinedTermSet
            url (string): url to the Operator's webpage
        """
        self.identifier = random.randint(20000, 29999)
        super().__init__(name, keywords)
        self.location = make_DefinedTerm_location_block(location_url, name_location)
        self.url = url
   

class Creator(DB_SESAM_Object) : 
    def __init__(self,
                 type,  
                 keywords,
                 name,
                 sameAs, 
                 givenName=None, 
                 familyName=None,
                 additionalName=None) : 
        """Constructor for Creator Object (inherits from DB_SESAM_Object)

        Args:
            type (string): schema.org type of the Creator Object (person, performinggroup, sportsassociation)
            keywords (list): list of strings that are keywords associated to Cultural Creator. From DefinedTermSet
            name (string): name of cultural Creator
            sameAs (string): url to webpage representing the cultural Creator (prefered : wikidata)
            givenName (string, optional): given name of cultural Creator (if type is Person). Defaults to None.
            familyName (string, optional): family name of cultural Creator (if type is Person). Defaults to None.
            additionalName (string, optional): additional name of cultural Creator (if type is Person). Defaults to None.
        """
        self.identifier = random.randint(30000, 39999)
        self.type = type
        self.name = name
        if additionalName is not None :
            self.additionalName = None
        if givenName is not None : 
            self.givenName = givenName
        if familyName is not None : 
            self.familyName = familyName
        self.keywords =  [make_DefinedTerm_keywords_block(category_url, c) for c in keywords]
        self.sameAs = sameAs
