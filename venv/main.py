import requests

API_KEY = "d79de0249cd455e8aac686f898f03317"

cidade = "campo grande"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}"

requisicao = requests.get(link)
requisicao_dict = requisicao.json()
descricao = requisicao_dict['weather'][0]['description']
temperatura = requisicao_dict['main']['temp'] - 273.15
print(descricao, f"{temperatura:.2f}°C")
