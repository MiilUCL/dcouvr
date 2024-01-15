import json
from jsonschema import validate 
import sys

# filepaths 
path_event_schema = "validation_schemas/event_schema.json"
path_operator_schema = "validation_schemas/operator_schema.json"
path_creator_schema = "validation_schemas/creator_schema.json"
path_profile_schema = "validation_schemas/profile_schema.json"


#print(reference)

def __main__(obj):
    """uses jsonschema.validate to evaluate if the submitted object matches with the SESAM data model and ontology

    Args:
        obj (dict): the object to be valited in dictionary format : is expected to be of the following classes : Profile, Event, Operator, Creator
    """
    if "@type" in obj.keys() :
        if obj["@type"]=="Event": 
            with open(path_event_schema, "r", encoding="utf-8") as f_event: 
                ref = json.load(f_event)
        elif obj["@type"]=="Organization":
            with open(path_operator_schema, "r", encoding="utf-8") as f_operator: 
                ref = json.load(f_operator)
        elif( obj["@type"]=="Person" or obj["@type"]=="PerformingGroup" or obj["@type"]=="SportsOrganization"):
            with open(path_creator_schema, "r", encoding="utf-8") as f_creator: 
                ref = json.load(f_creator)
        else:
            print("The provided dictionary is of an unrecognized type")
        # validating with schema.org ontology
        try : 
            validate(obj, ref) 
            print("object is valid based on Schema.org ontology") 
        except Exception as e :
            print(f"object is not valid based on schema.org ontology : {e}")
    else : 
        with open(path_profile_schema, "r", encoding="utf-8") as f_profile: 
            ref = json.load(f_profile)
        # validating with SESAM propriatary ontology
        try : 
            validate(obj, ref) 
            print("object is valid based on SESAM ontology") 
        except Exception as e :
            print(f"object is not valid based on SESAM ontology : {e}")


args = sys.argv
if len(args) !=2: 
    print("you have entered an incorrect number of arguments")
    print("please enter as only argument the relative path to the json object to be validated")
    exit()


path = args[1]
with open(path, "r", encoding="utf-8") as fp : 
    json_data = json.load(fp)
__main__(json_data)
