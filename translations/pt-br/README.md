<p align="center">
Traduções <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/README.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/README.md>🇬🇧 EN   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/fr/README.md>🇫🇷 FR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/README.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/README.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/README.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/README.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/README.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/README.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/README.md>🇨🇳 ZH   </a>
 <br><br>
➡️
<a href="https://github.com/Ciphey/Ciphey/wiki">Documentação</a> |
<a href="https://discord.ciphey.online">Discord</a> |
 <a href="https://github.com/Ciphey/Ciphey/wiki/Installation">Guia de Instalação</a>
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

  <img src="https://github.com/brandonskerritt/Ciphey/workflows/Python%20application/badge.svg?branch=master" alt="Ciphey">
<br>
Ferramenta totalmente automatizada de descriptografia/decodificação/quebra de códigos, que utiliza processamento de linguagem natural e inteligência artificial, junto com um pouco de senso comum.
</p>
<hr>

## [Guia de instalação](https://github.com/Ciphey/Ciphey/wiki/Installation) (Em inglês)

| <p align="center"><a href="https://pypi.org/project/ciphey">🐍 Python | <p align="center"><a href="https://hub.docker.com/r/remnux/ciphey">🐋 Docker (Universal) | <p align="center"><a href="https://ports.macports.org/port/ciphey/summary">🍎 MacPorts (macOS) | <p align="center"><a href="https://formulae.brew.sh/formula/ciphey">🍺 Homebrew (macOS/Linux) |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |--------------------------------------------------------------------------------- |
| <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/python.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/docker.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/macports.png" /></p> | <p align="center"><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/homebrew.png" /></p> |
| `python3 -m pip install ciphey --upgrade` | `docker run -it --rm remnux/ciphey` | `sudo port install ciphey` | `brew install ciphey` |

| Linux                                                                                                                   | Mac OS                                                                                                                     | Windows                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Linux) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Mac%20OS) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ciphey/ciphey/Python%20application?label=Windows) |

<hr>

# 🤔 O que é Ciphey?

Digite um texto criptografado e receba o texto descriptografado de volta.

> "Que tipo de criptografia?"

Esse é o ponto. Você não sabe; só sabe que ele possivelmente está criptografado. O Ciphey descobrirá para você.

O Ciphey pode resolver a maioria dos casos em 3 segundos ou menos.

<p align="center" href="https://asciinema.org/a/336257">
  <img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/index.gif" alt="Demonstração do Ciphey">
</p>

O objetivo do Ciphey é ser uma ferramenta para automatizar várias tarefas de descriptografia e descodificação, como múltiplas codificações em base, cifras clássicas, hashes ou criptografia mais avançada.

Se você não conhece muito sobre criptografia ou quer verificar rapidamente o texto cifrado antes de trabalhar nele, o Ciphey é para você.

**A parte técnica** O Ciphey usa um módulo de inteligência artificial personalizado (_AuSearch_) com uma _Interface de Detecção de Cifras_ para aproximar o tipo de criptografia usado. Além disso, possui uma _Interface de Verificação de Linguagem_ personalizável, que detecta quando o texto se torna legível.

Nada de redes neurais ou IA pesada aqui. Usamos apenas o que é rápido e minimalista.

