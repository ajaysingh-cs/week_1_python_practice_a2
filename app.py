from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! Yeh mera pehla Flask server hai"

if __name__ == "__main__":
    app.run(debug=True)