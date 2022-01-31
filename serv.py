from flask import Flask, request
import json
import psycopg2

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def hello():
    return "hello", 200

@app.route("/knitting")
@cross_origin()
def get_knit_urls():
    cur.execute(f"select url, name, description from knitting")
    rows = cur.fetchall()
    all_info = list()
    for row in rows:
        all_info.append({"url":row[0], "name":row[1], "description":row[2]})
    return json.dumps(all_info), 200

if __name__ == "__main__":
    con = psycopg2.connect(
    user='qgwtaffqzzkrwi', 
    password='28b447e5b3da81fbc19e2ee85dc08f11df796755ec15e8c5b516d8f968a025ad', 
    host='ec2-52-31-201-170.eu-west-1.compute.amazonaws.com', 
    port=5432,
    database="d76afhoa7m2dj5"
    )
    cur = con.cursor()
    app.run()