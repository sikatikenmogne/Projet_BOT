import json
import os
import google.generativeai as gn
import requests
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)


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

def get_all_prod():
    app = Flask(__name__)
    mysql = MySQL(app)
    cur = mysql.connection.cursor()
    cur.execute("SELECT Nom, Prix,description FROM produit")
    products = cur.fetchall()
    cur.close()
    print("----------------")
    productList = ''
    for i in products:
        for j in i:
            print(j)
            productList += str(j) + ' ,'
    return productList

def get_list_prod():
    productsList = []
    app = Flask(__name__)
    mysql = MySQL(app)
    cur = mysql.connection.cursor()
    cur.execute("SELECT Nom FROM produit")
    products = cur.fetchall()
    cur.close()
    for product in products:
        productsList.append(product[0])
    return productsList

def word_in_product(word):
    product_names = get_list_prod()
    lower_word = word.lower()
    for product_name in product_names:
        if lower_word in product_name.lower():
            return True
    return False

def discussion(user_input):

    # Chemin vers le fichier de configuration JSON
    PROMPTS_FILE = './Prompts/prompts.json'


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

        for scenario in prompts_data['scenarios']:
            if user_input.lower() in scenario['input'].lower():
                if user_input.lower() in ['commande','commander','acheter']:

                    prompt = scenario['output'] + get_all_prod();
                    response = model.generate_content(prompt)
                    print(response.text)
                    return response.text
                else:
                    prompt = scenario['output']
                    response = model.generate_content(prompt)
                    return response.text
            else:
                words = user_input.split()
                for word in words:
                    if word.lower() in scenario['input'].lower():
                        prompt = scenario['output']
                        response = model.generate_content(prompt)
                        return response.text

                    elif word.lower() in ['commande','commander','acheter']:

                        prompt = scenario['output'] + get_all_prod();
                        response = model.generate_content(prompt)
                        print(response.text)
                        return response.text

                    elif word_in_product(word):

                        url = "http://127.0.0.1:5000/commande"
                        payload = {
                            "idUser": 1,
                            "date": "2024-05-24 12:00:00",
                            "heure": "2024-05-24 14:38:40",
                            "stat": "en cours"
                        }
                        # Convertir le dictionnaire en chaîne JSON pour vérification
                        payload_json = json.dumps(payload)
                        print("Payload JSON:", payload_json)

                        headers = {
                            "Content-Type": "application/json",  # Indique que le contenu est en JSON
                            "Authorization": "Bearer your_token_here"
                            # Remplacez par votre token d'autorisation si nécessaire
                        }
                        responseApi = requests.post(url, data=payload_json, headers=headers)

                        # Vérifier le statut de la réponse
                        if responseApi.status_code == 200:
                            data = responseApi.json()
                            print(data)
                            # Afficher les détails de la requête pour diagnostic
                            print("Request URL:", responseApi.request.url)
                            print("Request Headers:", responseApi.request.headers)
                            print("Request Body:", responseApi.request.body)
                            prompt = "le client a commander " + word.lower() + ". dis luis que sa commande a été enregistré avec succès"
                            response = model.generate_content(prompt)
                            print(response.text)

                            return 'response.text'
                        else:
                            # Afficher le statut et le message d'erreur
                            print(f"Error: {responseApi.status_code}")
                            return " commande non enregistrée"



        return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler votre question?"


    # Exemple d'utilisation
    response = generate_response(user_input)
    return response