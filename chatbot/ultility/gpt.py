OPENAI_API_KEY = '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'

from openai import OpenAI
client = OpenAI(api_key = OPENAI_API_KEY)


def run(input):
    completion = client.chat.completions.create(
    model="microsoft/DialoGPT-medium",
    messages=[
        {"role": "system", "content": "You are a therapist and love to talk about everything "},
        {"role": "user", "content": input}
    ]
    )

    reply = completion.choices[0].message.content
    return reply

