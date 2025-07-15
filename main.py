from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        paciente = request.form['paciente']
        produto = request.form['produto']
        dose = request.form['dose']
        return f'Laudo para {paciente}, {produto}, {dose} mg/dia'
    return render_template('index.html')  # Certifique-se de que o arquivo index.html está no diretório 'templates'

@app.route('/gerar', methods=['POST'])
def gerar_laudo():
    # Aqui você pode pegar os dados do formulário
    paciente = request.form['paciente']
    produto = request.form['produto']
    dose = request.form['dose']
    # Aqui você pode fazer o processamento para gerar o laudo ou retornar os dados
    return f'Laudo gerado para {paciente}, produto: {produto}, dose: {dose} mg.'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
