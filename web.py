from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>Device Specifications</title>
</head>
<body>
<table border="2" cellspacing="10" cellpading="6">
<h1> DEVICE SPECIFICATIONS - FARZANA (25013772)</h1>
<tr>
<th>s.no</th>
<th>Specification</th>
<th>Details</th>
</tr>
<tr>
<td>1</td>
<td>Device Name</td>
<td>Asus</td>
</tr>
<tr>
<th>2</th>
<td>Processor</td>
<td>13th Gen Intel(R) Core(TM) i5-13420H (2.10 GHz)</td>
</tr>
<tr>
<td>3</td>
<td>Installed RAM</td>
<td>16.0 GB (15.6 GB usable)</td>
</tr>
<tr>
<td>4</td>
<td>System Type</td>
<td>64-bit operating system, x64-based processor</td>
</tr>
<tr>
<td>5</td>
<td>Pen and touch</td>
<td>No pen or touch input is available for this display</td>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
