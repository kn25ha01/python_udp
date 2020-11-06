import socket
from data_structure import Payload

class SendUdp():
  def __init__(self, dst_host, dst_port):
    self.dst_host = dst_host
    self.dst_port = dst_port
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def send(self, payload):
    self.sock.sendto(payload, (self.dst_host, self.dst_port))

if __name__ == "__main__":
  import time
  udp = SendUdp('192.168.0.9', 60000)
  payload = Payload()

  cnt = 0
  while True:
    try:
      payload.seq_no = cnt
      unixtime = time.time()
      payload.unixtime = unixtime
      print(unixtime)
      udp.send(payload)
      cnt += 1
      time.sleep(1)
    except KeyboardInterrupt:
      print('')
      udp.sock.close()
      break
