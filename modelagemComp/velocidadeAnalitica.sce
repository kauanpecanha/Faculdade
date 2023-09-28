clear
clc

function v = velocidade(t)
    m = 68.1;
    c=12.5;
    g=9.8;
    v = (g * m / c) * ( 1 - exp(-c/m*t))
endfunction

// segunda função
t = linspace(0, 12)'
v = velocidade(t)
plot(t, v)
