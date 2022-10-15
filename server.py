from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', num = 4, num2 = 4, color1 = 'red', color2 = 'black')

@app.route('/4')
def checkerboardFour():
    return render_template('index.html', num = 4, num2 = 2, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>')
def checkerboardCustom(x,y):
    return render_template('index.html', num = int(x/2), num2 = int(y/2), color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboardTotalCustom(x,y,color1,color2):
    return render_template('index.html', num = int(x/2), num2 = int(y/2), color1 = color1, color2 = color2)


if __name__ == '__main__':
    app.run(debug=True)
