from mvc import db


categoria_proyecto = db.Table('categoria_proyecto',
    db.Column('idcategoria', db.Integer, db.ForeignKey('categoria.id')),
    db.Column('idproyecto', db.Integer, db.ForeignKey('proyecto.id'))
)

necesidad_proyecto = db.Table('necesidad_proyecto',
    db.Column('idnecesidad', db.Integer, db.ForeignKey('necesidad.id')),
    db.Column('idproyecto', db.Integer, db.ForeignKey('proyecto.id'))
)