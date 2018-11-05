import random
slowa = ("python", 'ziom', "dlaczego", "ziomeczek", "dom")
word = random.choice(slowa)
print(word)
poprawnie = word
pomie = ""
while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position + 1):]
print(pomie)
