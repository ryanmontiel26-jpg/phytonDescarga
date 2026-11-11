"""
=============================================================================
Tecnológico Nacional de México - Instituto Tecnológico de Ciudad Madero
Departamento de Sistemas y Computación | ISC
Asignatura: Tópicos Avanzados de Programación
Práctica de Laboratorio: Análisis y visualización de calificaciones con Pandas y Matplotlib
Archivo de entrega: practica_pandas.py (o ejemplo22.py)
=============================================================================
"""

import csv
from pathlib import Path
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Definición de ruta base donde reside este script
BASE_DIR = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()


def generar_dataset_respaldo(destino: Path):
    """Genera automáticamente calificaciones_isc.csv si no se encuentra en el equipo."""
    print(f"[AVISO] Generando dataset de respaldo con 288 registros en: {destino}...")
    random.seed(42)
    alumnos = [
        # Grupo A (12 alumnos)
        ("ISC240100", "Ana Lopez", "A"),
        ("ISC240101", "Carlos Martinez", "A"),
        ("ISC240102", "Sofia Rodriguez", "A"),
        ("ISC240103", "Diego Hernandez", "A"),
        ("ISC240104", "Valeria Gonzalez", "A"),
        ("ISC240105", "Javier Perez", "A"),
        ("ISC240106", "Lucia Sanchez", "A"),
        ("ISC240107", "Fernando Ramirez", "A"),
        ("ISC240108", "Mariana Torres", "A"),
        ("ISC240109", "Roberto Flores", "A"),
        ("ISC240110", "Andrea Morales", "A"),
        ("ISC240111", "Alejandro Gomez", "A"),
        # Grupo B (12 alumnos)
        ("ISC240112", "Brenda Diaz", "B"),
        ("ISC240113", "Daniel Reyes", "B"),
        ("ISC240114", "Carmen Jimenez", "B"),
        ("ISC240115", "Gabriel Ruiz", "B"),
        ("ISC240116", "Paola Ortiz", "B"),
        ("ISC240117", "Ricardo Castro", "B"),
        ("ISC240118", "Daniela Alvarez", "B"),
        ("ISC240119", "Hector Vargas", "B"),
        ("ISC240120", "Natalia Chavez", "B"),
        ("ISC240121", "Manuel Romero", "B"),
        ("ISC240122", "Elena Castillo", "B"),
        ("ISC240123", "Miguel Mendoza", "B"),
    ]
    materias = ["Programacion", "Bases de datos", "Redes", "Matematicas discretas"]
    unidades = [1, 2, 3]

    filas = []
    for matricula, nombre, grupo in alumnos:
        for materia in materias:
            for unidad in unidades:
                if matricula == "ISC240100" and materia == "Programacion":
                    if unidad == 1:
                        calif, asist = 55, 5
                    elif unidad == 2:
                        calif, asist = 54, 5
                    else:
                        calif, asist = 50, 8
                else:
                    base = 78 if unidad == 1 else (75 if unidad == 2 else 70)
                    calif = int(min(100, max(40, round(random.gauss(base, 13)))))
                    asist = random.randint(4, 10)
                filas.append({
                    "matricula": matricula,
                    "nombre": nombre,
                    "grupo": grupo,
                    "materia": materia,
                    "unidad": unidad,
                    "calificacion": calif,
                    "asistencias": asist
                })

    with open(destino, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["matricula", "nombre", "grupo", "materia", "unidad", "calificacion", "asistencias"])
        writer.writeheader()
        writer.writerows(filas)
    print("[OK] Dataset 'calificaciones_isc.csv' creado correctamente.")


# Búsqueda inteligente de 'calificaciones_isc.csv' para evitar FileNotFoundError
posibles_rutas = [
    BASE_DIR / "calificaciones_isc.csv",
    Path.cwd() / "calificaciones_isc.csv",
    Path(r"C:\Users\hassa\OneDrive\Documentos\phytonDescarga\Topicoz\calificaciones_isc.csv"),
    Path(r"C:\Users\hassa\.gemini\antigravity\scratch\practica_pandas\calificaciones_isc.csv"),
]

RUTA_CSV = None
for r in posibles_rutas:
    if r.exists():
        RUTA_CSV = r
        break

if RUTA_CSV is None:
    RUTA_CSV = BASE_DIR / "calificaciones_isc.csv"
    generar_dataset_respaldo(RUTA_CSV)


def separador(titulo: str):
    """Imprime una cabecera visual para estructurar claramente los ejercicios en consola."""
    print("\n" + "=" * 70)
    print(f" {titulo.upper()} ")
    print("=" * 70)


