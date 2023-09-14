# версия
VERSION = '3.0'

# sqlite файл
SQLITE_DB = 'db/auth.db' 

# максимальное количество авторизованных входящих IP 
MAX_AUTH_IP_COUNT = 255

# Автоматическая авторизация без добавления входящего IP в доверенные
# Не меняйте на True, только если АБСОЛЮТНО уверены что делаете
AUTO_AUTH = False

# включить/выключить отладку
DEBUG = False

# порт по умолчанию
DEFAULT_PORT = 8080

# вход
FORM_INPUTS_HIDDEN = False

# параметры авторизации
USERNAME_MAX_LEN = 8
PASSWORD_MAX_LEN = 16
