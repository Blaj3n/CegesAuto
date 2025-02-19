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

print("2.2. feladat ")
for egyelem in autok:
    if egyelem[-1] == 0:
        utolso_kihajtas = []
        utolso_kihajtas = [egyelem[0], egyelem[2]]
print(f"{utolso_kihajtas[0]}. nap rendszám: {utolso_kihajtas[1]}")

"""
végig megyünk a 'autok' listánkon, és ha találunk egy kihajtó kocsit,
akkor belehelyezzük a listánkba a kért adatokat [nap, rendszám].
Miután minden egyes ciklusban a listánk frissül, ezért a legutolsó kihajtáskor
a kért adataink lesznek benne, amit kiprintelhetünk.
"""

print("2.3. feladat ")
kihajtas = []
for egyelem in autok:
    if egyelem[-1] == 0:
        kihajtas.append(egyelem)
print(kihajtas)
print(f"{kihajtas[-1][0]}. nap rendszám: {kihajtas[len(kihajtas)-1][2]}")

print("3. feladat ")
nap = 4 #int(input("Nap: "))
print(f"Forgalom a(z) {nap}. napon: ")
for auto in autok:
    if auto[0] == nap:
        print(f"{auto[1]} {auto[2]} {auto[3]}", end=" ")
        if auto[5] == 0:
            print("ki")
        else:
            print("be")

print("4. feladat ")
auto_kint = 0
osszes_auto = []
for auto in autok:
    if auto[2] not in osszes_auto:
        osszes_auto.append(auto[2])

print(osszes_auto)
for kocsi in osszes_auto:
    kocsik = []
    for auto in autok:
        if auto[2] == kocsi:
            kocsik.append(auto[5])
    print(kocsik)
    if len(kocsik) % 2 == 1:
        auto_kint += 1
print(f"A hónap végén {auto_kint} autót nem hoztak vissza.")

print("5. feladat")
for kocsi in sorted(osszes_auto):
    kilometerek = []
    for auto in autok:
        if auto[2] == kocsi:
            kilometerek.append(auto[4])
    megtett_km = kilometerek[-1] - kilometerek[0]
    print(f"{kocsi} {megtett_km} km ")

print("6. feladat")
szemelyek = []
for auto in autok:
    if auto[3] not in szemelyek:
        szemelyek.append(auto[3])
print(sorted(szemelyek))

megtett_kilometer = []
for szemely in sorted(szemelyek):
    szemelyenkent_kilometer = []
    for auto in autok:
        if szemely == auto[3]:
            szemelyenkent_kilometer.append(auto[4])
    megtett_kilometer.append(szemelyenkent_kilometer)
print(megtett_kilometer)
# HÁZI: Ugye a leghosszabb utat akarjuk megnézni, tehát a páratlan indexü elemből kivonjuk az az előttit.
# 500 -> 25945 - 25385 = 560
# [[560], []] -> range(kezdő, vég-1, 2)