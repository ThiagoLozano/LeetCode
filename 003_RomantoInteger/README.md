# Desafio 003: Roman to Integer

## O que Fazer?
Os algarismos romanos são representados por sete símbolos diferentes  : I, V, X, L, e C.DM

Valor do símbolo
    I 1
    V 5
    X 10
    L 50
    C 100
    D 500
    M 1000

Por exemplo,  2é escrito II em algarismo romano, apenas duas unidades somadas. 12é escrito como  XII, que é simplesmente X + II. O número 27é escrito como XXVII, que é XX + V + II.

Os algarismos romanos são geralmente escritos do maior para o menor, da esquerda para a direita. No entanto, o número para quatro não é IIII. Em vez disso, o número quatro é escrito como IV. Como o um está antes do cinco, subtraímo-lo, totalizando quatro. O mesmo princípio se aplica ao número nove, que é escrito como IX. Existem seis casos em que a subtração é usada:

I pode ser colocado antes de V(5) e X(10) para formar 4 e 9. 
X pode ser colocado antes de L(50) e C(100) para formar 40 e 90. 
C pode ser colocado antes de D(500) e M(1000) para perfazer 400 e 900.

Dado um algarismo romano, converta-o para um número inteiro.


### Exemplo 1:
Entrada: s = "III"
Saída: 3

### Exemplo 2:
Entrada: s = "LVIII"
Saída: 58

### Exemplo 3:
Entrada: s = "MCMXCIV"
Saída: 1994
