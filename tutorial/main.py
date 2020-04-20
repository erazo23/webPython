from flask import Flask #importamos la liberia de flask

app = Flask(__name__) # realizamos una instancia, en la cual el contexto es name

if __name__ == '__main__': # si el contexto es igual a main ejecuta la instancia
    app.run(debug=True)
