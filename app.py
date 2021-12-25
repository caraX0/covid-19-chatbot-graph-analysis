from azure.core.exceptions import ResourceNotFoundError
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
from flask import Flask, render_template,request,url_for
from werkzeug.utils import redirect,secure_filename


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html') 



     

if __name__=="__main__":
    app.run(debug=True)