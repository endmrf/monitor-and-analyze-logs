import time
import requests
from urllib.parse import quote

# Codificando a consulta LogQL
query = '{app="simulador"}'
encoded_query = quote(query)

# Definindo intervalo de tempo para buscar os logs recém enviados
end = int(time.time() * 1e9)
start = end - int(5 * 60 * 1e9)  # últimos 5 minutos

url = f"http://localhost:3100/loki/api/v1/query_range?query={encoded_query}&limit=10&start={start}&end={end}"

res = requests.get(url)
print("🔍 Status:", res.status_code)
print("📄 Conteúdo:", res.text)

if res.status_code == 200:
    data = res.json()
    logs = data["data"]["result"]
    for stream in logs:
        print("Rótulos:", stream["stream"])
        for ts, linha in stream["values"]:
            print(f"🕒 {ts} | {linha}")