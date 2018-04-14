# Python 3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pprint import pprint

import time
import json

hostName = "localhost"
hostPort = 9000

OK = 200

class MyServer(BaseHTTPRequestHandler):
    
    def do_POST(self):

        if self.path.startswith('/webhooks/inbound-sms') :

            self.send_response(OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            data = self.rfile.read()
            pprint (data)
            
    def do_GET(self):

        self.send_response(OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

            
# Run server        
myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
        
try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass
    
myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

