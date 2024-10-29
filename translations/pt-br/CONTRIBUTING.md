<p align="center">
Traduções <br>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/de/CONTRIBUTING.md>🇩🇪 DE   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/CONTRIBUTING.md>🇬🇧 EN   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/hu/CONTRIBUTING.md>🇭🇺 HU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/id/CONTRIBUTING.md>🇮🇩 ID   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/it/CONTRIBUTING.md>🇮🇹 IT   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/nl/CONTRIBUTING.md>🇳🇱 NL   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/pt-br/CONTRIBUTING.md>🇧🇷 PT-BR   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/ru/CONTRIBUTING.md>🇷🇺 RU   </a>
<a href=https://github.com/Ciphey/Ciphey/tree/master/translations/zh/CONTRIBUTING.md>🇨🇳 ZH   </a>
</p>

Olá!

Então, você tem interesse em contribuir para o Ciphey? 🤔

Talvez você esteja com dúvidas sobre onde começar ou ache que suas habilidades de programação não são "boas o suficiente". Bem, quanto a isso - isso é ridículo! Somos bem de boa com "código ruim" e, se você está lendo este documento, provavelmente você já tem grande capacidade em programação. Afinal, iniciantes não costumam aprender a contribuir para projetos no GitHub 😉

Aqui estão algumas maneiras de contribuir com Ciphey:

- Adicionar um novo idioma 🧏
- Adicionar mais métodos de criptografia 📚
- Criar mais documentação (muito importante! Ficaríamos eternamente gratos)
- Corrigir bugs enviados via issues no GitHub (podemos dar suporte nisso 😊)
- Refatorar o código 🥺

Se isso parece difícil, não se preocupe! Este documento vai te guiar em como realizar qualquer uma dessas tarefas. Além disso, seu nome será adicionado à lista de contribuições do Ciphey, e seremos eternamente gratos! 🙏

Temos um pequeno chat no Discord para que você possa conversar com os desenvolvedores e receber uma ajuda. Alternativamente, você pode abrir uma issue no GitHub para enviar sua sugestão. Se quiser que te adicionemos ao Discord, envie uma DM ou entre em contato conosco de alguma forma.

[Servidor do Discord](https://discord.gg/KfyRUWw)

# Como contribuir

O Ciphey sempre precisa de mais ferramentas de descriptografia! Para aprender como integrar código ao Ciphey, confira:

- <https://github.com/Ciphey/Ciphey/wiki/Adding-your-own-ciphers> para um tutorial simples
- <https://github.com/Ciphey/Ciphey/wiki/Extending-Ciphey> para a referência da API

Seria ótimo se você pudesse escrever alguns testes para o seu código, copiando uma função no Ciphey/tests/test_main.py e substituindo o texto cifrado por algo codificado com sua cifra. Se não adicionar testes, provavelmente ainda faremos o merge, mas será bem mais difícil diagnosticar bugs!

Nem preciso dizer que vamos te adicionar à lista de contribuições pelo seu trabalho duro!

# Adicionar um novo idioma 🧏

O verificador de idiomas padrão, `brandon`, funciona com vários idiomas. Pode parecer um pouco complicado no início.
Mas, sinceramente, tudo o que você precisa fazer é pegar um dicionário, fazer uma pequena análise (nós já escrevemos um código para te ajudar com isso), adicionar os dicionários e a análise a um repositório. E então adicionar a opção em `settings.yml`.

# Criar mais documentação

A documentação é a parte mais importante do Ciphey. Sem documentação, o código fica difícil de entender, e não queremos isso.

Acredite em mim: se você contribuir com uma ótima documentação, será no mesmo nível que as pessoas que contribuem com código. A documentação é absolutamente essencial.

Há várias formas de adicionar documentação:

- Doc strings no código
- Melhorando nossa documentação atual (README, este arquivo, páginas do Wiki do Ciphey)
- Traduzindo a documentação

E muito mais!

# Currigir bugs

Visite nossa página de issues no GitHub para encontrar todos os bugs que o Ciphey tem! Resolva-os, colocaremos você na lista de contribuições. ;)

# Refactorar o código

Nem todo o código do Ciphey segue o padrão PEP8, e algumas partes do código são repetitivas.
