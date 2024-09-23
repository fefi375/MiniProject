# Fejezetek

- [Jelenlegi Helyzet](#1-jelenlegi-helyzet)
- [Vágyálom rendszer](#2-vágyálom-rendszer)
- [Jelenlegi üzleti folyamatok](#3-jelenlegi-üzleti-folyamatok)
- [Igényelt üzleti folyamatok](#4-igényelt-üzleti-folyamatok)
- [rendszer szabályok](#5-rendszerre-vonatkozó-szabályok)
- [Követelménylista](#6-követelménylista)

## 1. Jelenlegi helyzet
    Az OI bankcsorpt egy feltörekvő vállalkozás ami versenyképes kamatokat és nagy fokú biztonságot kínál ügyfelei számára.
    Viszont bankunknak jelenleg nincs megfelelő applikációja ügyintézés lebonyolitására.
    Ez nagyban megnehezíti az ügyfelek számára az ügyintézést ,hiszen jelenleg füzetben és papíron tarjuk nyilván az ügyfelek
    banki adatait. Ez a helyzet trathatatlan.

## 2. Vágyálom rendszer
    Vállalkozásunk bővítése érdekében szeretnénk egy telefonos applikációt készíteni ami nem csak megkönnyíti az ügyintézést
    hanem biztonságosabbá is teszi azt. Elvárt a platformfüggetlenség, nem elfogadható csak Microsoft Windows operációs rendszeren
    üzemeltethető rendszerre vonatkozó javaslat. Az online megjenés lehetőleg mobil telefonon, tableten is működjön, reszponzív felülettel.

## 3. Jelenlegi üzleti folyamatok
-   3.1. Új ugyfél Felvétele a rendszerbe: banki ugyintéző végzi => füzetbe való bejegyzése
-    3.2 Számla nyitás banki ugyintéző végzi => füzetbe való bejegyzése, a kézpénz széfben tárolása a főigazgató hálósoábályában a
    festmény mögött a kód 1111
-    3.3 Ügyfelek a számlájukon lévő összeget lekérdezése.
-    3.4  Új számla vagy megtakításos számla igénylése -> csak személyesen, papír alapú regisztrálás

## 4. Igényelt üzleti folyamatok
-    4.1. Online megjelenés
-    4.1.1. Ügyfél felvitele az adatbázisba: felhasználónév, jelszó felvétele az adatbázisba
-    4.1.2. Új számla igénylése: regisztrált felhasználói belépés => "Új számla fül" 

## 5. Rendszerre vonatkozó szabályok
    Az applikácíó pythonban készül. A felhasználók adatait tároló applikációk esetében betartandó szabályok betartása a legfőbb
    prioritás.

## 6. Követelménylista

   |   Modul   |   ID  |   Név |   version |   Kifejtés    |
   |:----------|:------|:------|:----------|:--------------|
   |    Jogosultság |   1   |   Regisztráció    |   1.0 | Felhasználói fiók létrehozása  |
   |    Jogosultság |   2   |   Adat mentése    |   1.0 |   Regisztrált adatok mentése JSON file-ba |
   |   Jogosultság |   3  |    Bejelentkezés   |   1.0 |   A felhasználó a felhasználói nevével illetve PIN kód párossal bejelentkezhet. Ha a felhasználónév illetve a PIN kód páros nem megfelelő, hibaüzenetet kap. |
   |   Felület |   4   |   Balance Check   |   1.0 |   A felhasználó megnézheti a számláján való összeget.|
   |   Jogosultság |   5   |   Pénz Deposit   |   1.0 |   A felhasználó pénzt tölthet fel a számlájára.   |
   |   Jogosultság    |   6   |   Pénz Withdraw   |   1.0 |   A felhasználó pénzt vehet fel.    |
