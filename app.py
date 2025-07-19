from flask import Flask, render_template, request, jsonify, session
from cipher.logic import caesar_encrypt, caesar_decrypt

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Change this to a random secret in production

import json


def get_user_data():
    history = session.get('history', [])
    favorites = session.get('favorites', [])
    return history, favorites

def set_user_data(history, favorites):
    session['history'] = history
    session['favorites'] = favorites

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    text = ""
    shift = 3
    action = ""
    user_history, user_favorites = get_user_data()

    if request.method == "POST":
        text = request.form.get("text")
        shift = int(request.form.get("shift", 3))
        action = request.form.get("action")

        if action == "encrypt":
            result = caesar_encrypt(text, shift)
        elif action == "decrypt":
            result = caesar_decrypt(text, shift)
        elif action == "favorite":
            user_favorites.append(text)
        elif action == "clear":
            result = ""
            text = ""

        if action in ["encrypt", "decrypt"]:
            user_history.append((action, text, result))

        set_user_data(user_history, user_favorites)

    return render_template("index.html", result=result, text=text, shift=shift,
                           history=user_history[-5:], favorites=user_favorites[-5:])

@app.route("/process", methods=["POST"])
def process():
    text = request.form.get("text", "")
    shift = int(request.form.get("shift", 3))
    action = request.form.get("action", "")
    result = ""
    user_history, user_favorites = get_user_data()

    if action == "encrypt":
        result = caesar_encrypt(text, shift)
    elif action == "decrypt":
        result = caesar_decrypt(text, shift)
    elif action == "favorite":
        user_favorites.append(text)
    elif action == "clear":
        result = ""
        text = ""

    if action in ["encrypt", "decrypt"]:
        user_history.append((action, text, result))

    set_user_data(user_history, user_favorites)

    return jsonify({
        "result": result,
        "text": text,
        "shift": shift,
        "history": user_history[-5:],
        "favorites": user_favorites[-5:]
    })

# if __name__ == "__main__":
#     app.run(debug=True)
