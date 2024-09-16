
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

<br>

1. ##  Áttekintés<br>

       A célunk egy egyszerűen kezelhető online banki applikáció létrehozása a bankszámlák kezelésének megkönnyítésére. Az applikációt az adott bank bármely ottani bankszámlával rendelkező felhasználó igénybe veheti.

2. ## Jelenlegi helyzet<br>
       Az OI bankcsorpt egy feltörekvő vállalkozás ami versenyképes kamatokat és nagy fokú biztonságot kínál ügyfelei számára. Viszont bankunknak jelenleg nincs megfelelő applikációja ügyintézés lebonyolitására.
       Ez nagyban megnehezíti az ügyfelek számára az ügyintézést ,hiszen jelenleg füzetben és papíron tarjuk nyilván az ügyfelek banki adatait. Ez a helyzet trathatatlan.
        
3. ## Követelménylista<br>


    |   Modul   |   ID  |   Név |   version |   Kifejtés    |
    |:----------|:------|:------|:----------|:--------------|
    |   Jogosultság |   1  |    Bejelentkezés   |   1.0 |   A felhasználó az email címe illetve jelszó párossal bejelentkezhet. Ha az email és jelszó páros nem megfelelő, hibaüzenetet kap. |
    |   Jogosultság    |   2   |   PIN Recovery    |   1.0 |   A felhasználó elfelejtett PIN kód esetén lekérdezheti a PIN kódját. |
    |   Felület |   3   |   Balance Check   |   1.0 |   A felhasználó megnézheti a számláján való összeget.|
    |   Jogosultság |   4   |   Pénz Transfer   |   1.0 |   A felhasználó online pénzt utalhat más számlákra.   |
    |   Jogosultság    |   5   |   Pénz Withdraw   |   1.0 |   A felhasználó kikérhet egy kódot, ami megkönnyíti a pénzfelvételt a banki ATM-eknél.    |
    |   Felület |   6   |   Betéti kamatláb  |   1.0 |---|
    |   Felület |   7   |   Kamatos kamat számítás  |   1.0 |---|


<br>

4. ## Jelenlegi üzleti folyamatok modellje
       3.1. Új ugyfél Felvétele a rendszerbe: banki ugyintéző végzi => füzetbe való bejegyzése
       3.2 Számla nyitás banki ugyintéző végzi => füzetbe való bejegyzése, a kézpénz széfben tárolása a főigazgató hálósoábályában a festmény mögött a kód 1111
       3.3 Ügyfelek a számlájukon lévő összeget lekérdezése.
       3.4  Új számla vagy megtakításos számla igénylése -> csak személyesen, papír      alapú regisztrálás
5. ## Igényelt üzleti folyamatok modellje
       4.1. Online megjelenés
       4.1.1. Ügyfél felvitele az adatbázisba: felhasználónév, jelszó felvétele az adatbázisba
       4.1.2. Új számla igénylése: regisztrált felhasználói belépés => "Új számla fül" 
6. ## Használati esetek

7. ## Megfeleltetés

8. ## Képernyőtervek

9. ## Forgatókönyv

       A felhasználó számlanyitás után, esetleg számlanyitás közben egyből regisztrálhat a felületen. Bejelentkezést követően hozzájut saját bankszámlaadataihoz, beleértve számlaszámát és a számlán lévő pénzösszeg mennyiségét. Számlájára nyomva elérheti a pénzátutalás illetve pénzfelvételhez való kódgenerálást.
    

10. ## Funkció