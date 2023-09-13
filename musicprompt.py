import openai
import os


def generate_prompt(image_descriptions):

    return """in 1 line can you explain music genres instruments bpm suitable for this scene?""" + image_descriptions


def generate_music_prompt(image_descriptions):

    openai.api_key = os.environ['OPENAI_API_KEY']

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(image_descriptions),
        temperature=0.6,
        max_tokens=60,
    )

    print("OpenAI Response: ", response)
    return response['choices'][0]['text']
