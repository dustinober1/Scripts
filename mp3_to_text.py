import os
from google.cloud import speech_v1p1beta1 as speech

# Set up the speech recognizer
client = speech.SpeechClient()
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US',
)

# Set the path to the folder containing the mp3 files
folder_path = '/users/dustinober/Downloads/secret_father_brown_2304_librivox'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an mp3
    if filename.endswith('.mp3'):
        # Load the mp3 file
        file_path = os.path.join(folder_path, filename)

        # Convert the mp3 file to WAV format
        wav_filename = os.path.splitext(filename)[0] + '.wav'
        wav_path = os.path.join(folder_path, wav_filename)
        os.system(f'ffmpeg -i "{file_path}" -acodec pcm_s16le -ac 1 -ar 16000 "{wav_path}"')

        # Use the speech recognizer to transcribe the audio
        audio = speech.RecognitionAudio(content=open(wav_path, 'rb').read())
        response = client.recognize(config=config, audio=audio)
        text = response.results[0].alternatives[0].transcript

        # Save the transcribed text as a txt file with the same name as the mp3 file
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_path = os.path.join(folder_path, txt_filename)
        with open(txt_path, 'w') as f:
            f.write(text)

        # Delete the temporary WAV file
        os.remove(wav_path)