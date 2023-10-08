from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de proyectos preestablecidos
proyectos = [
    {"nombre": "Proyecto QuantumX", "descripcion": "Investigación en física cuántica y mecánica cuántica.", "tipo de ciencia": 'Física'},
    {"nombre": "Proyecto BioTechGen", "descripcion": "Avances en biotecnología y genética molecular.", "tipo de ciencia": 'Biología'},
    {"nombre": "Proyecto AstroVisión", "descripcion": "Exploración de observaciones astronómicas y telescopios avanzados.", "tipo de ciencia": 'Astronomía'},
    {"nombre": "Proyecto GeoUniverse", "descripcion": "Estudio de geología planetaria y formación de planetas.", "tipo de ciencia": 'Geología'},
    {"nombre": "Proyecto EcoBalance", "descripcion": "Sostenibilidad ambiental y gestión de recursos.", "tipo de ciencia": 'Ciencias del Medio Ambiente'},
    {"nombre": "Proyecto MathInnovate", "descripcion": "Desarrollo de algoritmos y teoría de números.", "tipo de ciencia": 'Matemáticas'},
    {"nombre": "Proyecto CodeFusion", "descripcion": "Desarrollo de software de código abierto y colaborativo.", "tipo de ciencia": 'Informática'},
    {"nombre": "Proyecto HealthHub", "descripcion": "Investigación médica y desarrollo de soluciones de atención médica.", "tipo de ciencia": 'Medicina'},
    {"nombre": "Proyecto MindWave", "descripcion": "Exploración de la psicología cognitiva y neurociencia del cerebro.", "tipo de ciencia": 'Psicología'},
    {"nombre": "Proyecto SocialConnect", "descripcion": "Análisis de tendencias sociales y dinámicas de grupos.", "tipo de ciencia": 'Sociología'},
    {"nombre": "Proyecto AnthroExplore", "descripcion": "Estudio de culturas y evolución humana.", "tipo de ciencia": 'Antropología'},
    {"nombre": "Proyecto EconoSolutions", "descripcion": "Investigación económica y políticas de desarrollo.", "tipo de ciencia": 'Economía'},
    {"nombre": "Proyecto HistoryQuest", "descripcion": "Exploración de eventos históricos y arqueología.", "tipo de ciencia": 'Historia'},
    {"nombre": "Proyecto LinguaTech", "descripcion": "Lingüística computacional y análisis de lenguaje natural.", "tipo de ciencia": 'Lingüística'},
    {"nombre": "Proyecto GreenEarth", "descripcion": "Conservación del medio ambiente y ciencias de la tierra.", "tipo de ciencia": 'Ciencias del Medio Ambiente'},
    {"nombre": "Proyecto BrainSync", "descripcion": "Estudio de la sincronización cerebral y la cognición.", "tipo de ciencia": 'Neurociencia'},
    {"nombre": "Proyecto GenoLink", "descripcion": "Genómica y análisis de la herencia genética.", "tipo de ciencia": 'Genética'},
    {"nombre": "Proyecto OceanXplorer", "descripcion": "Investigación oceanográfica y estudio de ecosistemas marinos.", "tipo de ciencia": 'Oceanografía'},
    {"nombre": "Proyecto PhotonXpress", "descripcion": "Aplicaciones avanzadas de fotónica y óptica.", "tipo de ciencia": 'Fotónica'},
    {"nombre": "Proyecto SocioDynamics", "descripcion": "Dinámicas sociales y análisis de redes.", "tipo de ciencia": 'Ciencias Sociales'},
    {"nombre": "Proyecto PolarExplora", "descripcion": "Investigación en regiones polares y cambio climático.", "tipo de ciencia": 'Ciencias Polares'},
    {"nombre": "Proyecto EngiSolutions", "descripcion": "Ingeniería innovadora y soluciones tecnológicas.", "tipo de ciencia": 'Ingeniería'},
]

