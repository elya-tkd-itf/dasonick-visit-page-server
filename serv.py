from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/knit_urls", methods=['GET'])
def get_knit_urls():
    pass