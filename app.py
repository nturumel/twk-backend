from dotenv import load_dotenv

# settings.py
env = load_dotenv(".env.local")

from twk_backend.router import app

if __name__ == "main":
    app.run(port=5000)  #
