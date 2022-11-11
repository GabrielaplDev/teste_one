# Faça um algoritimo que leia o preço de um produto e mostre seu novo preõ, com 5% de desconto

preco = float(input('Digite o valor do produto em R$: '))
novo = preco - (preco * 5 / 100)


print('O produto que custava R${:.2f}, na promoção com 5% de desconto, ira custar R${:.2f} '.format(preco, novo))
