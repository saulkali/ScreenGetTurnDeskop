from app.run import App
from app.common.utils.generate_logs_error import GenerateLogError
__author__ = "Saul Burciaga Hernandez"
__version__ = "1.0.0.0"
__github__ = "https://github.com/saulkali"


def main():
    app = App().run()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        GenerateLogError().save(str(error))
