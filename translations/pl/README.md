<p align="center">
Tłumaczenia <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/fr/README.md>🇫🇷 FR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/README.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/README.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pl/README.md>🇵🇱 PL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/README.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/README.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/README.md>🇨🇳 ZH   </a>
<a href="https://github.com/Ciphey/Ciphey/tree/master/translations/th/README.md">🇹🇭 TH   </a>
 <br><br>
➡️
<a href="https://github.com/Ciphey/Ciphey/wiki">Dokumentacja</a> |
<a href="https://discord.gg/zYTM3rZM4T">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Podręcznik instalacji</a>
 ⬅️

<br>
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/binoculars.png" alt="Ciphey">
</p>

<p align="center">
<img src="https://pepy.tech/badge/ciphey">
 <img src="https://pepy.tech/badge/ciphey/month">
  <a href="https://discord.gg/zYTM3rZM4T"><img alt="Discord" src="https://img.shields.io/discord/754001738184392704"></a>
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">

<br>
W pełni zautomatyzowane narzędzie do deszyfrowania/dekodowania/łamania kodu, wykorzystujące przetwarzanie języka naturalnego i sztuczną inteligencję, wraz z odrobiną zdrowego rozsądku..</p>
<hr>

## [Podręcznik instalacji](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://hub.docker.com/r/remnux/ciphey">🐋 Docker (Universal) | <p align="center"><a href="https://ports.macports.org/port/ciphey/summary">🍎 MacPorts (macOS) | <p align="center"><a href="https://formulae.brew.sh/formula/ciphey">🍺 Homebrew (macOS/Linux) |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |--------------------------------------------------------------------------------- |
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p>    | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/macports.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/homebrew.png" /></p> |
| `python3 -m pip install ciphey --upgrade` | `docker run -it --rm remnux/ciphey` | `sudo port install ciphey` | `brew install ciphey` |

| Linux                                                                                                                   | Mac OS                                                                                                                     | Windows                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |

<hr>

# 🤔 Co to takiego?

Wprowadź zaszyfrowany tekst i otrzymaj odszyfrowany.

> "Jaki to typ szyfrowania?"

Właśnie o to chodzi. Nie wiesz za dużo, wiesz tylko, że tekst jest prawdopodobnie zaszyfrowany. Ciphey rozgryzie to za ciebie.

Ciphey potrafi rozwiązać większość problemów w 3 sekundy lub krócej.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

Ciphey ma być narzędziem umożliwiającym automatyzację wielu operacji odszyfrowywania i dekodowania, takich jak kodowanie wielobazowe, szyfry klasyczne, hasze i bardziej zaawansowana kryptografia.

Jeśli nie wiesz zbyt wiele o kryptografii lub chcesz szybko sprawdzić szyfrogram przed samodzielną pracą nad nim, Ciphey jest dla Ciebie.

**Część techniczna.** Ciphey używa niestandardowego modułu sztucznej inteligencji (_AuSearch_) z _Cipher Detection Interface_ (_Interfejsem Wykrywania Szyfrowania_), aby przybliżyć, czym coś jest zaszyfrowane. A następnie niestandardowego, konfigurowalnego przetwarzania języka naturalnego _Language Checker Interface_ (_Interfejsem Sprawdzania Języka_), który może wykryć, kiedy dany tekst staje się tekstem jawnym.

Nie ma tu sieci neuronowych ani rozdętej sztucznej inteligencji. Używamy tylko tego, co jest szybkie i minimalne.

