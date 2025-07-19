import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.0-flash")

def get_answer(question):
    prompt = f"You are an intelligent assistant. Answer the following question clearly:\n\n{question}"
    response = model.generate_content([prompt])
    return response.text.strip()
