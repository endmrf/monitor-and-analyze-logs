import subprocess

grafana = subprocess.Popen(["/usr/sbin/grafana-server", "--homepath=/usr/share/grafana"])
print("✅ Grafana iniciado em background na porta 3000")