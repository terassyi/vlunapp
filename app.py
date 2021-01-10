from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def vlun_form():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        cmd = request.form.get("cmd").split(' ')
        res = subprocess.run(cmd, stdout=subprocess.PIPE)
        return render_template('form.html', res=res.stdout)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