tipos_ciencias = [
    "Física",
    "Química",
    "Biología",
    "Astronomía",
    "Geología",
    "Ecología",
    "Matemáticas",
    "Informática",
    "Medicina",
    "Psicología",
    "Sociología",
    "Antropología",
    "Economía",
    "Política",
    "Historia",
    "Lingüística",
    "Ciencias del Medio Ambiente",
    "Neurociencia",
    "Bioquímica",
    "Genética",
    "Oceanografía",
    "Fotónica",
    "Ciencias Sociales",
    "Ciencias Polares",
    "Ingeniería"
]
users = [
    {
        "id": 1,
        "nombre": "Juan Pérez",
        "profesion": "Ingeniero de Software",
        "resumen": "Ingeniero de software con experiencia en desarrollo web y aplicaciones móviles. Apasionado por la programación y la tecnología.",
        "tipo de ciencia": "Informática",
    },
    {
        "id": 2,
        "nombre": "María García",
        "profesion": "Médica",
        "resumen": "Médica especializada en pediatría. Trabaja en un hospital local y se dedica al cuidado de niños y adolescentes.",
        "tipo de ciencia": "Medicina",
    },
    {
        "id": 3,
        "nombre": "Luis Rodríguez",
        "profesion": "Abogado",
        "resumen": "Abogado con experiencia en derecho laboral y civil. Representa a clientes en casos de litigios y asesoramiento legal.",
        "tipo de ciencia": "Ciencias Sociales",
    },
    {
        "id": 4,
        "nombre": "Milan Ortellado",
        "profesion": "Abogado",
        "resumen": "Abogado con experiencia en derecho laboral y civil. Representa a clientes en casos de litigios y asesoramiento legal.",
        "tipo de ciencia": "Ciencias Sociales",
    },
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profesionales', methods=['GET', 'POST'])
def ruta_profesionales():
    if request.method == 'GET':
        return render_template('profesionales.html')
    else:
        # Obtén el término de búsqueda del formulario
        filtro = request.form.get('filtro', '').lower()
        
        # Filtra los profesionales que coincidan con la búsqueda y el filtro
        resultados = [profesional for profesional in users if filtro in profesional["tipo de ciencia"].lower()]
        
        if resultados:
            return render_template('profesionales.html', resultados=resultados, filtro=filtro)
        else:
            respuesta = "No se encontraron resultados"
            return render_template('profesionales.html', respuesta=respuesta)


    

@app.route('/ruta2')
def ruta2():
    return "Esta es la Ruta 2"

@app.route('/proyectos', methods=['GET', 'POST'])
def ruta3():
    if request.method == 'GET':
        return render_template('proyectos.html')
    else:
        # Asegúrate de manejar el caso en el que 'filtro' no esté en el formulario.
        filtro = request.form.get('filtro', '')
        # Filtra los proyectos que coincidan con la búsqueda
        resultados = [p for p in proyectos if filtro.lower() in p["tipo de ciencia"].lower()]
        if resultados:
            return render_template('proyectos.html', resultados=resultados, filtro=filtro)
        else:
            respuesta = "No se encontraron resultados"
            return render_template('proyectos.html', respuesta=respuesta)

@app.route('/chat/<int:user_id>', methods=['GET', 'POST'])
def chat(user_id):
    # Obtiene el usuario correspondiente al ID
    usuario = None
    for user in users:
        if user["id"] == user_id:
            usuario = user
            break

    if usuario is None:
        return "Usuario no encontrado"

    if request.method == 'POST':
        # Obtiene el mensaje enviado desde el formulario
        mensaje = request.form.get('mensaje', '')

        # Aquí puedes guardar el mensaje en una lista asociada al usuario o en una base de datos
        # Por ejemplo, puedes crear una lista de mensajes para cada usuario en el diccionario del usuario.

        if 'mensajes' not in usuario:
            usuario['mensajes'] = []

        usuario['mensajes'].append(mensaje)

    return render_template('chat.html', usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)
    
