<p align="center">
<p align="center">
Terjemahan <br>
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
<a href="https://github.com/Ciphey/Ciphey/wiki">Dokumentasi</a> |
<a href="https://discord.ciphey.online">Discord</a> |
<a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Petunjuk Instalasi</a>
⬅️

<br>
  <img src="../../Pictures_for_README/binoculars.png" alt="Ciphey">
</p>

<p align="center">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/ciphey/ciphey">
<img src="https://pepy.tech/badge/ciphey">
 <img src="https://pepy.tech/badge/ciphey/month">
  <a href="https://discord.gg/wM3scnc"><img alt="Discord" src="https://img.shields.io/discord/728245678895136898"></a>
<a href="https://pypi.org/project/ciphey/"><img src="https://img.shields.io/pypi/v/ciphey.svg"></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Ciphey">

<br>
Alat dekripsi otomatis yang menggunakan pemrosesan bahasa alami & kecerdasan buatan, bersama dengan beberapa akal sehat.
</p>
<hr>

## [Petunjuk Instalasi](https://github.com/Ciphey/Ciphey/wiki/Installation)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://hub.docker.com/r/remnux/ciphey">🐋 Docker (Universal) | <p align="center"><a href="https://ports.macports.org/port/ciphey/summary">🍎 MacPorts (macOS) | <p align="center"><a href="https://formulae.brew.sh/formula/ciphey">🍺 Homebrew (macOS/Linux) |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |--------------------------------------------------------------------------------- |
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/macports.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/homebrew.png" /></p> |
| `python3 -m pip install ciphey --upgrade` | `docker run -it --rm remnux/ciphey` | `sudo port install ciphey` | `brew install ciphey` |

| Linux                                                                                                                   | Mac OS                                                                                                                     | Windows                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |

<hr>

# 🤔 Apa itu Ciphey?

Ciphey adalah sebuah alat dekripsi otomatis. Masukkan teks terenkripsi, dapatkan kembali teks yang didekripsi

> "Jenis enkripsi apa?"

Itulah intinya. Anda tidak tahu, Anda hanya tahu itu mungkin dienkripsi. Ciphey akan mencari tahu untuk Anda.

Ciphey dapat mendekripsi kebanyakan hal dalam 3 detik atau kurang.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="../../Pictures_for_README/index.gif" alt="Demo Ciphey">
</p>

**Detail teknis** Ciphey mengunakan modul kecerdasan buatan (_AuSearch_) dengan sebuah _Antarmuka Deteksi Cipher_ untuk memperkirakan enkripsi teks yang diberikan. Dan kemudian, sebuah _Antarmuka Pemerika Bahasa_ yang dibuat khusus dipakai untuk mendeteksi kapan teks yang diberikan sudah terdekripsi.

