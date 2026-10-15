
from flask import Flask, jsonify
import pandas as pd
import requests
import json

app = Flask(__name__)
with open("data_local.json", "r", encoding="utf-8") as fichier:
    produits_locaux = json.load(fichier)

df_local = pd.DataFrame(produits_locaux)

@app.route("/")
def accueil():
    return "Bienvenue dans Veille Pandas de Pierrette !"

@app.route("/api/v1/stats/produits", methods=["GET"])
def statistiques_produits():
    url = "https://dummyjson.com/products"

    reponse = requests.get(url, timeout=10)
    reponse.raise_for_status()

    donnees = reponse.json()
    df = pd.DataFrame(donnees["products"])

    series_prix = df["price"]
    stats = series_prix.describe().to_dict()

    resultat = {
        "total_produits": int(stats["count"]),
        "prix_moyen": round(stats["mean"], 2),
        "prix_min": stats["min"],
        "prix_max": stats["max"],
        "apercu_colonnes": list(df.columns)
    }

    return jsonify(resultat)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
