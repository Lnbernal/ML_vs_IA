from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Flask"
if __name__ == " main ":     
        app.run(debug=True) 