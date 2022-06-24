import ipaddress
import proxy
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    proxy.main(
        hostname=ipaddress.IPv4Address('0.0.0.0'),
        port=port
    )