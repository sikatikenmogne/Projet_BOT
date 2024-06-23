import json
import os
import google.generativeai as gn
import requests
from flask import Flask
from flask_mysqldb import MySQL



app = Flask(__name__)


def discussion(message):

    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the relative path to the credentials file
    credentials_path = os.path.join(dir_path, 
                                    'chatbot-2024-427303-7d23c72c172f.json')
    # print(credentials_path)
    # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    model = gn.GenerativeModel('gemini-pro')
    response = model.generate_content(message)

    print(response.text)
    return response.text

# discussion("Parle moi du Cameroun")



def getProduct(word):
    app = Flask(__name__)
    mysql = MySQL(app)
    cur = mysql.connection.cursor()
    query = "SELECT Nom, Prix, description FROM produit WHERE nom = %s"

    word_bytes = word.encode('utf-8')

    cur.execute(query, (word_bytes,))

    product = cur.fetchall()
    cur.close()

    return product

def get_all_prod():
    app = Flask(__name__)
    mysql = MySQL(app)
    cur = mysql.connection.cursor()
    cur.execute("SELECT Nom, Prix,description FROM produit")
    products = cur.fetchall()
    cur.close()
    productList = ''
    for i in products:
        for j in i:
            productList += str(j) + ' ,'
    return str(products)


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
        print(word)
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
    
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.abspath(__file__))

    # Construct the relative path to the credentials file
    credentials_path = os.path.join(dir_path, 'chatbot-2024-427303-7d23c72c172f.json')

    # print(credentials_path)

    # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

    model = gn.GenerativeModel('gemini-pro')


    # Fonction pour générer une réponse en utilisant les prompts JSON

    def generate_response(user_input):

        # from app import gmail_send_message

        for scenario in prompts_data['scenarios']:
            if user_input.lower() in scenario['input'].lower():
                if user_input.lower() in ['commande','commander','acheter']:

                    prompt = scenario['output'] + get_all_prod();
                    print(prompt)
                    response = model.generate_content(prompt)
                    # gmail_send_message()
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

                        # prompt = scenario['output'][2] + get_all_prod();
                        prompt = scenario['output'][1] + get_all_prod()
                        print(prompt)
                        response = model.generate_content(prompt)
                        return "Que souhaiteriez vous commander? \n"+response.text

                    elif word_in_product(word):

                        url = "http://127.0.0.1:5000/commande"
                        payload = {
                            "idUser": "1",
                            "date": "2024-05-24 12:00:00",
                            "heure": "2024-05-24 14:38:40",
                            "stat": "pret"
                        }

                        payload_json = json.dumps(payload)
                        responseApi = requests.post(url, data=payload_json, headers={'Content-Type': 'application/json'})
                        print(responseApi.status_code)
                        print(word)
                        detail = str(getProduct(word))
                        # Vérifier le statut de la réponse
                        if responseApi.status_code == 200:
                            prompt = f"Le client a commandé {word.lower()}. Dis-lui que sa commande a été enregistrée avec succès. Donne lui en fin la facture de sa commande en fonction du produit suivant et le montant total :"+detail
                            response = model.generate_content(prompt)

                            return response.text
                        else:
                            print(responseApi.text)
                            return "Commande non enregistrée"
            return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler votre question?"



    # Exemple d'utilisation
    response = generate_response(user_input)
    return response