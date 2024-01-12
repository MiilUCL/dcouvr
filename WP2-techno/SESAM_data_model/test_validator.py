import json
from validator import __main__

# load predifined schemas 
with open("data/validation_schemas/profile_schema.json", "r", encoding="utf-8") as f_profile: 
    profile_reference = json.load(f_profile)
with open("data/validation_schemas/creator_schema.json", "r", encoding="utf-8") as f_creator: 
    creator_reference = json.load(f_creator)
with open("data/validation_schemas/operator_schema.json", "r", encoding="utf-8") as f_operator: 
    operator_reference = json.load(f_operator)
with open("data/validation_schemas/event_schema.json", "r", encoding="utf-8") as f_event: 
    event_reference = json.load(f_event)

test_profile = {
  "identifier":124,
  "timestamp": "2023-12-06T16:43:05.160547",
  "preferences": {
    "categories": [
      {
        "name": "CONTES / LITTÉRATURES - littérature",
        "termCode": "CAT06-02",
        "inDefinedTermSet": "https://tinyurl.com/sesam-categories",
        "rating": 4,
        "timestamp": "2023-12-06T16:43:05.187900"
      }
    ],
    "areas": [
      {
        "name": "Soignies",
        "termCode": "LOC13",
        "inDefinedTermSet": "https://tinyurl.com/sesam-areas",
        "rating": 1,
        "timestamp": "2023-12-06T16:43:05.220335"
      }
    ],
    "culturalProducts": [
      {
        "identifier": 10008,
        "name": "\"Les Bonnes\" de Jean genet",
        "type": "Event",
        "rating": 4,
        "timestamp": "2023-12-06T16:43:05.160547"
      },
      {
        "identifier": 10005,
        "name": "Vos livres ont la parole !",
        "type": "Event",
        "rating": 3,
        "timestamp": "2023-12-06T16:43:05.160547"
      },
      {
        "identifier": 10009,
        "name": "New project : KAIS FRIHAT QUARTET",
        "type": "Event",
        "rating": 2,
        "timestamp": "2023-12-06T16:43:05.160547"
      }
    ],
    "culturalOperators": [
      {
        "identifier": 20009,
        "name": "The Music Village",
        "rating": 1,
        "timestamp": "2023-12-06T16:43:05.160547"
      }
    ],
    "culturalCreators": [
    ]
  }
}


test_creator = {
      "@context": "https://schema.org",
      "@type":"PerformingGroup",
      "name": "Girls in Hawaii",
      "sameAs": "https://www.wikidata.org/wiki/Q2439293",
      "identifier": 30001,
      "keywords": []
    }



test_event = {
      "@context":"https://schema.org",
      "identifier": 10001,
      "name": "Raios Quartet (B) musique brésilienne et portugaise",
      "keywords": [
        {
          "@type": "DefinedTerm",
          "name": "CONCERTS - world (musique du monde) / Musique traditionnelle",
          "termCode": "CAT01-21",
          "inDefinedTermSet": "https://tinyurl.com/sesam-categories"
        }
      ],
      "location": {
        "@type": ["Place", "DefinedTerm"],
        "name": "Liège",
        "termCode": "LOC07",
        "inDefinedTermSet": "https://tinyurl.com/sesam-areas"
      },
      "organizer": {
        "@type": "Organization",
        "identifier":123,
        "name": "Blues-sphere Bar"
      },
      "description" : "Découvrez la musique brésilienne et portugaise avec le Raios Quartet au Blues-sphere Bar à Liège.",
      "startDate": "2023-11-23",
      "sameAs": "https://www.out.be/fr/evenements/136594_raios-quartet-b-musique-bresilienne-et-portugaise.html?proximus"
    }



test_operator = {
      "@context":"https://schema.org",
      "@type": "Organization",
      "name":"skibidi",
      "identifier": 20001,
      "keywords": [
        {
          "@type": "DefinedTerm",
          "name": "CONCERTS - world (musique du monde) / Musique traditionnelle",
          "termCode": "CAT01-21",
          "inDefinedTermSet": "https://tinyurl.com/sesam-categories"
        }
      ],
      "location": {
        "@type": ["Place", "DefinedTerm"],
        "name": "Liège",
        "termCode": "LOC07",
        "inDefinedTermSet": "https://tinyurl.com/sesam-areas"
      },
      "description" : "Lieu musical animé à Liège, concerts de musique traditionnelle et du monde.",
      "url": "https://www.blues-sphere.com/WordPress/", 
    }


with open("data/creators_examples.json", "r", encoding="utf-8") as f_creators: 
    creators = json.load(f_creators)
for c in creators["creators"]:
  __main__(c)
