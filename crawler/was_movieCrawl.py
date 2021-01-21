#!/usr/bin/python
# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys, string, cgi, time, datetime, io, pkg_resources
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib import response
from urllib.parse import urlparse, urlsplit, parse_qsl
from collections import OrderedDict
import MovieCrawler
import RepleCrawler

print("Python start")

PORT_NUMBER = 8082

s_prod_list = []

# This class will handle any incoming request from
# a browser
class myHandler(BaseHTTPRequestHandler):

    print(1)
    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:8080')
        self.send_header("Content-type", "application/json")
        self.end_headers()
        url_path = urlparse(self.path).path
        print(url_path)
        if url_path == "":
            return self

        params = OrderedDict()
        if "?" in self.path:
            for key, value in dict(parse_qsl(urlparse(self.path).query)).items():
                print(key + " = " + value)
                params[key] = value
        print(params)

        output = io.StringIO()
        q = OrderedDict()
        if url_path == "/py_getMovieCrawl.py":   # 검색부모 insert
            print(1)
            MovieCrawler.createExcel()
            print(2)
            RepleCrawler.createExcelReple(params["movieTitle"])
            print(3)

        output.write("<html><head>222")
        output.write("<style type=\"text/css\">")
        output.write("h1 {color:blue;}")
        output.write("h2 {color:red;}")
        output.write("</style>")
        # output.write("<h1>Device #" + " Root Content</h1>" + s_prod_list)
        # output.write("<h2>Device Addr: " + sys + "</h1>")
        # output.write("<h2>Device Time: " + now.strftime("%Y-%m-%d %H:%M:%S") + "</h2>")
        output.write("<body>Python start")
        output.write("</body>")
        output.write("</html>")

        self.wfile.write(output.getvalue().encode())
        return self

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print ('Started httpserver on port ' , PORT_NUMBER)
    # s_prod_list =

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()