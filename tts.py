import csv
from gtts import gTTS

# Loop through the CSV file and generate audio files
with open('tts.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        filename = row[0]
        text = row[1]
        audio = gTTS(text=text, lang='en', slow=False)
        audio.save(filename)
