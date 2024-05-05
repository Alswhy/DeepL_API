# uvicorn trans_api:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    target_lang: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the translation API!"}

@app.post("/translate/")
def translate_text(request: TranslationRequest):
    # DeepL API 엔드포인트
    url = "https://api-free.deepl.com/v2/translate"

    # DeepL API 키 가져오기
    api_key = os.environ.get('DEEPL_API_KEY')

    # 번역할 텍스트 및 목표 언어 설정
    params = {
        'auth_key': api_key,
        'text': request.text,
        'target_lang': request.target_lang
    }

    # DeepL API에 POST 요청 보내기
    response = requests.post(url, data=params)

    # 응답 확인
    if response.status_code == 200:
        translated_text = response.json()['translations'][0]['text']
        return {"translated_text": translated_text}
    else:
        raise HTTPException(status_code=500, detail="번역 요청에 실패했습니다.")