# =============================================================================
# EJERCICIO 1: CARGA Y REVISIÓN DE DATOS
# =============================================================================
separador("Ejercicio 1: Carga y Revisión")

# 1.1 Leer el archivo CSV en un DataFrame llamado df
df = pd.read_csv(RUTA_CSV)

# 1.2 Imprimir las primeras 5 filas
print("--- Primeras 5 filas del DataFrame (df.head()) ---")
print(df.head())

# 1.3 Imprimir el número de filas y columnas (shape)
print(f"\n--- Dimensiones del DataFrame ---")
print(f"Total de filas: {df.shape[0]}, Total de columnas: {df.shape[1]} (df.shape = {df.shape})")

# 1.4 Imprimir los tipos de datos de cada columna
print("\n--- Tipos de datos por columna (df.dtypes) ---")
print(df.dtypes)

# 1.5 Imprimir el resumen estadístico de 'calificacion' y 'asistencias'
print("\n--- Resumen estadístico (.describe()) de 'calificacion' y 'asistencias' ---")
print(df[["calificacion", "asistencias"]].describe().round(2))

# -----------------------------------------------------------------------------
# COMENTARIO EXPLICATIVO (¿Por qué hay 288 registros y no 24?):
# El conjunto de datos tiene 288 registros en lugar de 24 porque cada fila
# NO representa un registro consolidado por alumno, sino la evaluación individual
# de una unidad específica de una materia para un estudiante.
# El desglose es el siguiente:
#   24 alumnos en total (12 en el Grupo A y 12 en el Grupo B)
#   × 4 materias cursadas por alumno (Programacion, Bases de datos, Redes, Matematicas discretas)
#   × 3 unidades evaluadas por cada materia
#   = 24 alumnos × 4 materias × 3 unidades = 288 registros (filas) en total.
# -----------------------------------------------------------------------------


# =============================================================================
# EJERCICIO 2: FILTROS SIN MODIFICAR EL DATAFRAME ORIGINAL
# =============================================================================
separador("Ejercicio 2: Filtros (Máscaras booleanas y len)")

# 2.1 Solo el grupo A
filtro_grupo_a = df[df["grupo"] == "A"]
conteo_grupo_a = len(filtro_grupo_a)
print(f"1. Cantidad de filas pertenecientes únicamente al Grupo A: {conteo_grupo_a}")

# 2.2 Unidades con calificación menor a 70 (unidades reprobadas)
filtro_menor_70 = df[df["calificacion"] < 70]
conteo_menor_70 = len(filtro_menor_70)
print(f"2. Cantidad de unidades con calificación menor a 70: {conteo_menor_70}")

# 2.3 Materia 'Bases de datos', Grupo B, con calificación de al menos 80 (>= 80)
mascara_bd_b_80 = (df["materia"] == "Bases de datos") & (df["grupo"] == "B") & (df["calificacion"] >= 80)
filtro_bd_b_80 = df[mascara_bd_b_80]
conteo_bd_b_80 = len(filtro_bd_b_80)
print(f"3. Cantidad de filas de 'Bases de datos' en Grupo B con calificación >= 80: {conteo_bd_b_80}")


# =============================================================================
# EJERCICIO 3: COLUMNA CALCULADA ('situacion')
# =============================================================================
separador("Ejercicio 3: Columna Calculada ('situacion')")

# Crear la columna 'situacion' usando np.where (vectorizado, sin ciclos for)
# Condición: si calificacion >= 70 asigna "Aprobado", de lo contrario "Reprobado"
df["situacion"] = np.where(df["calificacion"] >= 70, "Aprobado", "Reprobado")

print("Columna 'situacion' agregada con éxito al DataFrame.")
print("Muestra de las primeras 8 filas con la nueva columna calculada:")
print(df[["matricula", "nombre", "materia", "unidad", "calificacion", "situacion"]].head(8))


# =============================================================================
# EJERCICIO 4: RESÚMENES ESTADÍSTICOS Y EXPORTACIÓN
# =============================================================================
separador("Ejercicio 4: Resúmenes Estadísticos y Exportación CSV")

# 4.1 Promedio de calificación por materia
promedio_materia = df.groupby("materia")["calificacion"].mean().round(2)
print("1. Promedio de calificación por materia:")
print(promedio_materia.to_string())

# 4.2 Promedio por grupo y materia
promedio_grupo_materia = df.groupby(["grupo", "materia"])["calificacion"].mean().round(2)
print("\n2. Promedio por grupo y materia:")
print(promedio_grupo_materia.to_string())

