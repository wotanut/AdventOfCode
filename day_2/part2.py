import fnmatch

def readFile():
    with open('example.txt', 'r') as f:
        lines = f.readlines()
        return lines

def sanitize(line: str):
    line = line.replace("\n", "")
    return line

def main():
    file = readFile()
    sum = 0

    for line in file:
        line = sanitize(line)
        gameId = line.split(" ")[1]
        gameId = gameId.replace(":", "")

        split = line.split(" ")
        games = line.split(";")

        games[0] = games[0].split(":")[1] # for the first game

        totals = [0,0,0]

        for _ in range(len(games)):
            rTotal, gTotal, bTotal = 0, 0, 0
            game = games[_]
            split = game.split(",")

            red = fnmatch.filter(split, "*red")[0] if fnmatch.filter(split, "*red") else -1
            green = fnmatch.filter(split, "*green")[0] if fnmatch.filter(split, "*green") else -1
            blue = fnmatch.filter(split, "*blue")[0] if fnmatch.filter(split, "*blue") else -1

            rTotal = int(red[:-3]) if red != -1 else 0
            gTotal = int(green[:-5]) if green != -1 else 0
            bTotal = int(blue[:-4]) if blue != -1 else 0

            if rTotal > totals[0]:
                totals[0] = rTotal
            if gTotal > totals[1]:
                totals[1] = gTotal
            if bTotal > totals[2]:
                totals[2] = bTotal

        sum = sum + (totals[0] * totals[1] * totals[2])

    print(sum)
main()