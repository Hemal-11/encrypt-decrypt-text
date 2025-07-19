from flask import Flask, render_template, request, jsonify
from cipher.logic import caesar_encrypt, caesar_decrypt

app = Flask(__name__)

history = {}
favorites = {}

@app.route("/", methods=["GET", "POST"])
def get_ip():
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[0]
    else:
        ip = request.remote_addr
    return ip

def index():
    result = ""
    text = ""
    shift = 3
    action = ""
    ip = get_ip()
    user_history = history.setdefault(ip, [])
    user_favorites = favorites.setdefault(ip, [])

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

    return render_template("index.html", result=result, text=text, shift=shift,
                           history=user_history[-5:], favorites=user_favorites[-5:])

@app.route("/process", methods=["POST"])
def process():
    text = request.form.get("text", "")
    shift = int(request.form.get("shift", 3))
    action = request.form.get("action", "")
    result = ""
    ip = get_ip()
    user_history = history.setdefault(ip, [])
    user_favorites = favorites.setdefault(ip, [])

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

    return jsonify({
        "result": result,
        "text": text,
        "shift": shift,
        "history": user_history[-5:],
        "favorites": user_favorites[-5:]
    })

if __name__ == "__main__":
    app.run(debug=True)
