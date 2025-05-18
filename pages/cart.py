class CartPage:
    def __init__(self, page):
        self.page = page
        self.nome_produto = page.locator(".inventory_item_name")
        self.botao_remover = page.locator(".cart_button")
        self.botao_voltar_comprar = page.locator('[data-test="continue-shopping"]')

    async def get_nomes_dos_produtos(self):
        return await self.nome_produto.all_text_contents()

    async def remover_item(self):
        await self.botao_remover.first.click()

    async def continuar_comprando(self):
        await self.botao_voltar_comprar.click()