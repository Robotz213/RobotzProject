from app.config import debug

from app import app

if __name__ == "__main__":

    app.run("0.0.0.0", 6064, debug())