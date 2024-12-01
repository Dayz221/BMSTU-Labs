from os import system


def getWords(text: list[str]) -> list[list[str]]:
    return [line.split() for line in text]


def alignLeft(text: list[str]) -> list[str]:
    text = [" ".join(line.split()) for line in text]
    return text


def alignRight(text: list[str]) -> list[str]:
    text = [" ".join(line.split()) for line in text]
    maxLen = max([len(line) for line in text])

    for i in range(len(text)):
        text[i] = " " * (maxLen - len(text[i])) + text[i]
    return text


def stretch(text: list[str]) -> list[str]:
    text = getWords(text)
    maxLen = max(
        [sum([len(word) for word in line]) + max(0, len(line) - 1) for line in text]
    )

    for line in range(len(text)):
        newLine = ""

        words_len = sum([len(word) for word in text[line]])
        words_num = max(1, len(text[line]) - 1)

        spaces = (maxLen - words_len) // words_num
        delta = (maxLen - words_len) % words_num

        for i, word in enumerate(text[line]):
            newLine += word + " " * (spaces + (i < delta))

        text[line] = newLine

    return text


def deleteWord(text: list[str], wordForDelete: str, alignment=alignLeft) -> list[str]:
    return alignment(
        [
            " ".join(
                [word for word in line.split() if word.lower() != wordForDelete.lower()]
            )
            for line in text
        ]
    )


def replaceWord(text: list[str], old: str, new: str, alignment=alignLeft) -> list[str]:
    return alignment(
        [
            " ".join(
                [
                    (word if word.lower() != old.lower() else new)
                    for word in line.split()
                ]
            )
            for line in text
        ]
    )


def countExpressions(text: list[str], alignment=alignLeft) -> list[str]:
    text = getWords(text)
    for li, line in enumerate(text):
        answ = 0
        isExp = False
        newLine = []
        for i, word in enumerate(line):
            if word.isnumeric():
                if not isExp:
                    isExp = True
                    answ = int(word)
            elif word == "-" and line[i + 1].isnumeric() and isExp:
                answ -= int(line[i + 1])
            elif word == "*" and line[i + 1].isnumeric() and isExp:
                answ *= int(line[i + 1])
            elif isExp:
                isExp = False
                newLine.append(str(answ))
                newLine.append(word)
            else:
                isExp = False
                newLine.append(word)

        if isExp:
            newLine.append(str(answ))

        text[li] = newLine
    return alignment([" ".join(line) for line in text])


def findAndDelete(text: list[str], alignment=alignLeft) -> tuple[list[str], str]:
    text = getWords(text)
    words = {}
    maximum = 0
    mword = ""

    for line in text:
        for word in line:
            words[word] = words.get(word, 0) + 1
            if words[word] > maximum:
                maximum = words[word]
                mword = word

    return alignment([ ' '.join([word for word in line if word != mword]) for line in text ]), mword

def clear() -> None:
    system("cls")


def pause() -> None:
    print("Нажмите любую клавишу...")
    system("pause > nul")
