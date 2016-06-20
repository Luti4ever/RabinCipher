import sympy
import random

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
            if(sentenceProvided[i] == dictionaryWords[j]):
                letterFound = True
                break
        if(letterFound):
            letterFound = False
            sentenceCorrect = True
        else:
            sentenceCorrect = False
            print("Nie znaleziono znaku \"", sentenceProvided[i], "\" w słowniku. Proszę zmienić szyfrowaną wiadomość.")
            break

    if(sentenceCorrect):
        print("Słowo \"",sentenceProvided,"\" jest prawidłowe.")
        return True
    else:
        return False

def EncodeSentenceProvided(sentenceProvided):
    #This method is used for encoding message and adding redundancy
    encodedSentence = []

    print("Rozpoczynam szyfrowanie słowa: \"", sentenceProvided, "\"")
    for i in range(0, len(sentenceProvided)):
        for j in range(0, len(dictionaryWords)):
            if (sentenceProvided[i] == dictionaryWords[j]):
                encodedSentence.append(EncodeNumber(j+1))
                print("Kod znaku \033[94m", sentenceProvided[i],"\033[0m to \033[91m",j+1,"\033[0m")
                print("Kod znaku po redundancji: \033[95m", encodedSentence[i], "\033[0m")
                break

    return encodedSentence

def EncodeNumber(numberRaw):
    #This method encodes number provided using redundancy method
    encNum = (numberRaw << 8) + numberRaw
    return encNum

def FindPrimeMod4(numberOfPrimes):
    #This method calculates given number of primes j, with condition j mod 4 = 3.
    listOfPrimes = []
    i = 1;

    while (len(listOfPrimes) < numberOfPrimes):
        prime = sympy.prime(i)
        if(prime%4 == 3 and prime >= 600):
            listOfPrimes.append(prime)
        i = i + 1

    # print("Lista znalezionych liczb pierwszych spełniających warunki:")
    # for j in range(0, len(listOfPrimes)):
    #     print(listOfPrimes[j], " ", end="")
    # print("\n")

    return listOfPrimes

def CheckPair(p, q, n = 65535):
    #This method checks if the product of selected pair of numbers is large enough
    temp = p*q
    print("\nIloczyn liczb \033[94m p = ", p, "\033[0m oraz \033[94m q = ", q, "\033[0m wynosi \033[91m", temp, "\033[0m")

    if(temp > n):
        print("Liczba ta jest większa od wartości granicznej \033[95m", n, "\033[0m - wartość prawidłowa")
        return True
    else:
        print("Liczba ta nie jest większa od wartości granicznej \033[95m", n, "\033[0m - wartość nieprawidłowa")
        return False

def SelectPair():
    #This method randomly selects the pair of Primes p and q
    pair = []
    listOfPrimes = FindPrimeMod4(100)
    pair.append(random.choice(listOfPrimes))
    pair.append(random.choice(listOfPrimes))

    while(CheckPair(pair[0], pair[1]) == False):
        pair[0] = random.choice(listOfPrimes)
        pair[1] = random.choice(listOfPrimes)

    return pair

def RabinCypherMessage(message):
    cyphertext = []
    print("\nWiadomość do zaszyfrowania w postaci cyfrowej:")
    for i in range(0, len(message)):
        print(message[i], " ", end="")

    print("\n--------------------- Rozpoczynam szyfrowanie ---------------------")
    privateKey = SelectPair()
    publicKey = privateKey[0] * privateKey[1]

    for i in range(0, len(message)):
        calcTemp = pow(message[i],2,publicKey)
        cyphertext.append(calcTemp)

    print("Kryptogram:")
    for i in range(0, len(cyphertext)):
        print(cyphertext[i], " ", end="")


################################# MAIN PROGRAM #####################################

sentance = "Ola ma kutasa"

CheckSentence(sentance)
RabinCypherMessage(EncodeSentenceProvided(sentance))