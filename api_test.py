import requests

url = "http://127.0.0.1:8000/translate/"

# 사용자로부터 번역할 텍스트와 목표 언어 코드 입력 받기
text_to_translate = input("텍스트 입력: ")
target_lang = input("번역할 언어 코드 입력 (예: 독일어 = 'DE', 프랑스어 = 'FR' 등): ")

data = {
    "text": text_to_translate,
    "target_lang": target_lang
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    translated_text = result['translated_text']
    print("번역 결과:", translated_text)
else:
    print("번역 요청에 실패했습니다.")
