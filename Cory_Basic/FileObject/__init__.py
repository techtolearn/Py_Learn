import os
with open("testfile.txt", mode="w", encoding="utf-8") as myFile:

    myFile.write("Some random text\nMore random text\nAnd some more")

with open("testfile.txt",encoding='utf-8') as myFile:
    lineNum = 1
    while True:
        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum)
        wordList = line.split()
        print("Number of words : ",len(wordList))

        charCount=0
        for word in wordList:
            for char in word:
                charCount+=1

        avgNumChar = charCount/len(wordList)
        print('Avg word of length : {:.2f} '.format(avgNumChar))

        lineNum+=1




