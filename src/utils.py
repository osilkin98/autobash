import openai


def get_choices(user_prompt: str, response_length: int, ) -> list[str]:
    # create the autocompleted bash response 
    openai_prompt = f'#!/bin/bash\n\n#{user_prompt}\n'

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=openai_prompt,
        temperature=0,
        max_tokens=response_length,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n\n", "#",]
    )

    # split up all of the provided choices and provide them back to the user
    choices = [c['text'].lstrip('\n') for c in response.get('choices', [])]  
    return choices