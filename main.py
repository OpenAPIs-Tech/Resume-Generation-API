import json
from flask import Flask, request,jsonify,Response
from flask_cors import CORS, cross_origin

from service.pdfgen import genpdf1


app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello():
    return "hello"

@app.route('/generatePdf',methods=['POST'])
@cross_origin()
def mainpdfmaker():
    body = request.get_json()
    getPdf = genpdf1.generatePdff(body)
    return getPdf

if __name__=="__main__":
    app.run()
    # app.run(host='0.0.0.0', port=5000, debug=True)







