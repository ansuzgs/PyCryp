

#cipherText = raw_input("What is your ciphertext? ")

def frequencyAnalisys(message):

    frequency_analysis = { "a" : 0,  "b" : 0,  "c" : 0,  "d" : 0,  "e" : 0, "f" : 0,  "g" : 0,
        "h" : 0,  "i" : 0,  "j" : 0,  "k" : 0,  "l" : 0,  "m" : 0,  "n" : 0,  "o" :   0,
        "p" : 0,  "q" : 0,  "r" : 0,  "s" : 0,  "t" : 0,  "u" : 0,  "v" : 0,  "w" : 0,
        "x" : 0,  "y" : 0,  "z" : 0 }
    txtLenght = len(message)
    # print txtLenght
    for c in message:
        if c.isalpha():
              frequency_analysis[c.lower()] += 1
    i = 0
    por = [0]*26
    for c in frequency_analysis:
        por[i] = float(frequency_analysis.get(c))/txtLenght
        i = i+1
        print c + " => " + str(float(frequency_analysis.get(c))/txtLenght)

    #print max(frequency_analysis.values())

    for name, value in frequency_analysis.iteritems():
        if value == max(frequency_analysis.values()):
            print name
            key = ord(name) - ord('e')
            print key

    return por,key

#frequencyAnalisys(cipherText)
