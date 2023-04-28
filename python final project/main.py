from flask import Flask, render_template, send_file
import os
import sqlite3


app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect('finalproject.db')
    c = conn.cursor()
    HTML="My dogs are:<br>"
    for row in c.execute('SELECT * FROM dogs ORDER BY dateofbirth'):
        dogname=row[0]
        HTML+= "<li><a href=\""+dogname+"\">"+dogname+"</a>"
    return HTML

@app.route("/<dogname>")
def showlist(dogname):
    return "list of images for " + dogname+ "<p><ul><li><a href=\"/images/nugget1.jpg\">Nuggets birthday</a></li></ul>"

@app.route("/images/<filename>")
def showimages(filename):
    return send_file( os.path.join("image_folder",filename), mimetype='image/gif')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
    
