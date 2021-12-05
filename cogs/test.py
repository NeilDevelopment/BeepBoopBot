from dotenv import load_dotenv
from os import getenv
import os

load_dotenv()

log = os.getenv("LOG_CHANNEL")

print(log)