import numpy as np
import pandas as pd
import Preference_Item
from datetime import datetime

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


