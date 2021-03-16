from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mike')
def mike():
    return render_template('mike.html')

@app.route('/loan', methods=['GET'])
def loan():
    return render_template('loan.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        num1 = int(request.form['numOne'])
        num2 = int(request.form['numTwo'])
        mySum = num1 + num2
        print(mySum)
    return render_template('loan.html', myValue = mySum)

if __name__ == '__main__':
    app.run(debug=True)



 