'''
References: 
# https://flask.palletsprojects.com/en/stable/patterns/fileuploads/
'''

from flask import Flask
from config import Config
from utils import create_ssh_tunnel, bp

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(bp)


if __name__ == "__main__":
    tunnel = create_ssh_tunnel()
    try:
        tunnel.start()
        app.run(host='0.0.0.0', port=8000, debug=True)
    finally:
        tunnel.stop()
