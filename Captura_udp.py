import socket

# Configurações
UDP_IP = "0.0.0.0"  # Escuta em todas as interfaces de rede
UDP_PORT = 3000     # Porta UDP
FILE_NAME = "placar.txt"  # Nome do arquivo onde os dados serão salvos

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Escutando na porta {UDP_PORT}...")

try:
    while True:
        try:
            # Recebe os dados
            data, addr = sock.recvfrom(2048)  # Buffer maior para garantir que recebe o XML completo
            print(f"Recebido {len(data)} bytes de {addr}")

            # Decodifica os dados como texto (assumindo UTF-8)
            message = data.decode('utf-8')

            # Salva os dados no arquivo
            with open(FILE_NAME, 'a') as file:
                file.write(message + '\n')

            print(f"Dados salvos no arquivo {FILE_NAME}")

        except Exception as e:
            print(f"Ocorreu um erro ao processar os dados: {e}")

except KeyboardInterrupt:
    print("Interrupção pelo usuário. Encerrando...")
finally:
    sock.close()
    print("Socket fechado.")
