import socket

def scan_ports(target_ip):
    open_ports = []

    print(f"Scanning ports on {target_ip}...")
    print("Progress: ", end='')

    for port in [22, 443]:  # Only scan ports 22 and 443
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((target_ip, port))
            open_ports.append(port)
            sock.close()
        except (socket.timeout, ConnectionRefusedError):
            pass

        print("*", end='', flush=True)

    return open_ports

def main():
    print("**********************************************")
    print("*           PORT SCANNER       *")
    print("**********************************************\n")

    target_ip = input("Enter the target IP address: ")

    open_ports = scan_ports(target_ip)

    if open_ports:
        print(f"\n\nThe following ports are open on {target_ip}:")
        for port in open_ports:
            print(port)
    else:
        print(f"\n\nNo open ports found on {target_ip}.")
    print(r'''
         / \__
        (    @\___
         /         O
       /   (_____/
     /_____/   U
    '''
    )

if __name__ == "__main__":
    main()
