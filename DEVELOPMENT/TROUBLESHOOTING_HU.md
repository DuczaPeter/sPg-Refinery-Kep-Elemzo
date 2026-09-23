# Hibaelhárítás — magyar

## OCR nem indul

- legyen legalább egy kép betöltve;
- ellenőrizd az internetkapcsolatot;
- ellenőrizd, hogy a jsDelivr/Tesseract runtime nem blokkolt;
- nézd meg a böngésző konzolt és az **1 kattintásos logot**.

## UEX nem működik

- a UEX API külső szolgáltatás;
- endpoint, CORS, rate limit vagy uptime változhat;
- a program beépített material fallback listája ettől még működhet;
- ár/eladóhely adat nélkül ne találj ki értéket.

## Vágólap / DC gomb

`file://` környezetben a böngésző clipboard szabályai szigorúbbak lehetnek. GitHub Pages / HTTPS megbízhatóbb.

## Téves OCR

Hibajelentéshez:
1. teljes fájlnév;
2. screenshot;
3. elvárt material/Q/amount;
4. tényleges material/Q/amount;
5. 1 kattintásos log;
6. Star Citizen patch/build;
7. felbontás;
8. böngésző.

Ne csak annyit írj, hogy „rossz”. A konkrét kép + log kell ahhoz, hogy ne hardcode legyen a javítás.

## Review

A review nem feltétlenül programhiba. A projekt szándékosan inkább review-t adjon, mint bizonyítatlan automatikus eredményt.

## Új Star Citizen patch

Ha a UI elmozdul, font/rendering változik vagy új panel jelenik meg, a geometry detector és az OCR cropok új validációt igényelhetnek.
