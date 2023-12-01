def readFile():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        return lines

def getFirstLetter(line: str):
    for letter in line:
        if letter.isnumeric():
            return letter
        
def main():
    file = readFile()
    sum = 0
    whole = ""

    for line in file:
        whole += getFirstLetter(line)
        line = line[::-1]
        whole += getFirstLetter(line)
        sum = sum + int(whole)
        whole = ""
    
    print(sum)

main()