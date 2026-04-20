from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # читаем HTML файл
        with open("contacts.html", "r", encoding="utf-8") as file:
            html = file.read()

        # ответ сервера
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(html.encode("utf-8"))


# запуск сервера
server = HTTPServer(("localhost", 8000), Handler)

print("Сервер запущен: http://localhost:8000")
server.serve_forever()