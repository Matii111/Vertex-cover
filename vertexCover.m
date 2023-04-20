% Define el grafo
V = [1, 2, 3, 4, 5];
E = [1 2; 2 4; 3 4; 5 1; 5 3; 5 4];

% Número de vértices
n = length(V);

% Crea el problema de optimización
f = ones(n,1);
A = zeros(size(E,1),n);
for i = 1:size(E,1)
    A(i,E(i,:)) = 1;
end
b = ones(size(E,1),1);
intcon = 1:n;
lb = zeros(n,1);
ub = ones(n,1);

% Resuelve el problema
x = intlinprog(f,intcon,A,b,[],[],lb,ub);

% Muestra la solución
disp('Cobertura de vértices mínima:');
disp(V(logical(x)));

% Dibuja el grafo
G = graph(E(:,1),E(:,2));
h = plot(G,'Layout','force');
highlight(h,V(logical(x)),'NodeColor','r');

