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

