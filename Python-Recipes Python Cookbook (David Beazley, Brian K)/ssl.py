import socket, os, hmac, multiprocessing
from multiprocessing.reduction import send_handle, recv_handle

SECRKEY = b'haseeb234'

def authenticate(conn):
    nonce = os.urandom(32)
    conn.sendall(nonce)
    digest = hmac.new(SECRKEY, nonce, 'sha256').digest()
    client_digest = conn.recv(len(digest))
    return hmac.compare_digest(digest, client_digest)

def worker(pipe):
    while True:
        fd = recv_handle(pipe)
        with socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM) as s:
            s.sendall(b"Access granted to vault!...")

def gatekeeper(address, pipe, worker_pid):
    raw_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_s.bind(address)
    raw_s.listen(5)
    print(f"Gatekeeper listening on {address}")
    while True:
        client, adr = raw_s.accept()
        print(f"Connection from {adr}")
        if authenticate(client):
            print("Authentication successful")
            send_handle(pipe, client.fileno(), worker_pid)
        client.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=worker, args=(child_conn,), daemon=True)
    p.start()
    gatekeeper(('localhost', 30000), parent_conn, p.pid)