# Fejezetek

- [Jelenlegi Helyzet](#1-jelenlegi-helyzet)
- [Vágyálom rendszer](#2-vágyálom-rendszer)
- [Jelenlegi üzleti folyamatok](#3-jelenlegi-üzleti-folyamatok)
- [Igényelt üzleti folyamatok](#4-igényelt-üzleti-folyamatok)
- [rendszer szabályok](#5-rendszerre-vonatkozó-szabályok)
- [Követelménylista](#6-követelménylista)

# 1. Jelenlegi helyzet
Az OI bankcsoport egy feltörekvő vállalkozás ami versenyképes kamatokat és nagy fokú biztonságot kínál ügyfelei számára, viszont bankunknak jelenleg nincs megfelelő applikációja ügyintézések lebonyolitására.

Ez nagyban megnehezíti az ügyfelek számára az ügyintézést, hiszen jelenleg füzetben és papíron tarjuk nyilván az ügyfelek banki adatait. Ez a helyzet trathatatlan.

Ennek érdekében készítünk jelenleg egy applikációt, amelynek segítségével a bankunkhoz tartozó ügyfelek online is lebonyolíthatják fontosabb ügyeiket.

Ide tartozik a számlán lévő pénzlekérdezés, a pénzfeltöltés illetve pénzfelvétel.

# 2. Vágyálom rendszer
Vállalkozásunk bővítése érdekében szeretnénk egy applikációt készíteni ami nem csak megkönnyíti az ügyintézést hanem biztonságosabbá is teszi azt.

Elvárt a platformfüggetlenség, nem elfogadható csak Microsoft Windows operációs rendszeren üzemeltethető rendszerre vonatkozó javaslat.

Bankszámlanyitás után egyből regisztrálni lehet az applikációban. Ezután belépés után a felhasználó lekérdezheti a számlán lévő pénzmennyiséget, ezen kívül tölthet fel számlájára és vehet le róla pénzt.

A bank alkalmazottai semmilyen mértékben nem férnek hozzá a felhasználók belépési PIN kódjához, így annak elfelejtése során új PIN kódot kell igényelni.

A csalók elleni védelem érdekében ezt csak személyesen lehet intézni, hiszen PIN kód cseréje csak teljeskörű személyazonosság bizonyítása után lehetséges.

Csalás esetén zárolhatja fiókját addig, míg nem tudja elvégezni a PIN kód cseréjét. Ezt egy telefonhívás keretében is elvégezzük, néhány személyi adat rögzítése után. A fiók tiltásának feloldásához azonban személyes jelenlétre és adategyeztetésre van szükség, amely PIN kód cseréjénél is kötelező, tehát PIN kód cseréjének esetében az adott fiókot azonnal feloldjuk.

# 3. Jelenlegi üzleti folyamatok
-   3.1. Új ügyfél Felvétele a rendszerbe: banki ugyintéző végzi => füzetbe való bejegyzése
-    3.2 Számla nyitás banki ügyintéző végzi => füzetbe való bejegyzése, a kézpénz széfben tárolása a főigazgató hálósoábályában a festmény mögött a kód 1111
-    3.3 Ügyfelek a számlájukon lévő összeget lekérdezése.
-    3.4  Új számla vagy megtakításos számla igénylése -> csak személyesen, papír alapú regisztrálás

# 4. Igényelt üzleti folyamatok
-    4.1. Igényelt funkciók
-    4.1.1. Új számla igénylése után: Regisztráció
-    4.1.2. Ügyfél adatainak elmentése: felhasználónév, PIN kód
-    4.1.3. Applikáción keresztüli pénzlekérdezés
-    4.1.4. Applikációs pénzfelvétel
-    4.1.5. Applikációs pénzfeltöltés

# 5. Rendszerre vonatkozó szabályok
- Az applikácíó pythonban készül.
- A felhasználók adatait tároló applikációk esetében betartandó szabályok betartása a legfőbb prioritás.
- Az egyéni számlákhoz egy alkalmazott sem fér hozzá
- PIN kód elfelejtése során a felhasználónak kötelező PIN kódot cserélnie, amihez személyazonosság bizonyítása szükséges.

# 6. Követelménylista

   |   Modul   |   ID  |   Név |   version |   Kifejtés    |
   |:----------|:------|:------|:----------|:--------------|
   |    Jogosultság |   1   |   Regisztráció    |   1.0 | Felhasználói fiók létrehozása  |
   |    Adatkezelés |   2   |   Adat mentése    |   1.0 |   Regisztrált adatok mentése adatbázisban |
   |   Jogosultság |   3  |    Bejelentkezés   |   1.0 |   A felhasználó a felhasználói nevével illetve PIN kód párossal bejelentkezhet. Ha a felhasználónév illetve a PIN kód páros nem megfelelő, hibaüzenetet kap. |
   |   Felület |   4   |   Balance Check   |   1.0 |   A felhasználó megnézheti a számláján való összeget.|
   |   Jogosultság |   5   |   Pénz Deposit   |   1.0 |   A felhasználó pénzt tölthet fel a számlájára.   |
   |   Jogosultság    |   6   |   Pénz Withdraw   |   1.0 |   A felhasználó pénzt vehet fel.    |

# 7. Fogalomtár
- **Applikáció**: Egy szoftver, amely lehetővé teszi a felhasználók számára, hogy különféle banki tevékenységeket végezzenek online, például pénzügyi tranzakciókat vagy egyenleglekérdezést.
- **Platformfüggetlenség**: A rendszer azon képessége, hogy többféle operációs rendszeren (például Windows, Linux, macOS) egyaránt működjön.
- **Regisztráció**: Az a folyamat, amely során egy új ügyfél létrehozza saját fiókját a banki applikációban, hogy hozzáférjen a szolgáltatásokhoz.
- **PIN kód**: Négyjegyű biztonsági azonosító, amelyet a felhasználók a banki műveleteikhez és a bejelentkezéshez használnak.
- **Balance Check (Pénzlekérdezés)**: Az a funkció, amely lehetővé teszi a felhasználónak, hogy megtekintse az aktuális egyenlegét a számláján.
- **Deposit (Pénzfeltöltés)**: Az a folyamat, amely során a felhasználó pénzt helyez el a bankszámláján az applikáción keresztül.
- **Withdraw (Pénzfelvétel)**: Az a folyamat, amelynek során a felhasználó pénzt vesz fel a bankszámlájáról az applikáció segítségével.
- **Adatbázis**: Az adatbázis egy strukturált adattároló, amely lehetővé teszi adatok rendszerezett, biztonságos és hatékony tárolását, lekérdezését és kezelését (Név, PIN kód, balance).
- **Adatmentés**: Az ügyfél adatainak (például felhasználónév és PIN kód) biztonságos tárolása a rendszerben későbbi felhasználásra.