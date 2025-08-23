import os
from dotenv import load_dotenv
import google.generativeai as genai

# 1. Load environment variables from .env file
load_dotenv()

# 2. Get API key from environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Did you set GOOGLE_API_KEY in .env?")

print("Loaded API Key:", api_key[:10], "...")  # show only first 10 chars

# 3. Configure Gemini with API key
genai.configure(api_key=api_key)

# 4. Create model object
model = genai.GenerativeModel("gemini-1.5-flash")

# 5. Send a prompt to Gemini
response = model.generate_content("Explain how AI works in a few words.")

# 6. Print Gemini's response
print("Gemini Response:", response.text)
