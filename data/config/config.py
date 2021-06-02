
def get_config(CONFIG_NAME):
    return (config[config_name])

def refresh_config():
    datei = open(config_dateiname,'r')
    Lines = datei.readlines()
    datei.close()
    for line in Lines:
        zeile = line.strip()
        if (zeile != "" and zeile != " " and "key" not in zeile):
            args = zeile.split('=')
            config_name = args[0]
            config_data = args[1]
            if ("key" in zeile):
                __key = args[2]
                config_data = config_data + __key
            config[config_name] = config_data
        else:
            pass

config = {}
global config_filename
config_filename = "config.conf"
