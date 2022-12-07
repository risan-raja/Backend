from .configDB import configDB
from .configGeneric import AppBaseConfig
from .configSecurity import configSecurity
from .configGenericExt import FlaskExtConfig


class Config(AppBaseConfig, configDB, configSecurity, FlaskExtConfig):
    pass