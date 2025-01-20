pássaro(joão).
pássaro(pássaro).
peixe(pedro).
minhoca(maria).
gato(gato).
gato(chuck_norris).
pessoa(eu).
pessoa(pessoa).
pessoa(pessoas).
amigo(eu).

gosta(X, Y) :- pássaro(X), minhoca(Y) ; gato(X), peixe(Y) ; gato(X), pássaro(Y) ; amigo(X), amigo(Y).
come(X, Y) :- gato(X), comida(Y), gosta(X, Y).
amigo(X,Y) :- gato(X), peixe(Y) ; gato(X), pássaro(Y) ; gato(X), pessoa(Y).
comida(X) :- peixe(X);pássaro(X).
nome(meu_gato,chuck_norris).