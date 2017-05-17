import configparser
import os

def create_config(path):
    # Creates config file

    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)

def get_config(path):
    # Checks for a config path and returns the object

    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section}, {setting} is {value}".format(section=section, setting=setting, value=value)
    print(msg)
    return value

def update_setting(path, section, setting, value):
    # Updates a setting

    config = get_config(path)
    config.set(section, setting, value)

    with open(path, "w") as config_file:
        config.write(config_file)

def delete_setting(path, section, setting):
    # Delete a setting

    config = get_config(path)
    config.remove_option(section, setting)

    with open(path, "w") as config_file:
        config.write(config_file)

def interpolation_demo(path):
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    print(config.get("Settings", "font_info"))
    print(config.get("Settings", "font_info", vars={"font": "Ariel", "font_size": "100"}))


if __name__ == "__main__":
    path = "settings.ini"
    interpolation_demo(path)
