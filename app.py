receitas=int(input("Digite o total de despesas: "))
despesas=int(input("Digite o total de receitas: "))
saldo=receitas-despesas
if(saldo>0):
    print("Saldo positivo: ",saldo)
else:
    print("Saldo negativo ou zero: ",saldo)