import pytest

class Product: 
    def __init__(self, category, pct_size, name):
        self.category = category
        self.pct_size = pct_size
        self.name = name 


    def register_new_product(self, categoria, tamanho, nome_produto):
        if tamanho not in ["P (100 g)", "M (300g)", "G (500g)"]:
            return False
        categorias_validas = ["Banana", "Batata", "Amendoim"]
        if categoria not in categorias_validas:
            return False

        if len(nome_produto) > 100:
            return False

        return True


def test_register_new_product():
    product = Product("default_category", "default_size", "default_name")
   
    assert product.register_new_product("Banana", "P (100 g)", "Produto válido") == True
    assert product.register_new_product("Banana", "Tamanho Inválido", "Produto inválido") == False
    assert product.register_new_product("Categoria Inválida", "P (100 g)", "Produto inválido") == False
    assert product.register_new_product("Banana", "P (100 g)", "Nome de produto muito longo" * 10) == False
