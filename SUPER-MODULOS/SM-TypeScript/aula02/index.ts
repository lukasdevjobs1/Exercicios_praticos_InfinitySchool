// const listaUsuarios: (string | number)[] = ["lukas", "25", "true", 25] // array de strings ou numbers
// const listaPessoas: string[] | boolean[] = ["lukas", "25", "true"] // array de strings ou booleans

// const listaNumeros: Array<number> = [1, 2, 3, 4, 5] // array de numbers generico

// const tuplaUsuarios: [string, number, boolean] = ["lukas", 25, true]   // tupla

// const listaUsuarios: string[] = ["lukas", "31", "fortaleza"];

// const listaPessoas: boolean[] = [true, false, true];

// const listaNumeros: number[] = [1, 2, 3, 4, 5];

// const listaArmazenamento: (number | string)[] = [1, 2, 3, 4, 5, "lukas"];

// console.log(listaUsuarios);
// console.log(listaPessoas);
// console.log(listaNumeros);
// console.log(listaArmazenamento);

interface Pessoas {
  nome: string;
  idade: number;
  cidade: string;
  profissao?: string;
  saudar(texto: string): void;
}

const listaPessoas: Pessoas = {
  nome: "lukas",
  idade: 31,
  cidade: "fortaleza",
  profissao: "programador",

  saudar(texto: string) {
    console.log(`Ola, ${texto} ${this.nome}`); // 'Ola, (texto) ${this.nome}';
  },
};

console.log(listaPessoas);
