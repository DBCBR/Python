import requests
x = requests.get('http://ec2-52-67-202-220.sa-east-1.compute.amazonaws.com:5005/consulta?hora=10:30&origem=Novo%20Hamburgo')
print(x.text)
