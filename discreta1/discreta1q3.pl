progenitor(joão, helena).
progenitor(joão, joana).
progenitor(maria, helena).
progenitor(maria, joana).

progenitor(joão, mário).

progenitor(helena, carlos).
progenitor(mário, carlos).

homem(joão).
homem(mário).
homem(carlos).
mulher(maria).
mulher(helena).
mulher(joana).

irmão(X, Y) :- homem(X),progenitor(Z, X),progenitor(Z, Y).
irmã(X, Y) :- mulher(X),progenitor(Z, X),progenitor(Z, Y).

irmãos(X, Y) :- irmão(X, Y) ; irmã(X, Y).

descendente(X, Y) :- progenitor(Y, X).
mãe(X, Y) :- mulher(X), progenitor(X, Y).
pai(X, Y) :- homem(X), progenitor(X, Y).
avô(X, Y) :- homem(X), progenitor(X,Z), progenitor(Z,Y).
avó(X, Y) :- mulher(X), progenitor(X,Z), progenitor(Z,Y).