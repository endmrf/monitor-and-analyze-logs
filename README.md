# Monitor and Analyze Logs

Projeto simples para realizar o monitoramento e análise de logs de um servidor **nginx**.

## 📄 Sobre

Este projeto simula o envio de arquivos de log para uma ferramenta de monitoramento (como Grafana Loki) e oferece exemplos de como consultar e visualizar esses logs.

## 🛠 Estrutura

- `nginx_simulated.log`: Arquivo de log simulado do nginx.
- `send_log_file.py`: Script para enviar logs ao Loki.
- `query_api_loki.py`: Script para consultar logs no Loki.
- `start_grafana.py`: Script para iniciar o Grafana localmente.

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/endmrf/monitor-and-analyze-logs.git
   cd monitor-and-analyze-logs

2. Simule o envio de logs:
    ```bash
    python send_log_file.py

3. Inicie o Grafana:
   ```bash
   python start_grafana.py

4. Consulte logs:
   ```bash
   python query_api_loki.py


## 📈 Tecnologias

- Python 3
- Grafana
- Loki
- Nginx (simulado)

## 🧩 Melhorias Futuras

- Autenticação para envio de logs
- Dashboard Grafana personalizado
- Coleta de métricas adicionais

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
