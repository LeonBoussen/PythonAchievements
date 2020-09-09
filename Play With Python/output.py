Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
3 * 10
100 - 10
25 / 5
10 / 3
10 // 3
SyntaxError: multiple statements found while compiling a single statement
>>> 2 + 2
4
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 25 / 5
5.0
>>> 10 // 3
3
>>> print('Mijn naam is Leon')
Mijn naam is Leon
>>> naam = 'Leon'
>>> print(naam)
Leon
>>> print(naam.upper())
LEON
>>> print(naam[0:2])
Le
>>> print(naam[::-1])
noeL
>>> leeftijd = 17
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Leon ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 1 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
945
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
603
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 603
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 12:05:36.667182
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 09 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'mercoledì 09 settembre 2020'
>>> 