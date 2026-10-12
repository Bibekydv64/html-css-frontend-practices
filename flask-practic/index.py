from flask import Flask,request




app  = Flask(__name__)

@app.route('/')
def home():
    return '<h1> bibek</h1>'

@app.route('/home/<name>')
def name_data(name):
    return f'your name{name}'

@app.route('/submits', methods = ['GET','POST'])
def method():
    if request.method == 'POST':

        return 'KUX DATA AILXAU!'
    else:
        return 'KUX DATA ANI AILXAU!'

app.run(debug=True)






























