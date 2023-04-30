from flask import Flask, render_template, send_file
import os
import sqlite3


app = Flask(__name__)

def table_cell(cell_text):
    return "<td align=center>"+cell_text+"</td>"

def table_row(row_text):
    return "<tr>"+row_text+"</tr>"

def htmltable(rows,parameters):
    return "<table "+parameters+">"+rows+"</table>"

def dog_info(dogname,icon_filename):
    return "<a href=\""+dogname+"\"> <img src=images/"+icon_filename+" width=100><br>"+dogname+" </a>"

#default page
@app.route("/")
def index():
    conn = sqlite3.connect('finalproject.db')
    c = conn.cursor()
    HTML='''<head><title>Avery's dog friends</title></head>
        <body>
        <center><h1>Avery's dog friends</h1>

        Welcome to my website. I chose to make an interactive photo album for my python class.

        <h4>Click on the dog's name to see photos</h4>
        </center>
    '''
    cells=""
    for row in c.execute('SELECT name,icon_filename FROM dogs ORDER BY dateofbirth'):
        dogname=row[0]
        icon_filename=row[1]
        cells+= table_cell(dog_info(dogname,icon_filename))

    HTML+=htmltable(table_row(cells),"border=2 width=100%")
    HTML+="</body>"
    return "<html>"+HTML+"</html>"

#dog details
@app.route("/<dogname>")
def showlist(dogname):
    conn = sqlite3.connect('finalproject.db')
    c = conn.cursor()
    HTML=""
    SQL="SELECT dog,descr,filename FROM pictures where dog='"+dogname+"'"
    #return SQL
    for row in c.execute(SQL):
        descr=row[1]
        filename=row[2]
        HTML+= "<li><a href=\"/images/"+filename+"\">"+descr+"</a>"

    if HTML=="": 
        HTML="no pictures of "+dogname+" found"
    else:
        HTML="Pictures of "+dogname+":<br>"+HTML 

    return HTML


#display image
@app.route("/images/<filename>")
def showimages(filename):
    return send_file( os.path.join("image_folder",filename), mimetype='image/gif')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
    
