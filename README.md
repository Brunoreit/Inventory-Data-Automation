# Automação de Inventário e Cadastro com Python 

Este projeto desenvolve uma solução de **RPA (Robotic Process Automation)** para otimizar o fluxo de entrada de dados em sistemas de inventário. A automação aborda o desafio de processar grandes volumes de informações, eliminando o erro humano e reduzindo drasticamente o tempo de execução de tarefas repetitivas.

Utilizando o ecossistema Python para manipulação de dados e controle de periféricos, o sistema lê bases de dados estruturadas em CSV e simula a interação de um operador humano em interfaces web, garantindo que o cadastro de produtos seja realizado de forma precisa e escalável.

## Arquitetura da Automação

O sistema opera através de uma integração entre o sistema de arquivos local e a interface do navegador:

```text
┌───────────────────────────┐          ┌───────────────────────────┐
│     FONTE DE DADOS        │          │    MOTOR DE EXECUÇÃO      │
│  ┌─────────────────────┐  │          │  ┌─────────────────────┐  │
│  │   Arquivo .CSV      │  │          │  │   Python Script     │  │
│  │ (Tabela de Produtos)│──┼──────────┼─▶│ • Lógica de Loop    │  │
│  └─────────────────────┘  │          │  │ • Tratamento Dados  │  │
└───────────────────────────┘          │  │ • Delay Inteligente │  │
                                       └─────────────────────┘
                                                  │
                                                  │ Simulação de Input
                                                  ▼
┌───────────────────────────┐          ┌───────────────────────────┐
│    INTERFACE DESTINO      │          │   BIBLIOTECAS CORE        │
│  ┌─────────────────────┐  │          │  ┌─────────────────────┐  │
│  │    Sistema Web      │  │          │  │      Pandas         │  │
│  │ (Formulário Cadastro)│◀─┼──────────┼──│ (Data Manipulation) │  │
│  │                     │  │          │  ├─────────────────────┤  │
│  │                     │  │          │  │     PyAutoGUI       │  │
│  └─────────────────────┘  │          │  │   (UI Automation)   │  │
└───────────────────────────┘          └─────────────────────┘
```
## Fluxo de Execução

1. Setup Inicial: O script configura um PAUSE global de 0.5s para garantir a sincronia entre comandos.

2. Acesso ao Sistema: Automatiza a abertura do navegador Chrome e navegação até a URL de login.

3. Autenticação: Realiza o login utilizando credenciais pré-definidas (Email/Senha).

4. Extração de Dados: Utiliza a biblioteca Pandas para carregar o arquivo produtos.csv em um DataFrame.

5. Loop de Cadastro:

  - Itera sobre cada linha da tabela.
  - Mapeia as colunas (Código, Marca, Tipo, Categoria, Preço, Custo).
  - Executa comandos de teclado (tab, write, press) para preencher o formulário.

6. Finalização: Envia o formulário e reinicia o ciclo para o próximo item até o fim do arquivo.

## Como Rodar o Projeto
1. Pré-requisitos

Certifique-se de ter o Python instalado e as bibliotecas necessárias:
```Bash
pip install pyautogui pandas
```

2. Configuração de Tela (Importante)

Como a automação utiliza coordenadas de pixels, é necessário calibrar o script para a sua resolução de tela:
```Bash

# Execute o auxiliar para descobrir as coordenadas de clique
python auxiliar.py
```
Posicione o mouse sobre os campos do formulário e anote os valores X e Y retornados no terminal.

3. Execução

Com o navegador fechado ou em segundo plano:
```Bash

python projectPowerUp.py
```

| Nome |
|------|
| **Bruno Reitano** |


