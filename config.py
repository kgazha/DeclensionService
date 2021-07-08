from sqlalchemy import create_engine


DATABASE_NAME = 'declension'
DATABASE_HOST = 'localhost:5432'
DATABASE_PASSWORD = ''
DATABASE_USER = 'postgres'
DATABASE_ENGINE = 'postgresql'
ENGINE = create_engine('{0}://{1}:{2}@{3}/{4}'.format(DATABASE_ENGINE,
                                                      DATABASE_USER,
                                                      DATABASE_PASSWORD,
                                                      DATABASE_HOST,
                                                      DATABASE_NAME))
FEMALE = "femn"
MALE = "masc"
