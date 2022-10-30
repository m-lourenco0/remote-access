from flask import Flask

app = Flask(__name__)

#Controllers import
from src.controller import Remote

app.register_blueprint(Remote)

if __name__ == '__main__':
    app.run()