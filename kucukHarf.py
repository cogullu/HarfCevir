#Tümünü Küçük veya büyük harflere çeviren program.

buyukAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
kucukAlfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

def kucukHarfCevir(text:str):
    newText = str()
    for i in text:
        if i in buyukAlfabe:
            index = buyukAlfabe.index(i)
            newText += kucukAlfabe[index]
        else:
            newText += i

    return newText

def buyukHarfCevir(text:str):
    newText = str()
    for i in text:
        if i in kucukAlfabe:
            index = kucukAlfabe.index(i)
            newText += buyukAlfabe[index]
        else:
            newText += i

    return newText