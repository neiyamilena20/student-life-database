import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("/Users/neiyamilenadasilvametange/Desktop/projet portfolio/student-life-database/student_depression_dataset.csv")

# Nettoyer les noms de colonnes
colonnes_nettoyees = []  # Une nouvelle liste vide

for i in df.columns:  # Pour chaque nom de colonne existant
    colonnes_nettoyees.append(i.strip())  # On enlève les espaces et on ajoute à la liste

# On remplace les anciennes colonnes par les nouvelles colonnes propres
df.columns = colonnes_nettoyees

# === Étape 2 : Créer la table city ===
city_df = df[['City']].drop_duplicates().reset_index(drop=True)
city_df['id'] = city_df.index + 1  # créer une colonne ID
city_df.rename(columns={'City': 'name'}, inplace=True)
city_df = city_df[['id', 'name']]


# === Étape 2 : Créer la table profession ===
profession_df = df[['Profession']].drop_duplicates().reset_index(drop=True)
profession_df['id'] = profession_df.index + 1  # créer une colonne ID
profession_df.rename(columns={'Profession': 'name'}, inplace=True)
profession_df = profession_df[['id', 'name']] # Reordonner les colonnes : d'abord id, puis name


#les merges avec les id city et profession pour la table perosn
df = df.merge(city_df[['name', 'id']], left_on='City', right_on='name')
df.rename(columns={'id_y': 'city_id'}, inplace=True)

df = df.merge(profession_df[['name', 'id']], left_on='Profession', right_on='name')
df.rename(columns={'id': 'profession_id'}, inplace=True)

#print(df.columns)

# === Étape 3 : Créer la table person ===
person_df = df[['Gender', 'Age', 'Degree', 'city_id', 'profession_id']].reset_index(drop=True)
person_df['id'] = person_df.index + 1
person_df = person_df[['id', 'Gender', 'Age', 'Degree', 'city_id', 'profession_id']]
df.drop(columns=['name_x', 'name_y', 'id_x'], inplace=True)

print("====== Table des personnes ======")
print(person_df)
