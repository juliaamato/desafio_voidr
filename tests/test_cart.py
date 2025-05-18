import pytest
from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage

@pytest.mark.asyncio
async def test_item_correto_no_carrinho(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    await inventory.adicionar_primeiro_item_ao_carrinho()
    await inventory.ir_para_o_carrinho()

    cart = CartPage(page)
    nomes = await cart.get_nomes_dos_produtos()

    assert "Sauce Labs Backpack" in nomes

@pytest.mark.asyncio
async def test_remover_item_do_carrinho_via_cart(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    await inventory.adicionar_primeiro_item_ao_carrinho()
    await inventory.ir_para_o_carrinho()

    cart = CartPage(page)
    await cart.remover_item()
    nomes = await cart.get_nomes_dos_produtos()

    assert "Sauce Labs Backpack" not in nomes

@pytest.mark.asyncio
async def test_adicionar_dois_itens_ao_carrinho(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    await inventory.adicionar_primeiro_item_ao_carrinho()
    await inventory.ir_para_o_carrinho()

    cart = CartPage(page)
    nomes = await cart.get_nomes_dos_produtos()
    assert "Sauce Labs Backpack" in nomes

    await cart.continuar_comprando()
    await inventory.adicionar_bike_light()
    await inventory.ir_para_o_carrinho()

    nomes_finais = await cart.get_nomes_dos_produtos()
    assert "Sauce Labs Backpack" in nomes_finais
    assert "Sauce Labs Bike Light" in nomes_finais

