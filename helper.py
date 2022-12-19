import os
import ssl
def getFile(file:str) -> str:
    '''
    obtiene la ruta de un archivo relativo donde se encuentra el sistema
    :param file:
    :return:
    '''
    dirname: str = os.path.dirname(__file__)+"/"+file
    print("dirname: ",dirname)
    return dirname

def singleton(cls):
    '''
    patron de diseño singleton funciona para mantener viva solo una instancia de alguna clase
    funciona con decoradores o pasando la clase como argumento
    :param cls: clase a la cual se le aplicara el singleton
    :return:
    '''
    instances = dict()
    def wrap(*args,**kwargs):
        if cls in instances:
            return instances[cls]
        new_instance = cls(*args,**kwargs)
        instances[cls] = new_instance
        return instances[cls]
    return wrap
