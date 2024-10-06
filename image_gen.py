import enviroment
import requests
import time

def requestAIImageGen(prompt: str) -> str:
    request = requests.post(
        'https://api.bfl.ml/v1/flux-pro-1.1',
        headers={
            'accept': 'application/json',
            'x-key': enviroment.FLUX_API_KEY,
            'Content-Type': 'application/json',
        },
        json={
            'prompt': prompt,
            'width': 1024,
            'height': 768,
        },
    ).json()
    return request["id"]

def getAIImageURL(request_id: str) -> str:
    while True:
        time.sleep(0.5)
        result = requests.get(
            'https://api.bfl.ml/v1/get_result',
            headers={
                'accept': 'application/json',
                'x-key': enviroment.FLUX_API_KEY,
            },
            params={
                'id': request_id,
            },
        ).json()
        if result["status"] == "Ready":
            return result['result']['sample']