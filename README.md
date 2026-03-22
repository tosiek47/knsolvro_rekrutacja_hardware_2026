# knsolvro_rekrutacja_hardware_2026
Notatki co do zadań:

## 3. ZADANIE

W symulacji ujętę są 2 rodzaje błędów:
   - losowe
   - ciągłe

Procentowo wypisana jest skuteczność 3 metod:
  - Brak kontroli
  - Kody Hamminga (FAC)
  - Kody Hamminga z przeplotem

W symulacji ująłem, że prawdopodobieństwo wystąpienia błędu losowego wynosi 2%

Brak kontroli został pokazany, aby sprawdzić ile procentowo danych przechodzi bezbłędnie.

Wyniki pokazały, że ~28% pakietów przechodzi bez błędnie. To za mało

Aby temu zapobiec zastosowalem kody Hamminga, które dodają kilka bitów kontrolnych wplątanych w ciąg bitów informacyjnych i potrafią naprawić ciąg bitów jeżeli tylko jeden bit jest błędny. 
W symulacji jest to sprawdzany w ten sposób - jeżeli więcej niż jeden bit jest błędny funkcja zwraca informacje o błędnym przesyłaniu danych.

Ten algorytm nie radzi dobrze sobie z błędami ciągłymi, przez to, że jest często dużo więcej niż 1 bit błędny. 

Ostatnim algorytmem jest wstępne przeplatanie bitów. Zamiast ciągłego A1A2A3... mamy A1B1C1, gdzie litery oznaczają różne paczki, a cyfry kolejne bity. Dzięki temu, jeżeli pojawi się błąd ciągły, to zostanie to rozdzielone pomiędzy paczki. Skutkujące jednym bitem uszkodzonym. (To jest uproszczony model symulacji)

Najlepszym okazał się kod hamminga ze wcześniejszym przeplotem, ponieważ jednocześnie eliminował błędy ciągłe jak i losowe. 


## 4. Zadanie

Obudowa została stworzona w programie fusion 360 na laptopa Lenovo ThinkPad T480. Jest to wierzchnia obudowa zawierająca otwór na kieliszek martini o średnicy 12.5cm (otwór jest delikatnie większy niż sama podstawa kieliszka). Ze względu na zbyt małą podstawę drukarki bambulab carbon x1 podzieliłem tą obudowę na 2 części tak, aby dało się to w prosty sposób złożyć i przymocować (na przykład klejem). Jako materiał wybrałem ASA, ponieważ jest zdecydowanie wystarczający do tego typu projektu pod względem wytrzymałości na temperaturę - obudowa znajduje się na samej górze (tam gdzie jest ekran) więc w okół nie ma zbyt dużego ciepła. Obudowę się wsuwa na górną część laptopa, więc nie trzeba jej odginać w żaden sposób, co też jest istotne przy wybieraniu materiału. Aby nie porysować obudowy laptopa zaprojektowałem 4 wgłębienia na bocznych częściach obudowy, aby włożyć tam kawałki gumy. Zniweluje ona ewentualne poruszanie się obudowy. Załączam zdjęcia z konfiguracji w bambulab studio (rotacja jednego boku wynika z tego, że nie trzeba używać podpórek), 2 pliki .3mf oraz sam plik z fusiona 360 (.f3d)


## 5. Zadanie 

Kufel został wykonany w prorgamie blender. Do samego kufla został stworzony otwieracz do butelek, który ułatwi otwieranie butelek z piwem :)) Do samego zadania załączam 2 zdjęcia z renderu oraz sam plik .blend z kuflem.


