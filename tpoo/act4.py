n = int(input("Ingresa la cantidad de elementos: "))
res = []
sum = 0

for i in range(0, n):
    name = input("Ingresa el nombre: ")
    price = int(input("Ingresa la cantidad: ")) 
    res.append({'name': name, 'price': price})
    sum += price

# Imprimir
print("\nBienvenido a HEB\nProductos:")
for i, dict in enumerate(res):
    print('{} {:<10}  ${} pesos'.format(i + 1, dict['name'], dict['price']))

print("\nTotal a pagar: ${} pesos".format(sum))
print("HEB agradece su compra")