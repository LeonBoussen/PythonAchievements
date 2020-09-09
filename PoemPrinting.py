
vers0 = " Ik weet, \n wat ik denk."
vers1 = " maar ik denk niet, \n wat ik diep van binnen weet."
vers2 = " Ik maak de gekste dingen mee, \n maar meestal negatief, \n waarom ik?"
vers3 = " Iedereen lijkt, \n mij beter te kennen"
vers4 = " ben ik een vreemde in mijn lichaam, \n of ben ik niet ik?"
vers5 = " Kloppen de gedachte maar het lichaam niet, \n of andersom?"
vers6 = " Helaas, \n ik weet het niet."
vers7 = " Ik krijg mijn hoofd niet op orde er raast zoveel doorheen, \n net als alle pijnen bijeen."
vers8 = " Het wil niet weg het blijft daar maar, \n dat is niet zo raar."
vers9 = " Al die gedachten over plezier en pijn, \n dat is niet fijn."
vers10 = " Ben ik iemand in een vreemd lichaam, \n of kijk ik mee vanuit mijn lichaam, \n naar iets wat een ander doet?"
vers11 = " Denk ik en voel ik, \n wat een ander in mijn lichaam ook doet?"
vers12 = " Het lijkt alsof ik bestuurd word naar iets, \n door iemand dat ik niet wil."
vers13 = " Alsof ik het zelf meemaak, \n maar niet weet wat er mis is."
vers14 = " Word ik bestuurd naar iets dat ik niet ken, \n niet weet en nooit zal kennen."
vers15 = " Werkelijk wie, \n of wat ben ik?"
vers16 = " Een Poem van Vera Zandvliet"

import sys
import time

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Wie Ben Ik', font='doom'),
       'green', 'on_blue', attrs=['bold'])


print(" 'Wie Ben Ik' Poem", '\n')  
time.sleep(2)
print(vers0, '\n')
time.sleep(2.5)
print(vers1, '\n')
time.sleep(2.5)
print(vers2, '\n')
time.sleep(2.5)
print(vers3, '\n')
time.sleep(2.5)
print(vers4, '\n')
time.sleep(2.5)
print(vers5, '\n')
time.sleep(2.5)
print(vers6, '\n')
time.sleep(2.5)
print(vers7, '\n')
time.sleep(2.5)
print(vers8, '\n')
time.sleep(2.5)
print(vers9, '\n')
time.sleep(2.5)
print(vers10, '\n')
time.sleep(2.5)
print(vers11, '\n')
time.sleep(2.5)
print(vers12, '\n')
time.sleep(2.5)
print(vers13, '\n')
time.sleep(2.5)
print(vers14, '\n')
time.sleep(2.5)
print(vers15, '\n')
time.sleep(5)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print(vers16,'\n')
time.sleep(3)
exit()