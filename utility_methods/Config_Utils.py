import os
from configparser import ConfigParser


def get_config(section, option):
    config = ConfigParser()
    file_path = os.path.join(os.path.dirname(os.path.abspath('..')), "config.ini")
    print(file_path)
    config.read(file_path)

    return config.get(section, option)
