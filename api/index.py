from flask import Flask, render_template
from flask_cors import CORS
from mangum import Mangum

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

handler = Mangum(app)  # Adaptador serverless
