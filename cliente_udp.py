import socket
import time

HOST = 'localhost'  # <- Substitua pelo IP da máquina do servidor 200.135.79.79
PORT = 12345

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_socket.settimeout(1.0)  # Tempo máximo de espera por resposta (1 segundo)

for i in range(10):  # Envia 5 pings
    mensagem = f"ping {i}"
    inicio = time.time()
    
    try:
        cliente_socket.sendto(mensagem.encode(), (HOST, PORT))
        resposta, _ = cliente_socket.recvfrom(1024)
        fim = time.time()
        rtt = (fim - inicio) * 1000  # RTT em milissegundos

        print(f"[Cliente] Resposta: {resposta.decode()} | RTT: {rtt:.2f} ms")
    
    except socket.timeout:
        print("[Cliente] Tempo esgotado (sem resposta)")
    
    time.sleep(1)  # Aguarda 1 segundo entre os pings

cliente_socket.close()
