def readFile():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        return lines

letterMap = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}

def replaceStrings(line: str):
    line = line.replace("\n", "")
    string = ""

    for letter in line:
        string += letter
        for key in letterMap:
            # print(string)
            if string.endswith(letterMap[key]):
                string += str(key)
                string += letter
            # string = string.replace(letterMap[key], str(key))
    return string

def getFirstLetter(line: str):
    line = replaceStrings(line)
    for letter in line:
        if letter.isnumeric():
            return letter, line
        
def main():
    file = readFile()
    sum = 0
    whole = ""

    for line in file:
        letter, line = getFirstLetter(line)
        whole += letter
        line = line[::-1]
        letter, line = getFirstLetter(line)
        whole += letter
        sum = sum + int(whole)
        whole = ""
    
    print(sum)

main()