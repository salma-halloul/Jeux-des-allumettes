from math import *
from random import *

allumettes=[i for i in range(20)]
print("l"*len(allumettes))

while len(allumettes)>1:
 sub=int(input("Choisir un nombre entre 1 et 3:"))
 for i in range(sub):
  allumettes.remove(allumettes[-1])
 print("l"*len(allumettes))
 if len(allumettes)==1:
  print("Vous avez gagne")
 else:
  ia=randint(1,3 if len(allumettes)>3 else len(allumettes)-1)
  print("L'ordinateur enleve",ia)
  for i in range(ia):
   allumettes.remove(allumettes[-1])
  print("l"*len(allumettes))
 if len(allumettes)==1:
  print("Vous avez perdu !")