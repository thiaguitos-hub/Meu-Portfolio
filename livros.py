best_seller = bool(input('O livro é um best-seller?'))
lancado_ha_2_anos = bool(input('O livro foi lançado há mais de 2 anos? (verdadeiro ou falso):'))
quantidade_livros = int(input('Quantos livros você quer comprar?'))
preco_livro = float(input('Qual o preço do livro?'))
desconto = 20
if best_seller or lancado_ha_2_anos:
    desconto += 20
    if quantidade_livros > 3:
        desconto += 5
    preco_final = preco_livro *(1-desconto /100)* quantidade_livros
    print(f'O preço final após os descontos é de R${preco_final:.2f}.')