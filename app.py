import ipaddress
import proxy

if __name__ == '__main__':
  proxy.main(
    hostname=ipaddress.IPv4Address('0.0.0.0'),
    port=32792
  )