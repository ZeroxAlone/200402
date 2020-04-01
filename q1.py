# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:20:04 2020

@author: lisa_
"""


import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("serving at port", 8000)
    httpd.serve_forever()