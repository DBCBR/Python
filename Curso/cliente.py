import requests
x = requests.get("http://ec2-54-207-131-39.sa-east-1.compute.amazonaws.com:5003/cotacaocompleta?valor=10&mes=Janeiro")
print(x.text)

