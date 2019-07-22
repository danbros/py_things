#!/usr/bin/env python3

# author @danbros
# Pset2 do curso MITx: 6.00.1x (edX)
"""
Calcular o valor mais baixo (onde média é constante, = min ou max) necessário
para pagar um débito em doze vezes usando um método recursivo.
"""
balance = 87855
annualInterestRate = 0.21

interest = 1 + annualInterestRate / 12
xmin = balance / 12
xmax = balance * (interest + 1)

def solver_pay2(xmin, xmax):
    bal = balance
    xmid = (xmin + xmax) / 2
    
    for _ in range(12):
        bal = (bal - xmid) * interest

    if xmid == xmin or xmid == xmax:
        return xmid
    if bal < 0:
        return solver_pay2(xmin, xmid)
    elif bal > 0:
        return solver_pay2(xmid, xmax)

print("Lowest Payment: ", round(solver_pay2(xmin, xmax), 2))