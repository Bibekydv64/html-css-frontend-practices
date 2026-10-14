from flask import Flask,render_template



app = Flask(__name__)


@app.route('/')
def home():
    name = 'bibek'
    marks = 35
    return render_template('index.html', name=name ,marks=marks)




app.run(debug=True)
