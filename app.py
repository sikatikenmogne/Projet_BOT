from flask import Flask, jsonify, render_template, request, url_for
from flask_mysqldb import MySQL
from jinja2 import TemplateNotFound
import smtplib
import os
from dotenv import load_dotenv
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Chat import discussion


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


@app.route('/mail', methods=['POST'])
def send_mail():
    data = request.get_json()

    required_keys = ['sender', 'recipient', 'subject', 'body']
    for key in required_keys:
        if key not in data:
            return jsonify({"error": f"La clé '{key}' est manquante"}), 400

    sender = data['sender']
    recipient = data['recipient']
    subject = data['subject']
    body = data['body']

     # Envoi du mail
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    email_address = os.getenv('kengnimires003@gmail.com')
    email_password = os.getenv('698206094')

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(sender, recipient, msg.as_string())
    except smtplib.SMTPAuthenticationError:
        return jsonify({"error": "Erreur d'authentification SMTP. Vérifiez vos identifiants."}), 500
    except smtplib.SMTPException as e:
        return jsonify({"error": f"Erreur lors de l'envoi du mail: {str(e)}"}), 500

    return jsonify({'message': 'Mail envoyé avec succès.'}), 200

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