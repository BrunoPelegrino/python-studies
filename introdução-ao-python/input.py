numbers = input('insira aqui seus números separados por um espaço')

numbers_arr = numbers.split(" ")

sum = 0

for numbers in numbers_arr:
    if not numbers.isdigit():
        print(f"Erro ao somar valores, {numbers} não é um digito")

    else:
        sum += int(numbers)

print(f"o valor final da soma de todos os numeros é {sum}")
