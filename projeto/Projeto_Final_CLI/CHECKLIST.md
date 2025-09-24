# Checklist de Desenvolvimento

## Funcionalidades Core
- [ ] Menu em loop com 8 opções
- [ ] Adicionar despesa com validação
- [ ] Listar despesas formatadas
- [ ] Filtrar por categoria
- [ ] Calcular total por categoria
- [ ] Calcular total geral
- [ ] Salvar em CSV
- [ ] Carregar de CSV
- [ ] Sair do programa

## Validações
- [ ] Título obrigatório (não vazio)
- [ ] Valor obrigatório (float > 0)
- [ ] Categoria obrigatória (não vazia)
- [ ] Data opcional (formato AAAA-MM-DD)
- [ ] Tratamento de erros sem quebrar programa

## Estrutura de Dados
- [ ] Lista de dicionários para despesas
- [ ] Formato: {"titulo": str, "valor": float, "categoria": str, "data": str}

## Persistência
- [ ] Formato CSV: titulo;valor;categoria;data
- [ ] Salvar preserva todos os campos
- [ ] Carregar ignora linhas malformadas com aviso
- [ ] Arquivo legível manualmente

## Qualidade do Código
- [ ] Funções puras e pequenas
- [ ] Nomes claros e descritivos
- [ ] Sem bibliotecas externas
- [ ] Sem POO (apenas funções)
- [ ] Bloco main com loop do menu

## Testes Manuais
- [ ] Iniciar sem arquivo existente
- [ ] Adicionar despesa válida
- [ ] Adicionar despesa com dados inválidos
- [ ] Listar despesas vazias
- [ ] Listar despesas com dados
- [ ] Filtrar categoria existente
- [ ] Filtrar categoria inexistente
- [ ] Calcular totais corretos
- [ ] Salvar arquivo
- [ ] Carregar arquivo
- [ ] Carregar arquivo com linhas malformadas

## Caminho Feliz Completo
- [ ] 1. Adicionar despesa
- [ ] 2. Listar despesas
- [ ] 3. Filtrar por categoria
- [ ] 4. Totalizar por categoria
- [ ] 5. Total geral
- [ ] 6. Salvar em arquivo
- [ ] 7. Carregar do arquivo
- [ ] 8. Listar novamente para confirmar