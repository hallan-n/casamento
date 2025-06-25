from os import getenv

from dotenv import load_dotenv

load_dotenv(override=True)
ACCESS_TOKEN = getenv("ACCESS_TOKEN")
USER = getenv("USER")
PWD = getenv("PWD")
DATABASE_URL = getenv("DATABASE_URL")
