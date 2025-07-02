# VAMOS USAR A BIBLIOTECA pyautogi PARA PODER FAZER NOSSA AUTOMAÇÃO

from time import sleep
import pyautogui # BIBLIOTECA DE AUTOMAÇÃO
import pandas # PARA IMPORTAR DADOS PARA DENTRO DO PYTHON

#pyautogui.click() == CLICAR
#pyautogui.position() == SABER A POSIÇÃO DO MOUSE PARA COLOCAR NO CLICK ^ O COMANDO DE CIMA
#pyautogui.press() == PRESSIONAR UMA TECLA
#pyautogui.write() == ESCREVER
#pyautogui.hotkey() == ATALHO DE TECLADO EX: CTRL + C

# 1° PASSO - ABRIR O SISTEMA DA EMPRESA https://dlp.hashtagtreinamentos.com/python/intensivao/login
def abrir_sistema():
    pyautogui.PAUSE=1 # DETERMINA UMA PAUSE DE 1 SEGUNDO PARA CDA COMANDO +- COMO O SLEEP()
    pyautogui.press('win') # PRESSIONAR A TECLA WINDOWS
    pyautogui.write('chrome') # DIGITAR CHROME
    pyautogui.press('enter') # PRESSIONAR A TECLA ENTER
    pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
    pyautogui.press('enter') # PRESSIONAR ENTERwww.globo.com


# 2° PASSO - FAZER O LOGINlOGITECH  mOUSE   1   25.95   6.5NAN
def fazer_login():
    sleep(3) # AQUI EU DETERMINEI QUE ELE ESPERASSE 3 SEGUNDOS POR CAUSA DA INTERNET POR GARANTIA 
    pyautogui.click(x=572, y=557) # POSIÇÃO DO MOUSE QUE DESCOBRI EM OUTRA ABA NO VS CODE COM O COMANDO .POSITION()
    pyautogui.write('devyurifg@gmail.com')
    pyautogui.click(x=545, y=709) # POSIÇÃO DO MOUSE QUE DESCOBRI EM OUTRA ABA NO VS CODE COM O COMANDO .POSITION()
    pyautogui.write('123456')
    pyautogui.click(x=919, y=817)
    pyautogui.press('enter')


# 3° PASSO  - IMPORTAR A BASE DE DADOS DOS PRODUTOS
def importar_tabela(): 
    tabela = pandas.read_csv('C:\\Users\\yuri2\\OneDrive\\Área de Trabalho\\1 Semestre 2025 - Blusoft\\JORNADA PYTHON - LIRA\\PYTHON POWER UP - AUTOMAÇÃO\\produtos.csv', delimiter=',', encoding='latin-1') # .read PARA ESCOLHER O TIPO DE DOCUMENTO A SER IMPORTADO
    print(tabela) # TEM QUE DEIXAR COMO VARIÁVEL
    return tabela

# 4° PASSO - CADASTRAR PRODUTO1
def cadastrar_produtos(tabela):
    sleep(2)
    for linha in tabela.index: # 5° PASSO - REPETIR O 4° PASSO ATÉ ACABAR
        pyautogui.click(x=547, y=391)
        codigo=tabela.loc[linha,'codigo']
        pyautogui.write(str(codigo))
        pyautogui.press('tab')
        marca=tabela.loc[linha,'marca']
        pyautogui.write(marca)
        pyautogui.press('tab')
        tipo=tabela.loc[linha,'tipo']
        pyautogui.write(tipo)
        pyautogui.press('tab')
        categoria=tabela.loc[linha,'categoria']
        pyautogui.write(str(categoria))
        pyautogui.press('tab')
        preco_unitario=tabela.loc[linha,'preco_unitario']
        pyautogui.write(str(preco_unitario))
        pyautogui.press('tab')
        custo=tabela.loc[linha,'custo']
        pyautogui.write(str(custo))
        pyautogui.press('tab')
        obs=tabela.loc[linha,'obs']
        if obs!= 'nan': # NAN SIGNIFICA VALOR VAZIO EM BASE DE DADOS 
            pyautogui.write(str(obs))
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.scroll(5000)
        
# PROGRAMA PRINCIPAL        

if __name__ == "__main__":
    abrir_sistema()
    fazer_login()
    tabela = importar_tabela()  
    cadastrar_produtos(tabela)      