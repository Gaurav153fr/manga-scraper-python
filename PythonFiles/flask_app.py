from flask import Flask,render_template,Response,request
from main import *
import os
app = Flask(__name__)



@app.route('/')
def watch():
    return render_template('home.html')

@app.route('/search' ,methods =('GET','POST'))
def hello_world():
    searchTerm = request.args.get('q')
    src = search(searchTerm)
    
  
    return render_template('Search.html',src=src,searchTerm=searchTerm)

@app.route('/mang/<name>',  methods=('GET', 'POST'))
def epi(name):
    src = getepi(name)
    
    return render_template('epi.html',epi=src,name=name,n=1)

@app.route("/manga/<li>/<cha>/",  methods=('GET', 'POST'))
def get_chap(li,cha):
    URL = 'https://www.mangaread.org/manga/'+li +"/" +cha
    
    src = scrapeImg(URL)
    print(URL)
    return render_template('Chapter.html',src=src,chapter = cha)
    
 


if __name__ == '__main__':
  app.run( port=5000, debug=True)