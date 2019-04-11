Robot Emil sa veľmi sa podobá na robota Karla:

robot sa pohybuje v štvorcovej sieti, v ktorej sa môžu na niektorých políčkach nachádzať prekážky a na niektorých iných zase nejaké predmety s písmenami
robot sa pohybuje v jednom zo štyroch smerov vždy až po najbližšiu prekážku, resp. okraj plochy, pri svojom pohybe vyzbiera všetky predmety z políčok cez ktoré prejde, smery určujeme písmenami:

v = pohybuje sa v smere na východ
j = pohybuje sa v smere na juh
z = pohybuje sa v smere na západ
s = pohybuje sa v smere na sever


__init__(meno_suboru, pozicia):
prečíta textový súbor a vytvorí hraciu plochu pre robota; súbor v prvom riadku obsahuje dve celé čísla - rozmer plochy a v každom ďalšom je trojica: znak riadok stĺpec, znak 'M' označuje prekážku, malé písmená označujú predmety, ktoré bude Emil zbierať, ostatné políčka sú pre Emila voľné
parameter pozicia je dvojica celých čísel: riadok a stĺpec pozície robota v ploche (táto pozícia je voľné políčko - bez predmetu a prekážky)

__str__():
vráti znakový reťazec - reprezentáciu plochy Emila: prázdne políčka znakom '.', pozícia robota znakom 'E'

rob(prikazy):
vykoná postupnosť príkazov - vždy ide daným smerom, kým sa dá
'v' - pôjde na východ
'j' - pôjde na juh
'z' - pôjde na západ
's' - pôjde na sever
iné písmená ignoruje
vráti počet zozbieraných predmetov touto postupnosťou príkazov

co_pozbieral()
vráti zoznam (list) zozbieraných predmetov (malé písmená) v poradí, v ktorom ich zbieral
