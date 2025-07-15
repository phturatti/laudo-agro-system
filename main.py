from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        paciente = request.form['paciente']
        produto = request.form['produto']
        dose = request.form['dose']
        return f"Laudo para {paciente}: {produto}, {dose} mg/dia"
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
