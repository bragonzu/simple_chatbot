from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pares = [
    [
        r"Hola",
        ["¡Hola! ¿En qué puedo ayudarte?"]
    ],
    [
        r"¿Cómo estás?",
        ["Estoy bien, gracias. ¿Y tú?"]
    ],
    [
        r"¿Cuál es tu nombre?",
        ["Mi nombre es ChatBot Grupo 9."]
    ],
    [
        r"Adiós",
        ["¡Hasta luego! Que tengas un buen día."]
    ],
    [
        r" (.*)(¿Qué puedes hacer\? | Que haces\?) (.*)",
        ["Puedo responder preguntas, darte información o simplemente tener una conversación contigo."]
    ],
    [
        r"Cuéntame un chiste|Cuentame un chiste",
        ["Claro, aquí tienes uno: ¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter."]
    ],
    [
        r"¿Dónde estás ubicado\?",
        ["Soy un chatbot en línea, así que estoy ubicado en el mundo virtual."]
    ],
    [
        r"Gracias",
        ["De nada. Si tienes más preguntas, estaré encantado de ayudarte."]
    ],
    [
        r"(.*) (triste|deprimido|mal)",
        ["Lamento escuchar eso. ¿Hay algo en lo que pueda ayudarte?"]
    ],
    [
        r"(.*) (feliz|bien)",
        ["Me alegra escuchar eso."]
    ],
    [
        r"quit",
        ["Hasta luego. ¡Que tengas un buen día!"]
    ]
]

chatbot = Chat(pares, reflections)

@app.route("/")
def home():
    return render_template("index.html")

mensajes = [] 

@app.route("/get_response", methods=["POST"])
def get_response():
    mensaje = request.form["mensaje"]
    respuesta = chatbot.respond(mensaje)
    mensajes.append((mensaje, respuesta))
    respuesta_actual = respuesta
    return jsonify({"respuesta": respuesta_actual, "mensajes": ''})

if __name__ == "__main__":
    app.run()
