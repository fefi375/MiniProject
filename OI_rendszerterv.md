# Fejezetek
- [Rendszer célja](#1-rendszer-célja)
- [Projektterv](#2-projektterv)
- [Üzleti folyamatok modellje](#3-üzleti-folyamatok-modellje)
- [Követelmények](#4-követelmények)
- [Funkcionális terv](#5-funkcionális-terv)
- [Fizikai környezet](#6-fizikai-környezet)
- [Architekturális terv](#7-architekturális-terv)
- [Implementációs terv](#8-implementációs-terv)
- [Tesztterv](#9-tesztterv)
- [Telepítési terv](#10-telepítési-terv)
- [Karbantartási terv](#11-karbantartási-terv)


# 1. Rendszer célja
- A banki applikáció célja egy egyszerű, Python nyelven fejlesztett asztali alkalmazás biztosítása.<br>
- Az alkalmazás lehetővé teszi a felhasználók számára bankszámlájuk hatékony kezelését.<br>
- A rendszer alapvető funkciói közé tartozik a felhasználói regisztráció, belépés, egyenleglekérdezés.<br>
- A felhasználók pénzfelvételt (withdraw) és pénzbefizetést (deposit) is végezhetnek az applikációban.<br>
- A regisztráció során meg kell adni a felhasználó nevét, PIN kódját és az alap egyenleget.<br>
- A regisztrált felhasználói adatok JSON fájlban kerülnek tárolásra.<br>
- Ez a megoldás megkönnyíti az adatkezelést és egy egyszerű fájlstruktúrát biztosít.<br>
- A cél az, hogy a felhasználók könnyen hozzáférhessenek pénzügyi információikhoz.<br>
- Ezen kívül biztonságosan tudják kezelni számlájukat a rendszer segítségével.<br>

# 2. Projektterv
- A projekt során egy asztali alkalmazást fejlesztünk Python nyelven.<br>
- Az alkalmazás minimális külső függőségekkel rendelkezik.<br>
- A fejlesztés három fő fázisra oszlik: tervezés, implementáció és tesztelés.<br>
- A tervezési szakasz során a felhasználói igények azonosítása a cél.<br>
- Az implementáció során a funkciók valódi megvalósítása történik.<br>
- A tesztelés során biztosítjuk, hogy a rendszer megfelelően működjön.<br>
- A fejlesztési folyamatot agilis szemlélettel kezeljük.<br>
- Rövid iterációkban dolgozunk, hogy rugalmasan alkalmazkodjunk az igényekhez.<br>
- Az adatok kezelése egyszerű JSON fájlokkal történik.<br>
- Ez lehetővé teszi az egyszerű regisztrációt és a felhasználói adatkezelést.<br>
- A projekt tervezett időtartama 3 hét, figyelembe véve az időlimitációkat.<br>
- Folyamatosan teszteljük és fejlesztjük a funkciókat a projekt során.<br>

# 3. Üzleti folyamatok modellje
Az alkalmazás fő üzleti folyamatai a következők:
1. Felhasználói regisztráció:
    - A felhasználó megadja a szükséges adatokat.
    - A szükséges adatok közé tartozik a név, e-mail cím, és PIN kód.
    - Ezek az adatok egy JSON fájlba kerülnek mentésre a rendszerben.
2. Bejelentkezés:
    - A felhasználó a regisztrált e-mail címével és jelszavával tud belépni.
    - A rendszer a JSON fájlban tárolt adatokat ellenőrzi a bejelentkezés során.
3. Egyenleg lekérdezés:
    - A felhasználó lekérheti a számlaegyenlegét.
    - Ez az egyenleg egy egyszerű számként van tárolva, és frissül a tranzakciók során.
4. Pénzfelvétel (Withdraw):
    - A felhasználó megad egy összeget.
    - Ezt az összeget le szeretné venni a számlájáról.
    - Ha elegendő egyenlege van, az összeg levonásra kerül a számláról.
5. Pénzbefizetés (Deposit):
    - A felhasználó megadhat egy összeget, amelyet szeretne befizetni.
    - Ez az összeg növeli a számla egyenlegét a tranzakció során.

# 4. Követelmények
1. Python környezet:
    - A rendszer Python 3.8+ verziót igényel.
2. Adatkezelés:
    - A felhasználói adatok JSON fájlban tárolódnak, amely gyors és egyszerű hozzáférést biztosít a program számára.
3. Felhasználói hitelesítés:
    - A rendszernek biztonságosan kell kezelnie a felhasználói bejelentkezéseket, PIN kód hashelésével.
4. Adatvédelmi követelmények:
    - A funkciók elérhetősége kulcsfontosságú, és minden esetben megfelelően kell működniük.
    - A felhasználói regisztráció, belépés, egyenleglekérdezés, pénzfelvétel és befizetés funkciók kulcsfontosságúak.
5. Funkciók elérhetősége:
    - A felhasználói regisztráció, belépés, egyenleglekérdezés, pénzfelvétel és befizetés funkcióknak minden esetben megfelelően kell működniük.
6. Könnyű kezelhetőség:
    - Az alkalmazásnak felhasználóbarátnak és intuitívnak kell lennie.

# 5. Funkcionális terv
1. Felhasználói regisztráció:
    - A felhasználó megadja nevét és PIN kódját majd a rendszer validálja az adatokat, és JSON fájlban tárolja őket.
2. Bejelentkezés:
    - A felhasználó a regisztrált név(first_name last_name) és PIN kód párosával lép be az alkalmazásba.
    - A rendszer ellenőrzi a JSON fájlban tárolt adatokat, és hitelesíti a felhasználót.
3. Egyenleg lekérdezés:
    - A felhasználó egy gombnyomás segítségével lekérheti az aktuális számlaegyenlegét, amely a JSON fájlból kerül beolvasásra.
4. Withdraw (pénzfelvétel):
    - A felhasználó megadja, mekkora összeget szeretne felvenni. A rendszer ellenőrzi, hogy van-e elegendő egyenleg, majd levonja a megfelelő összeget.
5. Deposit (pénzbefizetés):
    - A felhasználó megadja a befizetni kívánt összeget, amely növeli a számla egyenlegét.

# 6. Fizikai környezet
- A rendszer egy Python környezetben futó asztali alkalmazás.<br>
- Bármilyen operációs rendszeren lehet futtatni, amely támogatja a Python-t.<br>
- Nincs szükség külső szerverekre vagy adatbázisokra, mivel az adatok JSON fájlokban tárolódnak helyben a felhasználó gépén.<br>
- A program minimális rendszerkövetelményekkel rendelkezik, és futtatható alacsony erőforrású gépeken is.

# 7. Architekturális terv
- Az alkalmazás egy egyszerű, egyrétegű architektúrával rendelkezik.<br>
- Minden művelet helyben, a felhasználó gépén történik a rendszerben.<br>
1. Felhasználói interfész:
    - A rendszer grafikus felhasználói felülettel rendelkezik.
    - A felhasználók gombnyomások segítségével végezhetik el a kívánt műveleteket.
2. Adatkezelés:
    - Minden felhasználói adat és tranzakció JSON fájlban tárolódik.
    - A program közvetlenül olvas és ír a JSON fájlba a működés során.
3. Hitelesítés:
    - A bejelentkezés során a felhasználói adatok egy JSON fájlba mentődnek, amiből beolvas az alkalmazás, így megőrizve a regisztrált accountokat.

# 8. Implementációs terv
1. Kezdeti fejlesztés:
    - A felhasználói regisztráció, bejelentkezés és JSON fájlkezelés implementálása.
    - A JSON fájlkezelés megvalósítása a felhasználói adatok tárolására.
2. Funkcionális fejlesztés:
    - Az egyenleglekérdezés, pénzfelvétel és befizetés funkciók implementálása.<br>
4. Tesztelés:
    - Minden funkció tesztelése különböző felhasználói forgatókönyvekkel.<br>
5. Finomítás:
    - Az esetleges hibák javítása és az alkalmazás teljesítményének optimalizálása.<br>

# 9. Tesztterv
A tesztelési folyamat során több szintű teszteket hajtunk végre.
1. Egységtesztek:
    - Minden egyes funkciót külön tesztelünk. Ide tartozik a regisztráció, belépés, egyenleglekérdezés, pénzfelvétel és befizetés funkciók.
2. Integrációs tesztek:
    - A funkciók közötti interakciókat teszteljük.
    - Ellenőrizzük, hogy a rendszer megfelelően kezeli a felhasználói adatokat és a tranzakciókat.
3. Funkcionális tesztek:
    - A felhasználói élmény ellenőrzése a teljes alkalmazásban.
    - Ellenőrizzük, hogy a felhasználók megfelelően tudják használni az applikációt.

# 10. Telepítési terv
- A telepítés egy egyszerű Python script telepítéséből áll, amelyet a felhasználók letölthetnek és futtathatnak a saját gépükön.<br>
- A szükséges függőségek telepítése pip segítségével történik, és az alkalmazás azonnal használható a futtatás után.<br>
- A JSON fájlok automatikusan létrejönnek a futtatás során, így a felhasználóknak nem kell külön adatbázist beállítaniuk.<br>

# 11. Karbantartási terv
- A karbantartás részeként rendszeres frissítéseket biztosítunk a hibák javítására és a funkciók bővítésére.<br>
- A felhasználói adatokat tartalmazó JSON fájlokat rendszeresen archiválni kell, hogy elkerüljük az adatvesztést.<br>
- A biztonsági frissítéseket szintén rendszeresen végrehajtjuk, különösen a hitelesítési rendszerek terén.<br>
