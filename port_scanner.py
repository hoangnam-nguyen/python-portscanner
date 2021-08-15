import socket
import common_ports
import ipaddress

def get_open_ports(target, port_range, verbose = False):
  open_ports = []
  if target.replace('.', '').isnumeric():
    try:
      host = ipaddress.ip_address(target)
    except ValueError:
      return "Error: Invalid IP address"
  else:
    try:
      host = socket.gethostbyname(target)
    except:
      return "Error: Invalid hostname"

  for port in range(port_range[0], port_range[-1] + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((str(host), port))
    s.close()
    if result == 0:
      open_ports.append(port)

  if verbose == False:    
    return open_ports
  else:
    if target.replace('.', '').isnumeric():
      try:
        host_name = socket.gethostbyaddr(target)[0]
        res = "Open ports for " + host_name + " (" + target + ")\nPORT     SERVICE\n"
      except:
        res = "Open ports for " + target + "\nPORT     SERVICE\n"
    else:
      res = "Open ports for " + target + " (" + host + ")\nPORT     SERVICE\n"
    for port in open_ports:
      res += (str(port).ljust(9) + common_ports.ports_and_services.get(port, ""))
      if port != open_ports[-1]:
        res += '\n'
    return res