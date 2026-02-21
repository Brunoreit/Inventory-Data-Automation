Automação de Inventário com Python

Este projeto é um script de automação desenvolvido para otimizar o processo de cadastro de produtos em sistemas web. Ele utiliza Python para ler bases de dados e simular a interação humana na interface, eliminando tarefas repetitivas e reduzindo erros de digitação.
 
 Sobre o Projeto

O script foi criado para resolver o problema comum de entrada manual de dados. Ele lê um arquivo .csv contendo informações de produtos e preenche automaticamente um formulário de cadastro online.
Principais Funcionalidades:

    Processamento de Dados: Utiliza a biblioteca Pandas para manipular e percorrer grandes volumes de dados de forma eficiente.

    Automação de UI: Utiliza PyAutoGUI para controlar mouse e teclado, realizando o preenchimento de campos, navegação via tab e cliques em botões.

    Controle de Fluxo: Implementação de pausas inteligentes (time.sleep) para garantir que o sistema web carregue corretamente antes de cada ação.

 Tecnologias Utilizadas

    Python 3

    Pandas: Para análise e manipulação de arquivos CSV.

    PyAutoGUI: Para automação de comandos de mouse e teclado.

    Time: Para gerenciamento de intervalos entre execuções.

 Como Executar

    Clone o repositório:
    Bash

git clone https://github.com/Brunoreit/NOME_DO_REPO.git

Instale as dependências:
Bash

pip install pyautogui pandas

Prepare o ambiente:

    Certifique-se de que o arquivo produtos.csv está na mesma pasta do script.

    Ajuste as coordenadas de clique no arquivo projectPowerUp.py (você pode usar o auxiliar.py para descobrir os pontos X e Y da sua tela).

Rode o script:
Bash

python projectPowerUp.py
