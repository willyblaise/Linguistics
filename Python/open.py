import openai

openai.api_key = 

prompt = input("Ask me something....")

response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.7,
        )


nixon = response.choices[0].text.strip()
print(f"Answer: {nixon}")
