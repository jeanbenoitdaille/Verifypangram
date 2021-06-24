import string
     
phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phrase_lower = phrase.lower()
     
alphabet = list(string.ascii_lowercase)
     
for l in phrase_lower:
        if l in alphabet:
            alphabet.remove(l)
     
if alphabet:
        print("La phrase n'est pas un Pangramme")
else:
        print("La phrase est un Pangramme")