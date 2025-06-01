import os
import google.generativeai as genai
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Set the API key for Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_response(prompt):
    """Generates a response from the AI model based on the given prompt."""
    response = model.generate_content(prompt)
    return response.text


def division(a, b):
    """Divides a by b and returns the result."""
    return a / b

if __name__ == "__main__":
    try:
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))
        result = division(a, b)
        print(f"The result of {a} divided by {b} is: {result}")
    except Exception as e:
        response = generate_response(f"Fix the error in the code: {e}")
        print(response)