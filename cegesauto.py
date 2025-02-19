# print("1. feladat")
autok = []
# autok_dict = []
with open("autok.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egyauto = egysor.strip().split(" ")
        autok.append([int(egyauto[0]), str(egyauto[1]), str(egyauto[2]), int(egyauto[3]),
                      int(egyauto[4]), int(egyauto[5])])
        # autok_dict.append({"nap": int(egyauto[0]), "idő": str(egyauto[1])})

print(autok)

print("2.1. feladat ")
i = len(autok) - 1  # összelemszám [293]
while autok[i][5] == 1:
    i -= 1
print(f"{autok[i][0]}. nap rendszám: {autok[i][2]}")
