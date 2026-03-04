# Validador de Acesso Simples
# Demonstração de condicionais, listas e entrada de dados

usuarios_autorizados = ["admin", "thiago_dev", "analista_spc"]

print("--- Sistema de Validação de Acesso ---")
usuario = input("Digite o seu nome de usuário: ").lower()

if usuario in usuarios_autorizados:
    print(f"Acesso concedido! Bem-vindo, {usuario}.")
else:
    print("Alerta: Usuário não autorizado. Tentativa registrada.")
