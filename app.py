
import http.server
import socket

# Base TCP Server
class TCPServer:
    
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
    
    # Start server
    def start(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(5)
        
        print("Listening at", s.getsockname())

        # Accept connections from outside
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            data = conn.recv(1024)
            response = self.handle_request(data)
            conn.sendall(response)
            conn.close()

    # Handle request
    def handle_request(self, data):
        request = data.decode('utf-8')
        print(request)
        return b'HTTP/1.1 200 OK\r\n\r\nHello World' # Sends bytes not strings
    
# HTTP Server
class HTTPServer(TCPServer):
    def handle_request(self, data):
        response_line = b"HTTP/1.1 200 OK\r\n"
        blank_line = b"\r\n"
        headers = b"".join([
            b"Server: Crude Server\r\n", 
            b"Content-Type: text/html\r\n"
        ])
        response_body = b"""<html>
            <head>
                <title>Crude Server</title> 
            </head>
            <body>
            <h1>Request received!</h1>
            <body>
            </html>
        """
        return b"".join([response_line, headers, blank_line, response_body])
    
# If this script is run as a program.
if __name__ == "__main__":
    server = HTTPServer()
    server.start()