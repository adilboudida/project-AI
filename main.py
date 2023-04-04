import openai
openai.api_key="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"
while True:
    ask=input("Adil_Boudida :")
    response=openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=700,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    text= response['choices'][0]['text']
    print("ChatGPT :"+text)













