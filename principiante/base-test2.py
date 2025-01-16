vowels = 'a e i o u'.split()
consonants = 'b c d f g h j k l m n p q r s t v w x y z'.split()

lines = input("How many lines the poem will be? ")
try:
    lines = int(lines)
except:
    print('Enter a valid digit!')
    exit()

poem = []

# poem = [
#     "Once there was an elephant,",
#     "Who tried to use the telephant",
#     "No! No! I mean an elephone",
#     "Who tried to use the telephone",
# ]

print("\n[*] Write your poem:\n\n")
for line in range(lines):
    poem.append(input())

total_vows = 0
total_cons = 0
for line in poem:
    line_vows = 0
    line_cons = 0
    for char in line:
        if char.lower() in vowels:
            line_vows += 1
            total_vows += 1
        elif char.lower() in consonants:
            line_cons += 1
            total_cons += 1
    print()
    print("Analyzing    line: {}".format(line or '(empty line)'))
    print("Line's     vowels: {}".format(line_vows))
    print("Line's consonants: {}".format(line_cons))

print()
print("Total number of      lines: {}".format(len(poem)))
print("Total number of     vowels: {}".format(total_vows))
print("Total number of consonants: {}".format(total_cons))