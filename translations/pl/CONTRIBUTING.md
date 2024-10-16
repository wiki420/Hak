<p align="center">
Translations <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/CONTRIBUTING.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/CONTRIBUTING.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/CONTRIBUTING.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/CONTRIBUTING.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/CONTRIBUTING.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pl/CONTRIBUTING.md>🇵🇱 PL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/CONTRIBUTING.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/CONTRIBUTING.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/CONTRIBUTING.md>🇨🇳 ZH   </a>
</p>

Siemka!

Więc jesteś zainteresowany współpracą z Ciphey? 🤔

Być może nie wiesz, od czego zacząć, albo uważasz, że Twoje umiejętności kodowania nie są "wystarczająco dobre"? Cóż, w przypadku tego drugiego – to śmieszne! Jesteśmy całkowicie w porządku ze "złym kodem", a nawet jeśli czytasz ten dokument, prawdopodobnie jesteś świetnym programistą. Mam na myśli, że nowicjusze rzadko uczą się wnosić wkład do projektów GitHub 😉

Oto kilka sposobów, w jakie możesz przyczynić się do rozwoju Ciphey:

- Dodaj nowy język 🧏
- Dodaj więcej metod szyfrowania 📚
- Stwórz więcej dokumentacji (Bardzo ważne! Bylibyśmy dozgonnie wdzięczni)
- Napraw błędy zgłoszone za pośrednictwem zgłoszeń GitHub (możemy Cię w tym wesprzeć 😊)
- Refaktoryzacja kodu bazowego 🥺

Jeśli brzmi to trudno, nie martw się! Ten dokument przeprowadzi Cię dokładnie przez to, jak osiągnąć każdy z nich. Ponadto Twoje imię i nazwisko zostanie dodane do listy współtwórców Ciphey, za co będziemy Ci dozgonnie wdzięczni! 🙏

Mamy mały czat Discord, na którym możesz porozmawiać z programistami i uzyskać pomoc. Możesz też napisać zgłoszenie GitHub ze swoją sugestią. Jeśli chcesz zostać dodany do Discord, napisz do nas wiadomość prywatną lub zapytaj nas w jakiś sposób.

[Serwer Discord](https://discord.gg/KfyRUWw)

# Jak kontrybuować

Ciphey zawsze potrzebuje więcej narzędzi do deszyfrowania! Aby dowiedzieć się, jak zintegrować kod z ciphey, sprawdź:

- <https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers> jako prosty samouczek
- <https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey> dla referencji API

Byłoby miło, gdybyś napisał dla niego jakieś testy, po prostu kopiując funkcję w Ciphey/tests/test_main.py i zastępując szyfrogram czymś zakodowanym Twoim szyfrem. Jeśli nie dodasz testów, prawdopodobnie i tak je połączymy, ale będzie nam znacznie trudniej diagnozować błędy!

It goes without saying that we will add you to the list of contributors for your hard work!

# Dodaj nowy język 🧏

Domyślny program sprawdzający język, `brandon`, działa z wieloma językami. Teraz może to brzmieć zniechęcająco.
Ale szczerze mówiąc, wszystko, co musisz zrobić, to wziąć słownik, wykonać małą analizę (napisaliśmy kod, który Ci w tym pomoże), dodać słowniki i analizę do repozytorium. A następnie dodać opcję do `settings.yml`.

# Stwórz więcej dokumentacji 

Dokumentacja jest najważniejszą częścią Ciphey. Brak dokumentacji to ekstremalne zadłużenie kodu, a tego nie chcemy.

Zaufaj mi, gdy mówię, że jeśli przyczynisz się do świetnej dokumentacji, będziesz postrzegany na tym samym poziomie, co współtwórcy kodu. Dokumentacja jest absolutnie niezbędna.

Istnieje wiele sposobów dodawania dokumentacji.

- Ciągi dokumentujące się w kodzie
- Ulepszanie naszej bieżącej dokumentacji (README, ten plik, nasze strony Wiki Ciphey)
- Tłumaczenie dokumentacji

I wiele więcej!

# Naprawa błędów

Odwiedź naszą stronę GitHub issues, aby znaleźć wszystkie błędy Ciphey! Rozbij je, a zostaniesz dodany do listy współtwórców. ;)

# Refaktoryzacja kodu bazowego

Nie cały Ciphey jest zgodny z PEP8, a część kodu się powtarza.
