import socket

HOST = '0.0.0.0'
PORT = 12345

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((HOST, PORT))
servidor_socket.listen()

print(f"[Servidor] Aguardando conexão em {HOST}:{PORT}...")
conexao, endereco = servidor_socket.accept()

print(f"[Servidor] Conexão aceita de {endereco}")

while True:
    dados = conexao.recv(1024)
    if not dados:
        break
    print(f"[Servidor] Recebido: {dados.decode()}")
    conexao.sendall(dados)  # Ecoa a mensagem

conexao.close()
servidor_socket.close()
