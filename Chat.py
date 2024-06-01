import os
import google.generativeai as gn

def discussion(message):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
        r"C:\Users\Miss MK\Desktop\2 EME ANNEE\STAGE\Projet BOT KENGNI Mires"
        r"\monprojetchat-2024-ca4187bfef81.json"
    )
    model = gn.GenerativeModel('gemini-pro')
    response = model.generate_content(message)

    print(response.text)
    return response.text

discussion("Parle moi du Cameroun")

