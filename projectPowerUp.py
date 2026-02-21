# pip install pyautogui - biblioteca para mexer no pc
# pip install pandas
import time # biblioteca padrão do python que controla o tempo das coisas
import pyautogui 
import pandas

#pyautogui.write() - escreve um texto
#pyautogui.click() - clica com o mouse
#pyautogui.press() - aperta uma tecla
#pyautoguit.hotkey() - apertar um atalho do teclado (ctrl, c)
#pyautoguit.drag() - aperta e arrasta
#pyautoguit.scroll() - usa o scroll
pyautogui.PAUSE = 0.5 # pausa entre os códigos para dar tempo dos App abrirem(todas as linhas)


# Passo 01: apertar a tecla windows para procurar o navegador e pressionar "enter"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Cola o site da empresa, pressiona "enter" e espera 3 segundos para o site abrir antes de continuar os códigos
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# utiliza as cordenadas x e y (valores específicos para cada parte da tela) para saber onde clicar
pyautogui.click(x=873, y=452) # valores tirados do "auxiliar.py"
pyautogui.write("brureitano@gmail.com")

pyautogui.press("tab") # tab geralmente passa do campo "email" para "senha" em formulários
pyautogui.write("minha senha")

# OU igual o outro EX:
# pyautogui.click(x=696, y=578)
# pyautogui.write(1234)

pyautogui.press("tab")
pyautogui.press("enter")

# importar a base de dados (pandas)

tabela = pandas.read_csv("produtos.csv")
linha = 0 
# Cadastrar produtos

for linha in tabela.index:
    
    pyautogui.click(x=664, y=302) # clicar no primeiro campo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")


    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")


    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")


    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")


    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")


    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000) # sobe de volta no inicio da página