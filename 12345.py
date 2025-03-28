import openai

# Set up your OpenAI API credentials
openai.api_key = skE1c7eBpKnDnSik0cAl7DT3BlbkFJtKP1hN95H5FTGfKAjTOZ

# Define a function to interact with the chat model
def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    
    # Extract the model's reply from the response
    reply = response.choices[0].text.strip()
    return reply

# Start the conversation
def start_conversation():
    print("Welcome! Let's chat.")
    print("Type 'exit' to end the conversation.\n")
    
    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("You: ")
        
        # Exit the loop if the user wants to end the conversation
        if user_input.lower() == "exit":
            break
        
        # Concatenate the user's input and the model's previous responses
        prompt = "User: " + user_input + "\nAI: "
        
        # Get the model's response
        model_reply = chat_with_gpt3(prompt)
        
        # Display the model's response
        print("AI:", model_reply)
    print("Goodbye!")

# Start the conversation
start_conversation()
