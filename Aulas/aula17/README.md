Implementação da Classe Tamagotchi
A atividade principal consiste na implementação de uma classe Tamagotchi que simula um animal de estimação virtual, seguindo os princípios de Programação Orientada a Objetos.

🎯 Objetivos de Aprendizado
Classes e Objetos: Criar e instanciar classes

Atributos: Gerenciar o estado interno do objeto

Métodos: Implementar comportamentos e ações

Validações: Controlar entradas e estados válidos

Encapsulamento: Organizar a lógica interna da classe

📊 Estrutura da Classe Tamagotchi
Atributos Públicos:

nome (str): Nome do Tamagotchi

idade (float): Idade em anos (inicia em 0.0)

fome (int): Nível de fome de 0 a 100 (inicia em 50)

felicidade (int): Nível de felicidade de 0 a 100 (inicia em 50)

vivo (bool): Estado de vida (inicia em True)

Métodos de Ação:

alimentar(qtd): Reduz a fome do Tamagotchi

brincar(minutos): Aumenta a felicidade (mas também aumenta a fome)

passar_tempo(horas): Simula a passagem do tempo

Métodos de Status:

status() -> str: Retorna o estado atual completo

esta_morto() -> bool: Verifica se o Tamagotchi morreu

⚠️ Regras de Funcionamento
Mecânica de Morte:

Morre se fome >= 100 (morte por fome)

Morre se felicidade <= 0 (morte por tristeza)

Uma vez morto, não pode realizar mais ações

Sistema de Limites:

fome e felicidade sempre entre 0 e 100

Valores são ajustados automaticamente após cada ação

Validações:

Parâmetros devem ser maiores que 0

Verificação de estado de vida antes de ações

Mensagens informativas para ações inválidas

🔧 Regras Específicas Implementadas
Alimentar: Cada unidade reduz 2 pontos de fome

Brincar: Cada minuto aumenta 1 ponto de felicidade e 0.5 ponto de fome

Passar Tempo: Cada hora aumenta 3 pontos de fome e reduz 2 pontos de felicidade

🚀 Como Executar
Clone o repositório:

bash
git clone https://github.com/lukasdevjobs1/Exercicios_praticos_InfinitySchool.git
Navegue até a pasta da aula:

bash
cd Exercicios_praticos_InfinitySchool/Aulas/aula17
Execute o código Python:

bash
python Atividades17_POO.py
💡 Exemplo de Uso
python

# Criando um Tamagotchi

pet = Tamagotchi("Tama")

# Interagindo com o pet

pet.alimentar(10)
pet.brincar(15)
pet.passar_tempo(2)

# Verificando status

print(pet.status())

# Testando cenários de erro

pet.alimentar(-5) # Inválido - quantidade negativa
pet.brincar(0) # Inválido - zero minutos

🎓 Conceitos de POO Praticados
✅ Abstração: Modelagem de um conceito do mundo real
✅ Encapsulamento: Controle interno do estado do objeto
✅ Métodos: Comportamentos específicos da classe
✅ Atributos: Características do objeto
✅ Validações: Garantia de integridade do estado

📝 Observações
O código não utiliza encapsulamento avançado (atributos são públicos)

Não há persistência de dados entre execuções

Foco no entendimento dos conceitos básicos de POO

👨‍💻 Autor
Desenvolvido como parte das atividades práticas da Infinity School.
