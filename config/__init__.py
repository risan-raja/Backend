from .ConfigDB import ConfigDB
from .configGeneric import AppBaseConfig
from .configGenericExt import FlaskExtConfig
from .configSecurity import configSecurity
from .envDevelop import DevelopmentConfig


class Config(AppBaseConfig, ConfigDB, configSecurity, FlaskExtConfig, DevelopmentConfig):
    pass
