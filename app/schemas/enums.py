from enum import Enum

class Sex(str,Enum):
    Man = "Homme"
    Woman = "Femme"
    Personnalized = "Personnalisé"

class Relation(str,Enum):
    single = "Célibataire"
    in_a_relationship = "En couple"
    Married = "Marié(e)"
    Complicated = "Compliqué"