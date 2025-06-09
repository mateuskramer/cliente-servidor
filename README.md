# T1 cliente-servidor

💻 Neste trabalho, estamos desenvolvendo uma aplicação em Python para testar a comunicação entre um cliente e um servidor, utilizando a tecnologia de sockets com os protocolos UDP e TCP.

O cliente envia mensagens chamadas "ping" para o servidor, que responde. A cada envio, o cliente mede o tempo que a resposta demora para voltar, conhecido como latência ou RTT.

❗Obs:
Ping: é uma mensagem simples enviada de um computador para outro com o objetivo de testar se há resposta e medir o tempo de ida e volta da mensagem. É como perguntar "Você está aí?" e esperar pela resposta.

Latência (RTT): significa Round Trip Time (tempo de ida e volta). É o intervalo entre o momento em que o cliente envia o "ping" e o momento em que ele recebe o "pong" do servidor. Mede a velocidade da resposta da comunicação.

📈 Processo resumido:

Servidor inicia e fica esperando mensagens.

Cliente envia um "ping 1", "ping 2", ..., até 10 pings.

O servidor responde com "ping: ping 1", e assim por diante.

O cliente mede o tempo entre envio e recebimento da resposta.

Ao final, temos uma noção da latência da rede ou da eficiência da comunicação.

📊Protocolos:

TCP (Transmission Control Protocol)
É um protocolo da camada de transporte, orientado à conexão e confiável. Garante que os dados cheguem sem erros, na ordem correta e sem perdas, usando confirmações e retransmissões. É mais lento e pesado, mas ideal para aplicações como web (HTTP), e-mail, FTP e SSH.

UDP (User Datagram Protocol)
Também da camada de transporte, o UDP é sem conexão e não confiável — não garante entrega nem ordem dos dados. Por ser mais leve e rápido, é usado em jogos online, vídeo ao vivo, VoIP e DNS, onde a velocidade é mais importante que a confiabilidade.

👁️‍🗨️Exemplo Visual:

Servidor tcp

https://github.com/user-attachments/assets/85c44e3f-7097-435e-a7ff-072d941d6647

servidor udp

https://github.com/user-attachments/assets/a50e49f9-c5cb-491c-a38c-8544dd18c739

cliente tcp

https://github.com/user-attachments/assets/888435d7-086b-4574-bc51-16a2e09cc5ec

cliente udp

https://github.com/user-attachments/assets/79395cd1-9287-4c12-9c8d-2b162b45ea87



