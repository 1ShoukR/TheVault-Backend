from . import app
import os

if __name__ == "__main__":
    app.run(port=os.environ.get('FLASK_RUN_PORT'), debug=True)