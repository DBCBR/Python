import requests
x = requests.get('http://127.0.0.1:5000/cotacaocompleta?valor=100&mes=Janeiro')
print(x.text)

