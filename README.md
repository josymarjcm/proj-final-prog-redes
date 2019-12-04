### Projeto final da disciplina de Programação para Redes

Professor: [Charles Freitas](https://github.com/charles-freitas/)
Turma: Programação para Redes - 2019.2.
IFRN

#### Objetivo

Desenvolver um sistema para coleta de dados (humidade, temperatura e gás) de um ambiente utilizando a plataforma Arduino juntamente com a linguagem Python.

### Baixando o repositório
1) Instale o Git: ```sudo apt install git```;
2) Clone este repositório: ```git clone https://github.com/josymarjcm/proj-final-prog-redes.git```;
3) Entre no mesmo para as próximas configurações.

#### Configuração do ambiente

1) Instale o Python e pip3: ```sudo apt install python3 python3-pip```;
2) Instale as dependências para o Python: ```sudo pip3 install -r requirements.txt ```;
3) Substitua a variável ```ip_servidor``` dos arquivos [app.py](), [arduino.py]() e [cliente.py]() para o respectivo IP das máquinas;
4) Faça o upload do arquivo [monitor.ino]() para o seu Arduino.

#### Execução

1) Execute o arquivo [app.py]() no servidor;
2) Execute os arquivos [arduino.py]() e [cliente.py]() na máquina cliente.

#### Funcionamento

1) O script [arduino.py]() é responsável por capturar os dados enviados do Arduino para a porta serial e enviá-los ao servidor;
2) O script [cliente.py]() faz requisições ao servidor em busca dos dados definidos em tempo real pelo cliente;
3) Após os dados serem obtidos, o script [cliente.py]() os salva em um arquivo no formato JSON e exibe a média dos mesmos para o usuário. O usuário tem quatro opções de consulta: temperatura, humidade, gás e todas as anteriores.

#### Exemplo de funcionamento

```
Bem-vindo. Selecione a opção desejada:
1. Informações de temperatura
2. Informações de humidade
3. Informações de gás
4. Todas as informações
>> 4

Início (formato: YYYY-MM-DD HH:MM:SS) >> 2019-10-10
Fim (formato: YYYY-MM-DD HH:MM:SS) >> 2019-12-12
[+] Dados obtidos!
[+] Arquivo salvo em: arquivos_json/2660004936.json
[+] Lendo dados do arquivo...

	=== Informações dos sensores === 

Valor de temperatura médio: 		26.5
Valor de humidade médio: 		201.0
Valor de gás médio: 			188.5

```
