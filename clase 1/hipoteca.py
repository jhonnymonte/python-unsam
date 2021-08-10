saldo=500000
mes=0
total_pagado=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
    tasa_anual=0.05
    pago_extra = 1000
    mes=mes+1
    pago_mensual = 2684.11

    if saldo < pago_mensual:    
        pago_mensual = saldo
        total_pagado = total_pagado + pago_mensual
        saldo=0
    
    elif mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago_mensual = pago_mensual + pago_extra
        total_pagado= total_pagado + pago_mensual
        saldo = saldo * (1+tasa_anual/12) - pago_mensual

    else:
        pago_mensual=pago_mensual
        total_pagado= total_pagado + pago_mensual
        saldo = saldo * (1+tasa_anual/12) - pago_mensual
        

    print(f'{mes:3} ${total_pagado:<9.2f} ${saldo:0.2f}')

print("Cantidad de meses =", mes)
print("Total pagado =", round(total_pagado,2)) 
