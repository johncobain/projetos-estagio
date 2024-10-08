import requests

token = 'bp_pat_gofJ1speJEnIM19wqtVe03gfRSKVNGSUAwjY'
url = 'https://cdn.botpress.cloud/webchat/v2/shareable.html?botId=6dad216d-5a2d-422e-b5a7-44163535160e'
headers = {
'Authorization': f'Bearer {token}',
'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
# Imprima a resposta da API
    print('Resposta da API:', response.json())
else:
    print('Erro ao acessar a API:', response.status_code, response.text)