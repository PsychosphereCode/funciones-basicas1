#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#  imprime 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# undifined porque la primera funcion nunca fue definida


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#  retorna 5 por lo que imprime 5 y el 10 no se alcanza a devolver.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# retorna 5 y emprime 5, la linea print(10) no se alcanza a ejecutar


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# imprime un 5 solamente cuando se llama la funcion (imprime la linea 37)


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# no imprime nada porque no puede sumarlos al llamar a la funcion add


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# imprime un 25 porque esta concatenando el 2 y el 5 gracias a str


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# 100 y luego 10 porque imprime b en la linea 63 y luego se salta el primer if ya que 100 no es menor que 10, entra al else y devuelve un 10 y luego imprime el return que dio la funcion


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# 7, 14, 7+14 (21).... imprime 7 cuando llama a la funcion con los argumentos 2,3 porque 2 si es menor que 3, luego imprime 14 cuando los argumentos 5,3 estan en el llamado a la funcion y imprime 14 y luego retorna un 7 y un 14 que se suman y da 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# retorna b+c que cuando se llama la funcion en el print linea 92 son 3 y 5, por lo que imprime 8.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# 500, 500, 300, 500. 


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# 500, 500, 300, 500    el ultimo 500 me enreda pero entiendo que es porque no estoy almacenando el llamado a la funcion en ninguna variable por lo que imprime 500 de nuevo que es el valor de b antes de iniciar la funcion


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# 500, 500, 300, 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# 1, 3, 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# 1,3, 5, 10


