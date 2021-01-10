from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def vlun_form():
    if request.method == "GET":
        return render_template('form.html')
    elif request.method == "POST":
        cmd = request.form.get("cmd")
        print(cmd)
        # res = subprocess.run(cmd, stdout=subprocess.PIPE)
        res = os.system(cmd)
        return render_template('form.html', res=res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
