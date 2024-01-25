from enum import Enum


class ConfigEnvironments(Enum):
    LOCAL = 'local'
    DEFAULT = LOCAL


valid_environments = [ConfigEnvironments.LOCAL.value,
                      ConfigEnvironments.DEFAULT.value]


class Config:
    """
    Configuration for entire project
    Read env variables
    """
    @staticmethod
    def getConnectionString(environment: str = None):
        configValues = Config.config_values()
        if environment not in valid_environments:
            raise ValueError(f'Invalid environment: "{environment}".')
        if environment == ConfigEnvironments.LOCAL.value:
            return configValues['local_connection_string']

    @staticmethod
    def config_values():
        config_dict = dict()
        config_dict = {'local_connection_string': {'host': 'localhost',
                                                   'database': 'test',
                                                   'username': 'postgres',
                                                   'password': 'postgres@2024',
                                                   'port_id': 5432}}
        return config_dict
