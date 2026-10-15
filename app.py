
from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Bienvenue dans mon projet Pandas et Flask !"

if __name__ == "__main__":
    app.run(debug=True)