E isso é só o começo. Para uma explicação técnica completa, confira nossa [documentação](https://github.com/Ciphey/Ciphey/wiki) (Em inglês).

# ✨ Funcionalidades

- **Mais de 50 criptografias/codificações suportadas**, como binário, código Morse e Base64. Cifras clássicas como a cifra de César, cifra Afim e a cifra de Vigenère. Junto com criptografias modernas, como XOR de chave repetida e mais. **[Para a lista inteira clique aqui](https://github.com/Ciphey/Ciphey/wiki/Supported-Ciphers)**
- **Inteligência Artificial Personalizada com Busca Aumentada (AuSearch) para responder à pergunta "qual criptografia foi usada?"** Resultando em descriptografias em menos de 3 segundos.
- **Módulo de processamento de linguagem natural personalizado** O Ciphey pode determinar se algo é texto legível ou não. Seja JSON, uma flag de CTF ou inglês, o Ciphey detecta em milissegundos.
- **Suporte Multilíngue** atualmente disponível apenas em alemão e inglês (com variantes AU, UK, CAN, EUA).
- **Suporte para criptografias e hashes** Algo que alternativas como o CyberChef Magic não oferecem.
- **[Núcleo em C++](https://github.com/Ciphey/CipheyCore)** Extremamente rápido.

# 🔭 Ciphey contra CyberChef

## 🔁 Codficado 42 vezes com Base64

<table>
  <tr>
  <th>Nome</th>
    <th>⚡ Ciphey ⚡ </th>
    <th>🐢 CyberChef 🐢</th>
  </tr>
  <tr>
  <th>Gif</th>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/ciphey_gooder_cyberchef.gif" alt="O cara que ela fala para você não se preocupar"></td>
    <td><img src="https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/not_dying.gif" alt="Você"></td>
  </tr>
  <tr>
  <th>Tempo</th>
    <td>2 segundos</td>
    <td>6 segundos</td>
  </tr>
    <tr>
  <th>Configuração</th>
    <td><ul><li>Execute o Ciphey com o arquivo.</li></ul></td>
    <td><ul><li>Defina o parâmetro regex como "{"</li>
    <li>É preciso saber a profundidade da recursão</li>
    <li>É preciso saber que tudo é Base64</li>
    <li>É preciso carregar o CyberChef (um app JS pesado)</li>
    <li>Conhecer o suficiente sobre o CyberChef para criar esse pipeline</li>
    <li>Inverter a combinação</li></ul></td>
  </tr>
</table>

<sub><b>Nota</b> Os gifs podem carregar em tempos diferentes, então um pode parecer muito mais rápido que o outro.</sub><br>
<sub><b>Uma observação sobre o Magic:</b> O recurso mais parecido com o Ciphey no CyberChef é o Magic. O Magic falha num instante com essa entrada e trava. A única maneira de forçar o CyberChef a competir foi configurá-lo manualmente.</sub>

Nós também testamos o CyberChef e o Ciphey com um **arquivo de 6gb**. O Ciphey decifrou ele em **5 minutos e 54 segundos**. O CyberChef travou antes mesmo de começar.

## 📊 Ciphey contra Katana contra CyberChef Magic

| **Name**                                               | ⚡ Ciphey ⚡ | 🗡️ Katana 🗡️ | 🐢 CyberChef Magic 🐢 |
| ------------------------------------------------------ | ------------ | ------------ | --------------------- |
| Verificação avançada de linguagem                      | ✅           | ❌           | ✅                    |
| Suporta Criptografias                                  | ✅           | ✅           | ❌                    |
| Lançamentos com nomes provindos de temas distópicos 🌃 | ✅           | ❌           | ❌                    |
| Suporta Hashes                                         | ✅           | ✅           | ❌                    |
| Fácil de configurar                                    | ✅           | ❌           | ✅                    |
| Pode descobrir qual a criptografia usada               | ✅           | ❌           | ❌                    |
| Criado por hackers para hackers                        | ✅           | ✅           | ❌                    |

# 🎬 Começando

Se tiver problemas para instalar o Ciphey, [leia isso](https://github.com/Ciphey/Ciphey/wiki/Common-Issues-&-Their-Solutions) (em inglês).

## ‼️ Links importantes (Documentação, Guia de instalação, Suporte do Discord)

| Guia de instalação                                                          | Documentação                                             | Discord                                     | Imagem Docker (de REMnux)                                                                          |
| --------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 📖 [Guia de instalação](https://github.com/Ciphey/Ciphey/wiki/Installation) | 📚 [Documentação](https://github.com/Ciphey/Ciphey/wiki) | 🦜 [Discord](https://discord.gg/zYTM3rZM4T) | 🐋 [Documentação Docker](https://docs.remnux.org/run-tools-in-containers/remnux-containers#ciphey) |

## 🌀Rodando Ciphey

Existem 3 maneiras de executar o Ciphey.

1. Entrada de arquivo `ciphey -f criptografado.txt`
2. Entrada indefinida `ciphey -- "Texto criptografado"`
3. Modo normal `ciphey -t "Texto criptografado"`

![Gif mostrando 3 maneiras de executar o Ciphey](https://github.com/Ciphey/Ciphey/raw/master/Pictures_for_README/3ways.gif)

Para tirar as barras de progresso, tabela de probabilidades e de todas as mensagens adicionais, use o modo silencioso.

`ciphey -t "texto criptografado aqui" -q`

Para uma lista completa de argumentos, execute `ciphey --help`.

### ⚗️ Importando Ciphey

Você pode importar o módulo principal do Ciphey e usá-lo em seus próprios programas e códigos. `from Ciphey.__main__ import main`

# 🎪 Contribuidores

Ciphey foi inventado por [Brandon](https://github.com/bee-san) em 2008 e revivido em 2019.
Ciphey não estaria onde está hoje sem [Cyclic3](https://github.com/Cyclic3) - presidente da Cyber Security Society da Universidade de Liverpool.

Ciphey foi revivido e recriado pela [Cyber Security Society](https://www.cybersoc.cf/) para uso em competições de CTF. Se você estiver em Liverpool, considere dar uma palestra ou patrocinar nossos eventos. Envie um e-mail para `cybersecurity@society.liverpoolguild.org` para saber mais 🤠

**Crédito principal** a George H por descobrir como poderíamos usar algoritmos eficientes para acelerar o processo de busca.

**Agradecimentos especiais** a [varghalladesign](https://www.facebook.com/varghalladesign) por desenhar o logo. Confira outros trabalhos de design deles!

## 🐕‍🦺 [Contribuindo](CONTRIBUTING.md)

Não tenha medo de contribuir! Temos muitas, muitas coisas que você pode fazer para ajudar. Cada uma rotulada e explicada com exemplos. Se você estiver tentando contribuir, mas travou em algum ponto, marque @bee-san ✨

Alternativamente, entre no grupo do Discord e mande uma mensagem lá (link no [arquivo de contribuição](CONTRIBUTING.md)) ou no topo desse README.

Por favor, leia o [arquivo de contribuição](CONTRIBUTING.md) para detalhes exatos sobre como contribuir.✨

Ao contribuir, você terá seu nome adicionado ao README abaixo e fará parte de um projeto em constante crescimento!
[![Stargazers over time](https://starchart.cc/Ciphey/Ciphey.svg)](https://starchart.cc/Ciphey/Ciphey)

## 💰 Contribuições financeiras

As contribuições serão usadas para financiar não apenas o futuro do Ciphey e seus autores, mas também a Cyber Security Society na Universidade de Liverpool.

O GitHub não permite "patrocinar este projeto e dividiremos o valor igualmente", então escolha um link e nós cuidaremos disso 🥰

## ✨ Contribuidores

Agradecimentos a essas pessoas maravilhosas ([guia de emojis](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Cyclic3"><img src="https://avatars1.githubusercontent.com/u/15613874?v=4" width="100px;" alt=""/><br /><sub><b>cyclic3</b></sub></a><br /><a href="#design-cyclic3" title="Design">🎨</a> <a href="#maintenance-cyclic3" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=cyclic3" title="Code">💻</a> <a href="#ideas-cyclic3" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4" width="100px;" alt=""/><br /><sub><b>Brandon</b></sub></a><br /><a href="#design-brandonskerritt" title="Design">🎨</a> <a href="#maintenance-brandonskerritt" title="Maintenance">🚧</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=brandonskerritt" title="Code">💻</a> <a href="#ideas-brandonskerritt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/michalani"><img src="https://avatars0.githubusercontent.com/u/27767884?v=4" width="100px;" alt=""/><br /><sub><b>michalani</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=michalani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ashb07"><img src="https://avatars2.githubusercontent.com/u/24845568?v=4" width="100px;" alt=""/><br /><sub><b>ashb07</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=ashb07" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/TheAlcanian"><img src="https://avatars3.githubusercontent.com/u/22127191?v=4" width="100px;" alt=""/><br /><sub><b>Shardion</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ATheAlcanian" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Bryzizzle"><img src="https://avatars0.githubusercontent.com/u/57810197?v=4" width="100px;" alt=""/><br /><sub><b>Bryan</b></sub></a><br /><a href="#translation-Bryzizzle" title="Translation">🌍</a> <a href="https://github.com/Ciphey/Ciphey/commits?author=Bryzizzle" title="Documentation">📖</a></td>
    <td align="center"><a href="https://lukasgabriel.net"><img src="https://avatars0.githubusercontent.com/u/52338810?v=4" width="100px;" alt=""/><br /><sub><b>Lukas Gabriel</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=lukasgabriel" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Alukasgabriel" title="Bug reports">🐛</a> <a href="#translation-lukasgabriel" title="Translation">🌍</a> <a href="#ideas-lukasgabriel" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/DarshanBhoi"><img src="https://avatars2.githubusercontent.com/u/70128281?v=4" width="100px;" alt=""/><br /><sub><b>Darshan</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/issues?q=author%3ADarshanBhoi" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/SkeletalDemise"><img src="https://avatars1.githubusercontent.com/u/29117662?v=4" width="100px;" alt=""/><br /><sub><b>SkeletalDemise</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=SkeletalDemise" title="Code">💻</a></td>
    <td align="center"><a href="https://www.patreon.com/cclauss"><img src="https://avatars3.githubusercontent.com/u/3709715?v=4" width="100px;" alt=""/><br /><sub><b>Christian Clauss</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=cclauss" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Acclauss" title="Bug reports">🐛</a></td>
    <td align="center"><a href="http://machinexa.xss.ht"><img src="https://avatars1.githubusercontent.com/u/60662297?v=4" width="100px;" alt=""/><br /><sub><b>Machinexa2</b></sub></a><br /><a href="#content-machinexa2" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/anantverma275"><img src="https://avatars1.githubusercontent.com/u/18184503?v=4" width="100px;" alt=""/><br /><sub><b>Anant Verma</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=anantverma275" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3Aanantverma275" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/XVXTOR"><img src="https://avatars1.githubusercontent.com/u/40268197?v=4" width="100px;" alt=""/><br /><sub><b>XVXTOR</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=XVXTOR" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/Itamikame"><img src="https://avatars2.githubusercontent.com/u/59034423?v=4" width="100px;" alt=""/><br /><sub><b>Itamikame</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamikame" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/MikeMerz"><img src="https://avatars3.githubusercontent.com/u/50526795?v=4" width="100px;" alt=""/><br /><sub><b>MikeMerz</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=MikeMerz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jacobggman"><img src="https://avatars2.githubusercontent.com/u/30216976?v=4" width="100px;" alt=""/><br /><sub><b>Jacob Galam</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=jacobggman" title="Code">💻</a></td>
    <td align="center"><a href="https://tuxthexplorer.github.io/"><img src="https://avatars1.githubusercontent.com/u/37508897?v=4" width="100px;" alt=""/><br /><sub><b>TuxTheXplorer</b></sub></a><br /><a href="#translation-TuxTheXplorer" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/Itamai"><img src="https://avatars3.githubusercontent.com/u/53093696?v=4" width="100px;" alt=""/><br /><sub><b>Itamai</b></sub></a><br /><a href="https://github.com/Ciphey/Ciphey/commits?author=Itamai" title="Code">💻</a> <a href="https://github.com/Ciphey/Ciphey/issues?q=author%3AItamai" title="Bug reports">🐛</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Esse projeto segue a especificação [todos contribuidores](https://github.com/all-contributors/all-contributors). Contribuições de qualquer tipo são bem-vindas!
