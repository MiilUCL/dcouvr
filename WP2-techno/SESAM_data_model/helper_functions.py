import pandas as pd

# GLOBAL VARIABLES
# links to termSets on the internet 
category_url = "https://tinyurl.com/sesam-categories"
location_url = "https://tinyurl.com/sesam-areas"
audience_url = "https://tinyurl.com/sesam-audiences"
# paths to termSets in local 
category_termSet_path = "data/DefinedTermSet_categories.csv"
audience_termSet_path = "data/DefinedTermSet_audience.csv"
location_termSet_path = "data/DefinedTermSet_location.csv"

def make_audience_block(url, name): 
    termSet = pd.read_csv(audience_termSet_path, encoding="latin1")
    termCode = termSet.loc[termSet["name"]==name, "termCode"].values[0]
    block = {"name":name, "termCode":termCode, "inDefinedTermSet":url}
    return block


def make_category_block(url, name):
    termSet = pd.read_csv(category_termSet_path, encoding="latin1")
    termCode = termSet.loc[termSet["name"]==name, "termCode"].values[0]
    block = {"name":name, "termCode":termCode, "inDefinedTermSet":url}
    return block 

def make_location_block(url, name):
    termSet = pd.read_csv(location_termSet_path, encoding="latin1")
    termCode = termSet.loc[termSet["name"]==name, "termCode"].values[0]
    block = {"name":name, "termCode":termCode, "inDefinedTermSet":url}
    return block 

def make_DefinedTerm_keywords_block(url, name): 
    termSet = pd.read_csv(category_termSet_path, encoding="latin1")
    termCode = termSet.loc[termSet["name"]==name, "termCode"].values[0]
    block = {"@type":"DefinedTerm", "name":name, "termCode":termCode, "inDefinedTermSet":url}
    return block 

def make_DefinedTerm_audience_block(url, name):
    termSet = pd.read_csv(audience_termSet_path, encoding="latin1")
    termCode = termSet.loc[termSet["name"]==name, "termCode"].values[0]
    block = {"@type":["Audience", "DefinedTerm"], "name":name, "termCode":termCode, "inDefinedTermSet":url}
    return block

def make_DefinedTerm_location_block(url, name):
    termSet = pd.read_csv(location_termSet_path, encoding="latin1")
    termCode = termSet.loc[termSet["name"]==name, "termCode"].values[0]
    block = {"@type":["Place", "DefinedTerm"], "name":name, "termCode":termCode, "inDefinedTermSet":url}
    return block 



