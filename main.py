import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

# openai.api_key = "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"
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