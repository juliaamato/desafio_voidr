class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.botao_add_carrinho = page.locator("text=Add to cart")
        self.botao_remover = page.locator("text=Remove")
        self.qtd_itens_carrinho = page.locator(".shopping_cart_badge")
        self.icone_carrinho = page.locator(".shopping_cart_link")
        self.dropdown = page.locator('[data-test="product-sort-container"]')
        self.produtos_precos = page.locator(".inventory_item_price")
        self.botao_bike = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')

    async def adicionar_primeiro_item_ao_carrinho(self):
        await self.botao_add_carrinho.first.click()

    async def remover_primeiro_item_do_carrinho(self):
        await self.botao_remover.first.click()

    async def get_quantidade_itens_no_carrinho(self):
        if await self.qtd_itens_carrinho.is_visible():
            return await self.qtd_itens_carrinho.text_content()
        return "0"

    async def ir_para_o_carrinho(self):
        await self.icone_carrinho.click()
    
    async def ordenar_por_preco_crescente(self):
        await self.dropdown.select_option("lohi")

    async def get_precos_visiveis(self):
        precos_texto = await self.produtos_precos.all_text_contents()
        return [float(p.replace("$", "")) for p in precos_texto]
    
    async def adicionar_bike_light(self):
        await self.botao_bike.click()
