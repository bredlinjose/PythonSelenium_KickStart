import os

from utility_methods import Log_Utils, Excel_Utils, Config_Utils

logger = Log_Utils.generate_log()
logger.info("For loop started")
for i in range(1, 6):
    print(i)
    logger.info("The current value of i is: " + str(i))
logger.info("For loop ended")

print("URL:", Config_Utils.get_config("basic info", "url"))
print("Password:", Config_Utils.get_config("credentials", "password"))

# file = os.path.abspath('.') + '\\files' + "\\test_data.xlsx"
file = os.path.join(os.path.dirname(os.path.abspath('..')), "files\\test_data.xlsx")

print(file)
print("Value:", Excel_Utils.read_data(file, "calculate", 1, 1))
