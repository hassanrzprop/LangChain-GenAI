from langchain_openai import OpenAI  # Ensure you're importing the correct module
from dotenv import load_dotenv  # Import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the OpenAI object correctly
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) #google api key is paid

# Define the prompt
prompt = "What would be the cost to build a house of 1 kanal in DHA phase 3 Lahore?"

# Get the response from the model
response = llm.invoke(prompt)

# Print the response
print(response)