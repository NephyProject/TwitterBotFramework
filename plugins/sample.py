# coding=utf-8
from pychroner import PluginType, PluginAPI

@PluginAPI(PluginType.Schedule)
def 任意の関数名():
    # なんらかの処理

    print("Hello World")