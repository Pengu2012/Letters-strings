inputStr =input("Enter your  string here")

vowels= {'a':0 , 'e':0 , 'i':0 , 'o':0 , 'u':0}
for c in inputStr:
    if c in vowels:
        vowels[c]+=1

print(vowels)


EnterStr = input ("enter your string here: ")
letter = {'a':0 , 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
for a in EnterStr:
    if a in letter:
        letter[a]+=1

print(letter)