import socket

# Configurações do servidor
HOST = 'localhost'  
PORT = 12345        # Porta para escutar

# Criando o socket UDP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind((HOST, PORT))

print(f"Servidor UDP escutando em {HOST}:{PORT}...")

while True:
    mensagem, endereco = servidor_socket.recvfrom(1024)  # 1024 bytes de buffer
    print(f"Mensagem recebida de {endereco}: {mensagem.decode()}")
    
    resposta = f"Recebido: {mensagem.decode()}"
    servidor_socket.sendto(resposta.encode(), endereco)
