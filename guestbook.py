from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello There!</h1>'

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('example.html')

if __name__ == '__main__':
    app.run(debug=True)