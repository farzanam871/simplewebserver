# EX01 Developing a Simple Webserver
## Date: 01.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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

```



## OUTPUT:
![alt text](<Screenshot 2025-09-30 172626.png>)

![alt text](<Screenshot 2025-09-30 172823.png>)














## RESULT:
The program for implementing simple webserver is executed successfully.