Dan itu hanya baru puncak dari gunung es. Untuk penjelasan teknis yang lebih lengkap, lihat [dokumentasi](https://github.com/Ciphey/Ciphey/wiki) kita.

# ✨ Fitur-fitur

- **Lebih dari 20 jenis enkripsi didukung** seperti penyandian (binary, base64) dan enkripsi normal seperti cipher Caesar, Transposisi dan banyak lagi. **[Untuk daftar lengkap, klik disini](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Ciphey mengunakan modul kecerdasan buatan dengan Pencarian Bertambah (_AuSearch_) untuk menjawab pertanyaan "enkripsi apa yang digunakan?"** Ini memunkinkan dekripsi untuk membutuhkan waktu kurang dari 3 detik.
- **Modul pemrosesan bahasa alami yang dibangun khusus** Ciphey dapat mendeteksi ketika sesuatu adalah teks biasa dengan akurasi yang sangat tinggi dan dengan cepat.
- **Dukungan Multi Bahasa** saat ini, hanya Bahasa Jerman & Inggris (dengan varian AU, UK, CAN, USA) yang tersedia.
- **Mendukung enkripsi** yang alternatif seperti CyberChef Magic tidak memiliki.
- **[Memakai inti C++](https://github.com/Ciphey/CipheyCore)** Sangat Cepat.

# 🔭 Ciphey vs CyberChef

## 🔁 Dikodekan Base64 42 kali

<table>
  <tr>
  <th>Name</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="The guy she tells you not to worry about"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="You"></td>
  </tr>
  <tr>
  <th>Durasi</th>
    <td>2 detik</td>
    <td>6 detik</td>
  </tr>
    <tr>
  <th>Pemakaian</th>
    <td><ul><li>Jalankan ciphey pada file</li></ul></td>
    <td><ul><li>Setel parameter regex menjadi "{"</li><li>Anda perlu tahu berapa kali untuk mengulang</li><li>Anda harus tahu teksnya dikodekan dengan Base64 sepenuhnya</li><li>Anda perluh memuat CyberChef (sebuah aplikasi JS yang besar)</li><li>Cukup tahu tentang CyberChef untuk menggunakannya dalam hal ini</li></ul></td>
  </tr>
</table>

<sub><b>Catatan</b> Gif diatas dapat memuat pada waktu yang berbeda sehingga satu terlihat jauh lebih cepat daripada yang lain.</sub><br>
<sub><b>Sebuah catatan tentang magic,</b> fitur CyberChef's yang paling mirip Ciphey. Magic gagal secara instan pada input ini dan cara satu-satunya untuk memaska CyberChef bersaing adalah untuk mendefinisikannya secara manual.</sub>

Kami juga menguji CyberChef dan Ciphey dengan file sebesar **6gb**. Ciphey memecahkannya dalam **5 menit dan 54 detik** dan CyberChef gagal bahkan sebelum memulai.

## 📊 Ciphey vs Katana vs CyberChef Magic

| **Name**                                   | ⚡ Ciphey ⚡ | 🤡 Katana 🤡 | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------ | ------------ | ------------ | --------------------- |
| Pemerika Bahasa yang Mahir                 | ✅           | ❌           | ✅                    |
| Mendukung Enkripsi                         | ✅           | ✅           | ❌                    |
| Rilis diberi nama sesuai tema Dystopian 🌃 | ✅           | ❌           | ❌                    |
| Mendukung Fungsi Hash                      | ✅           | ✅           | ❌                    |
| Mudah dipakai                              | ✅           | ❌           | ✅                    |
| Dapat menebak enkripsi yang dipakai        | ✅           | ❌           | ❌                    |
| Dibuat untuk peretas oleh peretas          | ✅           | ✅           | ❌                    |

# 🎬 Getting Started

If you're having trouble with installing Ciphey, [read this.](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions)

## ‼️ Important Links (Docs, Installation guide, Discord Support)

| Petunjuk Instalasi                                                          | Dokumentasi                                             | Discord                                     |
| --------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------- |
| 📖 [Petunjuk Instalasi](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Dokumentasi](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.ciphey.online) |

## 🏃‍♀️Menggunakan Ciphey

Ada 3 cara untuk memakai Ciphey.

1. Input File `ciphey - encrypted.txt`
2. Input Unqualified `ciphey -- "Teks terenkripsi di sini"`
3. Cara Biasa `ciphey -t "Teks terenkripsi di sini"`

![Gif menunjukkan 3 cara untuk memakai Ciphey](../../Pictures_for_README/3ways.gif)

Untuk menyingkirkan progress bar, tabel probabilitas, dan lain-lain gunakan mode senyap.

`ciphey -t "teks terenkripsi di sini" -q`

Untuk daftar argumen lengkap, jalankan `ciphey --help`.

### ⚗️ Mengimpor Ciphey

Anda dapat mengimpor file utama Ciphey dan menggunakannya dalam program dan kode Anda sendiri. `from Ciphey.__main__ import main`

# 🎪 Kontributor

Ciphey dibuat oleh [Brandon Skerritt](https://github.com/brandonskerritt) pada 2008, and dihidupkan kembali pada 2019. Ciphey tidak akan berada di ia berada tanpa [Cyclic3](https://github.com/Cyclic3) - presiden Cyber Security Society UoL.

Ciphey dihidupkan & diciptakan kembali oleh [Cyber Security Society](https://www.cybersoc.cf/) untuk digunakan dalam CTFs. Jika Anda pernah berada di Liverpool, pertimbangkan untuk memberi ceramah atau mensponsori acara kami. Kirimkan email kepada kami di `cybersecurity@society.liverpoolguild.org` untuk mengetahui lebih lanjut 🤠

**Kredit Besar** kepada George H untuk mengetahui bagaimana kami dapat menggunakan algoritma yang tepat untuk mempercepat proses pencarian. \
**Terima kasih khusus** untuk [varghalladesign](https://www.facebook.com/varghalladesign) untuk mendesain logo. Lihat karya desain mereka yang lain!

## 🐕‍🦺 [Berkontribusi](CONTRIBUTING.md)

Jangan takut untuk berkontribusi! Kami memiliki banyak, banyak hal yang dapat Anda lakukan untuk membantu. Masing-masing diberi label dan mudah dijelaskan dengan contoh-contoh. Jika Anda mencoba berkontribusi tetapi macet, tag @brandonskerritt di sebuah GitHub issue ✨

Atau, bergabung dengan grup Discord kita dan kirim pesan di sana (link di [file contribusi](CONTRIBUTING.md)) atau di bagian atas README ini sebagai lencana.

Silakan baca [file kontribusi](CONTRIBUTING.md) untuk detail yang tepat tentang cara berkontribusi ✨

## 💰 Kontributor Keuangan

Semua kontribusi akan digunakan untuk mendanai tidak hanya masa depan Ciphey dan penulisnya, tetapi juga Cyber Security Society di Universitas Liverpool.

GitHub tidak mendukung "mensponsori proyek ini dan kami akan mendistribusikan uang secara merata", jadi salah satu link dan kami akan mengatasinya di pihak kami 🥰

## ✨ Kontributor

Terima kasih kepada orang-orang hebat ini ([kunci emoji](https://allcontributors.org/docs/en/emoji-key)):

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

Proyek ini mengikuti spesifikasi [all-contributors](https://github.com/all-contributors/all-contributors). Kontribusi dalam bentuk apa pun dianjurkan!
