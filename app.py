from flask import Flask, jsonify, request
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configuration de la base de données
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'chatbot_projet'
app.config['MYSQL_DB'] = 'chatbot_second'


mysql = MySQL(app)


@app.route('/reservation', methods = ['POST'])
def ajouter_reservation():
    data = request.get_json()
    idUser = data.get('idUser')
    date = data.get('date')
    heure = data.get('heure')
    np = data.get('np')
    stat = data.get('stat')
    try:
        cur = mysql.connection.cursor()
        cur.execute("call addreservation(%s,%s, %s, %s, %s)", (idUser, date,heure,np,stat))
        mysql.connection.commit()
        cur.close()
        return ("Sucess")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/commande', methods=['POST'])
def addCommande():
    data = request.get_json()
    idUser = data.get('idUser')
    date = data.get('date')
    heure = data.get('heure')
    stat = data.get('stat')
    quant = data.get('quant')

    try:
        cur = mysql.connection.cursor()

        cur.execute("CALL InsertCommande_new(%s, %s, %s)", (idUser, date, stat))

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


@app.route('/products', methods=['GET'])
def get_products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produit")
    products = cur.fetchall()
    cur.close()

    # Transformation des produits en dictionnaires
    products_list = []
    print(products)
    for product in products:
        product_dict = {
            'id': product[0],
            'name': product[1],
            'description': product[2],
            'price': product[3],
            'category': product[4],
            'availability': product[5],

        }
        products_list.append(product_dict)

    return jsonify(products_list)


if __name__ == '__main__':
    app.run(debug=True)






