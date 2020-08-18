inputmsg = input("In put string you want to swap words: ")
print(inputmsg.split())
separatewords = inputmsg.split()

print("separate words")
for a in separatewords:
    print(a)

print("modify each words")
print(len(separatewords))
for b in range(len(separatewords)):
    separatewords[b] = 'G' + separatewords[b]
    print(separatewords[b])

print(separatewords)
print(" ".join(separatewords),)