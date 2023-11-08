saludo:str = "hola mundo desde github codespaces"

# print(saludo)

# Array \ str ==> list

my_first_list:list = [1,2]

my_first_list.append("cacafuti")

# print( len(my_first_list) ) #length

my_first_list.append([',','~', '-'])

# print(my_first_list)

# for e in my_first_list:
    # print(e)

fruits:list = ['grape', 'apple', 'orange', 'strawberry', 'blueberry']
frutas:list = ["🍎", "🍌", "🍇", "🍊", "🍓", "🍍", "🥝", "🥥", "🍒", "🍑"]+fruits

fruits.insert(1,'banana')

two_fruits:list = fruits[0:4]
two_fruits2:list = fruits[:4]
two_fruits3:list = fruits[:4][::-1]
last_fruits:list = fruits[3:]
print(two_fruits)
print(two_fruits2)
print(two_fruits3)
print(last_fruits)

indice = 1

for fruit in fruits:
    print(f"item #{indice} => con fruta {fruit:_^15}")
    indice += 1

for indice, fruit in enumerate(fruits, start=1):
    print(f"item #{indice} => con fruta {fruit:_^15}")
    indice += 1

#------------------------------------------

dato:tuple = ('uno', ['dos']) # la tupla es no mutable
# dato[0] = 'tres' da ERROR

#------------------------------------------

# Diccionarios

matias:dict = {
    "nombre": "Matías",
    "DNI": 98654321,
    "status": True,
    "lang":['java', 'JS'],
    ('a','b'):'soy una tupla'
}

print(matias)
print(matias.items())

for k,v in matias.items():
    print(f"{k} -> {v}")

print(sum([1,2,3,4,5,6]))

for index, fruta in enumerate(fruits):
    if fruta == 'apple':
        fruits.pop(index)

#list complrehension

nuevas_frutas_sin_grapes = [
    fruta # Variable que va a quedar
    for fruta in fruits # iteración
    if fruta != 'grape' # condicion
]

print(nuevas_frutas_sin_grapes)
print(fruits)

#------------------------------------------

# dict comprehention

usuarios:list = [
    "John",
    "Hecotr",
    "Ale",
    "Gastón",
]

usuarios_cbu:list = [
    "cuv-129837918273981",
    "cuv-908980985049580",
    "cuv-987981212112123",
    "cuv-111111122222333",
]

## zip

cuenta_usuario = zip(usuarios, usuarios_cbu)

dict_usuario:dict = {
    nombre:cbu
    for nombre, cbu in
    list(cuenta_usuario)
}
print(dict_usuario)