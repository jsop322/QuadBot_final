import http.server
import socketserver
from walking import Walking

class HTTPServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        http.server.SimpleHTTPRequestHandler.do_GET(self)
 
    def do_POST(self):
        
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
 
        if post_body.decode("utf-8") == "Direction=forward":
            walk.testWalking(walk.getServoZeroes(), walk.getKit1(), walk.getKit2(), walk.getPwmMin(), walk.getPwmMax())
        elif post_body.decode("utf-8") == "Direction=left":
            print('hamis liikkuu vasemmalle!')
            walk.turnLeft(walk.getServoZeroes(), walk.getKit1(), walk.getKit2(), walk.getPwmMin(), walk.getPwmMax())        
        elif post_body.decode("utf-8") == "Direction=back":
            walk.walkBack(walk.getServoZeroes(), walk.getKit1(), walk.getKit2(), walk.getPwmMin(), walk.getPwmMax())
            print('hamis liikkuu bäkkii!')
        elif post_body.decode("utf-8") == "Direction=right":
            walk.turnRight(walk.getServoZeroes(), walk.getKit1(), walk.getKit2(), walk.getPwmMin(), walk.getPwmMax()) 
            print('hamis liikkuu oikeelle!')
        elif post_body.decode("utf-8") == "Camera=left":
            walk.cameraLeft(walk.getKit1(), walk.getPwmMin(), walk.getPwmMax())
        elif post_body.decode("utf-8") == "Camera=right":
            walk.cameraRight(walk.getKit1(), walk.getPwmMin(), walk.getPwmMax())
        elif post_body.decode("utf-8") == "Camera=center":
            walk.cameraCenter(walk.getKit1(), walk.getPwmMin(), walk.getPwmMax())  
        elif post_body.decode("utf-8") == "Stop=movement":
            print("liike loppuu!!")

        response = post_body
        self.send_response(200)
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

 
PORT = 8000

walk = Walking()
Handler = HTTPServerHandler
 
httpd = socketserver.TCPServer(("192.168.43.207", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()