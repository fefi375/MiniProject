
#  Fejezetek
- [Áttekintés](#áttekintés)
- [Jelenlegi helyzet](#jelenlegi-helyzet)
- [Követelménylista](#követelménylista)
- [Jelenlegi üzleti folyamatok](#igényelt-üzleti-folyamatok-modellje)
- [Igényelt üzleti folyamatok](#igényelt-üzleti-folyamatok-modellje)
- [Használati esetek](#használati-esetek)
- [Megfeleltetés](#megfeleltetés)
- [Képernyőtervek](#képernyőtervek)
- [Forgatókönyv](#forgatókönyv)
- [Funkció](#funkció)



1. ##  Áttekintés

       A célunk egy egyszerűen kezelhető online banki applikáció létrehozása a bankszámlák kezelésének megkönnyítésére. Az applikációt az adott bank bármely ottani bankszámlával rendelkező felhasználó igénybe veheti.

2. ## Jelenlegi helyzet
       Az OI bankcsorpt egy feltörekvő vállalkozás ami versenyképes kamatokat és nagy fokú biztonságot kínál ügyfelei számára. Viszont bankunknak jelenleg nincs megfelelő applikációja ügyintézés lebonyolitására.
       Ez nagyban megnehezíti az ügyfelek számára az ügyintézést ,hiszen jelenleg füzetben és papíron tarjuk nyilván az ügyfelek banki adatait. Ez a helyzet trathatatlan.
        
3. ## Követelménylista


   |   Modul   |   ID  |   Név |   version |   Kifejtés    |
   |:----------|:------|:------|:----------|:--------------|
   |    Jogosultság |   1   |   Regisztráció    |   1.0 | Felhasználói fiók létrehozása  |
   |    Jogosultság |   2   |   Adat mentése    |   1.0 |   Regisztrált adatok mentése JSON file-ba |
   |   Jogosultság |   3  |    Bejelentkezés   |   1.0 |   A felhasználó a felhasználói nevével illetve PIN kód párossal bejelentkezhet. Ha a felhasználónév illetve a PIN kód páros nem megfelelő, hibaüzenetet kap. |
   |   Felület |   4   |   Balance Check   |   1.0 |   A felhasználó megnézheti a számláján való összeget.|
   |   Jogosultság |   5   |   Pénz Deposit   |   1.0 |   A felhasználó pénzt tölthet fel a számlájára.   |
   |   Jogosultság    |   6   |   Pénz Withdraw   |   1.0 |   A felhasználó pénzt vehet fel.    |


4. ## Jelenlegi üzleti folyamatok modellje
   - 3.1. Új ugyfél Felvétele a rendszerbe: banki ugyintéző végzi => füzetbe való bejegyzése
   - 3.2 Számla nyitás banki ugyintéző végzi => füzetbe való bejegyzése, a kézpénz széfben tárolása a főigazgató hálósoábályában a festmény mögött a kód 1111
   - 3.3 Ügyfelek a számlájukon lévő összeget lekérdezése.
   - 3.4  Új számla vagy megtakításos számla igénylése -> csak személyesen, papír alapú regisztrálás
5. ## Igényelt üzleti folyamatok modellje
   - 4.1. Online megjelenés
   - 4.1.1. Ügyfél felvitele az adatbázisba: felhasználónév, jelszó felvétele az adatbázisba
   - 4.1.2. Új számla igénylése: regisztrált felhasználói belépés => "Új számla fül" 
6. ## Használati esetek
       Világszerte bármely bankcsoport hasznára lehet felhasználók nyílvántartására és tranzakciók lebonyolítására.
       Az ügyfelek számára magas fokú kényelmet biztosít hiszen mobil eszközükről bárhonnan intézhetik banki ügyeiket
       mint a pénz feltöltés számlára, pénz felvétele számláról valamint számlán lévő összeg lekérdezése.
      
7. ## Megfeleltetés

8. ## Képernyőtervek

9. ## Forgatókönyv

       A felhasználó számlanyitás után, esetleg számlanyitás közben egyből regisztrálhat a felületen. Bejelentkezést követően
       hozzájut saját bankszámlaadataihoz, beleértve számlaszámát és a számlán lévő pénzösszeg mennyiségét. Számlájára nyomva
       elérheti a pénzátutalás illetve pénzfelvételhez való kódgenerálást.
    

10. ## Funkció
       - Új fiók létrehozása amit egy JSON fájlba ment az applikáció ezzel megőrizve a fiókokat programfuttatások között
       - Fiók létrehozásakor a program odafigyel hogy pin codenak csakis 4 számjegyet fogadjon el ezeket beiráskor * karakter mögé relyti ezzel is védve a pin code titkosságát
       - Fiók létrehozása után automatikusan bejelentkezteti az applikáció és előhozza a menüt ami lehetővé teszi a felhasználó számára a további funkciók elérését.
       - Pénz felvételt tesz lehetővé az applikáció, egy összeget kér be ha az összeg tobb mint a számlán lévő összeg akkor figyelmezteti afelhasználót, ha az összeg megfelelő akkor azt leveszi a számláról.
       - Pénz feltöltésére is képes, szintén egy összget kér be amit azután hozzáad a jelenlegi számlán lévő összeghez.
       - Összeg lekérdezése opció pedig megjeleníti a jelenleg számlán lévő összeget.
       - Végül a bejelentkezett felhasználónak lehetősége van kijelentkezni ami a kezdő menube viszi ahonna fiókot lehet létrehozni vagy bejelentkezni másik fiókba.