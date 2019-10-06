from mvc import db,ma
from mvc.model.comentario import ComentarioSchema

from mvc.model.categoria import CategoriaSchema
from mvc.model.necesidad import NecesidadSchema


class Proyecto(db.Model):
    __tablename__ = 'proyecto'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column (db.String(100))
    ubicacion = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    descripcion = db.Column(db.Text())
    objetivo = db.Column(db.Text())
    resultado = db.Column(db.Text())
    telefono = db.Column(db.CHAR(9))
    link = db.Column(db.String(200))
    facebook = db.Column(db.String(200))
    twitter = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    categoria = db.relationship('Categoria', secondary="categoria_proyecto", lazy="joined")
    necesidad = db.relationship('Necesidad', secondary="necesidad_proyecto", lazy="joined")
    # comentario = db.relationship('Comentario', secondary="necesidad_proyecto", backref='proyectos',
    #                             lazy="joined")

    comentarios = db.relationship("Comentario")


class ProyectoSchema(ma.ModelSchema):
    categoria = ma.Nested(CategoriaSchema, many=True)
    comentarios = ma.Nested(ComentarioSchema, many=True)
    necesidad = ma.Nested(NecesidadSchema, many=True)

    class Meta:
        model = Proyecto
        fields = (
            'id',
            'nombre',
            'ubicacion',
            'correo',
            'descripcion',
            'objetivo',
            'resultado',
            'telefono_organizacion',
            'link',
            'facebook',
            'twitter',
            'linkedin',
            'categoria',
            'comentarios',
            'necesidad'
        )


proyecto_schema = ProyectoSchema(many=True)
proyecto_id_schema = ProyectoSchema()