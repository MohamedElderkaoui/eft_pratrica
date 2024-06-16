import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime

# Datos de las tareas
data = {
    'Tarea': [
        'Reuniones iniciales', 'Definición de objetivos', 'Configuración de herramientas',
        'Desarrollo de nuevas funcionalidades', 'Integración de contenido nuevo', 'Pruebas de funcionalidad',
        'Pruebas de usuario', 'Corrección de errores', 'Preparación para el lanzamiento',
        'Lanzamiento de la nueva página', 'Monitoreo y mantenimiento inicial'
    ],
    'Inicio': [
        '2024-04-01', '2024-04-08', '2024-04-15', '2024-04-15', '2024-04-29', '2024-04-29',
        '2024-05-13', '2024-06-03', '2024-06-13', '2024-07-07', '2024-07-15'
    ],
    'Final': [
        '2024-04-08', '2024-04-15', '2024-04-29', '2024-04-29', '2024-05-13', '2024-05-13',
        '2024-06-03', '2024-06-13', '2024-07-07', '2024-07-15', '2024-07-30'
    ]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Convertir las fechas a objetos datetime
df['Inicio'] = pd.to_datetime(df['Inicio'])
df['Final'] = pd.to_datetime(df['Final'])

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(10, 6))

# Añadir las barras al diagrama de Gantt
for idx, row in df.iterrows():
    ax.broken_barh(
        [(date2num(row['Inicio']), (row['Final'] - row['Inicio']).days)],
        (idx - 0.4, 0.8),
        facecolors=('tab:blue')
    )

# Configurar el eje Y
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Tarea'])
ax.invert_yaxis()

# Configurar el eje X
ax.xaxis_date()
ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))

# Etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Tareas')
plt.title('Diagrama de Gantt')

# Rotar las etiquetas del eje X para que se lean mejor
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
