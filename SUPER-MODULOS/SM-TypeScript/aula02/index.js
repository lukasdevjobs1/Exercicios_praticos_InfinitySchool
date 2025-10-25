// const listaUsuarios: (string | number)[] = ["lukas", "25", "true", 25] // array de strings ou numbers
// const listaPessoas: string[] | boolean[] = ["lukas", "25", "true"] // array de strings ou booleans
const listaPessoas = {
    nome: "lukas",
    idade: 31,
    cidade: "fortaleza",
    profissao: "programador",
    saudar(texto) {
        console.log(`Ola, ${texto} ${this.nome}`); // 'Ola, (texto) ${this.nome}';
    },
};
console.log(listaPessoas);
export {};
