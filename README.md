# Task-Tracker
https://roadmap.sh/projects/task-tracker
Task Tracker CLI 

Task Tracker CLI es una herramienta de línea de comandos (CLI) diseñada para ayudarte a gestionar tus tareas de manera eficiente. Puedes agregar, actualizar, eliminar y marcar tareas como completadas o en progreso, además de listarlas según su estado. 
Tabla de Contenidos 

    Requisitos 
    Instalación 
    Uso 
        Agregar una Tarea 
        Actualizar una Tarea 
        Eliminar una Tarea 
        Marcar una Tarea como En Progreso 
        Marcar una Tarea como Completada 
        Listar Todas las Tareas 
        Listar Tareas por Estado 
         
    Estructura del Archivo JSON 
    Contribuciones 
    Licencia 
     

Requisitos 

    Python 3.x instalado en tu sistema.
    Acceso a la línea de comandos (terminal, consola, etc.).
     

Instalación 

    Clona este repositorio o descarga los archivos directamente: 
    bash
     

 
1
git clone https://github.com/Albertini97/Task-Tracker.git
 
 

Navega al directorio del proyecto: 
bash
 
 
1
cd task-tracker-cli
 
 

Asegúrate de tener Python instalado. Puedes verificarlo ejecutando: 
bash
 

     
    1
    python --version
     
     

    ¡Listo! No necesitas instalar dependencias adicionales, ya que este proyecto utiliza solo módulos nativos de Python. 
     

Uso 
Agregar una Tarea 

Para agregar una nueva tarea, usa el comando add seguido de la descripción de la tarea. 
bash
 
 
1
python task-cli.py add "Comprar pan"
 
 

Salida: 
 
 
1
Tarea agregada con éxito (ID: 1)
 
 
Actualizar una Tarea 

Para actualizar una tarea existente, usa el comando update seguido del ID de la tarea y la nueva descripción. 
bash
 
 
1
python task-cli.py update 1 "Comprar pan integral"
 
 

Salida: 
 
 
1
Tarea 1 actualizada con éxito
 
 
Eliminar una Tarea 

Para eliminar una tarea, usa el comando delete seguido del ID de la tarea. 
bash
 
 
1
python task-cli.py delete 1
 
 

Salida: 
 
 
1
Tarea 1 eliminada con éxito
 
 
Marcar una Tarea como En Progreso 

Para marcar una tarea como en progreso, usa el comando mark-in-progress seguido del ID de la tarea. 
bash
 
 
1
python task-cli.py mark-in-progress 1
 
 

Salida: 
 
 
1
Tarea 1 marcada como en-progreso
 
 
Marcar una Tarea como Completada 

Para marcar una tarea como completada, usa el comando mark-done seguido del ID de la tarea. 
bash
 
 
1
python task-cli.py mark-done 1
 
 

Salida: 
 
 
1
Tarea 1 marcada como done
 
 
Listar Todas las Tareas 

Para listar todas las tareas, simplemente usa el comando list. 
bash
 
 
1
python task-cli.py list
 
 

Salida: 
 
 
1
ID: 1, Descripción: Comprar pan, Estado: todo, Creada en: 2023-10-05T14:30:00.123456, Actualizada en: 2023-10-05T14:30:00.123456
 
 
Listar Tareas por Estado 

Para listar tareas según su estado, usa el comando list seguido del estado deseado (todo, in-progress, done). 
bash
 
 
1
python task-cli.py list todo
 
 

Salida: 
 
 
1
ID: 1, Descripción: Comprar pan, Estado: todo, Creada en: 2023-10-05T14:30:00.123456, Actualizada en: 2023-10-05T14:30:00.123456
 
 
Estructura del Archivo JSON 

El archivo tasks.json almacena todas las tareas en formato JSON. Aquí hay un ejemplo de cómo se ve el archivo: 
json
 
 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
⌄
⌄
⌄
[
    {
        "id": 1,
        "description": "Comprar pan",
        "status": "todo",
        "createdAt": "2023-10-05T14:30:00.123456",
        "updatedAt": "2023-10-05T14:30:00.123456"
    },
    {
        "id": 2,
        "description": "Estudiar Python",
        "status": "in-progress",
        "createdAt": "2023-10-05T14:35:00.654321",
        "updatedAt": "2023-10-05T14:40:00.987654"
    }
]
 
 

Este archivo se crea automáticamente si no existe. 
Contribuciones 

¡Las contribuciones son bienvenidas! Si encuentras algún error o tienes ideas para mejorar este proyecto, sigue estos pasos: 

    Haz un fork del repositorio.
    Crea una rama para tu cambio (git checkout -b feature/nueva-funcionalidad).
    Realiza tus cambios y haz commit (git commit -m "Añadir nueva funcionalidad").
    Sube tus cambios (git push origin feature/nueva-funcionalidad).
    Abre un Pull Request.
     

Licencia 

Este proyecto está bajo la licencia MIT . Esto significa que puedes usar, modificar y distribuir el código libremente, siempre que incluyas la licencia original. 

¡Esperamos que esta herramienta te sea útil para organizar tus tareas diarias! 😊 
