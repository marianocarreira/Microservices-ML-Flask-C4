import socket, time

def is_port_open(port):
    try:
        print(f"Waiting for port: {port}")
        # Try to create a socket connection
        with socket.create_connection(('127.0.0.1', port), timeout=1):
            return True
    except (socket.error, ConnectionRefusedError):
        return False

def wait_for_port(port, timeout=60):
    start_time = time.time()
    while not is_port_open(port):
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Timeout waiting for port {port} to open")
        time.sleep(15)

    print(f"Port {port} is now open!")
