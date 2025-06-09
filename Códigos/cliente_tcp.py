import socket
import time

HOST = '200.135.78.26'  
PORT = 12345

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((HOST, PORT))  # Estabelece conexão com o servidor

for i in range(10):
    mensagem = f"ping {i}"
    inicio = time.time()
    
    cliente_socket.sendall(mensagem.encode())
    resposta = cliente_socket.recv(1024)
    fim = time.time()
    
    rtt = (fim - inicio) * 1000
    print(f"[Cliente] Resposta: {resposta.decode()} | RTT: {rtt:.2f} ms")
    
    time.sleep(0.5)

cliente_socket.close()
