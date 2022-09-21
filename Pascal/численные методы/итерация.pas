program Итерация;
uses crt;
    const max_iter=100; 
var
  i :integer;
  x,x0,eps,M :real;
function F(x:real): real;
  begin
  F:=2-x-ln(x);
  end;
begin 
  clrscr;
  write('Введите приближенноё значение x='); 
  readln(x);
  write('Введите точность вычисления eps='); 
  readln(eps);
i:=0;
repeat
  M:=-(F(x+eps)-F(x-eps))/(2*eps); 
  x0:=x;
  x:=x0+F(x0)/M; inc(i); 
  writeln('--- Итерация ', i:3,' x=', x);
  writeln('F(x)=',F(x),'precision=', abs(x-x0));
until (abs(x-x0)<=eps)or(i>max_iter);
if (abs(x-x0)<=eps) then writeln('Ответ: X=', x)
else writeln('Ответ не найден. За ', max_iter:0,' шагов ');
Readln;
end.