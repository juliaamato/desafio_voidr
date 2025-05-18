import pytest
from pages.login import LoginPage

@pytest.mark.asyncio
async def test_login_sucesso(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "secret_sauce")
    assert page.url.endswith("/inventory.html")

@pytest.mark.asyncio
async def test_login_falha_usuario_invalido(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("invalid_user", "secret_sauce")
    assert await login.error_msg.is_visible()

@pytest.mark.asyncio
async def test_login_falha_senha_invalida(page):
    login = LoginPage(page)
    await login.goto()
    await login.login("standard_user", "invalid_password")
    assert await login.error_msg.is_visible()

