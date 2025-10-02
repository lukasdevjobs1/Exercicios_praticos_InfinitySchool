#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Gerenciamento de Tarefas Diárias
Permite criar, editar, excluir e listar tarefas com prioridades e categorias
"""

import json
import os
from datetime import datetime

# Estruturas de dados
tarefas = []  # Lista principal de tarefas
prioridades = {"alta": 1, "media": 2, "baixa": 3}  # Dicionário de prioridades
categorias = {"trabalho", "estudos", "lazer", "pessoal"}  # Conjunto de categorias
ARQUIVO_DADOS = "tarefas.json"

def carregar_dados():
    """Carrega tarefas do arquivo JSON"""
    global tarefas
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            tarefas = json.load(f)

def salvar_dados():
    """Salva tarefas no arquivo JSON"""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def mostrar_menu():
    """Exibe o menu principal"""
    print("\n" + "="*40)
    print("    GERENCIADOR DE TAREFAS DIÁRIAS")
    print("="*40)
    print("1. Criar tarefa")
    print("2. Listar tarefas")
    print("3. Editar tarefa")
    print("4. Excluir tarefa")
    print("5. Sair")
    print("="*40)

def criar_tarefa():
    """Cria uma nova tarefa"""
    print("\n--- CRIAR NOVA TAREFA ---")
    
    nome = input("Nome da tarefa: ").strip()
    if not nome:
        print(" Nome da tarefa não pode estar vazio!")
        return
    
    # Prioridade
    print("\nPrioridades disponíveis:", list(prioridades.keys()))
    prioridade = input("Prioridade (alta/media/baixa): ").lower().strip()
    if prioridade not in prioridades:
        print(" Prioridade inválida!")
        return
    
    # Categoria
    print("\nCategorias disponíveis:", list(categorias))
    categoria = input("Categoria: ").lower().strip()
    if categoria not in categorias:
        print(" Categoria inválida!")
        return
    
    # Criar tupla com dados da tarefa
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "nome": nome,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    tarefas.append(nova_tarefa)
    salvar_dados()
    print(f" Tarefa '{nome}' criada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas ordenadas por prioridade"""
    if not tarefas:
        print("\n Nenhuma tarefa cadastrada.")
        return
    
    # Ordenar por prioridade usando lambda
    tarefas_ordenadas = sorted(tarefas, key=lambda x: prioridades[x["prioridade"]])
    
    print("\n" + "="*60)
    print("                    LISTA DE TAREFAS")
    print("="*60)
    
    for tarefa in tarefas_ordenadas:
        status = "" if tarefa["concluida"] else ""
        prioridade_emoji = {"alta": "🔴", "media": "🟡", "baixa": "🟢"}[tarefa["prioridade"]]
        
        print(f"ID: {tarefa['id']} | {status} {tarefa['nome']}")
        print(f"   {prioridade_emoji} {tarefa['prioridade'].upper()} |  {tarefa['categoria']}")
        print(f"    {tarefa['data_criacao']}")
        print("-" * 60)

def editar_tarefa():
    """Edita uma tarefa existente"""
    if not tarefas:
        print("\n Nenhuma tarefa para editar.")
        return
    
    listar_tarefas()
    
    try:
        id_tarefa = int(input("\nID da tarefa para editar: "))
        tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
        
        if not tarefa:
            print(" Tarefa não encontrada!")
            return
        
        print(f"\nEditando: {tarefa['nome']}")
        print("1. Marcar como concluída/pendente")
        print("2. Alterar prioridade")
        print("3. Alterar categoria")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tarefa["concluida"] = not tarefa["concluida"]
            status = "concluída" if tarefa["concluida"] else "pendente"
            print(f" Tarefa marcada como {status}!")
        
        elif opcao == "2":
            print("Prioridades:", list(prioridades.keys()))
            nova_prioridade = input("Nova prioridade: ").lower()
            if nova_prioridade in prioridades:
                tarefa["prioridade"] = nova_prioridade
                print(" Prioridade alterada!")
            else:
                print(" Prioridade inválida!")
        
        elif opcao == "3":
            print("Categorias:", list(categorias))
            nova_categoria = input("Nova categoria: ").lower()
            if nova_categoria in categorias:
                tarefa["categoria"] = nova_categoria
                print(" Categoria alterada!")
            else:
                print(" Categoria inválida!")
        
        salvar_dados()
        
    except ValueError:
        print(" ID inválido!")

def excluir_tarefa():
    """Exclui uma tarefa"""
    if not tarefas:
        print("\n Nenhuma tarefa para excluir.")
        return
    
    listar_tarefas()
    
    try:
        id_tarefa = int(input("\nID da tarefa para excluir: "))
        tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)
        
        if not tarefa:
            print(" Tarefa não encontrada!")
            return
        
        confirmacao = input(f"Confirma exclusão de '{tarefa['nome']}'? (s/n): ")
        if confirmacao.lower() == 's':
            tarefas.remove(tarefa)
            salvar_dados()
            print(" Tarefa excluída com sucesso!")
        else:
            print(" Exclusão cancelada.")
            
    except ValueError:
        print(" ID inválido!")

def main():
    """Função principal do programa"""
    carregar_dados()
    
    while True:
        mostrar_menu()
        
        try:
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                criar_tarefa()
            elif opcao == "2":
                listar_tarefas()
            elif opcao == "3":
                editar_tarefa()
            elif opcao == "4":
                excluir_tarefa()
            elif opcao == "5":
                print("\n Até logo!")
                break
            else:
                print(" Opção inválida!")
                
        except KeyboardInterrupt:
            print("\n\n Programa encerrado pelo usuário.")
            break
        except Exception as e:
            print(f" Erro inesperado: {e}")

if __name__ == "__main__":
    main()
