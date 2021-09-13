http://plan.elektronik.edu.pl/lista.html - lista klas i nauczycieli oraz sali

http://plan.elektronik.edu.pl/plany/oX.html - plan danej klasy

http://plan.elektronik.edu.pl/plany/nX.html - plan danej nauczyciela

http://plan.elektronik.edu.pl/plany/sX.html - plan danej sali

Scrapper zawsze uzyskuje pełny zestaw informacji, można jedynie ograniczyć dane wyjściowe

Dostępne funkcje: 
 - query(query, data)
   Zwraca plan dla danego zapytania, z uzględnieniem filtru (data)
 - href_list()
   Zwraca listę linków pod którymy znajdują się plany, klas, nauczycieli, sal
 - text_list()
   Zwraca listę nazw klas, nauczycieli, sal
 - text2href()
   Zwraca scieżkę po domenie na której znajduje się dany plan

   Aby ograniczyć potrzebę aktualizacji Scrapper'a w przypadku dodania nowej klasy sali lub nauczyciela
   pobieram listę linków oraz nazw sali, każda nazwa sali posiada swój link pod tym samym indeksem na liście linków.
   
   Sale zawierające polskie znaki generowały błędy dlatego posłużyłem się zewnętrzną biblioteką ftfy do naprawienia wadliwych znaków.
   
   - pprint w apitest.py jest opcjonalny, zwiększa czytelność list.
   - requests słyży do komunikacji z planem zajęć przez HTTP.
   - pandas jest używane do odczytania tabeli.
   - BeautifulSoup4 pomaga odczytać listę klas, nauczycieli lub sali.

## Instalacja (linux)

```console
# Sklonuj Repozytoria
$ git clone https://github.com/100Daisy/plan_scrapper.git

# Otwórz Katalog
$ cd plan_scrapper

# Zainstaluj zależności
$ python3 -m pip install -r requirements.txt
```
