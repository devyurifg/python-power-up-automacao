# Automação de Cadastro de Produtos com PyAutoGUI

Este projeto automatiza o processo de cadastro de produtos em um sistema web utilizando Python e a biblioteca **pyautogui** para controle do mouse e teclado, e **pandas** para manipulação da base de dados em CSV.

## Funcionalidades

- Abre o navegador Chrome e acessa o sistema da empresa  
- Realiza o login automaticamente com usuário e senha  
- Importa uma base de dados `.csv` contendo os produtos  
- Navega na tela do sistema para cadastrar cada produto, preenchendo os campos automaticamente  
- Usa coordenadas do mouse para interação (click, digitação, tabulação)  
- Permite automatizar o cadastro de vários produtos em sequência  

## Exemplo de Uso
```
if __name__ == "__main__":
    abrir_sistema()
    fazer_login()
    tabela = importar_tabela()
    cadastrar_produtos(tabela)
```
Este código abrirá o sistema, fará o login, importará a tabela e cadastrará todos os produtos listados.

## Conceitos Envolvidos

- Automação de interface gráfica com pyautogui
- Manipulação e leitura de dados usando pandas
- Uso de funções para organizar o fluxo da automação
- Controle de tempo com sleep e pyautogui.PAUSE para garantir sincronismo

## Tecnologias Usadas

- **Python 3.x**
- Biblioteca pyautogui (controle do mouse e teclado)
- Biblioteca pandas (importação e manipulação de dados CSV)

## Instruções para rodar

- Instale as dependências:
  ```
  pip install pyautogui pandas
  ```
- Ajuste as posições do mouse (x, y) conforme seu monitor e tela do sistema.
- Atualize o caminho do arquivo CSV no código (importar_tabela).
- Execute o script Python.

## Autor

[Yuri Ferreira Gomes](https://github.com/devyurifg)  

📧 devyurifg@gmail.com
