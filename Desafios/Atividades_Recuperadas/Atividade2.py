def normalizar_email(email: str) -> str:
    email = email.strip().lower()
    
    if email.count('@') != 1:
        raise ValueError("Email deve conter exatamente um @")
    
    usuario, dominio = email.split('@')
    
    if not usuario or not dominio or '.' not in dominio:
        raise ValueError("Email deve ter usuário@dominio.extensão")
    
    return email

# Input do usuário
email_input = input("Digite um email: ")
try:
    email_normalizado = normalizar_email(email_input)
    print(f"Email normalizado: {email_normalizado}")
except ValueError as e:
    print(f"Erro: {e}")