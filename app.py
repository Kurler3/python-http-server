
import copy
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
    

# HTTP Request class (to parse the encoded request string)
class HTTPRequest:
    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = "1.1" # default to HTTP/1.1 if request doesn't provide a version
        # call self.parse() method to parse the request data
        self.parse(data)

    def parse(self, data):
        # Split the data into lines.
        lines = data.split(b"\r\n")

        # First is the request line
        request_line = lines[0]

        # Split the request line into words.
        words = request_line.split(b" ")

        # Method is the first word on the request line (encoded in utf-8)
        self.method = words[0].decode() # call decode to convert bytes to str

        # If more than 1 word => get the uri (second word)
        if len(words) > 1:
            # we put this in an if-block because sometimes 
            # browsers don't send uri for homepage
            self.uri = words[1].decode() # call decode to convert bytes to str

        # If more than 2 words => get the version
        if len(words) > 2:
            self.http_version = words[2]
            
    def __str__(self) -> str:
        return f"HTTPRequest(method={self.method}, uri={self.uri}, version={self.http_version})"
# HTTP Server
class HTTPServer(TCPServer):
    
    headers = {
        'Server': 'CrudeServer',
        'Content-Type': 'text/html',
    }

    status_codes = {
        200: 'OK',
        404: 'Not Found',
        403: 'Forbidden',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
    }
    
    def handle_request(self, data):
        
        # Get the proper request data from the request string.
        http_request = HTTPRequest(data)

        print(http_request.__str__())
        
        # Get the proper handler function for the method
        handler = getattr(self, "handler_%s" % http_request.method, None)

        if handler is None:
            return self.response_line(status_code=501)    
        response = handler(http_request)    
        return response
        


    ##########################################
    ## HANDLERS ##############################
    ##########################################
    
    # GET handler
    def handler_GET(self, request):
         # Response line
        response_line = self.response_line(status_code=200)
        
        # Line break
        blank_line = b"\r\n"
        
        # Headers
        headers = self.response_headers()
        
        
        html = """<html>
            <head>
                <title>Crude Server</title> 
            </head>
            <body>
            <h1>%s HELLO!</h1>
            <body>
            </html>
        """ % (request.method)
        
        # Body
        response_body = html.encode('utf-8')
        
        # Join and encode to bytes
        return b"".join([response_line, headers, blank_line, response_body])    
    
    ##########################################
    ## UTILITIES #############################
    ##########################################
    
    # Response line (contains thr protocol and the statu code)
    def response_line(self, status_code):
        return f"HTTP/1.1 {status_code} {self.status_codes[status_code]}\r\n".encode('utf-8') # Encode to utf-8 (bytes)

    # Get headers
    def response_headers(self, extra_headers=None):
        headers_copy = copy.deepcopy(self.headers) # Deep copy of default headers.
        
        # If passed extra headers
        if extra_headers:
            headers_copy.update(extra_headers) # Update with extra headers (could override existing default ones)
        headers = ""
        
        # For each key in the new headers
        for h in headers_copy:
            # Append the key: value + line break
            headers += "%s: %s\r\n" % (h, headers_copy[h])

        return headers.encode() # call encode to convert str to bytes
    
# If this script is run as a program.
if __name__ == "__main__":
    server = HTTPServer()
    server.start()