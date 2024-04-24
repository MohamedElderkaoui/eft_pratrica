from django.core.management import call_command
from django.core.management.base import CommandError
import os

# Directorio donde se guardará el archivo SQL
output_file = 'todas_las_migraciones.sql'

# Borrar el archivo existente si ya existe
if os.path.exists(output_file):
    os.remove(output_file)

# Obtener todas las aplicaciones instaladas en el proyecto
from django.apps import apps
app_configs = apps.get_app_configs()

# Iterar sobre cada aplicación y obtener las migraciones
for app_config in app_configs:
    app_name = app_config.name
    try:
        # Obtener las migraciones de la aplicación
        output = call_command('sqlmigrate', app_name, '0001', stdout=True)
        # Escribir las migraciones en el archivo SQL
        with open(output_file, 'a') as f:
            f.write(output)
            f.write('\n\n')
    except CommandError:
        # La aplicación no tiene migraciones
        pass

print(f'Todas las migraciones se han guardado en {output_file}')
