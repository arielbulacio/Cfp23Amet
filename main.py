import os

from flask import Flask, send_file

app = Flask(__name__, template_folder='src')

@app.route("/")
def index():
    return send_file('src/index.html')

 
# Ruta para "Quiénes somos"
@app.route("/quienes_somos")
def quienes_somos():
    return send_file('src/quienes_somos.html')

# Ruta para "Contacto"
@app.route("/contacto")
def contacto():
    return send_file('src/contacto.html')

# Ruta para "cursos"
@app.route("/cursos")
def cursos():
    return send_file('src/cursos.html')   

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
