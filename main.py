def calcular_inss(salario):
    # Regra do Teto: Ninguém paga desconto sobre o que passa de 7.786,02
    if salario > 7786.02:
        valor_base = 7786.02
    else:
        valor_base = salario

    desconto = 0

    # 1º Degrau (Até 1.412,00) -> 7,5%
    if valor_base <= 1412.00:
        return valor_base * 0.075
    else:
        desconto += 1412.00 * 0.075

    # 2º Degrau (Até 2.666,68) -> 9%
    if valor_base <= 2666.68:
        desconto += (valor_base - 1412.00) * 0.09
        return desconto
    else:
        desconto += (2666.68 - 1412.00) * 0.09

    # 3º Degrau (Até 4.000,03) -> 12%
    if valor_base <= 4000.03:
        desconto += (valor_base - 2666.68) * 0.12
        return desconto
    else:
        desconto += (4000.03 - 2666.68) * 0.12

    # 4º Degrau (Até o Teto) -> 14%
    desconto += (valor_base - 4000.03) * 0.14

    return desconto

# --- Começo do Programa ---
print("--- Calculadora de Salário Líquido (INSS) ---")

# Pedimos o salário bruto (usamos float porque tem centavos)
bruto = float(input("Digite o seu salário bruto: R$ "))

# Chamamos a função mágica que criamos lá em cima
valor_inss = calcular_inss(bruto)

# Fazemos a conta final
liquido = bruto - valor_inss

# Mostramos o resultado formatado com 2 casas decimais
print(f"\n--- Resultado ---")
print(f"Salário Bruto:   R$ {bruto:.2f}")
print(f"Desconto INSS:   R$ {valor_inss:.2f}")
print(f"Salário Líquido: R$ {liquido:.2f}")