#Program variables
dictionaryWords=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U','W', 'X', 'Y', 'Z',
                 '0','1','2','3','4','5','6','7','8','9',' ','.',',']

#Methods
def CheckSentence(sentenceProvided):
    #Method for checking if all signs used in word provided are present in a dictionary
    letterFound = False
    sentenceCorrect = False

    print("Sprawdzam słowo: \"",sentenceProvided,"\"")
    for i in range(0, len(sentenceProvided)):
        for j in range(0, len(dictionaryWords)):
            if(sentenceProvided[i]==dictionaryWords[j]):
                letterFound = True
                break
        if(letterFound):
            letterFound=False
            sentenceCorrect=True
        else:
            sentenceCorrect=False
            print("Nie znaleziono znaku \"", sentenceProvided[i], "\" w słowniku. Proszę zmienić szyfrowaną wiadomość.")
            break

    if(sentenceCorrect):
        print("Słowo \"",sentenceProvided,"\" jest prawidłowe.")
        return True
    else:
        return False

def encodeSentenceProvided(sentenceProvided):
    #This method is used for encoding message provided
    encodedSentence = []

    print("Rozpoczynam szyfrowanie słowa: \"", sentenceProvided, "\"")
    for i in range(0, len(sentenceProvided)):
        for j in range(0, len(dictionaryWords)):
            if (sentenceProvided[i] == dictionaryWords[j]):
                encodedSentence.append(encodeNumber(j+1))
                print("Kod znaku \033[94m",sentenceProvided[i],"\033[0m to \033[91m",j+1,"\033[0m")
                print("Kod znaku po redundancji: \033[95m", encodedSentence[i], "\033[0m")
                break

    return encodedSentence

def encodeNumber(numberRaw):
    #This method encodes number provided using redundancy method
    encNum = (numberRaw << 8) + numberRaw
    return encNum

sentance = "Ola ma kutasa"
#CheckSentence(sentance)
encSent = encodeSentenceProvided(sentance)

#for i in range(0,len(encSent)):
#    print(bin(encSent[i]))

#number = 39
#encNum = encodeNumber(number)

#print("Raw number: ", number)
#print("Encoded number: ", encNum)
#print("Encoded number (binary): ", bin(encNum))