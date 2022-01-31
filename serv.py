from flask import Flask, request
import json
import psycopg2

app = Flask(__name__)

@app.route("/knit_urls", methods=['GET'])
def get_knit_urls():
    pass

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