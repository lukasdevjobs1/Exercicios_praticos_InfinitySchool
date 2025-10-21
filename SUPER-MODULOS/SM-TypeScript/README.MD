# SM-TypeScript — Super Módulo de TypeScript

## Resumo

Coleção de exercícios práticos e notas para aprender os conceitos fundamentais do TypeScript e como integrá‑lo a um front-end simples.

## O que é o TypeScript?

TypeScript (TS) é um superset do JavaScript que adiciona tipagem estática opcional e recursos de orientação a objetos. TS é transpilado para JavaScript (JS) — o navegador/econtrorno executa o JS gerado.

## Principais intenções

- Adicionar tipagem estática ao JS.
- Detectar erros em tempo de desenvolvimento/compilação.
- Melhorar manutenção e refatoração de código.

## Diferenças principais (JS × TS)

- JS: tipagem dinâmica (checagem em runtime).
- TS: tipagem estática opcional (checagem em tempo de compilação).
- TS precisa ser transpilado para JS para rodar no navegador.

## Tipos de dados básicos

- string
- number
- boolean
- undefined
- null
- any (tipo curinga — evita checagem; usar com cautela)

## Tipagem: explícita vs inferência

- Tipagem explícita: declarar o tipo ao criar a variável. Ex.: `let idade: number = 25;`
- Inferência: TS deduz o tipo a partir do valor inicial e restringe alterações posteriores.

## Exemplo rápido

```ts
let nome: string = "Maria";
function somar(n1: number, n2: number): number {
  return n1 + n2;
}
```

## Por que compilar para JS?

- Navegadores não entendem TS nativamente.
  Compatibilidade universal: navegadores e ambientes (Node.js) entendem JS. TS é convertido para JS puro antes da execução.

## Como começar (rápido)

Requisitos:

Node.js
VS Code (recomendado)

# Comandos úteis:

Instalar TypeScript globalmente (opcional): npm install -g typescript
Inicializar tsconfig: tsc --init
Compilar um arquivo: npx tsc index.ts ou npx tsc (com tsconfig)
Servir arquivos (módulos ES precisam de HTTP): usar Live Server no VS Code ou http-server

## Boas práticas:

Usar tsconfig.json com "strict": true para maior segurança.
Preferir tipagem explícita em APIs, interação com DOM ou dados externos.
Evitar any sempre que possível.
Não editar o arquivo JavaScript gerado manualmente — editar .ts e recompilar.

## Estrutura sugerida do projeto:

index.ts — exercícios e lógica em TypeScript
index.js — compilação gerada (não versionar se preferir)
index.html — página que importa index.js como module
README.md — documentação

## Observações sobre integração com HTML:

Ao usar <script type="module" src="index.js"></script> abra o projeto via servidor HTTP (file:// pode bloquear imports).
Verifique o caminho de saída do compilador (outDir/rootDir) caso o arquivo gerado não esteja na mesma pasta do index.html.

## Autor

Desenvolvido por [Lukas Gomes].

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Agradecimentos

Agradecimentos especiais à comunidade TypeScript e aos recursos online que facilitam o aprendizado desta poderosa linguagem.

## Recursos adicionais

- [Documentação oficial do TypeScript](https://www.typescriptlang.org/docs/)
- [Curso gratuito de TypeScript - Microsoft Learn](https://learn.microsoft.com/pt-br/training/paths/learn-typescript/)
- [TypeScript Deep Dive - Basarat Ali Syed](https://basarat.gitbook.io/typescript/)
- [TypeScript no GitHub](https://github.com/microsoft/TypeScript)

Sinta-se à vontade para contribuir com melhorias, sugestões ou correções através de pull requests!

## Contribuições
