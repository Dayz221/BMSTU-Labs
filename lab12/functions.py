def alignLeft(text):
    text = [' '.join(line.split()) for line in text]
    return text

def alignRight(text):
    text = [' '.join(line.split()) for line in text]
    maxLen = max([len(line) for line in text])
    
    for i in range(len(text)):
        text[i] = ' ' * (maxLen-len(text[i])) + text[i]
    return text

def stretch(text):
    textWithWords = [line.split() for line in text]
    maxLen = max([sum([len(word) for word in line]) + max(0, len(line)-1) for line in textWithWords])
    
    text = []
    for line in textWithWords:
        newLine = ""
        words_len = sum([len(word) for word in line])
        spaces = (maxLen - words_len)//max(1, len(line)-1)
        delta = (maxLen - words_len)%max(1, len(line)-1)
        for i, word in enumerate(line):
            newLine += word + ' ' * (spaces + (i < delta))
        text.append(newLine)
    
    return text

def deleteWord(text, wordForDelete, alignment=alignLeft):
    for i in range(len(text)):
        text[i] = text[i].replace(wordForDelete, '')
    text = alignment(text)
    return text