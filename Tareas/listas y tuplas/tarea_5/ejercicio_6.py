materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
pasadas = []

for materia in materias:
    nota = float(input(f"cuanto sacaste en {materia}? "))
    if nota >= 3.5:
        pasadas.append(materia)
for materia in pasadas:
    materias.remove(materia)
print(f"perdiste estas materias: {materias}")       
