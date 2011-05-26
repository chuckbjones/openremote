#!/usr/bin/env python
import sys
import re
import subprocess
import urlparse
import platform
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class OpenRemoteHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = ''
        try:
            request_url = urlparse.urlsplit(self.path)
            if re.search('openurl', request_url.path):
                query = urlparse.parse_qs(request_url.query)            
                url = query["url"][0]
                subprocess.check_call(["xdg-open", url])
    
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("Opened %s on %s" % (url, platform.node()))           
            else:
                self.send_error(404)
        except:
            self.send_error(500,'Failed to open url: %s, error: %s' % (url, str(sys.exc_info()[1])))
            
def main():
    try:
        server = HTTPServer(('', 8080), OpenRemoteHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
