import sys
import ipaddress
import socket

class Porter:
  def __init__(self, addressPorts):
    self.address = addressPorts[0]
    self.ports = addressPorts[1]
    print(self.ports)

  def runScan(self):
    for addr in self.address:
      for prt in self.ports:
        self._checkPort(addr, prt)

  def _checkPort(self, addr, prt):
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        result = sock.connect_ex((addr, prt))
        if result == 0:
          print(prt, "open")
        else:
          print(prt, "closed")
    except socket.gaierror:
      print("Hostname couldn't be resolved")
      sys.exit()
    except socket.error:
      print("Couldn't connect to server")
      sys.exit()

class Expander:
  def __init__(self, address, ports):
    self.address = address
    self.ports = ports

  def _expand(self, thingToExpand):
    if "-" in thingToExpand:
      temp = tuple(thingToExpand.split('-'))
      return list(range(int(temp[0]), int(temp[1])))
    return (int(thingToExpand), int(thingToExpand)+1)

  def _prepareOutput(self):
    self.ports = self._expand(self.ports)
    self.address = [self.address]
    #temp = [x.split('-') if "-" in x else x for x in self.address.split('.')]
    #first = [ x[0] if isinstance(x, list) else x for x in temp]
    #last = [ x[1] if isinstance(x, list) else x for x in temp]
    #self.address = (ipaddress.IPv4Address('.'.join(first)), ipaddress.IPv4Address('.'.join(last)))


  def giveBack(self):
    self._prepareOutput()
    return (self.address, self.ports)

if __name__ == "__main__":
  exp = Expander(sys.argv[1], sys.argv[2])
  port = Porter(exp.giveBack())
  port.runScan()

