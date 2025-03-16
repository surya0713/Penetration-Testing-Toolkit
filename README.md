# Penetration Testing Toolkit

## Overview
This Python script is a basic penetration testing toolkit that includes two core functionalities: **Port Scanning** and **Brute Force Login Simulation**.

## Features
- **Port Scanner:** Scans a list of target ports to check whether they are open or closed.
- **Brute Force Login Tool:** Simulates a brute force attack by attempting multiple passwords for a given username.

## Prerequisites
- Python 3.x installed

## How to Use
1. Open the script and set the target host and ports:
   ```python
   target_host = "localhost"
   target_ports = [22, 80, 443, 3306]
   ```

2. For brute force, set the username and the list of passwords to try:
   ```python
   username = "admin"
   password_attempts = ['1234', 'password', 'admin123', 'password123']
   ```

3. Run the script:
   ```bash
   python penetration_toolkit.py
   ```

4. The script will scan the specified ports and attempt to brute force the password.

## Sample Output
```
Starting Port Scanner...
Port 22 is closed
Port 80 is open
Port 443 is open
Port 3306 is closed

Starting Brute Force Attack...
Trying admin:1234
Trying admin:password
Trying admin:admin123
Trying admin:password123
Success! Username: admin, Password: password123
```

## How It Works
1. **Port Scanner:** Uses `socket` to attempt connections to specified ports and identifies their status.
2. **Brute Force Attack:** Iterates through a list of passwords and stops when the correct one is found (simulated with a dummy condition).

## Limitations
- The brute force tool is a simulation and does not perform real authentication.
- Port scanning is limited by the timeout and network restrictions.

## Future Enhancements
- Support for more protocols (e.g., FTP, SSH).
- Real authentication handling for brute force testing (with proper authorization).

## Disclaimer
This tool is for educational purposes only. Use it responsibly and with proper authorization.

## License
MIT License

