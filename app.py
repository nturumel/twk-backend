# settings.py
import logging
import sys
import os
from dotenv import load_dotenv
env = load_dotenv(".env.local")
from twk_backend.router import app


# Set up root logger to write messages with level INFO or higher to stdout.
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', filename="app.log")

# Create a console handler and set its level to INFO
console_handler = logging.StreamHandler(sys.stdout)

# Create a formatter and add it to the console handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the root logger
logging.getLogger('').addHandler(console_handler)

if __name__ == "main":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
