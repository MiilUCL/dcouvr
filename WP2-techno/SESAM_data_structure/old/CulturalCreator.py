import random 
from datetime import datetime
import json
from datetime import datetime
from helper_functions import *
#from helper_functions import make_audience_block, make_category_block, make_location_block
import pandas as pd
import numpy as np
import Preference_Item
#from poc_examples import *


# GLOBAL VARIABLES
# links to termSets on the internet 
category_url = "https://tinyurl.com/sesam-categories"
location_url = "https://tinyurl.com/sesam-areas"
audience_url = "https://tinyurl.com/sesam-audiences"
# paths to termSets in local 
category_termSet_path = "SESAM_data_structure/data/DefinedTermSet_categories.csv"
audience_termSet_path = "SESAM_data_structure/data/DefinedTermSet_audience.csv"
location_termSet_path = "SESAM_data_structure/data/DefinedTermSet_location.csv"
# paths to events, creators, operators examples 
events_examples_path = "SESAM_data_structure/data/events_examples.json"
operators_examples_path = "SESAM_data_structure/data/operators_examples.json"
creators_examples_path = "SESAM_data_structure/data/creators_examples.json"
# current version to SESAM ontology (fake)
versioning_url = "https://sesam.be/data_model_v0" 

