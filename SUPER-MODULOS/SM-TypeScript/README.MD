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
