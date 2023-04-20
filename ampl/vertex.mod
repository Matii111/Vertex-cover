set V;
set E within V cross V;

var x{V} binary;

minimize obj: sum{i in V} x[i];

subject to cover{(i,j) in E}: x[i] + x[j] >= 1;