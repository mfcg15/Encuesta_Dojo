from _app.controllers import dojos
from _app import app
app.secret_key = 'claveSecreta15'

if __name__ == "__main__":
    app.run(debug=True)