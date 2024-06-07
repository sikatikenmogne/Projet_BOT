import os
import google.generativeai as gn
import json

from flask import Flask
from flask_mysqldb import MySQL

from app import mysql


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


    # def generate_response(user_input):
    #
    #     app = Flask(__name__)
    #     mysql = MySQL(app)
    #
    #     for scenario in prompts_data['scenario']:
    #         if user_input.lower() in scenario['input'].lower():
    #             if user_input.lower() == "je voudrais passer une reservation":
    #                 try:
    #                     cur = mysql.connection.cursor()
    #                     cur.execute("SELECT date, heure, np FROM reservation")
    #                     reservation = cur.fetchall()
    #                     cur.close()
    #                     reservation_list = ', '.join([f"{r[0]}, {r[1]}, {r[2]}" for r in reservation])
    #                     prompt = scenario['response'] + " " + reservation_list
    #                     response = model.generate_content(prompt)
    #                     return response.text
    #                 except Exception as e:
    #                     return f"Erreur lors de la récupération des réservations: {str(e)}"
    #             else:
    #                 prompt = scenario['response']
    #                 response = model.generate_content(prompt)
    #                 return response.text
    #     return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler votre question?"


    # Exemple d'utilisation
    response = generate_response(user_input)
    return response