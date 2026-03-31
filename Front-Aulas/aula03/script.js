// // REVISÃO DE CONDICIONAIS (usando if, else if e else)
// const peso = Number(prompt("Digite o seu peso: ")) // STRING
// const altura = Number(prompt("Digite a sua altura: "))
// const imc = peso / (altura * altura)


// if(!peso || !altura){
//     alert("Ei ta faltando preencher um campo")
// }
// else if(imc < 18.5){
//     console.log(`Você está abaixo do peso com imc de ${imc.toFixed(2)}`)
// }
// else if(imc >= 18.5 && imc <= 24.99){
//     console.log(`Você está com peso normal com imc de ${imc.toFixed(2)}`)
// }
// else if(imc >= 25 && imc <= 29.99){
//     console.log(`Você está sobrepeso com imc de ${imc.toFixed(2)}`)
// }
// else{
//     console.log(`Você está em obesidade com IMC de ${imc.toFixed(2)}`)
// }



// 1º exercicio 01: PERGUNTE AO USUÁRIO A SUA IDADE E SE ELE POSSUI CARTEIRA, 
// ONDE SE ELE FOR MAIOR DE IDADE E TIVER CARTEIRA,
// MOSTRE NO CONSOLE A MENSAGEM DE ''VOCÊ PODE DIRIGIR",
//  SE ALGUMA DESSAS INFORMAÇÕES FOREM FALSAS, INFORME QUE ELE NÃO PODE DIRIGIR


// const idade = Number(prompt("Digite sua idade: "));
// const possuiCarteira = Number(prompt("Possui carteira de motorista? Digite 1 para SIM e 0 para NAO: "));

// if (idade >= 18 && possuiCarteira) {
//     console.log("Você pode dirigir");
// }

// if (idade < 18 || !possuiCarteira) {
//     console.log(" Vocé não pode dirigir");
// }

// if (possuiCarteira === 1 || possuiCarteira === 0) {
//     console.log("Voce pode dirigir");
// }

// if (idade < 18 || !possuiCarteira) {
//     console.log("Voce não pode dirigir");
// }


// WHILE (ENQUANTO)

// let numero = 0;
// // laço infinito
// while(numero < 5) {
//     console.log("Estou dentro do loop de repetição!");
//     numero += 1
// }



// let contador = 0;

// while(contador < 5) {
//     console.log("Seja Bem vindo ao sistema!");
//     contador ++
// }


// exija que o usuario digite as informações correta e encerre caso o usuario erre 3x qualquer dos dados



let userName;
let userPassword;
let attempts = 0;

while (true) {
  userName = prompt("Digite o seu nome: ");
  userPassword = prompt("Digite a sua senha: ");

  if (userName === "admin" && userPassword === "1234") {
    console.log("Usuário logado com sucesso!");
    break;
  }

  attempts++;

  if (attempts === 3) {
    alert("Número máximo de tentativas atingido. Encerrando o programa.");
    console.log("Encerrando o programa.");
    break;
  }

  alert("Usuário ou senha incorretos");
}



// let acumuladoraDePares = 0;

// while(true){
//     const userNumber = Number(prompt("Digite um número (ou 0 para sair): "));

//     if (userNumber === 0) {
//         console.log("encerrando o programa");
//         break;
//     }else
//          if (userNumber % 2 === 0) {
//         console.log(`O número ${userNumber} é par`);
//         acumuladoraDePares += userNumber;
//     }
//     else {
//         console.log(`O número ${userNumber} é impar`);  
//     }

// }

