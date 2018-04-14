# Python 3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pprint import pprint

import time
import json

hostName = "www.fuddyduddies.org"
hostPort = 9000

NCCO = '''
[
    {
        "action": "talk",
        "voiceName": "Russell",
        "text": "Hi, this is Russell speaking. This message is from Tony's Nexmo web app."
    }
]
'''

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):

        if self.path=='/':        

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            self.wfile.write(bytes("<html><head><title>Tony's basic web app.</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>Please dial this number <b>+44-(0)7418340549</b> and listen to the message!</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

        elif self.path.startswith('/answer_url') :

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            self.wfile.write(bytes(NCCO, "utf-8"))

            result = urlparse(self.path)
            params = parse_qs(result.query)

            phone_to = params['to'][0]
            phone_from = params['from'][0]

            print ("to: %s from: %s" % (phone_to, phone_from))
        

    def do_POST(self):

        if self.path.startswith('/event_url'):
        
            len = int(self.headers['Content-Length'])
            content = self.rfile.read(len)
            msg = json.loads(content.decode('utf-8'))
            # DEBUGGING print (msg)
            print ("Message status: %s" % msg['status'])
            
            
        # Acknowledge the POST     
        self.send_response(200)
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

