import random

with open("newfile.txt", mode="r") as file:
    content = file.read()
    words = content.split()
    print(words)
word = random.choice(words)

scrambled_word = "".join(random.sample(word, len(word)))
tentativas = 3


for i in range(tentativas):
    user_word = input(
        f"{scrambled_word} {tentativas} chances para tentar acertar: "
        )
    if user_word == word:
        print("voce acertou")
        break
    else:
        print("tente novamente")
        tentativas -= 1

if user_word not in word:
    print(f"suas tentativas acabaram, a palavra era {word}")
