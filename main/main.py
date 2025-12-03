import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mysql.connector
import traceback
import matplotlib.pyplot as plt
import numpy as np


# ============================
# 1. CARGAR DATASET
# ============================
def cargar_dataset():
    print("\n=== CARGANDO DATASET ===")
    try:
        df = pd.read_csv("data/dataset_con_codigos.csv")
        print("Dataset cargado correctamente.")
        print(df.head())
        return df
    except Exception as e:
        print("Error al cargar dataset.")
        print(e)
        return None


# ============================
# 2. INSERTAR COMUNAS EN MYSQL (OPCIONAL)
# ============================
def insertar_comunas_mysql(df):
    print("\n=== INSERTANDO COMUNAS EN MYSQL ===")
    
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tu_clave",   # ← CAMBIA ESTO
            database="inmobiliario"
        )
        cursor = conexion.cursor()

        comunas = df["Comuna"].drop_duplicates()

        for codigo in comunas:
            sql = "INSERT IGNORE INTO comuna (codigo, nombre) VALUES (%s, %s)"
            cursor.execute(sql, (codigo, codigo))  # Luego puedes editar los nombres

        conexion.commit()
        cursor.close()
        conexion.close()

        print("Comunas insertadas correctamente.")

    except Exception as e:
        print("Error al insertar comunas.")
        traceback.print_exc()


# ============================
# 3. UNIR COMUNA (CODIGO → NOMBRE)
# En password escribir la que tengan en MySQL, en mi caso 1402
# ============================
def unir_comunas(df):
    print("\n=== UNIENDO COMUNA (MySQL) ===")
    
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1402",
            database="inmobiliario"
        )

        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT codigo, nombre FROM comuna")
        diccionario = cursor.fetchall()

        df_dic = pd.DataFrame(diccionario)

        df_unido = df.merge(df_dic, left_on="Comuna", right_on="codigo", how="left")

        df_unido.to_csv("data/dataset_con_nombres.csv", index=False)

        print("Archivo dataset_con_nombres.csv generado.")
        return df_unido

    except Exception as e:
        print("Error al unir comunas.")
        traceback.print_exc()
        return df


# ============================
# 4. ENTRENAR MODELO ML
# ============================
def entrenar_modelo(df):
    print("\n=== ENTRENANDO MODELO RANDOM FOREST ===")

    try:
        features = ["Price_UF", "Built Area", "Total Area", "Dorms", "Baths", "Parking"]
        X = df[features]
        y = df["Comuna"]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.25, random_state=42, stratify=y
        )

        modelo = RandomForestClassifier(n_estimators=200, random_state=42)
        modelo.fit(X_train, y_train)

        y_pred = modelo.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print(f"Exactitud del modelo: {acc:.4f}")

        return modelo

    except Exception as e:
        print("Error al entrenar el modelo.")
        print(e)


# ============================
# 5. VISUALIZACIÓN DEL MODELO
# ============================
def visualizar_modelo(modelo, features):
    print("\n=== VISUALIZANDO IMPORTANCIA DE VARIABLES ===")

    try:
        importancias = modelo.feature_importances_
        indices = np.argsort(importancias)

        plt.figure(figsize=(10, 6))
        plt.barh(range(len(features)), importancias[indices], color="skyblue")
        plt.yticks(range(len(features)), [features[i] for i in indices])
        plt.title("Importancia de Variables - Random Forest")
        plt.xlabel("Importancia")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error al visualizar el modelo.")
        print(e)


df_1 = pd.read_csv("data/dataset_con_nombres.csv")

# ============================
# 6. MAIN
# ============================
if __name__ == "__main__":
    print("\n====================================")
    print("        EJECUCIÓN COMPLETA")
    print("====================================")

    df = cargar_dataset()
    if df is None:
        exit()

    unir_comunas(df)
    
    print("\n====================================")
    print("        COLUMNA NOMBRE CAMBIADA")
    print("====================================")
    print(df_1.head())

    entrenar_modelo(df)

    print("\n====================================")
    print("        GRÁFICO")
    print("====================================")
    
    modelo = entrenar_modelo(df)
    visualizar_modelo(modelo, ["Price_UF", "Built Area", "Total Area", "Dorms", "Baths", "Parking"])

    print("\n====================================")
    print("        PROCESO FINALIZADO")
    print("====================================")

