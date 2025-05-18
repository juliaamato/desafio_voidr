class LoginPage:
    def __init__(self, page):
        self.page = page
        self.usuario_input = page.locator("#user-name")
        self.senha_input = page.locator("#password")
        self.botao_login= page.locator("#login-button")
        self.error_msg = page.locator('[data-test="error"]')

    async def goto(self):
        await self.page.goto("https://www.saucedemo.com/")

    async def login(self, username, password):
        await self.usuario_input.fill(username)
        await self.senha_input.fill(password)
        await self.botao_login.click()
