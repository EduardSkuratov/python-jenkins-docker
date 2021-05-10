from flask import Flask, request
import hashlib
import html

app = Flask(__name__)
salt = "UNIQUE_SALT"
default_name = 'Eduard'

@app.route('/', methods=['GET', 'POST'])
def mainpage():

    name = default_name
    if request.method == 'POST':
        name = html.escape( request.form['name'], quote=True )
    salted_name = salt + name
    name_hash = hashlib.sha256( salted_name.encode() ) .hexdigest()

    header = '<html><head><title>Web</title></head><body>'
    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{0}">
              <input type="submit" value="submit">
              </form>
              '''.format( name, name_hash )
    footer = '</body></html>'

    return header + body + footer


if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0' )
