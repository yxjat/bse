from flask import render_template, Flask, request
import firebase_admin
from firebase_admin import credentials,firestore


cred = credentials.Certificate("bse-proj-firebase-adminsdk-y2qpa-1d30589af1.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

db = firestore.client()




i = 0

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        obj = {
        "tradingPrice" :  request.form.get('tradingPrice').value,
        "buyingTeam" : request.form.get('buyerTeam').value,
        "sellerTeam" : request.form.get('sellerTeam').value,
        "numStocks" : request.form.get('numStocks').value,
        }
        doc = db.collections(u'tranac').document(str(i)).set(obj)
        i+=1
    return (render_template('index.html'))