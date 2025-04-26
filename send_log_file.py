import time
import json
import requests

LOG_FILE = "nginx_simulated.log"
API_ENDPOINT = "http://localhost:3100/loki/api/v1/push"

headers = {
    "Content-Type": "application/json"
}

with open(LOG_FILE, "r") as f:
    f.seek(0)
    for _ in range(100):
        linha = f.readline()
        if not linha:
            time.sleep(1)
            continue
        ts = str(int(time.time() * 1e9))
        payload = {
            "streams": [
                {
                    "stream": {"app": "simulador"},
                    "values": [[ts, linha.strip()]]
                }
            ]
        }
        r = requests.post(API_ENDPOINT, data=json.dumps(payload), headers=headers)
        print(f"[{r.status_code}] enviado: {linha.strip()}")


        # print("✅ Envio:", r.status_code)
        # print("📝 Resposta:", r.text)