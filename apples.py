import math
import time

trees = 333
print("total amount of trees are 333 but 2/3 are in the shadow of the mountain.")
time.sleep(2)
print("Because of that the 2/3 will preduce only 80% of normaal amount."'\n')
time.sleep(2)


suntrees = trees / 3; 
shadowtrees = suntrees * 2;

sunapples = 146
shadowapples = 146 / 10 * 8

print('\n'"The amount of trees in the sun are",suntrees, "and the amount of trees in the shadows are", shadowtrees,".")
time.sleep(2)
print('\n''\n')
print("A tree in the sun will give 146 apples, but trees in the shadows give 80% of the normal amount.")
print("the amount of apples the shadowtrees gives are", shadowapples,".")
print('\n''\n')
print("Lets calculate how many apples we get in total")

sunapplesAm = suntrees * sunapples;
shadowapplesAm = shadowtrees * shadowapples;
totalapplesAm = sunapplesAm + shadowapplesAm;

print("Trees in the sun x full amount of apples = total sunny tree apples.")
time.sleep(1)
print(suntrees,"x",sunapples,"=",sunapplesAm)
time.sleep(2)
print("Trees in the shadow x 80% of full amount of apples = total shadow tree apples.")
time.sleep(1)
print(shadowtrees,"x",shadowapples,"=",shadowapplesAm)
time.sleep(2)
print('\n''\n')
print("total sunny tree apples + total shadow tree apples = total amount of apples.")
time.sleep(1)
print(sunapplesAm,"+",shadowapplesAm,"=",totalapplesAm)
time.sleep(2)

applesperperson = totalapplesAm / 4 - 0.9;

print('\n''\n')
print("But all the trees are from me and 3 other friends, so we have to share them equally.")
time.sleep(1)
print("that would mean total amount of apples : 4.")
time.sleep(1)
print(totalapplesAm,":""4""=",applesperperson)
time.sleep(2)

print('\n''\n')
print("So we all have",applesperperson,"to sell")
time.sleep(5)




