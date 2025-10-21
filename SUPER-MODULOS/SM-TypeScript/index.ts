//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 1- Crie três variáveis chamadas nome, idade e ativo.

// let nome: string = "Nome";
// let idade: number = 0;
// let ativo: boolean = false;

// function cadastrar(nome: string, idade: number, ativo: boolean): void {
//   console.log(`Nome: ${nome}, Idade: ${idade}, Ativo: ${ativo}`);
// }

// cadastrar(nome, idade, ativo);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 2- Crie duas variáveis numéricas e exiba no console:

// let num1 = 10; // primeira variável numérica
// let num2 = 5; // segunda variável numérica
// let resultado = num1 + num2; // soma das duas variáveis

// console.log(`A soma de ${num1} e ${num2} é: ${resultado}`);

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 3- Corrija as variáveis e funções a seguir:
// let nome: string = "LukG";
// let idade: number = 25;

// function mostrarNome(nome: string): string {
//   return nome;
// }

// let preco: number = 50;
// console.log(preco = 50);

// function dobrarNumero(num: number): number {
//   return num * 2;
// }

// let ativo: boolean = true;

// function cumprimentar(nome: string): string {
//   return "Olá, " + nome;
// }

// // exemplos de uso
// console.log(mostrarNome(nome));
// console.log(dobrarNumero(10));
// console.log(cumprimentar(nome));

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// 4- Crie uma variável temPermissao (boolean). Depois, crie uma função que receba esse valor e retorne:

let temPermissao: boolean = true;

function verificarAcesso(temPermissao: boolean): string {
  return temPermissao ? "Acesso permitido" : "Acesso negado";
}

// exemplo de uso
console.log(verificarAcesso(temPermissao));
