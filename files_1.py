with open("dataset_24465_4.txt", 'r') as file , open("file2.txt", 'w') as copy:
    for line in reversed(file.readlines()):
        copy.write(line.rstrip())
        copy.write('\n')


