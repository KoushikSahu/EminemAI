import requests
import uuid
import wget
import time


class TextToSpeech():
    def __init__(self, tts_model_token='TM:27fj0gsh11pd'):
        self.tts_model_token = tts_model_token


    def make_request(self, inference_text):
        url = 'https://api.fakeyou.com/tts/inference'
        
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'} 
        
        data = {
            'tts_model_token': f'{self.tts_model_token}',
            'uuid_idempotency_token': f'{uuid.uuid4()}',
            'inference_text': f'{inference_text}'
        }
        
        response = requests.post(url, headers=headers, json=data)
        response_body = response.json()
        
        self.inference_job_token = response_body['inference_job_token']
        return response_body['inference_job_token']


    def track_request(self):
        url = f'https://api.fakeyou.com/tts/job/{self.inference_job_token}'
        
        headers = {'Content-Type': 'application/json'} 
        
        job_completed = False
        retries = 10

        while not job_completed and retries > 0:
            response = requests.get(url, headers=headers)
            response_body = response.json()

            request_status = response_body['state']['status']
            if request_status == 'complete_success':
                job_completed = True
                self.wav_audio_path = response_body['state']['maybe_public_bucket_wav_audio_path']
                return response_body['state']['maybe_public_bucket_wav_audio_path']
            elif request_status == 'complete_failure' or request_status == 'dead':
                raise Exception(f'Inference job failed: {response_body["state"]["maybe_error_message"]}')

            time.sleep(2)
            retries -= 1

        raise Exception('Inference job failed: exceeded retries')

    def download_audiofile(self):
        wget.download(f'https://storage.googleapis.com/vocodes-public{self.wav_audio_path}', './data/audio/output.wav') 
