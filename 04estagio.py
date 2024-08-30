#Desafio 04

estSP = 67836.43
estRJ = 36678.66
estMG = 29229.88
estES = 27165.48
outros = 19849.53

somaTotal = estSP+estRJ+estMG+estES+outros

percSP = (estSP*100)/somaTotal
print(f"SP - {percSP:.2f}%\n")

percRJ = (estRJ*100)/somaTotal
print(f"RJ - {percRJ:.2f}%\n")

percMG = (estMG*100)/somaTotal
print(f"MG - {percMG:.2f}%\n")

percES = (estES*100)/somaTotal
print(f"ES - {percES:.2f}%\n")

percOutrosEstados = (outros*100)/somaTotal
print(f"Outros Estados - {percOutrosEstados:.2f}%\n")

