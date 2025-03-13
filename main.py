import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def chat_w_gpt(prompt):
    response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like boyfriend/girlfriend.",
    input=prompt,
    )
    return response.output_text




if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            break
        response = chat_w_gpt(user_input)
        print("Chatbot: ", response)