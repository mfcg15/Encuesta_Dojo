from _app.config.connection import connectToMySQL
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data['idioma']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (nombre,ubicacion,idioma,comentario,created_at,updated_at) VALUES (%(nombre)s, %(ubicacion)s,%(idioma)s,%(comentario)s,NOW(),NOW());"
        return connectToMySQL('esquema_encuesta_dojo').query_db( query, data)

    @staticmethod
    def validate_dojo(data):
        is_valid = True
        if len(data['nombre']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
            print("valida1",is_valid)
        if data['ubicacion'] == ' ':
            flash("Must choose a dojo location.")
            is_valid = False
            print("valida2",is_valid)
        if data['idioma'] == ' ':
            flash("Must choose a favorite language.")
            is_valid = False
            print("valida3",is_valid)
        if len(data['comentario']) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
            print("valida4",is_valid)
        return is_valid

    @classmethod
    def get_dojo(cls,data):
        query = "SELECT * FROM dojos where id = %(id)s;"
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query,data)
        dojo = []
        for i in results:
            dojo.append(i)
        return dojo
