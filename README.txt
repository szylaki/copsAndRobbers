krótki opis silnika:
1. W pliku cops_thief_main uruchamia cały kod.
2. W pliku cops_thief_threads opisane są klasy policjantów oraz wątki.
3. Kolejne pliki cops_algorithm oraz thief_algorithm zawierają klasy planowania ruchów.
Funkcja algorithm jest dla was, pętla for (po k iteracjach) musą wykonywać się oblliczenia ruchu
i od razu podstawie go do listy ruchów.
4. W przypadku obliczeń dłuższych niż 500ms funkcja przerywa swoje działanie 
5. Dla obliczeń wykorzystujecie stan planszy w poprzednich ruchach. Jest to lista pod nazwą 
worlds_list_copy. Jej elemenyty są macierzami, bo plansza to macierz. Oznaczenie poszczególnych 
elementów:
fence 1
gates 2
walls 3
thief 4
cops 5 
cop's range 6
6. Na furtki może nachodzić tylko złodziej. W razie trafienia do lapek policjanta, 
złodziej przegrywa.
7. W razie zaplanowanego ruchu dla obydwu stron, który wymaga najście na ścianę, 
ruch nie zostanie wykonany.  

Na kolejnych zajęciach będzie uruchamiany silnik z różnywi plikami 
cops_algorithm oraz thief_algorithm, co są wysłane przez was wcześniej w wiadomości prywatnej.
 
