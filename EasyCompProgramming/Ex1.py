# Your program is to use the brute-force approach in order to find the Answer to Life, the Universe, and Everything. 
# More precisely... rewrite small numbers from input to output. Stop processing input after reading in the number 42.
# All numbers at input are integers of one or two digits.

EsCuatroDos = False
elementos = []

while not EsCuatroDos:
    entrada = input()
    if int(entrada) == 42:
        EsCuatroDos = True
    else:
        elementos.append(int(entrada))

for elem in elementos:
    print(elem)