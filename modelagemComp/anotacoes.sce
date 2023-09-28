// Anotações úteis

//Comandos:
    // clc: comando para limpar o console
    // clear('<nome da variável>')

// Como definir variáveis:
    // definição de um vetor: a = [1, 2, 3]
    // definição de um vetor em coluna: a = [1; 2; 3]
    // definição de um vetor através de um intervalo: a = 1:3
    // definição de um vetor através de um intervalo com passos: a = 1:1:3 (passos de uma unidade)
    // definição de um vetor através do comando linspace: a = linspace()
    // definição de uma matriz com zeros 2 linhas por 3 colunas: A = zeros(2, 3)
    // definição de uma matriz com uns 2 linhas por 3 colunas: A = ones(2, 3)
    // definição de uma matriz identidade 3x3: c = eye(3, 3)
    // definição de uma matriz 5x5 com entradas aleatórias dentro do intervalo [0,1): B = rand(5, 5)
    
// Observações:
    // - Sempre começar os scripts no bloco de notas com: clear; clc

// scripts no bloco de notas
    // estruturas de repetição(abaixo, um exemplo)
    
        clear
        clc
        
        a = 0
        
        if a > 1 then
            a = a+1;
        elseif a < 1
            a = a-1;
        else
            disp('Esse número é exatamente igual a 1')
        end
        
        disp(a)

    // estruturas de repetição
    // for
    
        clear
        clc
        
        for n = 1:10
            x(n) = cos(n*%pi / 10);
        end
        
        for n=1:5
            for m=5:-1:1
                A(n,m) = n.^2 + m.^2
        end

    // criação de funções
    
        function[x, y] = myfunc(a, b)
            x = a+b;
            y=a-b;
        endfunction
        
        [x, y] = myfunc(3, 2)
        
        disp(x, y)

// concatenação de vetores

v = []
novo_item = 2
v = [v, novo_item]
