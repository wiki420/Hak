<p align="center">
Übersetzungen <br>
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
<a href="https://github.com/Ciphey/Ciphey/wiki">Dokumentation</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Installationshilfe</a>
 ⬅️

<br>
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/binoculars.png" alt="Ciphey">
</p>

<p align="center">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/ciphey/ciphey">
<img src="https://pepy.tech/badge/ciphey">
 <img src="https://pepy.tech/badge/ciphey/month">
  <a href="https://discord.gg/wM3scnc"><img alt="Discord" src="https://img.shields.io/discord/728245678895136898"></a>
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">

<br>
Vollautomatisiertes Entschlüsselungs-Tool, gestützt durch algorithmische Sprachverarbeitung & künstliche Intelligenz.
</p>
<hr>

## [Installationshilfe](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://hub.docker.com/r/remnux/ciphey">🐋 Docker (Universell) | <p align="center"><a href="https://ports.macports.org/port/ciphey/summary">🍎 MacPorts (macOS) | <p align="center"><a href="https://formulae.brew.sh/formula/ciphey">🍺 Homebrew (macOS/Linux) |
| --------------------------- | ---------------------------------| ---------------------------------| ---------------------------------|
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/macports.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/homebrew.png" /></p> |
| `python3 -m pip install ciphey --upgrade`  | `docker run -it --rm remnux/ciphey` | `sudo port install ciphey` | `brew install ciphey` |


