import socket
import threading
import logging

#configure logging
logging.basicConfig(filename='firewall.log', level=logging.INFO, format='%(asctime)s - %(message)s')

IP = "0.0.0.0"
PORT = 9999


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()

def handle_client(client_socket):
      with client_socket as sock:
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode("utf-8")}')
            logging.info(f"Received: {request.decode('utf-8')} from {sock.getpeername()}")
            sock.send(b'ACK')

if __name__ == '__main__':
      main()