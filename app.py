import os
import ipaddress
import threading

from flask import Flask
import proxy

app = Flask(__name__)

def start_proxy_server():
     proxy.main(
        hostname=ipaddress.IPv4Address('0.0.0.0'),
        port=5000
    )

# @app.route("/start")
# def start_proxy():
#     # subprocess.run("proxy --hostname 0.0.0.0 --port 5000")
#     # x = threading.Thread(target=start_proxy_server)
#     # x.start()
#     proxy.main(
#         hostname=ipaddress.IPv4Address('0.0.0.0'),
#         port=5000
#     )
#     return "proxy started successfully"


# if __name__ == "__main__":
# #     port = int(os.environ.get('PORT', 5000))
# #     app.run(host='0.0.0.0', port=port)
#     start_proxy_server()
 
