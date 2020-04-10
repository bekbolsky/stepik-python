genome = input()

g = genome.upper().count("g".upper())
c = genome.upper().count("c".upper())
length = len(genome)

print(((g + c) / length) * 100)
