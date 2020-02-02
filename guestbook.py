from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello There!</h1>'

@app.route('/home', methods=['GET','POST'])
def home():
    links = ['https:www.youtube.com', 'https://bing.com', 'https://python.org', 'https://www.chevrolet.com']
    return render_template('example.html', links=links)

if __name__ == '__main__':
    app.run(debug=True)
