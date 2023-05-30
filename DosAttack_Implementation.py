import socket
import random
import string
import time

source_IP = input("Enter IP address of Source: ")
target_IP = input("Enter IP address of Target: ")
target_port = int(input("Enter target port: "))
packet_count = int(input("Enter the number of packets to send: "))
delay = float(input("Enter the delay between packets (in seconds): "))

success_count = 0
failure_count = 0


def generate_random_string(length):
    #string.ascii_letters is a string containing all the ASCII letters (both uppercase and lowercase).
    letters = string.ascii_letters
    #random.choice() function to randomly select a character from the letters string length number of times.
 
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_ip():
    ip_segments = []
    #This line starts a loop that iterates four times to generate the four segments of the IP address."xxx.xxx.xxx.xxx" 
    for _ in range(4):
        segment = str(random.randint(0, 255))
        ip_segments.append(segment)
    return '.'.join(ip_segments)

for i in range(1, packet_count + 1):
    try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) - This line creates a TCP socket using socket.AF_INET (IPv4)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #If a connection or communication takes longer than 1 second, a socket.timeout exception will be raised.
        s.settimeout(1)
        s.connect((target_IP, target_port))
        
        random_data = generate_random_string(1024)  # Generate a random payload of length 1024 bytes
        source_IP = generate_random_ip()  # Generate a random source IP for each packet
        
        headers = f"GET / HTTP/1.1\r\nHost: {target_IP}\r\n\r\n" #This line creates an HTTP GET request header with the target IP address in the Host field.
        packet = f"{headers}{random_data}".encode()
        
        s.send(packet) 
        s.close()
        
        success_count += 1
        print(f"Packet {i} sent successfully")
        
        time.sleep(delay)# delay 'time' variable between sending each packet.

        
    except socket.error as e:
        failure_count += 1
        print(f"Packet {i} failed to send. Error: {e}")

print("Packet sending complete!")
print(f"Total packets sent: {success_count}")
print(f"Total packets failed: {failure_count}")

