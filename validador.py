# Sistema de Controle de Acesso Baseado em Funções (RBAC)
# Estudo de IAM - Identity and Access Management

# Banco de dados simulado de usuários, suas funções e permissões
usuarios_db = {
    "admin_thiago": {"role": "admin", "status": "ativo"},
    "analista_soc": {"role": "operador", "status": "ativo"},
    "estagiario_ti": {"role": "leitura", "status": "ativo"},
    "ex_funcionario": {"role": "admin", "status": "inativo"}
}

permissoes_por_role = {
    "admin": ["visualizar_logs", "editar_acessos", "deletar_usuario"],
    "operador": ["visualizar_logs", "editar_acessos"],
    "leitura": ["visualizar_logs"]
}

def verificar_acesso(username, acao_desejada):
    usuario = usuarios_db.get(username)
    
    # 1. Verificação de Identidade (Autenticação)
    if not usuario:
        return "❌ ERRO: Usuário não encontrado no diretório."
    
    # 2. Verificação de Status (Ciclo de Vida do Usuário)
    if usuario["status"] == "inativo":
        return "⚠️ ALERTA: Conta desativada. Bloqueando tentativa de acesso."
    
    # 3. Verificação de Permissão (Autorização)
    role = usuario["role"]
    if acao_desejada in permissoes_por_role.get(role, []):
        return f"✅ SUCESSO: Acesso concedido para '{acao_desejada}' ao usuário {username}."
    else:
        return f"🚫 NEGADO: O perfil '{role}' não possui privilégios para '{acao_desejada}'."

# Exemplo de Teste
print(verificar_acesso("admin_thiago", "deletar_usuario"))
print(verificar_acesso("estagiario_ti", "editar_acessos"))
print(verificar_acesso("ex_funcionario", "visualizar_logs"))
