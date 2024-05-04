import os
import requests

def translate_text(text, target_lang):
    # DeepL API 엔드포인트
    url = "https://api-free.deepl.com/v2/translate"

    # DeepL API 키 가져오기
    api_key = os.environ.get('DEEPL_API_KEY')

    # 번역할 텍스트 및 목표 언어 설정
    params = {
        'auth_key': api_key,
        'text': text,
        'target_lang': target_lang
    }

    # DeepL API에 POST 요청 보내기
    response = requests.post(url, data=params)

    # 응답 확인
    if response.status_code == 200:
        translated_text = response.json()['translations'][0]['text']
        return translated_text
    else:
        print("번역 요청에 실패했습니다.")
        return None

# 번역할 텍스트 입력
text_to_translate = "Hello, how are you?"

# 번역할 언어 코드 설정 (예: 독일어 = "DE", 프랑스어 = "FR" 등)
target_language = "FR"

# 번역 실행
translated_text = translate_text(text_to_translate, target_language)

# 번역 결과 출력
if translated_text:
    print("번역 결과:", translated_text)