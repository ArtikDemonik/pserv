from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from urllib.parse import urlparse, parse_qs
import coding
import commands

if __name__ == '__main__':
    from sys import argv
    
    if len(argv) == 2:
        commands.run(port=int(argv[1]))
    else:
        commands.run()
