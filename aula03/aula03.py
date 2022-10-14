

salario_mensal = 2000
qtd_semanas = 4
dias_trabalhados_semana = 5
horas_diarias = 8



# Quantas horas trabalha por semana ?

qtd_horas_semanal = horas_diarias * dias_trabalhados_semana

print(qtd_horas_semanal) # resultado 40 horas semanais



# Quantas horas trabalha por mês ?

qtd_horas_mes = qtd_horas_semanal * qtd_semanas

print(qtd_horas_mes) # resultado 160 horas mês



# Qual salário por semana ?

salario_semanal = salario_mensal / qtd_semanas

print(salario_semanal) # Resultado R$ 500,00 por semana


# Qual salário por dia ?

salario_dia = salario_semanal / dias_trabalhados_semana

print(salario_dia) # Resultado R$ 100,00 por dia


# Qual salário por hora ? 

salario_hora = salario_dia / horas_diarias

print(salario_hora) # Resultado R$ 12,50 por hora de trabalho




# Forma simplificada

meu_salario = salario_mensal / qtd_horas_mes 

print(meu_salario) # Resultado R$ 12,50 por hora de trabalho