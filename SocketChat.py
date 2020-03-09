import socket
import threading
import time
import os

def server(host):
    HOST = ''               # Endereco IP do Servidor
    PORT = 64000            # Porta que o Servidor esta
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    orig = (HOST, PORT)
    udp.bind(orig)
    msg = ''
    print('Aguardando conexão em %s.' %host)
    nome = ''
    print('Conexão iniciada.')
    while nome == '':
        nome =  udp.recvfrom(1024)[0]
        nome = nome.decode()
        nome = {host:nome}
    while not msg == 'exit()':
        msg = udp.recvfrom(1024)[0]
        msg = msg.decode()
        os.system('tput dl1')
        print('[%s]: %s\n[Você]: ' %(nome[host], msg), end='')
    os.system('tput dl1')
    print('Conexão encerrada.')
    udp.close()

def client(HOST):
    #HOST = '10.0.1.124'  # Endereco IP do Servidor
    PORT = 64000            # Porta que o Servidor esta
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    msg = ''
    nome = ''
    while not nome:
        print('Digite seu user: ', end='')
        nome = input()
        udp.sendto (nome.encode(), dest)
    while not msg == 'exit()':
        print('[Você]: ', end="")
        msg = input()
        udp.sendto (msg.encode(), dest)
    udp.close()

print('Digite o ip a conectar: ', end='')
host = input()
    
threading.Thread(target=server, args= [host]).start()
time.sleep(.5)
threading.Thread(target=client, args= [host]).start()