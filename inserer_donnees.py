import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Connexion
try:
    engine = create_engine("postgresql://postgres:Solene33@localhost:5432/student_life")
    print("Connexion à la base PostgreSQL réussie.")
except Exception as e:
    print("Erreur de connexion à PostgreSQL :", e)
    exit()
# Charger les fichiers
try:
    person_df = pd.read_csv("person.csv")
    city_df = pd.read_csv("city.csv")
    profession_df = pd.read_csv("profession.csv")
    mentalhealth_df = pd.read_csv("mental_health.csv")
    academicwork_df = pd.read_csv("academic_work.csv")
    print("Tous les fichiers CSV ont été chargés.")
except Exception as e:
    print("Erreur lors du chargement des fichiers CSV :", e)
    exit()


# Étape 3 : Insertion des données dans PostgreSQL
tables = {
    "city": city_df,
    "profession": profession_df,
    "person": person_df,
    "mental_health": mentalhealth_df,
    "academic_work": academicwork_df
}

for table_name, df in tables.items():
    try:
        df.to_sql(table_name, engine, index=False, if_exists="append")
        print(f"Table '{table_name}' insérée avec succès.")
    except SQLAlchemyError as e:
        print(f"Erreur lors de l'insertion de la table '{table_name}' :", e)
