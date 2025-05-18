Casos de teste:


1.	Login com credenciais válidas

Dado que o usuário está na tela de login  
Quando preenche os campos de usuário e senha com valores válidos  
E clica no botão de login  
Então ele deve ser redirecionado para a tela de inventário

2. Login com usuário inválido

Dado que o usuário está na tela de login  
Quando preenche o campo de senha com um valor válido  
E o campo de usuário com um valor inválido  
E clica no botão de login  
Então uma mensagem de erro deve ser exibida informando usuário ou senha incorretos

3. Login com senha inválida

Dado que o usuário está na tela de login  
Quando preenche o campo de usuário com um valor válido  
E o campo de senha com um valor inválido  
E clica no botão de login  
Então uma mensagem de erro deve ser exibida informando usuário ou senha incorretos

4. Adicionar um item ao carrinho

Dado que o usuário está logado e na tela de inventário  
Quando clica no botão “Add to cart” de um produto  
Então o ícone do carrinho deve exibir a quantidade 1

5. Adicionar um item ao carrinho e ver se o item correto está no carrinho

Dado que o usuário está logado e adicionou um item ao carrinho  
Quando acessa a tela de carrinho  
Então o nome do produto adicionado deve estar listado corretamente

6. Remover item do carrinho -> via inventory

Dado que o usuário adicionou um item ao carrinho na tela de inventário  
Quando clica no botão “Remove” daquele item  
Então o carrinho deve voltar ao estado vazio

7. Remover item do carrinho -> via cart

Dado que o usuário adicionou um item ao carrinho  
E acessou a tela de carrinho  
Quando clica no botão “Remove” do item  
Então o produto deve ser removido da lista

8.	Ordenar por preço

Dado que o usuário está logado e na tela de inventário  
Quando seleciona a opção “Price (low to high)” no dropdown de ordenação  
Então os produtos devem ser exibidos em ordem crescente de preço

9.	Finalizar compra com sucesso

Dado que o usuário está logado com um item no carrinho  
Quando acessa o carrinho e preenche os dados do checkout corretamente  
E clica em “Finish”  
Então a mensagem “Thank you for your order!” deve ser exibida

10.	Logout

Dado que o usuário está logado  
Quando acessa o menu lateral e clica em “Logout”  
Então deve ser redirecionado para a tela de login

