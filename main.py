from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True
form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action = "/" method = "post" id ="myform">
        <label>Rotate by :</label>
        <input type = "text" name = "rot" value = "0"/>
        <textarea rows = "4" cols = "50" name = "text">{0}</textarea>
        <button type = "submit" name = "but">Submit Query</button>
      </form>
      
      
      
    </body>
</html>"""

from caesar import rotate_string

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods = ['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    irot = int(rot)
    rotated = rotate_string(text, irot)

    return form.format(rotated)




app.run() 