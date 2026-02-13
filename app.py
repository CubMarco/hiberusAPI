from flask import Flask, jsonify
import requests
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)

URL_API = "https://jsonplaceholder.typicode.com/"


# =============================================
#     SE EXTRAE INFORMACION DEL USUARIO
# =============================================
@app.route("/usuario/<int:id>", methods=['GET'])
def getUserInfo(id):
    try:
        response = requests.get(f"{URL_API}/users/{id}")

        # Si hubo un error en la respuesta se retorna 404
        if response.status_code != 200:
            logging.warning(f"El usuario con id={id} no se encontro")
            return jsonify({"status" : "error", "message":"No se encontro el usuario"}), 404
        
        response_json = response.json()
        # Se imprimen los mensajes en log y consola
        messageFromJson = f"Soy el usuario con id:{response_json["id"]}, y mi correo es: {response_json["email"]}"
        logging.info(messageFromJson)
        print(messageFromJson)

        return response_json

    except Exception as e:
        logging.error(f"Hubo un error en el servidor, con mensaje {str(e)}")
        return jsonify({"status" : "error", "message" : "Hubo un error en el servidor"}), 500


# =============================================
#                   MAIN
# =============================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")