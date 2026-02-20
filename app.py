from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello from Python 3.14!</h1><p>Azure Web App is running successfully.</p>"

if __name__ == "__main__":
    # Azure App Service usually handles the port via environment variables, 
    # but 8000 is a safe default for local testing.
    app.run(host='0.0.0.0', port=8000)
