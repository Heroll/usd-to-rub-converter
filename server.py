from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import currency
HOST_ADDRESS = "localhost"
HOST_PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    
    def send_response(self, code, message=None):
        self.log_request(code)
        self.send_response_only(code)
        self.send_header('Server','python3 http.server Development Server')     
        self.send_header('Date', self.date_time_string())
        self.end_headers()  
    
    def do_GET(self):
        """ response for a GET request """
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<head><style>p, button {font-size: 1em}</style></head>')
        self.wfile.write(b'<body>')
        self.wfile.write(b'<form method="POST">')
        self.wfile.write(b'<span>Enter something:</span>\
                            <input name="amount"> \
                            <input name="currency"> \
                            <button style="color:blue">Submit</button>')
        self.wfile.write(b'</form>')    
        self.wfile.write(b'</body>')
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        (input1, input2) = self.rfile.read(content_length).decode('utf-8').split('&')
        (a, amount) = input1.split('=')
        (b, cur) = input2.split('=')
        value = urllib.parse.unquote_plus(value)
        self.send_response(200)
        self.wfile.write(b'<head><style>p, button {font-size: 1em}</style></head>')
        self.wfile.write(b'<body>')
        self.wfile.write(b'<p>' + bytes(currency.convert(int(amount), cur),'utf-8') + b'</p>')
        self.wfile.write(b'</body>')    

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run(handler_class=RequestHandler)