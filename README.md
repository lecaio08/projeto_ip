# <img width="48" height="48" alt="image" src="assets/images/donk.ico" /> donkey kong

## membros e suas responsabilidades:

| nome | email | responsabilidades |
|-----------------------------------------|----------------------|-------------------------------------------------------------|
| Victor Amorim Padilha | vap4@cin.ufpe.br | Correção de bugs e implementação de features |
| Caio Leon Almeida Andrade Michalewicz | claam@cin.ufpe.br | Correção de bugs |
| Enzo Nogueira Sarafim | ens2@cin.ufpe.br | Arte |
| Leonardo Portela Chiu | lpc4@cin.ufpe.br | Arte |
| Pedro Henrique Borges Ribeiro | phbr@cin.ufpe.br | Coordenação criativa |
| [Gustavo Antônio Linhares Sales](https://linkedin.com/in/gustavo-linhares0xf) | gals2@cin.ufpe.br | Implementação dos requisitos mínimos, slides e relatório |



## syllabus

- jogo de plataforma 2D inspirado no clássico [Donkey Kong](https://pt.wikipedia.org/wiki/Donkey_Kong)
- menu principal com configurações, iniciar jogo e menu de pausa com opção de voltar para o jogo ou menu
- configurações: volume, instruções de jogo(controles)
- proposta do jogo:
    - controlar personagem com 3 "vidas" que se move no eixo X e sobe escadas, obtendo colecionáveis que modificam, de alguma forma, a gameplay, são eles:
        - maçã: quando acionado, recupera vida. 3 slots
        - martelo: quando pego, confere habilidade de quebrar barris
        - moedas: cada uma acresce 5% na pontuação final, ex.: 2 moedas = acréscimo de 10%
    - pontuação: máximo de 60 segundos, o tempo restante é multiplicado por 1000

## arquitetura
```bash
projeto/
├── assets
│   └── fonts
│       └── font.ttf
├── game.py
├── interface.py
├── main.py
├── settings.py
├── sprites_items.py
├── sprites_player.py
└── sprites_world.py
```

## screenshots
- prototipo: <br />
    <img width="920" height="677" alt="image" src="https://github.com/user-attachments/assets/b7c9a9d0-0192-4911-ae4d-31037d1fcc4a" />


## framework e libs
- [PyGame](https://www.pygame.org/docs/): o PyGame é o nosso framework principal pois ele abstrai diversas complexidades, tem uma síntaxe simples e é intuitivo para iniciantes, sendo ideal para esse tipo de projeto
- [Os](https://docs.python.org/3/library/os.html): essa lib built-in foi utilizada para carregar o arquivo .ttf, para conseguirmos customizar a fonte do jogo
- [Sys](https://docs.python.org/3/library/sys.html): essa lib built-in foi utiilzada apenas para possibilitar o encerramento do programa por parte do usuário

## divisão

- Gustavo: implementação dos requisitos mínimos, slides e relatório
- Victor: correção de bugs e implementação de features
- Caio: correção de bugs
- Pedro: coordenação criativa
- Leonardo: arte
- Enzo: arte

## conceitos trabalhos

- Orientação a objetos
- Modularização
- Bibliotecas em Python

## desafios e erros
- O maior erro cometido durante a execução do projeto foi tentar dividir os trabalhos antes de começar a estudar orientação a objetos e aprender a utilizar o PyGame. Lidamos com isso estudando de forma conjunta, compartilhando o conhecimento e já colocando-os em prática, começando a implementar os requisitos mínimos do projeto.
- O maior desafio enfrentado pelo projeto foi conciliar aprender orientação a objetos e a como utilizar os frameworks em meio à realização de duas provas que demandam horas de estudo e também nota (pra não depender de prova final). Lidamos com isso deixando o gerenciamento do projeto nas mãos de quem podia dedicar menos tempo pra preparação para as provas.
- Aprendemos que a humildade pra reconhecer o que não sabe é essencial em qualquer tipo de projeto. Além disso, aprendemos que trabalhar em grupo demanda, acima de tudo, saber lidar com pessoas e que o compartilhamento de conhecimento é o pilar pra um bom desenvolvimento em conjunto.

## instalação (linux)
```bash
linus@torvalds:~$ git clone https://github.com/lecaio08/projeto_ip.git
linus@torvalds:~$ cd projeto_ip/
linus@torvalds:~/projeto_ip$ pip3 install -r requirements.txt --break-system-packages
linus@torvalds:~/projeto_ip$ python3 main.py 
````
