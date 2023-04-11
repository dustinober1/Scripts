import csv

# Set up the CSV file and write the header row
with open('tts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['file', 'text'])

    # Loop through the input file and write each line to the CSV file
    with open('output.txt', 'r') as input_file:
        for i, line in enumerate(input_file):
            filename = 'audio{:03d}.wav'.format(i+1)
            writer.writerow([filename, line.strip()])