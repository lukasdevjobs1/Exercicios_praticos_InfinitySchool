=
# 🎯 Desafio: Sistema de Gerenciamento de Funcionários

*Objetivo: Criar um sistema que gerencie uma lista de funcionários usando dicionários, com menu interativo.*

# 📋 Estrutura dos Dados
*Cada funcionário deve ser um dicionário com:*

```
{
    'id': int,
    'nome': str,
    'cargo': str,
    'salario': float,
    'departamento': str,
    'ativo': bool
}
```

# 🎮 Menu do Sistema
*Implemente as seguintes funcionalidades:*

* Cadastrar funcionário - Adicionar novo funcionário à lista
* Listar todos - Mostrar todos os funcionários formatados
* Buscar por ID - Encontrar funcionário específico
* Buscar por departamento - Filtrar funcionários por departamento
* Atualizar salário - Modificar salário de um funcionário
* Demitir funcionário - Alterar status para inativo
* Relatório salarial - Mostrar estatísticas (maior, menor, média)
* Funcionários ativos - Listar apenas funcionários ativos
* Exportar dados - Salvar lista em formato legível
* Sair

# 🔧 Requisitos Técnicos
*Validações obrigatórias:*

* ID deve ser único e positivo
* Nome não pode estar vazio
* Salário deve ser positivo
* ~~Tratar entradas inválidas sem quebrar o programa~~
