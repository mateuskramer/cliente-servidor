# T1 cliente-servidor

Implementação de teste de comunicação entre cliente e servidor com sockets, onde o cliente mede a latência (RTT) entre envio e resposta de mensagens do tipo "ping". Essa é uma simulação bem próxima do comando ping do sistema operacional, mas feita usando UDP e TCP em Python.

O UDP (User Datagram Protocol) É um protocolo da camada de transporte, sem conexão, o que significa que o cliente pode enviar mensagens diretamente para o endereço IP e porta do servidor, sem a necessidade de estabelecer uma conexão com funções como connect() ou accept().

Por ser um protocolo não confiável, o UDP não garante que os dados cheguem ao destino, não confirma a entrega, não mantém a ordem dos pacotes e não realiza retransmissões em caso de perda. Por outro lado, justamente por dispensar esses controles, o UDP é muito mais leve e rápido, sendo ideal para aplicações que priorizam velocidade e podem tolerar alguma perda de dados, como jogos online, transmissões de vídeo ou áudio em tempo real (streaming), chamadas por voz (VoIP) e consultas DNS.

Já o TCP (Transmission Control Protocol) é um protocolo da camada de transporte, amplamente utilizado quando se exige uma comunicação confiável entre dois computadores. Ao contrário do UDP, o TCP é um protocolo orientado à conexão, ou seja, antes de qualquer troca de dados, é necessário estabelecer uma conexão entre cliente e servidor por meio de um processo conhecido como handshake.

Uma vez estabelecida a conexão, o TCP garante que todos os dados enviados cheguem corretamente ao destino, na mesma ordem em que foram transmitidos e sem perdas. Isso é possível graças a mecanismos internos como confirmação de recebimento (ACK), controle de fluxo, controle de congestionamento e retransmissão de pacotes quando necessário. Por essas razões, o TCP é considerado um protocolo confiável, embora seja naturalmente mais lento e pesado do que o UDP, justamente por causa desses controles adicionais.

Devido à sua confiabilidade, o TCP é amplamente utilizado em aplicações onde a integridade dos dados é essencial, como na navegação na web (HTTP/HTTPS), envio de e-mails (SMTP), transferência de arquivos (FTP) e acesso remoto (SSH).

Servidor tcp

https://github.com/user-attachments/assets/85c44e3f-7097-435e-a7ff-072d941d6647

servidor udp

https://github.com/user-attachments/assets/a50e49f9-c5cb-491c-a38c-8544dd18c739

cliente tcp

https://github.com/user-attachments/assets/7ee318dc-a92b-4927-a902-da82e4fcd3d1

cliente udp

https://github.com/user-attachments/assets/6383919f-b913-44d2-8bb1-cdc1922c00c1


