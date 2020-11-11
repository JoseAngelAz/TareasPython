var_uno = 5
var_dos = 20

mayor = var_uno > var_dos
menor = var_uno < var_dos
mayor_igual = var_uno >= var_dos
menor_igual = var_uno <= var_dos
igual = var_uno == var_dos
diferente = var_uno != var_dos

resultado = True and True and diferente
resultado2 = True and True and mayor
resultado3 = True or True and mayor #operador OR
resultadoIS = var_uno is var_dos
resultadonot = not True

print(resultadonot)
print(resultado)
print(resultado2)
print(resultadoIS," este es del IS")