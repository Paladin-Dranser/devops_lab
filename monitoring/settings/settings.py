import json
import os


def get_file_name() -> str:
    """Get file name where settings is written"""
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'settings.json'
    )

    with open(config_file) as settings_file:
        data = json.load(settings_file)

    return data['settings']['file']


def get_file_type() -> str:
    """Get file type where settings is written"""
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'settings.json'
    )

    with open(config_file) as settings_file:
        data = json.load(settings_file)

    return data['settings']['type']


def get_interval() -> str:
    """Get interval when the script is launched"""
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'settings.json'
    )

    with open(config_file) as settings_file:
        data = json.load(settings_file)

    return data['settings']['interval']


def set_file_name(name: str):
    """Set file name where settings is written"""
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'settings.json'
    )

    with open(config_file) as settings_file:
        data = json.load(settings_file)

    data['settings']['file'] = name

    with open(config_file, 'w', encoding='utf-8') as settings_file:
        json.dump(data, settings_file, ensure_ascii=False, indent=2)


def set_file_type(type: str):
    """Set file type where settings is written"""
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'settings.json'
    )

    with open(config_file) as settings_file:
        data = json.load(settings_file)

    data['settings']['type'] = type

    with open(config_file, 'w', encoding='utf-8') as settings_file:
        json.dump(data, settings_file, ensure_ascii=False, indent=2)


def set_interval(interval: int):
    """Set interval when the script is launched"""
    config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'settings.json'
    )

    with open(config_file) as settings_file:
        data = json.load(settings_file)

    data['settings']['interval'] = interval

    with open(config_file, 'w', encoding='utf-8') as settings_file:
        json.dump(data, settings_file, ensure_ascii=False, indent=2)
