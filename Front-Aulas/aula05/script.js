function verificar_idade(idade) {
    let idade = prompt("Digite sua idade: ")
    
    if (idade >= 18) {
        console.log("Maior de idade");
    } else {
        console.log("Menor de idade");
    }
}



function verificar_nome(nome) {
    if (nome === "Lukas") {
        console.log("Seu nome é Lukas");
    } else {
        console.log("Seu nome é diferente de Lukas");
    }
}