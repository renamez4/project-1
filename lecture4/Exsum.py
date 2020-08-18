str1= "English = 78 Science = 83 Math = 68 History = 65"
lit = (str1.split())
kim = 0
avg = 0
for i in lit:
    if i.isnumeric():
        kim = kim + int(i)
        avg = avg + 1
print(kim / avg) 
print(kim)