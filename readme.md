# superchips 

## Descrição

Superchips é uma fábrica de produtos alimentícios. Com foco na sua produção em batata e banana Chips com sua variedade de tamanho e sabores, presente a 8 anos no mercado tendo dificuldade em gerenciamento de estoque, devido o seu constante crescimento não esperado nos últimos anos. Atualmente trabalham 10 pessoas na empresa , que compartilham responsabilidades nos diversos setores operacionais: produção, empacotamento, estoque e entrega. 


## Funcionalidades Principais

- Cadastro de produtos 
- Atualização de estoque [in progress]
- Gerenciamento de usuários 
- Registro de pedidos e vendas [in progress]


## Instalação

1. Faça um clone do repositório em seu local 
2. Crie um ambiente virtual em seu repositório
3. Instale as dependências através do comando abaixo 

```bash
pip install -r requirements.txt
```

4. Execute os testes unitários através dos comandos abaixo :  
```bash
cd tests
pytest
```
você deverá receber uma resposta assim :

```bash
======================================== test session starts ========================================
platform win32 -- Python 3.11.4, pytest-7.4.3, pluggy-1.3.0
rootdir: C:\projetos\superchips-lib-repo\tests
plugins: mock-3.12.0
collected 7 items

test_get_main_components.py .                                                                  [ 14%]
test_get_usuarios_df.py s                                                                      [ 28%]
test_login.py ..                                                                               [ 57%]
test_register_new_product.py .                                                                 [ 71%]
test_show_product_info.py s                                                                    [ 85%]
test_show_user_info.py s                                                                       [100%]

=================================== 4 passed, 3 skipped in 6.44s ====================================
```
5. Execute o programa através do seguinte comando: 

```bash
streamlit run home.py
```