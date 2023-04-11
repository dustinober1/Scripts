with open('TTSData.txt', 'r') as input_file:
    data = input_file.read()
    sentences = data.split('. ')
    with open('output.txt', 'w') as output_file:
        for sentence in sentences:
            output_file.write(sentence + '.\n')

