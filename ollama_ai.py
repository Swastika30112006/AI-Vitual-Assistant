import ollama

def ask_ai(question):
    response = ollama.chat(
        model = 'phi',
        messages = [ 
            {"role": "user", "content": question}
        ]
    )

    return response['message']['content']