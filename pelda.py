lista = [["alma", 0],
         ["körte", 1],
         ["barack", 0],
         ["szőlő", 1],
         ["dinnye", 1]]

# arra vagyunk kiváncsiak, melyik volt az utolsó áru, amiből 0-át vettünk (azaz nem vettünk belőle.)

nem_vettunk = []
for i in lista:
    if i[1] == 0:
        nem_vettunk = []
        nem_vettunk = [i[0]]
print(nem_vettunk[0])