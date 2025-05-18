class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.botao_checkout= page.locator('[data-test="checkout"]')
        self.nome_input = page.locator('[data-test="firstName"]')
        self.sobrenome_input = page.locator('[data-test="lastName"]')
        self.cep_input = page.locator('[data-test="postalCode"]')
        self.botao_continue = page.locator('[data-test="continue"]')
        self.botao_finalizar = page.locator('[data-test="finish"]')
        self.mensagem_sucesso = page.locator(".complete-header")

    async def iniciar_checkout(self):
        await self.botao_checkout.click()

    async def preencher_formulario(self, nome, sobrenome, cep):
        await self.nome_input.fill(nome)
        await self.sobrenome_input.fill(sobrenome)
        await self.cep_input.fill(cep)
        await self.botao_continue.click()

    async def finalizar_compra(self):
        await self.botao_finalizar.click()

    async def get_mensagem_sucesso(self):
        return await self.mensagem_sucesso.text_content()
