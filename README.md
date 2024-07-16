# Python HTTP Server

Python implementation of a basic HTTP server

![image](https://github.com/user-attachments/assets/5cd7d156-a52e-41aa-ad8a-0c9bfb5cc5cf)


## Overview

This project is a simple HTTP server implemented entirely from scratch using Python. The server is capable of handling basic HTTP requests and serving static files. It provides a foundation for understanding the inner workings of an HTTP server and can be used as a learning resource or a starting point for more advanced server development.

## Things learned

### Socket Programming

Implementing an HTTP server from scratch involved a deep dive into socket programming. Sockets are the fundamental building blocks for network communication. Understanding how to create and manage sockets allowed me to establish connections with clients and handle incoming requests.

### HTTP Protocol

Request-Response Cycle
I gained a comprehensive understanding of the HTTP protocol and its request-response cycle. The server listens for incoming requests, parses them, processes the requested resource, and sends an appropriate response back to the client. This hands-on experience clarified the intricacies of HTTP communication.

### Status Codes and Headers

Working with status codes and headers was crucial for crafting valid HTTP responses. I learned how to set response headers to convey information about the server and the delivered content. Implementing common status codes enabled me to communicate the success or failure of a request effectively.

### Handling HTTP Methods

I explored the various HTTP methods, such as GET and HEAD, and implemented logic to handle different types of requests. This allowed the server to respond appropriately based on the method used by the client.

### Serving Static Files

Enabling the server to serve static files involved understanding file I/O operations and efficiently streaming content to clients. This feature is essential for delivering HTML, CSS, and JavaScript files, providing a foundation for more complex web applications.

### HTTP/1.1 Features

Implementing basic features of the HTTP/1.1 protocol, including persistent connections and chunked transfer encoding, showcased the evolution of the HTTP standard. This experience highlighted the importance of adapting the server to support modern web practices.

### Error Handling

Implementing robust error handling mechanisms was a critical aspect of the project. I learned how to gracefully handle various error scenarios, such as 404 Not Found or 500 Internal Server Error, to provide meaningful feedback to clients.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Kurler3/python-http-server
    ```

2. **Navigate to the project directory:**

    ```bash
    cd python-http-server
    ```

## Usage

Run the development server:

```bash
py app.py
```

Open your browser and navigate to http://127.0.0.1:8888 to explore the server!
