function exemploTiposBasicos(nome: string, idade: number, cidade: string) {
  // Exemplos de tipos básicos em TypeScript
  return nome + " tem " + idade + " anos e mora em " + cidade + ".";
}
let nome: string = "lukas";
let idade: number = 31;
let cidade: string = "fortaleza";

console.log(exemploTiposBasicos(nome, idade, cidade));

// string : Representa uma sequência de caracteres, como "Olá, mundo!".

// boolean : Representa um valor lógico, verdadeiro ou falso.

// number : Representa um valor numérico, como 42.

// null :  Representa a intencional ausência de qualquer valor de objeto.

// undefined : Representa a ausência de qualquer valor de objeto em casos em que uma variável não foi atribuída um valor.

// [] : Uma array sem elementos.
// {} : Um objeto sem propriedades.
// () :  Uma chamada de função vazia ou uma expressão vazia.

// any :  Um tipo que pode representar qualquer valor.

// void : Um tipo de retorno que indica que uma função não retorna um valor.

// unknown : Um tipo que representa um valor que pode ser conhecido em tempo de execução, mas não em tempo de compilação

// never : Um tipo que representa um valor que nunca ocorrerá. É frequentemente usado para indicar que uma função nunca retornará
