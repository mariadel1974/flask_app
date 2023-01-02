from elasticsearch import Elasticsearch
from flask import Flask, render_template
import os

app = Flask(__name__)

es = Elasticsearch(host='elastic')

picFolder=os.path.join('static','pics')

app.config['UPLOAD_FOLDER']=picFolder

@app.route("/")
def index():
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'],'pic2.png')
    return render_template("index.html", user_image = pic2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
