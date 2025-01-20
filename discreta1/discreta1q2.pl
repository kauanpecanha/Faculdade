aluno(joao, calculo).
aluno(maria, calculo).
aluno(joel, programacao).
aluno(joel, estrutura).
frequenta(joao, puc).
frequenta(maria, puc).
frequenta(joel, iprj).
professor(carlos, calculo).
professor(ana_paula, estrutura).
professor(pedro, programacao).
funcionario(pedro, iprj).
funcionario(ana_paula, puc).
funcionario(carlos, puc).

aluno_de(Y, X) :- aluno(Y, Z), professor(X, Z).

associado(X, Y) :- funcionario(X, Y) ; frequenta(X, Y).
