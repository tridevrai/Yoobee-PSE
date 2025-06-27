from flask import Flask
# create a flask app
app = Flask(__name__)

# define a route for the root URL
@app.route('/')
def hello_flask():
    return "<p>Hello, Flask!</p>"

@app.route('/bye')
def bye_flask():
    return "<p>Bye, Flask!</p>"

@app.route('/username/<name>')
def username(name):
    return f"<p>{name} is learning Flask!</p>"

# run the app
if __name__ == '__main__':
    app.run(debug=True)