from flask import Flask, render_template, request

app = Flask(__name__)


def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    original = ""
    action = ""
    shift = 3

    if request.method == "POST":

        original = request.form.get("message", "")
        action = request.form.get("action", "encrypt")

        try:
            shift = int(request.form.get("shift", 3))
            shift = max(1, min(25, shift))
        except ValueError:
            shift = 3

        if action == "encrypt":
            result = encrypt(original, shift)
        else:
            result = decrypt(original, shift)

    return render_template(
        "index.html",
        result=result,
        original=original,
        action=action,
        shift=shift
    )


if __name__ == "__main__":
    app.run(debug=True)