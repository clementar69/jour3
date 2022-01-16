
with open("input") as fin:
    data = [i for i in fin.read().strip().split("\n")]



def binary_to_int(binaryStr):
    return int(binaryStr, 2)


# Part 1
def part1():
    gammaRate = []
    epsilonRate = []


    for i in range(0, len(data[0])):
        zeros = 0
        ones = 0


        for bitString in data:


            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1


        if zeros > ones:
            gammaRate.append('0')
            epsilonRate.append('1')
        elif ones > zeros:
            gammaRate.append('1')
            epsilonRate.append('0')


    gammaRate = ''.join(gammaRate)
    epsilonRate = ''.join(epsilonRate)


    powerConsumption = binary_to_int(gammaRate) * binary_to_int(epsilonRate)
    return powerConsumption


# Part 2
def part2():

    firstData = data.copy()


    i = 0
    while len(firstData) > 1:
        zeros = 0
        ones = 0


        for bitString in firstData:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1


        if zeros > ones:
            firstData = [bitString for bitString in firstData if bitString[i] == '0']
        else:
            firstData = [bitString for bitString in firstData if bitString[i] == '1']

        i += 1

    oxygenRating = ''.join(firstData)


    secondData = data.copy()


    i = 0
    while len(secondData) > 1:
        zeros = 0
        ones = 0

        # Binary counter
        for bitString in secondData:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1


        if zeros > ones:
            secondData = [bitString for bitString in secondData if bitString[i] == '1']
        else:
            secondData = [bitString for bitString in secondData if bitString[i] == '0']

        i += 1

    carbonRating = ''.join(secondData)

    return binary_to_int(oxygenRating) * binary_to_int(carbonRating)


print("part 1: ", part1())
print("part 2: ", part2())