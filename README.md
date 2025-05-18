Este repositório contém uma suite de testes automatizados utilizando Playwright com Python e Pytest. 
Os testes estão organizados em Page Objects e os casos de testes na estrutura BDD (Behavior-Driven Development).
Os cenários de teste estão no arquivo: test_cases.md
O relatório dos testes realizados estão no arquivo: relatorio_testes.txt

Para executar os testes siga os passos abaixo (você já deve ter python instalado):

 1- Clone o repositório
 2- Entre no diretório do repositório em questão
 3- No cmd crie uma env:
   Windows:
     1- python -m venv venv
     3- voidr-env\Scripts\activate
  Linux/MacOs:
     1- python3 -m venv venv
     2- source voidr-env/bin/activate
4- Instale os requirements: pip install -r requirements.txt
5- Execute os testes: python -m pytest -v ou pytest -v --tb=short --maxfail=1 > relatorio_testes.txt (caso queira gerar também um relatório de testes)
