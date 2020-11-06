import io
import socket
from data_structure import Payload, print_payload

class RecvUdp():
  def __init__(self, src_host, src_port):
    self.src_host = src_host
    self.src_port = src_port
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.bind((self.src_host, self.src_port))

  def recv(self):
    data, addr = self.sock.recvfrom(1024)
    payload = Payload()
    buffer = io.BytesIO(data)
    buffer.readinto(payload)
    print_payload(payload)

if __name__ == "__main__":
  udp = RecvUdp('192.168.0.9', 60000)

  while True:
    try:
      udp.recv()
    except KeyboardInterrupt:
      print('')
      udp.sock.close()
      break
