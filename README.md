# Resgate ao Byte!

## membros e suas responsabilidades:

| nome | email | responsabilidades |
|-----------------------------------------|----------------------|-------------------------------------------------------------|
| Victor Amorim Padilha | vap4@cin.ufpe.br | Code review, correção de bugs, implementação de features e QA |
| Caio Leon Almeida Andrade Michalewicz | claam@cin.ufpe.br | Code review, correção de bugs e QA |
| Enzo Nogueira Sarafim | ens2@cin.ufpe.br | arte dos personagens |
| Leonardo Portela Chiu | lpc4@cin.ufpe.br | arte dos menus |
| Pedro Henrique Borges Ribeiro | phbr@cin.ufpe.br | coordenação criativa, fase building e correção de bugs |
| [Gustavo Antônio Linhares Sales](https://linkedin.com/in/gustavo-linhares0xf) | gals2@cin.ufpe.br | Estruturação do grupo, protótipo do projeto, correção de bugs, slides e relatório |


## arquitetura

<img width="675" height="789" alt="image" src="https://github.com/user-attachments/assets/59afcf32-f8aa-49bd-b4ef-ae711dfeb23e" />

## screenshots

<img width="1617" height="1121" alt="image" src="https://github.com/user-attachments/assets/a15b0e7c-fa06-4cb8-a065-e6212b9e533e" />
<img width="1615" height="1126" alt="image" src="https://github.com/user-attachments/assets/b5fa73df-bda2-4f4c-a3cc-121f4f04541a" />
<img width="1614" height="1128" alt="image" src="https://github.com/user-attachments/assets/7f8101c9-4e1a-4f02-b97f-2aa1d7d8ca58" />
<img width="973" height="680" alt="image" src="https://github.com/user-attachments/assets/b0c0e6f2-96a0-42d6-a275-6b4723c61a79" />


## framework e libs

- [PyGame](https://www.pygame.org/docs/): o PyGame é o nosso framework principal pois ele abstrai diversas complexidades, tem uma síntaxe simples e é intuitivo para iniciantes, sendo ideal para esse tipo de projeto
- [Os](https://docs.python.org/3/library/os.html): essa lib built-in foi utilizada para carregar o arquivo .ttf, para conseguirmos customizar a fonte do jogo
- [Sys](https://docs.python.org/3/library/sys.html): essa lib built-in foi utiilzada apenas para possibilitar o encerramento do programa por parte do usuário
- [Pillow](https://pypi.org/project/pillow/): essa lib possibilita fazer o carregamento de todos os gifs do projeto. normalmente utilizada com o PyGame

## conceitos trabalhos

- Orientação a objetos
- Modularização
- Uso de bibliotecas públicas e built-in

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
