import pytest
from pages.login import LoginPage
from pages.inventory import InventoryPage

@pytest.mark.asyncio
async def test_adicionar_item_ao_carrinho(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    await inventory.adicionar_primeiro_item_ao_carrinho()

    quantidade = await inventory.get_quantidade_itens_no_carrinho()
    assert quantidade == "1"

@pytest.mark.asyncio
async def test_remover_item_do_carrinho(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    await inventory.adicionar_primeiro_item_ao_carrinho()
    await inventory.remover_primeiro_item_do_carrinho()

    quantidade = await inventory.get_quantidade_itens_no_carrinho()
    assert quantidade == "0"

@pytest.mark.asyncio
async def test_ordenar_por_preco_crescente(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    await inventory.ordenar_por_preco_crescente()

    precos = await inventory.get_precos_visiveis()
    precos_ordenados = sorted(precos)

    assert precos == precos_ordenados