import json 
import pandas as pd
from helper_functions import make_audience_block, make_category_block, make_location_block, make_DefinedTerm_audience_block, make_DefinedTerm_keywords_block, make_DefinedTerm_location_block
from db_SESAM_Object import Event, Operator, Creator
from profiles import Profile, Preferences
from preference_item import Preference_Item, Category, Audience, Area, CulturalCreator, CulturalOperator, CulturalProduct


"""
TESTS TO RUN
1. (V) make_category_block, make_location_block, make_audience_block
3. (V) select random pour les 6 préférences
4. (V) Preferences.__init__() 
5. (V) Preferences.add_xxx()
6. (V) Profile.generate_random() 
7. (V) Profile.export_to_json()
8. (V) init pour Event, operator, creator
9. (V) DB_SESAM_Object.add_category()
10. (V) DB_SESAM_Object.export_to_schema_org_compliant_json() - save
11. (V) DB_SESAM_Object.export_to_schema_org_compliant_json() - print
""" 

# GLOBAL VARIABLES
# links to termSets on the internet 
category_url = "https://tinyurl.com/sesam-categories"
location_url = "https://tinyurl.com/sesam-areas"
audience_url = "https://tinyurl.com/sesam-audiences"
# paths to termSets in local 
category_termSet_path = "data/DefinedTermSet_categories.csv"
audience_termSet_path = "data/DefinedTermSet_audience.csv"
location_termSet_path = "data/DefinedTermSet_location.csv"
# paths to events, creators, operators examples 
events_examples_path = "data/events_examples.json"
operators_examples_path = "data/operators_examples.json"
creators_examples_path = "data/creators_examples.json"
# current version to SESAM ontology (fake)
versioning_url = "https://sesam.be/data_model_v0" 


def test_preference_items():
    print(vars(Audience("zzz", "code", "url.url", 1)))
    print(vars(CulturalCreator("josé", 10101, 5)))

#test_preference_items()


def test_select_random():
    cat = Category.select_random(category_termSet_path)
    are = Area.select_random(location_termSet_path)
    aud = Audience.select_random(audience_termSet_path)
    prod = CulturalProduct.select_random(events_examples_path)
    op = CulturalOperator.select_random(operators_examples_path)
    crea = CulturalCreator.select_random(creators_examples_path)
    vec = [cat, are, aud, prod, op, crea]
    #for v in vec : 
    #    print(v)
    #    print(vars(v))
    #    print('\n')
    return cat, are, aud, prod, op, crea

#c, a, au, p, o, c = test_select_random()

def test_preferences():
    cat, are, aud, prod, op, crea = test_select_random()
    Pref = Preferences([cat], [aud], [are], [prod], [op], [crea])
    print(vars(Pref))
    """
    new_cat = Category.select_random(category_termSet_path)
    new_aud = Audience.select_random(audience_termSet_path)
    new_are = Area.select_random(location_termSet_path)
    new_prod = CulturalProduct.select_random(events_examples_path)
    new_op = CulturalOperator.select_random(operators_examples_path)
    new_crea = CulturalCreator.select_random(creators_examples_path)
    Pref.add_category(new_cat)
    Pref.add_audiences(new_aud)
    Pref.add_areas(new_are)
    Pref.add_culturalProduct(new_prod)
    Pref.add_culturalOperator(new_op)
    Pref.add_culturalCreator(new_crea)
    """
    print(Pref.to_string(for_printing=True))
    print("\n\n")
    return Pref



def test_profile(n):
    #prefs = test_preferences()
    #profile1 = Profile(versioning_url, prefs)
    #print(vars(profile1))
    #print(profile1.to_string())
    profile2 = Profile.generate_random(2, 1, 3, 2, 0, 1)
    #print(profile2.to_string())
    #print(profile2.to_string())
    #profile2.export_json("SESAM_data_structure/test_result"+str(n)+".json")
    return profile2
#prof = test_profile(1)
#print(p.__class__.__name__)
#test_profile(2)



def test_DB_SESAM_Object():
    ev1 = Event("bbb", ["SPORTS"], 'Amis', 'Mons', 1001, "ccc", "du sport", "2024-01-04", None, "www.sport.be")
    #print(vars(ev1))
    op1 = Operator("aaa", ["EXPOS"], "Namur", "cinoche.com")
    #print(vars(op1))
    crea1 = Creator("Person",[],"johnny cupcake", "wiki.org", givenName=None, familyName=None)
    #print(vars(crea1))
    op1.add_category("EXPOS")
    crea1.add_category("CONCERTS")
    print(vars(op1))
    print(vars(crea1))
    crea1.export_to_schema_org_compliant_json("SESAM_data_structure/test_object.json",for_printing=True)
    #op1.export_to_schema_org_compliant_json("SESAM_data_structure/test_object.json")

#test_DB_SESAM_Object()
    
pro = Profile.generate_random(0,0,0,0,0,0)

pro.export_json("test_result2.json")

#__main__("test_result2.json")

#print(pro.to_string())

#pref = test_preferences()
#pref2 = pro.preferences
#print(pref2.to_string())
#r = pref2.to_string(for_printing=True)

#with open("test_result2.json", "w", encoding='utf-8') as f: 
#    json.dump(pro, f, ensure_ascii=False, indent=4)

#pi = Preference_Item(1, "random")
#print(pi.to_string())

#print(pref.categories[0].to_string())
