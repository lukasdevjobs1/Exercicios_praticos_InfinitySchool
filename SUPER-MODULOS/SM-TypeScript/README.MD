# SM-TypeScript — Super Módulo de TypeScript <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>ts-node</title><path d="M11.999 0c-.196 0-.392.05-.568.153L2.026 5.58a1.135 1.135 0 00-.568.983V17.43c0 .406.216.781.568.984l5.787 3.344v-7.344H4.748v-1.943h8.342v1.943h-3.065v8.622l1.406.812c.351.203.784.203 1.136 0l2.317-1.338a3.958 3.958 0 01-1.195-1.413l1.801-1.042c.361.59.806 1.06 1.48 1.25l2.174-1.256c-.127-.568-.698-.823-1.584-1.21l-.553-.238c-1.596-.68-2.655-1.532-2.655-3.334 0-1.658 1.265-2.922 3.24-2.922 1.406 0 2.417.49 3.144 1.77l-1.723 1.105c-.379-.68-.79-.948-1.421-.948-.648 0-1.06.41-1.06.948 0 .663.412.932 1.36 1.343l.553.237c1.336.573 2.255 1.155 2.676 2.107l.853-.493c.352-.203.568-.578.568-.984V6.565c0-.406-.216-.782-.568-.984L12.567.153A1.134 1.134 0 0011.999 0z"/></svg>

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

Node.js - https://nodejs.org/pt


VS Code (recomendado) - https://code.visualstudio.com/

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

Desenvolvido por [Lukas Gomes - https://github.com/lukasdevjobs1

## Licença

Este projeto está licenciado sob a Licença MIT. 

## Agradecimentos

Agradecimentos especiais à comunidade TypeScript e aos recursos online que facilitam o aprendizado desta poderosa linguagem.

## Recursos adicionais

- [Documentação oficial do TypeScript](https://www.typescriptlang.org/docs/)
- [Curso gratuito de TypeScript - Microsoft Learn](https://learn.microsoft.com/pt-br/training/paths/learn-typescript/)
- [TypeScript Deep Dive - Basarat Ali Syed](https://basarat.gitbook.io/typescript/)
- [TypeScript no GitHub](https://github.com/microsoft/TypeScript)

Sinta-se à vontade para contribuir com melhorias, sugestões ou correções através de pull requests!

## Contribuições
