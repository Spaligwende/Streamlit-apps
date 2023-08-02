import streamlit as st
# Désactiver tous les avertissements de Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Votre code Streamlit continue ci-dessous...

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Analyse des potentiels de gaz verts à horizon 2050 par département", layout="wide")

# Create menu
menu_options = ["Accueil", "Analyse descriptive", "Comparaison régionale", "Répartition géographique"]
selected_menu = st.sidebar.selectbox("Menu", menu_options)

# Load data
path = "repartition.xlsx"
df = pd.read_excel(path)

# Add personal information to the sidebar
st.sidebar.subheader("Personal Information")
st.sidebar.write("Nom: SIMPORE")
st.sidebar.write("Prénoms: Paligwende Idriss")
st.sidebar.write("LinkedIn: [Paligwendé Idriss SIMPORE](https://www.linkedin.com/in/paligwendé-idriss-simpore-97372a176/)")
st.sidebar.write("GitHub: [Spaligwende](https://github.com/Spaligwende)")

# Add course information to the sidebar
st.sidebar.subheader("Course Information")
st.sidebar.write("**Course Name:** Business Intelligence")
st.sidebar.write("Course Description: This is a business intelligence course where we learn about analyzing datasets and showcasing our skills using Streamlit, Python, and analytical techniques.")
st.sidebar.write("Professor: Mr. Mano MATHEW")

# Load logos
logo1 = Image.open(r"Efrei.png")
logo2 = Image.open(r"PSB.png")

# Display logos
st.sidebar.image(logo1, use_column_width=True)
st.sidebar.image(logo2, use_column_width=True)

# Add logos and contact information
#col1, col2 = st.sidebar.columns([1, 3])
#col1.image(r"C:\Users\Simpo\streamlitProject\Efrei.png", use_column_width=True)
#col1.image(r"C:\Users\Simpo\streamlitProject\PSB.png", use_column_width=True)
#col2.write("Nom: SIMPORE\nPrénoms: Paligwende Idriss\nLinkedin: [https://www.linkedin.com/in/paligwendé-idriss-simpore-97372a176/](https://www.linkedin.com/in/paligwendé-idriss-simpore-97372a176/)\nGitHub: Spaligwende")

if selected_menu == "Accueil":
    # Title and introduction
    st.title("Analyse des potentiels énergétiques")
    st.markdown("## Étude sur les potentiels de gaz verts à horizon 2050 par département énergétiques en France")
    st.markdown("Cette application permet d'analyser les potentiels énergétiques dans différentes régions et départements par type de ressource et par filière en France à l'horizon 2050.")
    st.write("Sont considérées les ressources primaires suivantes :")
    st.write("- Le potentiel de production de méthane avec les CIMSE (Cultures intermédiaires multi-services environnementaux), les résidus de cultures, les déjections d'élevage, les herbes, les résidus des industries agro-alimentaires (IAA), les bio-déchets et les algues, en GWh PCS.")
    st.write("- Le potentiel bois énergie - en GWh PCI.")
    st.write("- Le potentiel d'énergie de récupération : combustibles Solides de Récupération (CSR) et Hydrogène fatal (H2) - en GWh PCI.")
    st.write("- Le potentiel de production d'électricité par Power-to-Gas, en GWh élec.")
    st.write("Dans l'étude, le potentiel de gaz injectable est obtenu en appliquant les rendements de conversion suivants aux ressources primaires :")
    st.write("- 94% méthane injecté / méthane produit.")
    st.write("- 70% pour la gazéification (potentiel bois énergie et potentiel CSR).")
    st.write("- 66% pour le power-to-gas.")

    st.write("<p style='font-weight:bold; color:blue;'>Utilisez le menu de gauche pour accéder aux différentes analyses.</p>", unsafe_allow_html=True)

    # Add more content about the study

elif selected_menu == "Analyse descriptive":
    # Title
    st.title("Analyse descriptive des potentiels énergétiques")

    # Display first lines
    st.subheader("Afficher les premières lignes du dataframe")
    st.dataframe(df.head())

    # Number of departments
    nombre_departements = df['code_departement'].nunique()
    st.subheader("Nombre de départements")
    st.write(nombre_departements)

    # Number of variables
    nombre_variables = df.shape[1]
    st.subheader("Nombre de variables")
    st.write(nombre_variables)

    # Descriptive analysis of potentials
    potentiels = ['potentiel_total_production_methane', 'potentiel_bois_energie', 'potentiel_electricite_power_to_gas', 'energie_recuperation_csr']
    description_potentiels = df[potentiels].describe()
    st.subheader("Analyse descriptive des potentiels")
    st.dataframe(description_potentiels)

    # Correlation matrix
    correlation_matrix = df[["potentiel_total_production_methane", "potentiel_bois_energie", "potentiel_electricite_power_to_gas"]].corr()

    # Heatmap of correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation entre les potentiels")
    st.subheader("Matrice de corrélation entre les potentiels")
    st.pyplot()

