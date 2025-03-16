import socket
import itertools
import string

def port_scanner(target, ports):
    print("Starting Port Scanner...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")


def brute_force_login(target, user, password_list):
    print("Starting Brute Force Attack...")
    for password in password_list:
        print(f"Trying {user}:{password}")
        # Simulate authentication (replace with actual request handling for real systems)
        if password == "password123":  # Dummy successful password
            print(f"Success! Username: {user}, Password: {password}")
            break


if __name__ == "__main__":
    target_host = "localhost"
    target_ports = [22, 80, 443, 3306]

    # Port Scanner
    port_scanner(target_host, target_ports)

    # Brute Force Attack
    username = "admin"
    password_attempts = ['1234', 'password', 'admin123', 'password123']
    brute_force_login(target_host, username, password_attempts)
