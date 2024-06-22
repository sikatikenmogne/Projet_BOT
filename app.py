from flask import Flask, jsonify, render_template, request, url_for
from flask_mysqldb import MySQL
from google.oauth2.credentials import Credentials
from google_auth_httplib2 import Request
from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
from jinja2 import TemplateNotFound
from dotenv import load_dotenv
from Chat import discussion
import os
import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

load_dotenv()

app = Flask(__name__)

# Configuration de la base de données
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'chatbot'

mysql = MySQL(app)


@app.route('/')
def index():
    try:
        return render_template('bot.html')
    except TemplateNotFound as e:
        return f"Template not found: {e}", 404
    except Exception as e:
        return f"An error occurred: {e}", 500


@app.route('/reservation', methods=['POST'])
def ajouter_reservation():
    data = request.get_json()
    idUser = data.get('idUser')
    date = data.get('date')
    heure = data.get('heure')
    np = data.get('np')
    stat = data.get('stat')
    try:
        cur = mysql.connection.cursor()
        cur.execute("call addreservation(%s,%s, %s, %s, %s)", (idUser, date, heure, np, stat))
        mysql.connection.commit()
        cur.close()
        return ("Sucess")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/chat', methods=['POST'])
def interraction():
    data = request.get_json()
    message = data['message']
    response = discussion(message)
    response_str = str(response)

    return response_str



# def gmail_send_message():
#     creds = None
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 "API gmail.json ", SCOPES
#             )
#             creds = flow.run_local_server(port=0)
#         with open("token.json", "w") as token:
#             token.write(creds.to_json())
#
#     try:
#         # Créer un client API Gmail
#         service = build("gmail", "v1", credentials=creds)
#
#         # Créer le message email
#         message = EmailMessage()
#         message.set_content("votre commande est bien enregistrée. Merci! ")
#
#         message["To"] = "kengnimires003@gmail.com "
#         message["From"] = "miresmk004@gmail.com"
#         message["Subject"] = "PIZZALIGHT "
#
#         # Encoder le message en base64 pour l'API Gmail
#         encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
#
#         create_message = {"raw": encoded_message}
#         # pylint: disable=E1101
#         send_message = (
#             service.users()
#                 .messages()
#                 .send(userId="me", body=create_message)
#                 .execute()
#         )
#         print(f'ID du message : {send_message["id"]}')
#
#     except HttpError as error:
#         print(f"Une erreur s'est produite : {error}")
#         send_message = None
#
#     return send_message



@app.route('/commande', methods=['POST'])
def addCommande():
    data = request.get_json()
    idUser = data.get('idUser')
    date = data.get('date')
    heure = data.get('heure')
    stat = data.get('stat')
    # quant = data.get('quant')

    try:
        cur = mysql.connection.cursor()

        cur.execute("CALL AddCommande(%s, %s, %s)", (idUser, date, stat))

        cur.execute("SELECT @id_commande")

        id_commande = cur.fetchone()
        if id_commande:
            id_commande = id_commande[0]

            try:
                cur.execute("CALL AddLigneCommande(%s,%s, %s,%s)", (id_commande, date, heure, idUser))
            except Exception as e:
                print(e)

        mysql.connection.commit()
        cur.close()
        return "Succès"

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/produit', methods=['GET'])
def get_produit():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produit")
    produit = cur.fetchall()
    cur.close()

    # Transformation des produits en dictionnaires
    produit_list = []
    print(produit)
    for produit in produit:
        product_dict = {
            'id': produit[0],
            'name': produit[1],
            'description': produit[2],
            'prix': produit[3],
            'categorie': produit[4],
            'disponibilite': produit[5],

        }
        produit_list.append(product_dict)

    return jsonify(produit_list)


if __name__ == '__main__':
      app.run(debug=True)
      # gmail_send_message()