A to tylko wierzchołek góry lodowej. Aby uzyskać pełne wyjaśnienie techniczne, zapoznaj się z naszą [dokumentacją](https://github.com/Ciphey/Ciphey/wiki).

# ✨ Funkcje

- **Obsługa ponad 50 szyfrowań/kodowań** takie jak kod binarny, kod Morse'a i Base64. Klasyczne szyfry, takie jak szyfr Cezara, szyfr Afiniczny i szyfr Vigenere'a. Wraz z nowoczesnym szyfrowaniem, takim jak XOR z powtarzającym się kluczem i nie tylko. **[Pełną listę można znaleźć tutaj](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Spersonalizowana Sztuczna Inteligencja z Rozszerzonym Wyszukiwaniem (AuSearch) umożliwiająca udzielenie odpowiedzi na pytanie "jakiego szyfrowania użyto?"** Dzięki temu odszyfrowanie zajmuje mniej niż 3 sekundy.
- **Niestandardowy moduł przetwarzania języka naturalnego** Ciphey może określić, czy coś jest tekstem jawnym, czy nie. Niezależnie od tego, czy ten tekst jawny to JSON, flaga CTF czy język Angielski, Ciphey może to uzyskać w ciągu kilku milisekund.
- **Obsługa wielu języków** Obecnie tylko Niemiecki i Angielski (z wariantami AU, UK, CAN, USA).
- **Obsługuje szyfrowanie i haszowanie** Czego nie oferują takie alternatywy jak CyberChef Magic.
- **[Rdzeń w C++](https://github.com/Ciphey/CipheyCore)** Błyskawicznie szybki.

# 🔭 Ciphey kontra CyberChef

## 🔁 Kodowanie Base64 42 razy

<table>
  <tr>
  <th>Nazwa</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Czas</th>
    <td>2 sekundy</td>
    <td>6 sekund</td>
  </tr>
    <tr>
  <th>Konfiguracja</th>
    <td><ul><li>Uruchom ciphey na pliku</li></ul></td>
    <td><ul><li>Ustaw parametr wyrażenia regularnego na "{"</li><li>Musisz wiedzieć, ile razy przeprowadzić rekursję</li><li>Musisz wiedzieć, że to Base64 od początku do końca</li><li>Musisz załadować CyberChef (jest to rozdęta aplikacja JS)</li><li>Mieć wystarczającą wiedzę o CyberChef, aby utworzyć ten potok</li><li>Odwrócić dopasowanie</li></ul></td>
  </tr>
</table>

<sub><b>Notatka</b> Pliki GIF mogą ładować się w różnym czasie, więc jeden może pojawiać się znacznie szybciej niż drugi.</sub><br>
<sub><b>Uwaga na temat magicznej funkcji</b> Najbardziej podobną funkcją CyberChef do Ciphey jest Magic. Magic natychmiast zawodzi na tym wejściu i zawiesza się. Jedynym sposobem, w jaki mogliśmy zmusić CyberChef do rywalizacji, było ręczne zdefiniowanie zadania.</sub>

Przetestowaliśmy również CyberChef i Ciphey z plikiem **6 GB**. Ciphey złamał go w **5 minut i 54 sekundy**. CyberChef zawiesił się jeszcze przed uruchomieniem.

## 📊 Ciphey kontra Katana kontra CyberChef Magic

| **Nazwa**                                   | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ------------ | ------------ | --------------------- |
| Zaawansowane sprawdzanie języka            | ✅           | ❌           | ✅                    |
| Obsługuje szyfrowanie                      | ✅           | ✅           | ❌                    |
| Dystopijne nazwy wydań 🌃                  | ✅           | ❌           | ❌                    |
| Obsługa haszy                              | ✅           | ✅           | ❌                    |
| Łatwy w konfiguracji                       | ✅           | ❌           | ✅                    |
| Potrafi zgadnąć czym coś jest zaszyfrowane | ✅           | ❌           | ❌                    |
| Stworzone dla hackerów przez hackerów      | ✅           | ✅           | ❌                    |

# 🎬 Pierwsze Kroki

Jeśli masz problemy z instalacją Ciphey, [przeczytaj to.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Ważne linki (Dokumentacja, Podręcznik Instalacji, Wsparcie na Discord)

| Podręcznik Instalacji                                                          | Dokumentacja                                             | Discord                                     | Obraz Docker (z REMnux)                                                                          |
| --------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 📖 [Podręcznik Instalacji](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Dokumentacja](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.gg/zYTM3rZM4T) | 🐋 [Dokumentacja Docker](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey) |

## 🏃‍♀️Uruchamianie Ciphey

Istnieją 3 sposoby uruchomienia Ciphey.

1. Plik wejściowy `ciphey -f zaszyfrowany.txt`
2. Niekwalifikowane dane wejściowe `ciphey -- "Zaszyfrowane dane wejściowe"`
3. Normalny sposób `ciphey -t "Zaszyfrowane dane wejściowe"`

![Gif pokazujący 3 sposoby uruchomienia Ciphey](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Aby pozbyć się pasków postępu, tabeli prawdopodobieństwa i całego szumu, użyj trybu cichego.

`ciphey -t "zaszyfrowany tekst" -q`

Aby uzyskać pełną listę argumentów programu, uruchom `ciphey --help`.

### ⚗️ Importowanie Ciphey

Możesz zaimportować Ciphey jako moduł i używać go we własnych programach i kodzie. `from Ciphey.__main__ import main`

# 🎪 Kontrybutorzy

Ciphey został wymyślony przez [Bee](https://github.com/bee-san) w 2008, i odnowiony w 2019. Ciphey nie byłby dziś tam, gdzie jest, bez [Cyclic3](https://github.com/Cyclic3) - prezesa UoL's Cyber Security Society.

Ciphey został odnowiony i odtworzony przez [Cyber Security Society](https://www.cybersoc.cf/) do użycia w CTFach. Jeśli kiedykolwiek będziesz w Liverpoolu, rozważ wygłoszenie przemówienia lub sponsorowanie naszych wydarzeń. Napisz do nas na adres `cybersecurity@society.liverpoolguild.org` aby dowiedzieć się więcej 🤠

**Główne uznanie** dla George H za opracowanie sposobu wykorzystania odpowiednich algorytmów w celu przyspieszenia procesu wyszukiwania.
**Specjalne podziękowania** dla [varghalladesign](https://www.facebook.com/varghalladesign) za zaprojektowanie logo. Sprawdź ich inne prace projektowe!

## 🐕‍🦺 [Kontrybucja](https://github.com/Ciphey/Ciphey/wiki/Contributing)

Nie bój się wnosić swojego wkładu! Mamy wiele, wiele rzeczy, które możesz zrobić, aby pomóc. Każda z nich jest oznaczona i łatwo wyjaśniona przykładami. Jeśli próbujesz wnieść swój wkład, ale utknąłeś, oznacz @bee-san ✨

Możesz też dołączyć do grupy Discord i wysłać tam wiadomość (link w [pliku kontrybucji](https://github.com/Ciphey/Ciphey/wiki/Contributing)) lub na górze tego README jako odznaka.

Proszę przeczytaj [plik kontrybucji](https://github.com/Ciphey/Ciphey/wiki/Contributing) aby uzyskać dokładne informacje o tym, jak wnieść swój wkład ✨

Jeśli to zrobisz, Twoje imię zostanie dodane do pliku README poniżej i będziesz mógł stać się częścią stale rozwijającego się projektu!
[![Gwiezdni obserwatorzy na przestrzeni czasu](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)

## 💰 Darczyńcy finansowi

Wpłaty zostaną wykorzystane nie tylko do sfinansowania przyszłości Ciphey i jego autorów, ale także Cyber Security Society na Uniwersytecie w Liverpoolu.

GitHub nie obsługuje opcji „sponsoruj ten projekt, a my podzielimy pieniądze po równo”, więc wybierz link, a my zajmiemy się tym po naszej stronie 🥰

## ✨ Współtwórcy

Podziękowania dla tych wspaniałych ludzi ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Cyclic3"><img src="https://avatars1.githubusercontent.com/u/15613874?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cyclic3</b></sub></a><br /><a href="#design-cyclic3" title="Design">🎨</a> <a href="#maintenance-cyclic3" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=cyclic3" title="Code">💻</a> <a href="#ideas-cyclic3" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Brandon</b></sub></a><br /><a href="#design-brandonskerritt" title="Design">🎨</a> <a href="#maintenance-brandonskerritt" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=brandonskerritt" title="Code">💻</a> <a href="#ideas-brandonskerritt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/michalani"><img src="https://avatars0.githubusercontent.com/u/27767884?v=4?s=100" width="100px;" alt=""/><br /><sub><b>michalani</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=michalani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashb07"><img src="https://avatars2.githubusercontent.com/u/24845568?v=4?s=100" width="100px;" alt=""/><br /><sub><b>ashb07</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=ashb07" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/TheAlcanian"><img src="https://avatars3.githubusercontent.com/u/22127191?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shardion</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ATheAlcanian" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Bryzizzle"><img src="https://avatars0.githubusercontent.com/u/57810197?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bryan</b></sub></a><br /><a href="#translation-Bryzizzle" title="Translation">🌍</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=Bryzizzle" title="Documentation">📖</a></td>
    <td align="center"><a href="https://lukasgabriel.net"><img src="https://avatars0.githubusercontent.com/u/52338810?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lukas Gabriel</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=lukasgabriel" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Alukasgabriel" title="Bug reports">🐛</a> <a href="#translation-lukasgabriel" title="Translation">🌍</a> <a href="#ideas-lukasgabriel" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/DarshanBhoi"><img src="https://avatars2.githubusercontent.com/u/70128281?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Darshan</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ADarshanBhoi" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/SkeletalDemise"><img src="https://avatars1.githubusercontent.com/u/29117662?v=4?s=100" width="100px;" alt=""/><br /><sub><b>SkeletalDemise</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=SkeletalDemise" title="Code">💻</a></td>
    <td align="center"><a href="https://www.patreon.com/cclauss"><img src="https://avatars3.githubusercontent.com/u/3709715?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christian Clauss</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=cclauss" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Acclauss" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://machinexa.xss.ht"><img src="https://avatars1.githubusercontent.com/u/60662297?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Machinexa2</b></sub></a><br /><a href="#content-machinexa2" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/anantverma275"><img src="https://avatars1.githubusercontent.com/u/18184503?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Anant Verma</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=anantverma275" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Aanantverma275" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/XVXTOR"><img src="https://avatars1.githubusercontent.com/u/40268197?v=4?s=100" width="100px;" alt=""/><br /><sub><b>XVXTOR</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=XVXTOR" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Itamikame"><img src="https://avatars2.githubusercontent.com/u/59034423?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Itamikame</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamikame" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/MikeMerz"><img src="https://avatars3.githubusercontent.com/u/50526795?v=4?s=100" width="100px;" alt=""/><br /><sub><b>MikeMerz</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=MikeMerz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jacobggman"><img src="https://avatars2.githubusercontent.com/u/30216976?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jacob Galam</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=jacobggman" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Ajacobggman" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://tuxthexplorer.github.io/"><img src="https://avatars1.githubusercontent.com/u/37508897?v=4?s=100" width="100px;" alt=""/><br /><sub><b>TuxTheXplorer</b></sub></a><br /><a href="#translation-TuxTheXplorer" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/Itamai"><img src="https://avatars3.githubusercontent.com/u/53093696?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Itamai</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamai" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3AItamai" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Termack"><img src="https://avatars2.githubusercontent.com/u/26333901?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Filipe</b></sub></a><br /><a href="#translation-Termack" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/malathit"><img src="https://avatars0.githubusercontent.com/u/2684148?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Malathi</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=malathit" title="Code">💻</a></td>
    <td align="center"><a href="https://hexchaos.xyz/"><img src="https://avatars1.githubusercontent.com/u/8947820?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jack</b></sub></a><br /><a href="#translation-HexChaos" title="Translation">🌍</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/yafkari"><img src="https://avatars3.githubusercontent.com/u/41365655?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Younes</b></sub></a><br /><a href="#translation-yafkari" title="Translation">🌍</a></td>
    <td align="center"><a href="https://gitlab.com/Marnick39"><img src="https://avatars2.githubusercontent.com/u/17315511?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marnick Vandecauter</b></sub></a><br /><a href="#translation-Marnick39" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/mav8557"><img src="https://avatars0.githubusercontent.com/u/47306745?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Michael V</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=mav8557" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/chuinzer"><img src="https://avatars2.githubusercontent.com/u/64257785?v=4?s=100" width="100px;" alt=""/><br /><sub><b>chuinzer</b></sub></a><br /><a href="#translation-chuinzer" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/blackcat-917"><img src="https://avatars1.githubusercontent.com/u/53786619?v=4?s=100" width="100px;" alt=""/><br /><sub><b>blackcat-917</b></sub></a><br /><a href="#translation-blackcat-917" title="Translation">🌍</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=blackcat-917" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Ozzyz"><img src="https://avatars3.githubusercontent.com/u/6113447?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Åsmund Brekke</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Ozzyz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/sashreek1"><img src="https://avatars1.githubusercontent.com/u/45600974?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sashreek Shankar</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=sashreek1" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/cryptobadger"><img src="https://avatars2.githubusercontent.com/u/26308101?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cryptobadger</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=cryptobadger" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Acryptobadger" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/e1fy"><img src="https://avatars3.githubusercontent.com/u/61194758?v=4?s=100" width="100px;" alt=""/><br /><sub><b>elf</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=e1fy" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/rogercyyu"><img src="https://avatars0.githubusercontent.com/u/45835736?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Roger Yu</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=rogercyyu" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/JesseEmond"><img src="https://avatars.githubusercontent.com/u/1843555?v=4?s=100" width="100px;" alt=""/><br /><sub><b>dysleixa</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=JesseEmond" title="Code">💻</a></td>
    <td align="center"><a href="http://mohzulfikar.me"><img src="https://avatars.githubusercontent.com/u/48849323?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mohammad Zulfikar</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=mohzulfikar" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/AABur"><img src="https://avatars.githubusercontent.com/u/41373199?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexander Burchenko</b></sub></a><br /><a href="#translation-AABur" title="Translation">🌍</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Ten projekt jest zgodny ze specyfikacją [all-contributors](https://github.com/all-contributors/all-contributors). Wsparcja wszelkiego rodzaju mile widziane!
