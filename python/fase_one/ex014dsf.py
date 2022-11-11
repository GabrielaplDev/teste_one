# Escreva um programa que converta uma temperatura digitada em °c e converta para °f

cel = float(input('Digite a temperatura em °c: '))
fare = cel * 1.8 + 32

# Outra forma // fare = ((9 * cel) / 5) + 32

print('{:.2f}°c corresponde a: {:.2f}°f '.format(cel, fare))
