"""João Papo-de-Pescador, a good man, bought a microcomputer to control the daily yield of his work. Every time he brings a weight of fish greater than that established by the fishing regulations of the state of São Paulo (50 kilos), he must pay a fine of R$ 4,00 per excess kilo. João needs you to make a program that reads the variable weight (weight of fish) and calculates the excess. Record in the variable excess the amount of kilos beyond the limit and in the variable fine the amount of the fine that João will have to pay. Print the program data with the appropriate messages."""

weight = float(input("João, entre com o total de quilos pescados: "))
allowance = 50.0
fine_rate =  4.0
if weight > allowance:
    excess = weight - allowance
    fine = excess * fine_rate
    print(f"João, você pagará uma multa de R$ {fine:.2f}".replace('.', ',')+".")
else:
    print(f"Parabéns, João! Sem multas para você hoje! Você pescou um total de {weight} quilos!")
