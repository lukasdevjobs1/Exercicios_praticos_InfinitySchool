#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jogo de Dados - Simulador de apostas
Permite ao jogador apostar em resultados de dados
"""

import random

def rolar_dados():
    """Rola dois dados e retorna os valores"""
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def main():
    """Função principal do jogo"""
    print(" BEM-VINDO AO JOGO DE DADOS! ")
    print("Aposte no resultado da soma de dois dados (2-12)")
    
    saldo = 100
    
    while saldo > 0:
        print(f"\n💰 Saldo atual: ${saldo}")
        
        try:
            aposta = int(input("Sua aposta (2-12): "))
            if aposta < 2 or aposta > 12:
                print(" Aposta inválida! Digite um número entre 2 e 12.")
                continue
            
            valor_aposta = int(input("Valor da aposta: $"))
            if valor_aposta > saldo:
                print(" Saldo insuficiente!")
                continue
            
            dado1, dado2 = rolar_dados()
            soma = dado1 + dado2
            
            print(f"\n🎲 Dados: {dado1} + {dado2} = {soma}")
            
            if soma == aposta:
                ganho = valor_aposta * 5
                saldo += ganho
                print(f" PARABÉNS! Você ganhou ${ganho}!")
            else:
                saldo -= valor_aposta
                print(f" Você perdeu ${valor_aposta}")
            
            if input("\nJogar novamente? (s/n): ").lower() != 's':
                break
                
        except ValueError:
            print(" Digite apenas números!")
    
    print(f"\n🎮 Jogo encerrado! Saldo final: ${saldo}")

if __name__ == "__main__":
    main()
