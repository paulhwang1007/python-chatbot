from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model='llama3.2')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI ChatBot, Type 'exit' to quit.")

    # continues the conversation until the user types 'exit' and is not case sensitive
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # stores the conversation history
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\n AI: {result}"

if __name__ == "__main__":
    handle_conversation()

# run python3 main.py in the folder to use