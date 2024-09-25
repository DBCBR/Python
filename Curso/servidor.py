from flask import Flask, jsonify, request
from pyngrok import ngrok

app = Flask(__name__)

# Inicia o túnel ngrok
public_url = ngrok.connect(5000)
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))

@app.route('/cotacao/')
def cotacao():
    return '5.34'

@app.route('/conversao/<float:val>')
def conversao(val):
    return str(val * 5.34)

@app.route('/cotacaocompleta', methods=['GET'])
def cotacaocompleta():
    argumentos = request.args
    valor = float(argumentos.get('valor'))
    mes = argumentos.get('mes')
    
    total = 0.0
    if mes == 'Janeiro':
        total = valor * 5.34
    elif mes == 'Fevereiro':
        total = valor * 5.22
    elif mes == 'Marco':
        total = valor * 5.19
    
    return str(total)

@app.route('/tabela/')
def tabela():
    return jsonify({
        'Janeiro': 5.34,
        'Fevereiro': 5.22,
        'Marco': 5.19
    })

if __name__ == "__main__":
    app.run()
