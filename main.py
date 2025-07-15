from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')  # Formulário inicial

@app.route('/gerar', methods=['POST'])
def gerar_laudo():
    # Coleta de dados do formulário
    paciente = request.form['paciente']
    produto = request.form['produto']
    dose = request.form['dose']

    # Renderiza o laudo em nova página
    return render_template('laudo.html', paciente=paciente, produto=produto, dose=dose)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
