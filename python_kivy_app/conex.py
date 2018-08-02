import socket
class Conexao:
    def __init__(self, ip, porta):
        self.ip = ip
        self.porta =porta

        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest=((self.ip,self.porta))
        self.tcp.connect(dest)

    def enviar(self,msg):
        self.tcp.sendall(msg)

    def receber(self):
        msg=self.tcp.recv(1024)
        return msg

    def fechar(self):
        self.tcp.close()
