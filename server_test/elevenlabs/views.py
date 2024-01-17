import os
from django.conf import settings
from django.http import JsonResponse
import requests


def audio_request(request):
    if request.method == 'GET':
        voice_id = 'EXAVITQu4vr4xnSDxMaL'
        url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice_id

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": "8a5f522f7448296ad54b8a02e86c8e34"
        }

        data = {
            "text": 'Привет абоба',
            'model_id': 'eleven_multilingual_v2',
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }


        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            audio_content = response.content
            # save audio local
            audio_url = generate_name(1, 1, voice_id, 'en')
            save_local(audio_content, audio_url)
            path_to_audio = 'http://127.0.0.1:8000/media/'
            return JsonResponse({'type': 'SUCCESS', 'url': path_to_audio + audio_url})
        else:
            return JsonResponse({'type': 'ERROR', 'answer': 'Server error.'})
    else:
        return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})


def generate_name(book_id, part, voice_id, lang):
    # book id | part | voice_id | language
    return str(book_id) + '|' + str(part) + '|' + voice_id + '|' + lang + '.mpga'


def save_local(audio_content, name):
    audio_path = os.path.join(settings.MEDIA_ROOT, name)
    with open(audio_path, 'wb') as audio_file:
        audio_file.write(audio_content)
