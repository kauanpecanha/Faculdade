livro(os_maias).
autor(eça_de_queiroz).
nacionalidade(eça_de_queiroz, português).
escreveu(X, Y) :- autor(X), livro(Y).
romance(os_maias).