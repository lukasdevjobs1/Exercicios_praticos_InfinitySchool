# Projeto Final - Controle de Gastos Pessoais em CLI

## Objetivo
Criar um aplicativo de linha de comando para registrar despesas e gerar um resumo simples. 
**Sem bibliotecas externas, sem POO.** Use apenas funções, listas, dicionários, condicionais e laços, com persistência em arquivo texto.

## Escopo Mínimo Obrigatório

### Menu em Loop
- Adicionar despesa
- Listar despesas  
- Filtrar por categoria
- Total por categoria
- Total geral
- Salvar em arquivo
- Carregar do arquivo
- Sair

### Estrutura de Despesa
- **título** (str) - obrigatório
- **valor** (float > 0) - obrigatório  
- **categoria** (str) - obrigatório, não vazia
- **data** (str) - opcional, formato AAAA-MM-DD com validação simples

### Validação de Entrada
- Campos obrigatórios preenchidos
- Valores numéricos válidos
- Categorias não vazias
- Formato de data simples (AAAA-MM-DD)
- Mensagens claras de erro e sucesso
- Programa não encerra com entrada inválida

### Persistência
- Arquivo .csv simples
- Uma despesa por linha
- Formato: título;valor;categoria;data

## Critérios de Aceitação

1. **Inicialização**: Programa inicia sem arquivo prévio e permite adicionar/listar despesas
2. **Listagem**: Mostra índice, título, valor com 2 casas, categoria e data (se houver)
3. **Filtros**: Funcionam mesmo com categorias inexistentes (lista vazia, sem erro)
4. **Totais**: Por categoria e geral corretos, arredondamento a 2 casas
5. **Persistência**: Salvar/carregar preservam campos, ignoram linhas malformadas com aviso
6. **Organização**: Funções puras e bloco main com loop do menu

## Funções Obrigatórias
- `adicionar_despesa()`
- `listar_despesas()`
- `filtrar_por_categoria()`
- `total_por_categoria()`
- `total_geral()`
- `salvar_arquivo()`
- `carregar_arquivo()`

## Checklist de Qualidade
- [ ] Programa não quebra com entradas inválidas
- [ ] Totais e filtros corretos
- [ ] Arquivo gerado é legível
- [ ] Funções pequenas e nomeadas claramente
- [ ] Caminho feliz completo: adicionar → listar → filtrar → totalizar → salvar → carregar → listar

## Entregáveis
1. **controle_gastos.py** - arquivo executável principal
2. **despesas.csv** - arquivo de exemplo gerado pelo app
3. **README.txt** - instruções de execução, funcionalidades, exemplos de uso