elif selected_menu == "Comparaison régionale":
    # Title
    st.title("Comparaison des potentiels énergétiques entre régions")

    # Comparison of potentials between regions
    potentiels = ['potentiel_total_production_methane', 'potentiel_bois_energie', 'potentiel_electricite_power_to_gas', 'energie_recuperation_csr']
    potentiels_regions = df.groupby('code_insee_region')[potentiels].sum()
    #regions_max_potentiels = potentiels_regions.idx.
    # Comparison of potentials between regions (continued)
    regions_max_potentiels = potentiels_regions.idxmax(axis=0)
    regions_min_potentiels = potentiels_regions.idxmin(axis=0)

    st.subheader("Régions avec les potentiels les plus élevés")
    st.write(regions_max_potentiels)

    st.subheader("Régions avec les potentiels les plus faibles")
    st.write(regions_min_potentiels)

    # Bar plot of potentials by region
    plt.figure(figsize=(12, 8))
    potentiels_regions.plot(kind='bar')
    plt.title("Potentiels énergétiques par région")
    plt.xlabel("Région")
    plt.ylabel("Potentiel")
    st.subheader("Potentiels énergétiques par région")
    st.pyplot()

elif selected_menu == "Répartition géographique":
    # Title
    st.title("Répartition géographique des potentiels énergétiques")

    # Load shapefile data
    #shapefile_path = "regions_shapefile.shp"
    #gdf = gpd.read_file(shapefile_path)

    # Merge shapefile data with potential data
    #merged_df = gdf.merge(df, left_on='code_insee', right_on='code_insee_region')

    # Map of potential by region
    #fig, ax = plt.subplots(figsize=(12, 8))
    #merged_df.plot(column='potentiel_total_production_methane', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    #ax.set_title("Répartition géographique du potentiel de production de méthane")
    #ax.axis('off')
    #st.subheader("Répartition géographique du potentiel de production de méthane")
    #st.pyplot()

# Page: Répartition géographique des potentiels d'électricité power-to-gas
#elif selected_option == "Répartition géographique des potentiels d'électricité power-to-gas":
    st.subheader("Répartition géographique des potentiels d'électricité power-to-gas")
    shapefile_url = "https://www.data.gouv.fr/fr/datasets/r/90b9341a-e1f7-4d75-a73c-bbc010c7feeb"
    regions = gpd.read_file(shapefile_url)
    regions.rename(columns={'code': 'code_departement'}, inplace=True)
    merged_data = pd.concat([regions, df], axis=1, join='inner')
    plt.figure(figsize=(12, 8))
    merged_data.plot(column='potentiel_electricite_power_to_gas', cmap='coolwarm', legend=True)
    plt.title('Répartition géographique des potentiels d\'électricité power-to-gas')
    st.pyplot()

# Page: Répartition des potentiels de production de méthane par département
#elif selected_option == "Répartition des potentiels de production de méthane par département":
    st.subheader("Répartition des potentiels de production de méthane par département")
    plt.figure(figsize=(12, 6))
    sns.barplot(x="departement", y="potentiel_total_production_methane", data=df)
    plt.xticks(rotation=90)
    plt.title("Répartition des potentiels de production de méthane par département")
    plt.xlabel("Département")
    plt.ylabel("Potentiel de production de méthane")
    st.pyplot()

# Dropdown list of departments
departements_list = df['departement'].unique()
departements_dropdown = st.selectbox("Sélectionner un département", departements_list)

# Plot potentials distribution for selected department
def plot_repartition_potentiels(departement):
    plt.figure(figsize=(10, 6))
    df_departement = df[df['departement'] == departement]
    plt.bar(df_departement['code_departement'], df_departement['potentiel_total_production_methane'])
    plt.xlabel('Code Département')
    plt.ylabel('Potentiel total de production de méthane')
    plt.title('Répartition des potentiels de méthane pour {}'.format(departement))
    st.pyplot()

st.subheader("Répartition des potentiels de méthane par département")
plot_repartition_potentiels(departements_dropdown)

# Departments with highest wood energy potentials
top_departements_bois = df.nlargest(5, "potentiel_bois_energie")
plt.figure(figsize=(8, 6))
sns.barplot(x="departement", y="potentiel_bois_energie", data=top_departements_bois)
plt.title("Départements avec les plus hauts potentiels de bois énergie")
plt.xlabel("Département")
plt.ylabel("Potentiel de bois énergie")
st.subheader("Départements avec les plus hauts potentiels de bois énergie")
st.pyplot()

# Pie chart for top 10 departments with energy recovery potential
departement_potentiel = df.groupby('departement')['energie_recuperation_csr'].sum().reset_index()
top_10_departements = departement_potentiel.nlargest(10, 'energie_recuperation_csr')
plt.pie(top_10_departements['energie_recuperation_csr'], labels=top_10_departements['departement'], autopct='%1.1f%%')
plt.title('Top 10 des départements avec le plus de potentiel en énergie de récupération')
st.subheader("Top 10 des départements avec le plus de potentiel en énergie de récupération")
st.pyplot()

# Add a footer
st.markdown("---")
st.write("Contactez l'auteur pour plus d'informations sur l'étude et les résultats.")