| Linux       | Mac OS | Windows     |
| ----------- | ------ | ----------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) |![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |


<hr>

# 🤔 Was ist Ciphey?
Ciphey ist ein vollautomatisches Entschlüsselungs-Tool. Verschlüsselter Text wird eingegeben, entschlüsselter Text kommt zurück.
> "Welche Arten von Verschlüsselung?"

Das ist die Frage. Auch wenn die Art der Verschlüsselung unbekannt ist (und lediglich die Vermutung besteht, dass es sich um verschlüsselten Text handelt), wird Ciphey einen Lösungsweg suchen.

Ciphey hat in den meisten Fällen nach circa 3 Sekunden eine Lösung parat.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Ciphey demo">
</p>

**Der technische Teil.** In Ciphey kommt ein maßgeschneidertes KI-Modul (_AuSearch_) mit Verschlüsselungserkennung (_Cipher Detection Interface_) zum Einsatz, das abschätzen kann, mit welcher Methode etwas verschlüsselt wurde. Daraufhin prüft ein dediziertes Spracherkennungs-Interface (_Language Checker Interface_), ob es sich bei dem nun entschlüsselten Text um Klartext handelt.

Und das ist erst die Spitze des Eisbergs! Eine vollständige technische Erklärung ist in der [Dokumentation](https://docs.ciphey.online/en/latest) zu finden.

# ✨ Funktionen

- **Über 20 unterstützte Verschlüsselungsarten**, zum Beispiel Kodierungen (binär, base64) und traditionelle Verschlüsselungen wie die Caesar-Verschlüsselung, Transposition und weitere. **[Vollständige Liste](https://docs.ciphey.online/en/latest/ciphers.html)**
- **Maßgeschneidertes KI-Modul mit _Augmented Search (AuSearch)_, das erkennen kann, mit welcher Methode etwas verschlüsselt wurde.** Das Ergebnis sind Laufzeiten von unter 3 Sekunden.
- **Eigens entwickeltes Spracherkennungs-Modul** Ciphey kann erkennen, ob es sich bei etwas um Klartext handelt, oder nicht. Hierbei ist es nicht nur unglaublich genau, sondern auch unglaublich schnell.
- **Mehrere unterstützte Sprachen** Momentan nur Deutsch & Englisch.
- **Unterstützt Verschlüsselungen** Im Vergleich zu Alternativen wie CyberChef Magic, die dies nicht leisten können.
- **[C++ core](https://github.com/Ciphey/CipheyCore)** Rasend schnell.

# 🔭 Ciphey vs CyberChef

## 🔁 Base64 42-fach kodiert

<table>
  <tr>
  <th>Name</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="Der Typ, bei dem sie meint, du sollst dir keine Sorgen machen."></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="Du"></td>
  </tr>
  <tr>
  <th>Zeit</th>
    <td>2 Sekunden</td>
    <td>6 Sekunden</td>
  </tr>
    <tr>
  <th>Setup</th>
    <td><ul><li>Ciphey mit der Datei ausführen</li></ul></td>
    <td><ul><li>Regex-Parameter auf "{" setzen</li><li>Die Rekursionstiefe muss bekannt sein</li><li>Vor der Ausführung muss bekannt sein, dass es sich von Anfang bis Ende um base64 handelt</li><li>CyberChef (eine aufgeblähte JavaScript-App) muss geladen werden</li><li>Genug Vorwissen über CyberChef, um diese Pipeline überhaupt aufstellen zu können</li><li>Das gefundene Korrelat umkehren</li></ul></td>
  </tr>
</table>


<sub><b>Hinweis</b> Die GIFs laden asynchron, weshalb es sein kann, dass sie nach und nach erscheinen.</sub><br>
<sub><b>Eine Bemerkung zu Magic </b>Die Magic-Funktion von CyberChef kommt Ciphey am nächsten. Magic schlägt bei dieser Eingabe sofort fehl und stürzt ab. Die einzige Möglichkeit, CyberChef (für eine Gegenüberstellung mit Ciphey) mit diesem Input zum Laufen zu bekommen war durch eine manuelle Definition durch uns.</sub>


Außerdem haben wir Ciphey und CyberChef mit einer **6GB Eingabedatei** gegeneinander antreten lassen. Ciphey hatte nach **5 Minuten und 54 Sekunden** ein Lösung. CyberChef ist abgestürzt, bevor die Entschlüsselung überhaupt begonnen hatte.



## 📊 Ciphey vs Katana vs CyberChef Magic

| **Name**                                   | ⚡ Ciphey ⚡ | 🤡 Katana 🤡 | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ---------- | ---------- | ------------------- |
| Fortschrittliche Spracherkennung           | ✅          | ❌          | ✅                   |
| Unterstützt Verschlüsselungen              | ✅          | ✅          | ❌                   |
| Releases benannt nach dystopischen Motiven 🌃   | ✅          | ❌          | ❌              |
| Unterstützt Hashes                         | ✅          | ✅          | ❌                   |
| Einfache, unkomplizierte Einrichtung       | ✅          | ❌          | ✅                   |
| Kann abschätzen, welche Verschlüsselung verwendet wurde | ✅          | ❌          | ❌      |
| Von Hackern, für Hacker                    | ✅          | ✅          | ❌                   |

# 🎬 Erste Schritte

Bei Problemen bei der Installation von Ciphey, [hier weiterlesen.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Wichtige Links (Docs, Installationshilfe, Discord Support)

| Installationshilfe | Dokumentation | Discord | Docker Image (von REMnux)
| ------------------ | ------------- | ------- | ------- |
| 📖 [Installationshilfe](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Dokumentation](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) | 🐋 [Docker Dokumentation](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey)

## 🏃‍♀️Ciphey ausführen
Es gibt 3 Möglichkeiten, Ciphey auszuführen:
1. Datei als Input `ciphey - verschluesselt.txt`
2. Unqualifizierter Input `ciphey -- "Verschlüsselter Input"`
3. Standard `ciphey -t "Verschlüsselter Input"`

![GIF zeigt drei Möglichkeiten, Ciphey auszuführen.](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Um die Fortschrittsanzeige, Wahrscheinlichkeitstabelle und andere Anzeigen loszuwerden, kann Ciphey im *Quiet Mode* ausgeführt werden:

```ciphey -t "Verschlüsselter Text" -q```

Fur eine komplette Liste der Argumente: `ciphey --help`.

### ⚗️ Ciphey importieren
Wer Ciphey als Teil eines eigenen Projekts verwenden will, kann es mit `from Ciphey.__main__ import main` importieren.

# 🎪 Contributors
Ciphey wurde 2008 von [Brandon Skerritt](https://github.com/brandonskerritt) erfunden und 2019 wiederbelebt. Ciphey wäre nicht dort, wo es heute ist, ohne die Hilfe von [Cyclic3](https://github.com/Cyclic3) - Präsident der *Cyber Security Society* der *University of Liverpool*.

Ciphey wurde durch die [Cyber Security Society](https://www.cybersoc.cf/) für die Verwendung in CTFs (eine Art Hacker-Wettbewerb) aufgelegt. Wenn Du jemals in Liverpool bist, würden wir uns freuen, wenn Du einen Vortrag halten oder unsere Veranstaltungen sponsern würdest. Kontaktiere uns per E-Mail unter `cybersecurity@society.liverpoolguild.org` um mehr zu erfahren. 🤠

**Einen besonderen Dienst** leistete uns George H, als er uns geholfen hat, den Suchprozess durch Algorithmen zu beschleunigen.
**Besonderer Dank** an [varghalladesign](https://www.facebook.com/varghalladesign) für die Gestaltung unseres Logos. Schau mal in das Portfolio!

## 🐕‍🦺 [Mitwirken](CONTRIBUTING.md)
Du möchtest am Projekt teilhaben - keine Angst! Wir haben sehr viele Dinge, die du tun kannst, um uns zu helfen. Jedes Issue ist gelabelt und mit Beispielen unterlegt. Falls Du feststeckst, tagge @brandonskerritt im GitHub-Issue. ✨

Alternativ kannst du unserem Discord-Server beitreten und uns dort direkt erreichen. Den Link findest du in der [Contrib-Datei](CONTRIBUTING.md) und als Badge am Anfang dieser README.

Details zur Teilnahme findest du in der [Contrib-Datei](CONTRIBUTING.md) ✨
## 💰 Finanzielle Spender
Finanzielle Beiträge werden für die zukünftige Entwicklung von Ciphey und dessen Autorinnen und Autoren verwendet. Außerdem kommen finanzielle Zuwendungen der Cyber Security Society an der University of Liverpool zugute.

Da GitHub keine gleichmäßiger Verteilung der Sponsorenbeiträge unterstützt, kannst Du dir einfach einen Link aussuchen - wir regeln den Rest dann unter uns. 🥰

## ✨ Mitwirkende

Ein Dankeschön an die folgenden großartigen Helfer: ([Legende](https://allcontributors.org/docs/en/emoji-key))

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

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

Dieses Projekt folgt der [All-Contributors](https://github.com/all-contributors/all-contributors) Spezifikation. Jede Art von Beitrag ist herzlich willkommen!
