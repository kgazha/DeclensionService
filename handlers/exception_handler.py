from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
import config
import models

session = sessionmaker(bind=config.ENGINE)()


class ExceptionHandler:
    @staticmethod
    def save_exception(source_text: str, target_text: str,
                       case: str, gender: str = None,
                       number: str = "sing") -> str:
        try:
            if gender is not None:
                sentence = models.get_or_create(session, models.Sentence,
                                                source_text=source_text,
                                                case=case,
                                                gender=gender,
                                                number=number)[0]
            else:
                sentence = models.get_or_create(session, models.Sentence,
                                                source_text=source_text,
                                                case=case,
                                                number=number)[0]
            sentence.result = target_text
            session.commit()
        except SQLAlchemyError as error:
            print(error)
            return "An error occurred"
        return "Successfully saved"
