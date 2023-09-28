// método da bisseção
clear
clc

function y = funcao(x)
    y = x**3-7*x**2+14*x-6
endfunction

function data = bis(x0, x1, err)
    f0 = funcao(x0)
    f1 = funcao(x1)
    contador = 0
    
    // disp(x0, x1)
    
    while(1)
        
        if f0 * f1 < 0 then
            xm = (x0 + x1)/2
            
            fm = funcao(xm)
            
            if  f0 * fm < 0 then
                x1 = xm
            else
                x0 = xm
            end
            
            if (abs(x1 - x0) < err) then
                data = [xm, contador]
                break
            else
                contador = contador + 1
                continue
            end
        end
     end
endfunction

info = bis(0, 1, 0.01)
disp(info)
