from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    title= "Anagrams Website"
    
    return render_template('main.html', title=title )

@app.route('/words/<string:word>')
def word(word):
    file= open ("C:\words.txt",'r') 
    word_list = file.read().splitlines()
    words = word.upper() 
    l=[]
    for a in word_list:
        if sorted(word.upper()) == sorted(a):
            l.append (a)    
  
    return render_template('words.html', word=word,words=words, anagrams=l)