import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
import requests
import mimetypes


# Create your views here.
def test(request):
    return JsonResponse({'response': 'TEST'})


CHUNK_SIZE = 1024

url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "8a5f522f7448296ad54b8a02e86c8e34"
}

data = {
    "text": 'Born and raised in the charming south, I can add a touch of sweet southern hospitality to your audiobooks '
            'and podcasts',
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}


def audio_request(request):

    if request.method == 'GET':
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            audio_content = response.content

            audio_path = os.path.join(settings.MEDIA_ROOT, 'audio.mpga')
            with open(audio_path, 'wb') as audio_file:
                audio_file.write(audio_content)
            path_to_audio = 'http://127.0.0.1:8000/media/'
            return JsonResponse({'type': 'SUCCESS', 'url': path_to_audio + 'audio.mpga'})
        else:
            return JsonResponse({'type': 'ERROR', 'answer': 'Server error.'})
    else:
        return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})
