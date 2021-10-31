from flask import Flask,render_template,request
from database import *
from styleformer import Styleformer
import torch
app = Flask(__name__,template_folder='templates',static_folder='static')
get_users()
sf = Styleformer(style=0)
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form['name']
        topic = sf.transfer(request.form['topic'])
        essay_words = request.form['essay'].split(',')
        essay = ''
        for word in essay_words:
            essay += str(sf.transfer(word))+ " "
         
        if(not essay or not name or not topic):
            return render_template('index.html')
        else:
            CreateUser(name, topic, essay)
            get_users()
            return render_template('formal_index.html',
                essay = essay,
                name=name,
                topic=topic
                )
@app.route('/how-to',methods=['GET'])
def how_to():
    if request.method == 'GET':
        return render_template("how_to.html")
if __name__ == '__main__':
    app.run(debug=True)

