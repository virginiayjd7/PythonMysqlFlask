num = {
    "0":"cero",
    "1":"uno",
    "2":"dos",
    "3":"tres",
    "4":"cuatro",
    "5":"cinco",
    "6":"seis",
    "7":"siete",
    "8":"ocho",
    "9":"nueve"
}
texto = input('ingrese un numero:')

textof =''
for letra in texto:
    textof += num[letra]+' '
print(textof)