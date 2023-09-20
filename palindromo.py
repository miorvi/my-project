def palindromo(frase):
    for i in range(0, int(len(frase)/2)):
        if frase[i] != frase[-i-1]:
            return False
        return True
frase = input("escribe una frase, por favor: ").lower()
print(frase, "¿Es un palindromo?", palindromo(frase))
