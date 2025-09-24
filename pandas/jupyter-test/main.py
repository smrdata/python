from dotenv import load_dotenv
import os

load_dotenv() # read .env file

print(os.getenv("DB_USER"))  # prints: admin