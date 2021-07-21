from flask import Flask
from flask_restful import Api, Resource, reqparse

from handlers.declension_handler import DeclensionHandler
from handlers.exception_handler import ExceptionHandler

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("source_text")
parser.add_argument("target_text")
parser.add_argument("case")
parser.add_argument("number")
parser.add_argument("gender")
parser.add_argument("name")
parser.add_argument("surname")
parser.add_argument("patronymic")
parser.add_argument("fullname")
parser.add_argument("separator")


class BaseDeclensionService(Resource):
    def post(self):
        params = parser.parse_args()
        text = params["source_text"]
        case = params["case"]
        gender = params["gender"]
        number = params["number"] if params["number"] is not None else "sing"
        text_handler = DeclensionHandler()
        result = text_handler.get_inflected_text(text, case, number, gender)
        return {'result': result}


class PersonNameDeclensionService(Resource):
    def post(self):
        params = parser.parse_args()
        case = params["case"]
        number = params["number"] if params["number"] is not None else "sing"
        name = params["name"]
        surname = params["surname"]
        patronymic = params["patronymic"]
        fullname = params["fullname"]
        text_handler = DeclensionHandler()
        result = text_handler.get_inflected_person_name(case=case, number=number, name=name,
                                                        surname=surname, patronymic=patronymic,
                                                        fullname=fullname)
        return {'result': result}


class ExceptionService(Resource):
    def post(self):
        params = parser.parse_args()
        source_text = params["source_text"]
        target_text = params["target_text"]
        case = params["case"]
        gender = params["gender"]
        number = params["number"] if params["number"] is not None else "sing"
        exception_handler = ExceptionHandler()
        result = exception_handler.save_exception(source_text=source_text, target_text=target_text,
                                                  gender=gender, case=case, number=number)
        return result


api.add_resource(BaseDeclensionService, '/')
api.add_resource(PersonNameDeclensionService, '/person_name')
api.add_resource(ExceptionService, '/add_exception')

if __name__ == '__main__':
    app.run(debug=True)
