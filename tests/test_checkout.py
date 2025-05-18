import pytest
from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage

@pytest.mark.asyncio
async def test_finalizar_compra_com_sucesso(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    await inventory.adicionar_primeiro_item_ao_carrinho()
    await inventory.ir_para_o_carrinho()

    cart = CartPage(page)
    await cart.remover_item()  # se quiser garantir que tem 1, pode remover essa linha
    await cart.page.locator('[data-test="checkout"]').click()

    checkout = CheckoutPage(page)
    await checkout.preencher_formulario("Julia", "Teste", "12345")
    await checkout.finalizar_compra()

    mensagem = await checkout.get_mensagem_sucesso()
    assert "Thank you for your order!" in mensagem
