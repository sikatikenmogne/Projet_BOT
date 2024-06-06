import os
import google.generativeai as gn
import json

from flask import Flask
from flask_mysqldb import MySQL


def discussion(message):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
        r"C:\Users\Miss MK\Desktop\2 EME ANNEE\STAGE\Projet BOT KENGNI Mires"
        r"\monprojetchat-2024-ca4187bfef81.json"
    )
    model = gn.GenerativeModel('gemini-pro')
    response = model.generate_content(message)

    print(response.text)
    return response.text

# discussion("Parle moi du Cameroun")

def discussion(user_input):

    # Chemin vers le fichier de configuration JSON
    PROMPTS_FILE = './Prompts/promts.json'

    # Charger les prompts à partir du fichier JSON
    def load_prompts(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # Initialiser les prompts
    prompts_data = load_prompts(PROMPTS_FILE)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
        r"C:\Users\Miss MK\Desktop\2 EME ANNEE\STAGE\Projet BOT KENGNI Mires"
        r"\monprojetchat-2024-ca4187bfef81.json"
    )

    model = gn.GenerativeModel('gemini-pro')

    # Fonction pour générer une réponse en utilisant les prompts JSON
    def generate_response(user_input):
        app = Flask(__name__)
        mysql = MySQL(app)

        for scenario in prompts_data['scenarios']:
            if user_input.lower() in scenario['input'].lower():
                if user_input.lower() == "je voudrais passer une commande":
                    cur = mysql.connection.cursor()
                    cur.execute("SELECT Nom FROM produit")
                    products = cur.fetchall()
                    cur.close()
                    print("----------------")
                    productList = ''
                    for i in products:
                        for j in i:
                            print(j)
                            productList += str(j) + ' ,'
                    print(productList)
                    prompt = scenario['output'] + str(productList)
                    response = model.generate_content(prompt)
                    print(response.text)
                    return response.text
                else:
                    prompt = scenario['output']
                    response = model.generate_content(prompt)
                    return response.text

        return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler votre question?"

    # Exemple d'utilisation
    response = generate_response(user_input)
    return response