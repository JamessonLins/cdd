ano=int(input("Informe o ano que nasceu?\n"))
mes=int(input("Informe o mes que nasceu?\n"))
dia=int(input("Informe o dia que nasceu?\n"))

cal_ano=   ano  * 365
cal_mes=  mes  * 30
cal_dia=  cal_mes+cal_ano+dia
print(f"A quantidade de dia em anos é {cal_ano}")
print(f"A quantidade de dia em mes é {cal_mes}")
print(f"A quantidade de dia em dia é {cal_dia}")