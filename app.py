from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "سلام! Flask روی GitHub Actions ران شد 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
