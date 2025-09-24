# CONTROLE DE GASTOS PESSOAIS - CLI

## Como Executar
1. Abra o terminal/prompt de comando
2. Navegue até a pasta do projeto
3. Execute: python controle_gastos.py

## Funcionalidades

### 1. Adicionar Despesa
- Título: obrigatório, não pode ser vazio
- Valor: obrigatório, deve ser número maior que zero
- Categoria: obrigatória, não pode ser vazia
- Data: opcional, formato AAAA-MM-DD (ex: 2024-01-15)

### 2. Listar Despesas
- Mostra todas as despesas cadastradas
- Formato: índice, título, valor (R$ XX,XX), categoria, data

### 3. Filtrar por Categoria
- Digite o nome da categoria para ver apenas despesas dessa categoria
- Busca não diferencia maiúsculas/minúsculas

### 4. Total por Categoria
- Mostra o valor total gasto em cada categoria

### 5. Total Geral
- Mostra a soma de todas as despesas

### 6. Salvar em Arquivo
- Salva todas as despesas em arquivo CSV
- Formato: titulo;valor;categoria;data

### 7. Carregar do Arquivo
- Carrega despesas de um arquivo CSV
- Ignora linhas malformadas com aviso
- Adiciona às despesas já existentes na memória

### 8. Sair
- Encerra o programa

## Exemplos de Uso

### Exemplo 1 - Caminho Feliz Completo:
1. Adicionar despesa: "Almoço", 25.50, "Alimentação", "2024-01-15"
2. Adicionar despesa: "Gasolina", 80.00, "Transporte", "2024-01-15"
3. Listar despesas (mostra as 2 despesas)
4. Filtrar por "Alimentação" (mostra apenas o almoço)
5. Total por categoria (Alimentação: R$ 25,50, Transporte: R$ 80,00)
6. Total geral (R$ 105,50)
7. Salvar em "minhas_despesas.csv"
8. Carregar de "minhas_despesas.csv"

### Exemplo 2 - Tratamento de Erros:
- Título vazio → "Erro: Título é obrigatório!"
- Valor "abc" → "Erro: Valor deve ser um número válido!"
- Valor -10 → "Erro: Valor deve ser maior que zero!"
- Data "15/01/2024" → "Erro: Data deve estar no formato AAAA-MM-DD!"

## Formato do Arquivo CSV
```
Almoço;25.5;Alimentação;2024-01-15
Gasolina;80.0;Transporte;2024-01-15
Cinema;30.0;Lazer;
```

## Observações
- O programa não quebra com entradas inválidas
- Linhas malformadas no CSV são ignoradas com aviso
- Data é opcional (pode ficar em branco)
- Valores são sempre mostrados com 2 casas decimais
- Não usa bibliotecas externas além das padrão do Python