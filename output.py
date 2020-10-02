Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Evert Olsthoorn')
Mijn naam is Evert Olsthoorn
>>> naam = 'Evert Olsthoorn'
>>> print(naam)
Evert Olsthoorn
>>> print(naam.upper())
EVERT OLSTHOORN
>>> print(naam[0:2])
Ev
>>> print(naam[::-1])
nroohtslO trevE
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Evert Olsthoorn ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')

Over 2 jaar wordt je 18
>>> elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')

SyntaxError: invalid syntax
>>> elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
    
SyntaxError: invalid syntax
>>> else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
NameError: name 'hoelang_al18jaar' is not defined
>>> hoelang_al18jaar = leeftijd - 18
>>> print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
Het is alweer -2 jaar geleden dat je 18 werd ;-)
>>> else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> else: print('Je bent precies ' + str(leeftijd) + ' jaar')
SyntaxError: invalid syntax
>>> else: print('Je bent precies ' + str(leeftijd) + ' jaar')
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> print('boe')
boe
>>> elif leeftijd>18:
	
SyntaxError: invalid syntax
>>> if leeftijd <18:
	hoeland_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoeland_tot18jaar) + ' jaar wordt je 18')

	
Over 2 jaar wordt je 18
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 2 jaar wordt je 18
>>> 
>>> from random import randint
>>> randint(0,1000)
109
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
143
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

Willekeurig getal tussen 0 en 1000: 143
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-11 13:12:45.182910
>>> datum.strftime('%A %d %B %Y')
'Friday 11 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> atum.strftime('%A %d %B %Y')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    atum.strftime('%A %d %B %Y')
NameError: name 'atum' is not defined
>>> datum.strftime('%A %d %B %Y')
'vrijdag 11 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 11 settembre 2020'
>>> 