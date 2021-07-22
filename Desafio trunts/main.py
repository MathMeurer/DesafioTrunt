from os.path import split
from rw_sheet import read_sheets, write_final_result

def get_total_of_class():
    total_of_class = read_sheets("engenharia_de_software!A2:H2")
    text_split = total_of_class[0][0].split()
    total_class = text_split.pop() 
    return round(int (total_class))
#leia a quantidade de alunos na linha A2 H2
total_of_class = get_total_of_class()

def check_faults(faults):
    faults = int(faults)
    percentage_faults = faults * 100 / total_of_class
    return round(percentage_faults)

def sum_grades_and_return_average(*args):
    values = args[0][1:]
    soma = 0
    for value in values:
        soma += int(value)
    result = soma / 3
    return round(result)

def calculate_result_students(list_with_grades = []):
    possible_results = ("Reprovado por Nota", "Exame Final", "Aprovado", "Reprovado por Falta")
    final_result = []
    
    for grades in list_with_grades:

        average = sum_grades_and_return_average(grades)
        percentage_faults = check_faults(grades[0])

        if percentage_faults > 25:
            final_result.append([possible_results[3],possible_results[3]])

        if percentage_faults <= 25:
            if average < 50:
                final_result.append([possible_results[0],average])
            if average >= 50 and average < 70:
                final_result.append([possible_results[1],average])
            if average >= 70:
                final_result.append([possible_results[2],'0'])

    return final_result            

where_read = "engenharia_de_software!C4:F27"
grades_of_studants = read_sheets(where_read)
final_results_text = calculate_result_students(grades_of_studants)
print(final_results_text)
#Ler o banco de dados do sheets como base para o calculo descrito acima
write_final_result(final_results_text)
