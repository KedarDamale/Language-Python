from dotenv import load_dotenv
import os

load_dotenv()

weather_api_key = os.getenv("API_KEY")


print("API Key:", weather_api_key)


