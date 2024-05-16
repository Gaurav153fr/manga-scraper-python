from flask import Flask,render_template,Response,request
from main import *

app = Flask(__name__)



@app.route('/')
def watch():
    searchTerm=''
    src = search(searchTerm,0)
    return render_template('series-list.html',src=src,searchTerm=searchTerm)

@app.route('/search' ,methods =('GET','POST'))
def hello_world():
    searchTerm = request.args.get('q')
    pageNumber=request.args.get('p')
    src = search(searchTerm,pageNumber)
    
  
    return render_template('series-list.html',src=src,searchTerm=searchTerm)

@app.route('/manga/<name>',  methods=('GET', 'POST'))
def epi(name):
    src = getepi(name)
    
    return render_template('episode-list.html',epi=src,name=name,n=1)

@app.route("/manga/<li>/<cha>/",  methods=('GET', 'POST'))
def get_chap(li,cha):
    URL = 'https://www.mangaread.org/manga/'+li +"/" +cha
    
    src = scrapeImg(URL)
    print(URL)
    return render_template('chapter-read.html',src=src,chapter = cha)
    
 


if __name__ == '__main__':
  app.run( port=5000, debug=True)