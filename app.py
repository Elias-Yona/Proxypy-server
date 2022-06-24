import os
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route("/start")
def start_proxy():
    # proxy.main(
    #     hostname=ipaddress.IPv4Address('0.0.0.0'),
    #     port=5000
    # )
    subprocess.run("proxy --hostname 0.0.0.0 --port 5000")

    return "proxy started successfully"


if "__name__" == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
