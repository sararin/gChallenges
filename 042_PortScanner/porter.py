import sys
import socket

class Porter:
  def __init__(self, addressPorts):
    self.address = addressPorts[0]
    self.ports = addressPorts[1]

  def runScan(self):
    for addr in self.address:
      for prt in self.ports:
        self._checkPort(addr, prt)

  def _checkPort(self, addr, prt):
    try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(3)
      result = sock.connect_ex((addr, prt))
      if result == 0:
        print(prt, "open")
      else:
        print(prt, "closed")
      sock.close()
    except socket.gaierror:
      print("Hostname couldn't be resolved")
      sys.exit()
    except socket.error:
      print("Couldn't connect to server")
      sys.exit()

class Expander:
  def __init__(self, address, ports):
    self.address = [address]
    self.ports = [int(ports)]

  def giveBack(self):
    return (self.address, self.ports)

if __name__ == "__main__":
  exp = Expander(sys.argv[1], sys.argv[2])
  port = Porter(exp.giveBack())
  port.runScan()

