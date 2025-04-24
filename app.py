from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o front-end acesse esse servidor

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").lower()

    # Simulação simples de respostas
    if "adotar" in user_message:
        response = "Você pode adotar um pet clicando em 'Download' e preenchendo o formulário!"
    elif "contato" in user_message:
        response = "Você pode entrar em contato conosco pelo e-mail: contato@paraisopatinha.com.br"
    elif "oi" in user_message or "olá" in user_message:
        response = "Olá! Como posso te ajudar com nossos animaizinhos hoje? 🐶🐱"
    else:
        response = "Desculpe, não entendi. Você pode reformular a pergunta?"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
