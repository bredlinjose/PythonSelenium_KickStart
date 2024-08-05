from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

url = config.get("basic info", "url")
print("URL:", url)

username = config.get("credentials", "username")
print("Username:", username)

def get_config(section, option):
    config = ConfigParser()
    config.read("config.ini")

    return config.get(section, option)


print(get_config("credentials", "password"))