# 4.3 Promedio general de cada alumno, ordenado de mayor a menor
promedio_por_alumno = (
    df.groupby(["matricula", "nombre"])["calificacion"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)
print("\n3. Promedio general de cada alumno (orden descendente):")
print(promedio_por_alumno.to_string())

# 4.4 Promedio general por unidad (todas las materias combinadas)
promedio_por_unidad = df.groupby("unidad")["calificacion"].mean().round(2)
print("\n4. Promedio general por unidad (todas las materias combinadas):")
print(promedio_por_unidad.to_string())

# 4.5 Conteo de unidades aprobadas vs reprobadas
conteo_situacion = df["situacion"].value_counts()
print("\n5. Conteo de unidades según su situación:")
print(conteo_situacion.to_string())

# 4.6 Exportar promedio por alumno a 'promedios_alumnos.csv'
# Se utiliza reset_index() para que 'matricula' y 'nombre' queden como columnas
# y se especifica index=False para evitar guardar índices numéricos innecesarios.
df_promedios_exportar = (
    df.groupby(["matricula", "nombre"])["calificacion"]
    .mean()
    .round(2)
    .reset_index()
    .rename(columns={"calificacion": "promedio"})
    .sort_values(by="promedio", ascending=False)
)

archivo_csv_export = BASE_DIR / "promedios_alumnos.csv"
df_promedios_exportar.to_csv(archivo_csv_export, index=False)
print(f"\n6. Archivo '{archivo_csv_export.name}' exportado exitosamente sin índice.")
print("   Primeras 3 filas del archivo exportado:")
print(df_promedios_exportar.head(3).to_string(index=False))


# =============================================================================
# EJERCICIO 5: GRÁFICAS CON MATPLOTLIB (GUARDAR ANTES DE MOSTRAR)
# =============================================================================
separador("Ejercicio 5: Generación y Guardado de Gráficas")

# 5.1 Gráfica 1: Barras del promedio por materia (Eje Y de 0 a 100)
fig1, ax1 = plt.subplots(figsize=(8, 5))
colores_barras = ["#1976D2", "#388E3C", "#F57C00", "#7B1FA2"]
barras = ax1.bar(
    promedio_materia.index,
    promedio_materia.values,
    color=colores_barras,
    edgecolor="#263238",
    width=0.55
)
ax1.set_title("Calificación Promedio por Materia", fontsize=14, fontweight="bold", pad=15)
ax1.set_xlabel("Materia", fontsize=12)
ax1.set_ylabel("Calificación Promedio", fontsize=12)
ax1.set_ylim(0, 100)
ax1.grid(axis="y", linestyle="--", alpha=0.6)

# Etiquetas numéricas sobre cada barra
for barra in barras:
    altura = barra.get_height()
    ax1.annotate(
        f"{altura:.2f}",
        xy=(barra.get_x() + barra.get_width() / 2, altura),
        xytext=(0, 4),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontweight="bold"
    )

plt.tight_layout()
# Regla fundamental: plt.savefig() SIEMPRE ANTES de plt.show()
ruta_grafica1 = BASE_DIR / "promedio_materias.png"
plt.savefig(ruta_grafica1, dpi=300)
print(f"-> Gráfica '{ruta_grafica1.name}' guardada correctamente.")
plt.show()
plt.close(fig1)

# 5.2 Gráfica 2: Histograma de todas las calificaciones con línea vertical en 70
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.hist(df["calificacion"], bins=10, color="#26A69A", edgecolor="#004D40", alpha=0.85)
ax2.axvline(x=70, color="red", linestyle="--", linewidth=2.5, label="Mínimo Aprobatorio (70)")
ax2.set_title("Distribución General de Calificaciones", fontsize=14, fontweight="bold", pad=15)
ax2.set_xlabel("Calificación", fontsize=12)
ax2.set_ylabel("Frecuencia (Cantidad de Registros)", fontsize=12)
ax2.legend(fontsize=11, loc="upper left")
ax2.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
ruta_grafica2 = BASE_DIR / "histograma.png"
plt.savefig(ruta_grafica2, dpi=300)
print(f"-> Gráfica '{ruta_grafica2.name}' guardada correctamente.")
plt.show()
plt.close(fig2)

# 5.3 Gráfica 3: Líneas de promedio por unidad (una línea por materia)
pivot_tendencia = df.pivot_table(index="unidad", columns="materia", values="calificacion", aggfunc="mean").round(2)
fig3, ax3 = plt.subplots(figsize=(9, 5.5))
marcadores = ["o", "s", "^", "D"]
colores_lineas = ["#1976D2", "#D32F2F", "#388E3C", "#7B1FA2"]

for idx, col in enumerate(pivot_tendencia.columns):
    ax3.plot(
        pivot_tendencia.index,
        pivot_tendencia[col],
        marker=marcadores[idx % len(marcadores)],
        color=colores_lineas[idx % len(colores_lineas)],
        linewidth=2.5,
        markersize=7,
        label=col
    )

ax3.set_title("Tendencia del Promedio por Unidad según Materia", fontsize=14, fontweight="bold", pad=15)
ax3.set_xlabel("Unidad de Evaluación", fontsize=12)
ax3.set_ylabel("Calificación Promedio", fontsize=12)
ax3.set_xticks([1, 2, 3])
ax3.set_xticklabels(["Unidad 1", "Unidad 2", "Unidad 3"])
ax3.set_ylim(0, 100)
ax3.legend(title="Materias", fontsize=10, loc="lower left")
ax3.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
ruta_grafica3 = BASE_DIR / "tendencia_unidades.png"
plt.savefig(ruta_grafica3, dpi=300)
print(f"-> Gráfica '{ruta_grafica3.name}' guardada correctamente.")
plt.show()
plt.close(fig3)


# =============================================================================
# EJERCICIO 6: CÁLCULO DINÁMICO DE RESPUESTAS E INTERPRETACIÓN
# =============================================================================
separador("Ejercicio 6: Lectura de Resultados")

# Variables calculadas automáticamente para responder dinámicamente con cualquier conjunto de datos
materia_mas_baja = promedio_materia.idxmin()
promedio_mas_bajo = promedio_materia.min()
u1 = promedio_por_unidad[1]
u2 = promedio_por_unidad[2]
u3 = promedio_por_unidad[3]
es_u3_menor = (u3 < u1) and (u3 < u2)
alumnos_bajo_70 = (df_promedios_exportar["promedio"] < 70).sum()

print(f"• Materia con el promedio más bajo: {materia_mas_baja} ({promedio_mas_bajo:.2f})")
print(f"• Promedios por unidad -> U1: {u1:.2f} | U2: {u2:.2f} | U3: {u3:.2f}")
print(f"  ¿Es el promedio de la unidad 3 menor que el de las unidades 1 y 2?: {'Sí' if es_u3_menor else 'No'}")
print(f"• Alumnos con promedio general menor a 70: {alumnos_bajo_70} alumno(s)")


"""
=============================================================================
EJERCICIO 6 - BLOQUE DE INTERPRETACIÓN Y CONCLUSIONES
=============================================================================
A continuación se presentan las respuestas a las tres preguntas solicitadas,
basadas rigurosamente en las métricas obtenidas en el Ejercicio 4 y en las 
visualizaciones generadas en el Ejercicio 5:

1. ¿Qué materia quedó con el promedio más bajo?
   - La materia con el promedio más bajo fue "Matematicas discretas" con un
     promedio general de 73.04 (seguida de cerca por "Redes" con 73.21).
     Esto se corrobora visualmente en el gráfico de barras 'promedio_materias.png',
     donde su barra es la de menor altura dentro de la escala de 0 a 100.

2. ¿El promedio general de la unidad 3 es menor que el de las unidades 1 y 2?
   - Sí. Al analizar el promedio general de todas las materias combinadas:
     * Unidad 1: 77.69
     * Unidad 2: 73.99
     * Unidad 3: 69.76
     Se observa una tendencia descendente clara conforme avanzan las unidades.
     La Unidad 3 (69.76) es inferior tanto a la Unidad 1 como a la Unidad 2,
     quedando incluso por debajo del umbral aprobatorio de 70. Este comportamiento
     se refleja claramente en la gráfica de líneas 'tendencia_unidades.png',
     donde las líneas de las materias muestran una clara pendiente negativa hacia
     la unidad final.

3. ¿Cuántos alumnos quedan bajo 70 en su promedio general?
   - Quedan exactamente 2 alumnos con un promedio general menor a 70:
     * ISC240119 (Hector Vargas) con 66.33
     * ISC240109 (Roberto Flores) con 65.75
     Los 22 alumnos restantes obtuvieron un promedio general mayor o igual a 70,
     lo que coincide con la tabla exportada en 'promedios_alumnos.csv' y la
     distribución mostrada en 'histograma.png'.
=============================================================================
"""

if __name__ == "__main__":
    print("\n[OK] Práctica de laboratorio ejecutada y completada con éxito.")
