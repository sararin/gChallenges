import sys
import ipaddress
import socket
from threading import Thread

class Porter:
  def __init__(self, addressPorts):
    self.address = addressPorts[0]
    self.ports = addressPorts[1]
    self.threads = []
    self.countOpen = {}

  def runScan(self):
    for addr in self.address:
      for prt in self.ports:
        t = Thread(target=self._checkPort, args=(addr, prt,))
        self.threads.append(t)
        t.start()
    [x.join() for x in self.threads]
    self._showResults()

  def _checkPort(self, addr, prt):
    try:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        result = sock.connect_ex((addr, prt))
        if result == 0:
          self._addToOpenDict((addr, prt))
    except socket.gaierror:
      print("Hostname couldn't be resolved")
      sys.exit()
    except socket.error:
      print("Couldn't connect to server")
      sys.exit()

  def _showResults(self):
    for key, val in self.countOpen.items():
      print(key+":", ' '.join(val))

  def _addToOpenDict(self, addrprt):
    addr, prt = addrprt
    if not addr in self.countOpen:
      self.countOpen[addr] = [str(prt)]
    else:
      self.countOpen[addr].append(str(prt))


class Expander:
  def __init__(self, address, ports):
    self.address = address
    self.ports = ports

  def _expandPort(self, rangePorts):
    if "-" in rangePorts:
      temp = tuple(rangePorts.split('-'))
      return list(range(int(temp[0]), int(temp[1])))
    return [int(rangePorts)]

  def _expandAddr(self, rangeAddr):
    if '-' in rangeAddr:
      temp = [x.split('-') if "-" in x else x for x in self.address.split('.')]
      first = [ x[0] if isinstance(x, list) else x for x in temp]
      last = [ x[1] if isinstance(x, list) else x for x in temp]
      return [ str(ipaddress.IPv4Address(ipadd)) for ipadd in range(int(ipaddress.IPv4Address('.'.join(first))), int(ipaddress.IPv4Address('.'.join(last))))]
    return [rangeAddr]

  def _prepareOutput(self):
    self.ports = self._expandPort(self.ports)
    self.address = self._expandAddr(self.address)

  def giveBack(self):
    self._prepareOutput()
    return (self.address, self.ports)

if __name__ == "__main__":
  exp = Expander(sys.argv[1], sys.argv[2])
  port = Porter(exp.giveBack())
  port.runScan()

