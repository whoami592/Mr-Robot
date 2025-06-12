# Mr. Robot Toolkit by Mr. Sabaz Ali Khan
# Ethical Hacking Toolkit for Educational Purposes Only
# Inspired by the TV series Mr. Robot
# Use only with explicit permission and in legal, ethical contexts

import socket
import threading
import os
import hashlib
import time
from datetime import datetime
import getpass
import base64
import secrets

def banner():
    print("""
    ╔════════════════════════════════════════════╗
    ║     Mr. Robot Toolkit Coded by Pakistani   ║
    ║       ETHICAL Hacker MR Sabaz Ali Khan     ║
    ║               Educational USe              ║
    ╚════════════════════════════════════════════╝
    """)

# 1. Network Scanner (Inspired by Nmap)
def network_scanner():
    target = input("Enter target IP address (e.g., 192.168.1.1): ")
    port_range = input("Enter port range (e.g., 1-100): ")
    try:
        start_port, end_port = map(int, port_range.split('-'))
        print(f"Scanning {target} from ports {start_port} to {end_port}...")
        open_ports = []
        
        def scan_port(port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        
        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        if open_ports:
            print(f"Open ports: {', '.join(map(str, open_ports))}")
        else:
            print("No open ports found.")
    except ValueError:
        print("Invalid port range. Use format: start-end (e.g., 1-100)")
    except Exception as e:
        print(f"Error during scan: {e}")

# 2. Password Cracker (Dictionary Attack, Inspired by John the Ripper)
def password_cracker():
    print("Password Cracker - Dictionary Attack Simulation")
    target_hash = getpass.getpass("Enter target hash (MD5): ").strip()
    wordlist_path = input("Enter path to wordlist file (e.g., wordlist.txt): ")
    
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            wordlist = [line.strip() for line in file]
    except FileNotFoundError:
        print("Wordlist file not found.")
        return
    
    print("Cracking password... (This is a simulation)")
    for word in wordlist:
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        if hashed_word == target_hash:
            print(f"Password found: {word}")
            return
        time.sleep(0.01)  # Simulate processing time
    print("Password not found in wordlist.")

# 3. Phishing Page Generator (Inspired by Social-Engineer Toolkit)
def phishing_generator():
    print("Phishing Page Generator - Educational Simulation")
    site_name = input("Enter fake website name (e.g., FakeBank): ")
    output_file = f"{site_name}_login.html"
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{site_name} Login</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
            .login-box {{ width: 300px; margin: auto; padding: 20px; border: 1px solid #ccc; }}
            input {{ width: 100%; padding: 10px; margin: 10px 0; }}
            button {{ padding: 10px 20px; background: #007BFF; color: white; border: none; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>{site_name} Login</h2>
            <form action="javascript:alert('Credentials captured! This is a demo.');">
                <input type="text" placeholder="Username" required><br>
                <input type="password" placeholder="Password" required><br>
                <button type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    """
    
    with open(output_file, 'w') as file:
        file.write(html_content)
    print(f"Phishing page generated: {output_file}")
    print("WARNING: Use this for educational purposes only. Do not deploy without permission.")

# 4. Secure File Wiping (Inspired by HDShredder)
def secure_file_wiper():
    file_path = input("Enter file path to securely wipe: ")
    passes = 3  # Number of overwrite passes
    
    try:
        if not os.path.exists(file_path):
            print("File not found.")
            return
        
        file_size = os.path.getsize(file_path)
        with open(file_path, 'wb') as file:
            for _ in range(passes):
                file.write(secrets.token_bytes(file_size))
                file.flush()
                os.fsync(file.fileno())
        
        os.remove(file_path)
        print(f"File {file_path} securely wiped with {passes} passes.")
    except Exception as e:
        print(f"Error wiping file: {e}")

# 5. File Encryption/Decryption (Inspired by LUKS-like encryption)
def file_encryption():
    print("File Encryption/Decryption Tool")
    action = input("Choose action (encrypt/decrypt): ").lower()
    file_path = input("Enter file path: ")
    key = getpass.getpass("Enter encryption key (must be secure): ")
    
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        
        key_bytes = key.encode()
        if action == "encrypt":
            encrypted = base64.b64encode(data + key_bytes)  # Simple XOR-like with key
            output_path = file_path + ".enc"
            with open(output_path, 'wb') as file:
                file.write(encrypted)
            print(f"File encrypted: {output_path}")
        elif action == "decrypt":
            if not file_path.endswith(".enc"):
                print("File must have .enc extension for decryption.")
                return
            decrypted = base64.b64decode(data)[:-len(key_bytes)]
            output_path = file_path.replace(".enc", ".dec")
            with open(output_path, 'wb') as file:
                file.write(decrypted)
            print(f"File decrypted: {output_path}")
        else:
            print("Invalid action. Choose 'encrypt' or 'decrypt'.")
    except Exception as e:
        print(f"Error during {action}: {e}")

# Main Menu
def main():
    banner()
    while True:
        print("\nMr. Robot Toolkit Menu:")
        print("1. Network Scanner")
        print("2. Password Cracker")
        print("3. Phishing Page Generator")
        print("4. Secure File Wiper")
        print("5. File Encryption/Decryption")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")
        
        if choice == "1":
            network_scanner()
        elif choice == "2":
            password_cracker()
        elif choice == "3":
            phishing_generator()
        elif choice == "4":
            secure_file_wiper()
        elif choice == "5":
            file_encryption()
        elif choice == "6":
            print("Exiting toolkit. Stay ethical!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()