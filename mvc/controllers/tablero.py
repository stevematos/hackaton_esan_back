import datetime as datetimepackage

from flask import Blueprint,jsonify
from mvc import db
from sqlalchemy import func


from functools import wraps
from flask import request, abort

from mvc.model import Categoria, categoria_schema, Proyecto, proyecto_schema, proyecto_id_schema

tablero = Blueprint('tablero', __name__)


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

@tablero.route('/')
# @require_appkey
def hello():
    json = {}
    json['probando'] = "hola mundo"
    return jsonify(json)

@tablero.route('/proyecto/list')
def ProyectoLista():

    proyecto = Proyecto.query.all()
    proyectos_lista = proyecto_schema.dump(proyecto)

    for proyecto_lista in proyectos_lista:
        proyecto_lista["categoria"] = [ categoria['nombre'] for categoria in proyecto_lista["categoria"] ]


    return jsonify(proyectos_lista)


@tablero.route('/proyecto/<int:id>')
def ProyectoPorId(id):

    proyecto = Proyecto.query.get(id)
    proyecto_id = proyecto_id_schema.dump(proyecto)

    proyecto_id["categoria"] = [ categoria['id'] for categoria in proyecto_id["categoria"] ]

    return jsonify(proyecto_id)

@tablero.route('/proyecto/create',methods=['POST'])
def ProyectoCreate():
    categoria = request.json['categoria']

    print(categoria)
    return jsonify(categoria)


@tablero.route('/categoria/list')
def CategoriasLista():
    categorias = Categoria.query.all()
    categoria_lista = categoria_schema.dump(categorias)
    return jsonify(categoria_lista)



# @tablero.route('/api/tablero/<string:date_inicio>/<string:date_fin>/<string:date_now>/<string:comerciales>')
# @require_appkey
# def get_tablero_data(date_inicio,date_fin,date_now,comerciales):
#     # comerciales : solange-teresa- ...
#
#
#
#     anio = datetimepackage.datetime.now().year
#     date_inicio = datetimepackage.datetime.strptime(date_inicio,'%d-%m-%Y')
#     date_fin = datetimepackage.datetime.strptime(date_fin,'%d-%m-%Y')
#     date_now = datetimepackage.datetime.strptime(date_now,'%d-%m-%Y')
#
#     query_ejecutivos = Ejecutivo.query.all()
#     ejecutivos = ejecutivo_schema_nombre.dump(query_ejecutivos)
#
#
#
#     ejecutivos_datamart = { ejecutivo['nombre'].split(' ')[0].lower(): ejecutivo['nombre'] for ejecutivo in ejecutivos }
#
#     comerciales = [  comercial.lower()  for comercial in comerciales.split('-')]
#
#
#     comerciales_faltante = [  ejecutivos_datamart.pop(comercial) for comercial in comerciales ]
#
#     comerciales_faltante += list(ejecutivos_datamart.values())
#
#     list_ejecutivos = comerciales_faltante
#
#     query_eventos = db.session.query(Evento).filter(date_inicio<Evento.fecha_inicio,Evento.fecha_final<date_fin)
#     eventos = evento_schema_tablero.dump(query_eventos)
#
#     list_eventos = [{'nombre':evento['apodo_evento'],'fecha_final':evento['fecha_final'],'fecha_inicio': evento['fecha_inicio'], 'objetivo_cupos':evento['objetivo_cupos']} for evento in eventos]
#     list_eventos = sorted(list_eventos, key=lambda k: k['fecha_final'])
#
#     query_cupos = Cupo.query.all()
#     cupos = cupo_schema_nombre.dump(query_cupos)
#     list_cupos = [cupo['tipo_cupo'] for cupo in cupos]
#
#
#     # oportunidad_cupos = OportunidadCupos.query.all() # hacerlo por query. el where del anio
#     cupos_evento_ejecutivos = db.session\
#                         .query(func.sum(OportunidadCupos.cantidad).label('cantidad_cupos'),
#                                Cupo.peso.label('peso'),
#                                Cupo.tipo_cupo.label("cupo"),
#                                Evento.apodo_evento.label("nombre_evento"),
#                                Ejecutivo.nombre.label("nombre_ejecutivo"))\
#                         .join(OportunidadCupos.evento)\
#                         .join(OportunidadCupos.ejecutivo)\
#                         .join(OportunidadCupos.cupo) \
#                         .join(OportunidadCupos.etapa) \
#                         .filter(date_inicio<Evento.fecha_inicio,Evento.fecha_final<date_fin, Etapa.probabilidad >= 80
#                             ,OportunidadCupos.activo == True)\
#                         .group_by(Cupo.peso,Cupo.tipo_cupo,Evento.apodo_evento,Ejecutivo.nombre)
#
#
#     oportunidad_cupos_data = cupos_evento_ejecutivos_schema.dump(cupos_evento_ejecutivos)
#
#
#
#     json = {}
#
#     # solo el primer nombre
#     headers = [ ejecutivo.split(' ')[0] for ejecutivo in list_ejecutivos]+['TOTAL','OBJETIVO','DIF']
#     # json.append()
#
#
#
#
#     events_list = []
#     for evento in list_eventos:
#         eventos_cantidad = {}
#         cupo_cantidad = {}
#         total_cantidad = [0]*len(list_ejecutivos)
#         for cupo in list_cupos:
#             cantidades = []
#             i_total = 0
#             for ejecutivo in list_ejecutivos:
#                 cantidad = 0
#                 for oportunidad in oportunidad_cupos_data:
#                     if oportunidad['nombre_evento'] == evento['nombre'] and oportunidad['nombre_ejecutivo'] == ejecutivo and oportunidad['cupo'] == cupo:
#                         cantidad = oportunidad['cantidad_cupos']
#                         total_cantidad[i_total] += oportunidad['cantidad_cupos']*oportunidad['peso']
#                         break
#                 i_total += 1
#                 cantidades.append(cantidad)
#             nombre_cupo = 'DÍA '+cupo.split(' ')[1]
#
#             #llenada de data
#
#             total_por_cupo = 0
#             for cantidad_por_ejecutivo in cantidades:
#                 total_por_cupo += cantidad_por_ejecutivo
#
#             cantidades += [total_por_cupo]
#             cantidades += [' ']*(len(headers)-len(cantidades))
#
#             cupo_cantidad[nombre_cupo] = cantidades
#
#         fecha_final_event = datetimepackage.datetime.strptime(evento['fecha_final'] ,'%Y-%m-%dT%H:%M:%S')
#         fecha_inicio_event = datetimepackage.datetime.strptime(evento['fecha_inicio'] ,'%Y-%m-%dT%H:%M:%S')
#
#         total = 0
#         for cantidad in total_cantidad:
#             total += cantidad
#
#         row_total = total_cantidad + [total,evento['objetivo_cupos'],evento['objetivo_cupos'] - total]
#
#         es_un_dia = fecha_final_event.date() == fecha_inicio_event.date()
#
#         if not es_un_dia:
#             cupo_cantidad['TOTAL'] = row_total
#             eventos_cantidad[evento['nombre']] = cupo_cantidad
#         else:
#             eventos_cantidad[evento['nombre']] = row_total
#
#         if fecha_final_event > date_now:
#             eventos_cantidad['activo'] = True
#         else:
#             eventos_cantidad[evento['nombre']] = row_total
#             eventos_cantidad['activo'] = False
#         events_list.append(eventos_cantidad)
#     json['headers'] = [anio] + headers
#     json['data'] = events_list
#     return jsonify(json)
    # return jsonify(oportunidad_cupos_data)
