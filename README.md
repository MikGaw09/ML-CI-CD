# NTPD6

# Zadanie 1
Po wrzuceniu kodu z poprzednich zajęć, stworzyłem plik test.py stworzony w technologii pytest. Jego zadaniem będzie testowanie poprawności predykcji modelu za każdym razem gdy do repozytorium na gałęzi main zostanie dodany commit.
<img width="1018" height="769" alt="image" src="https://github.com/user-attachments/assets/bf075979-8fdb-4c0b-9c99-8038172f42b8" />

# Zadanie 2
Zadanie polegało na stworzeniu workflow które będzie uruchamiało się przy pushu lub pullu na main. musi ono również instalować plik z zależnościami(do którego należało dodać biblioteke pytest) oraz uruchomi skrypt z testami test.py. Wynik tego workflow jest widoczny po wejściu w zakładkę "Actions" gdzie widać jak przebiegają kolejne etapy ustawione w pliku yaml.
<img width="555" height="572" alt="image" src="https://github.com/user-attachments/assets/c1d3115b-da8c-4dc9-96a9-82186d155ffe" />
<img width="656" height="331" alt="image" src="https://github.com/user-attachments/assets/09cc3ba7-579b-46f1-92e6-34c1beb9a789" />


# Zadanie 3
Rozbudowa pliku main.yml. Poza uruchamianiem testów wdrożono tworzenie kontenera z aplikacją oraz publikował go. Do publikacji wykorzystałem Github Container Registry. Po utworzeniu tego pliku okazało się że korzystając z tej technologii, nazwa mojego repozytorium(będąca moją etykietą) jest niedozwolona, ponieważ zawiera w sobie duże litery. 
<img width="488" height="379" alt="image" src="https://github.com/user-attachments/assets/a564cc20-f3e6-4bf5-9573-647ce95cb064" />
Wynik Poprawionego workflow
<img width="654" height="406" alt="image" src="https://github.com/user-attachments/assets/e95f2502-8f90-4d67-9901-142f591ab849" />
Sekcja Packages
<img width="630" height="117" alt="image" src="https://github.com/user-attachments/assets/568533dd-9e4a-48de-b89b-21e710d43e51" />
