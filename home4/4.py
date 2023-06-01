#中翻英程式

import openai

openai.api_key = '你的 API 金鑰'

def translate(text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=100,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    translation = response.choices[0].text.strip()
    return translation

chinese_text = "你好，這是一個中文翻譯的示例。"

english_translation = translate(chinese_text)
print(english_translation)
