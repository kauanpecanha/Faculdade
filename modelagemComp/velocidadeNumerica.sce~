clear
clc
function[v] = calc(key, va, t)
    
    //              definição das constantes
    g = 9.8
    c = 12.5
    m = 68.1
    
    v = va + (g - (c/m)*(va)) * (t(key) - t(key-1))
    
endfunction

// primeira função
v = zeros(1, 10)
t = 0:1:9

for i = 2 : 10
    v(i) = calc(i, v(i-1), t)
end

plot(t, v)
