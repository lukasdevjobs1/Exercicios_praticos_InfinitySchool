def grading_students(grades):
    """
    Arredonda notas para o próximo múltiplo de 5 se:
    - Nota >= 38 (nota mínima para aprovação)
    - Diferença para próximo múltiplo de 5 <= 2
    """
    result = []
    
    for grade in grades:
        if grade >= 38:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade <= 2:
                result.append(next_multiple)
            else:
                result.append(grade)    
    return result

# Testes
if __name__ == '__main__':
    # Exemplo 1: [73, 67, 38, 33]
    test_grades = [73, 67, 38, 33]
    print(f"Entrada: {test_grades}")
    print(f"Saída: {grading_students(test_grades)}")  # [75, 67, 40, 33]
    
    # Exemplo 2: [84, 29, 57]
    test_grades2 = [84, 29, 57]
    print(f"\nEntrada: {test_grades2}")
    print(f"Saída: {grading_students(test_grades2)}")  # [85, 29, 57]