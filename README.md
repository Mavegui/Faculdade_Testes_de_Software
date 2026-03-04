# Faculdade Engenharia de Software

Este repositório reúne exemplos práticos da atividade proposta em Python, desenvolvido para a disciplina de Testes e Manutenção de Software. O projeto funciona como um repositório de estudos, com o intuito de promover o aprendizado mútuo através da exploração de algumas formas de testes.

## Estrutura do Projeto

- `maior_ou_menor.py` - Funções de maior ou menor, código base para realização dos testes de caixa branca.
- `test_Unittest.py` - Casos de teste usando `unittest`.
- `Usando_DocTest.py` - Demonstrações de `doctest`.

## Como usar

1. Tenha o Python 3.10+ no seu ambiente.
2. Crie um ambiente virtual e inicialize.
3. Executar código principal:
   ```bash
   python3 maior_ou_menor.py
   ```
2. Executar o DocTest:
   - O `-v` é importante usar para ver os resultados.
   ```bash
   python3 Usando_DocTest.py -v
   ```
3. Executar Unittest:
   ```bash
   python3 -m unittest test_Unittest.py
   ```

## Contribuições

Sinta-se à vontade para abrir issues ou pull requests para melhorar os exemplos ou adicionar novos testes.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
