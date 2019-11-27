from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

num = 0


@app.route('/')
def home():
    return render_template('index.html', num=num)


@app.route('/increase/<int:n>')
def increase(n):
    global num
    num += n
    return str(num)


@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
