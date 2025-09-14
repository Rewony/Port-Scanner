import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is OPEN")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            s.close()

if __name__ == "__main__":
    target = input("Enter target host (IP or domain): ")
    scan_ports(target, 20, 1024)
