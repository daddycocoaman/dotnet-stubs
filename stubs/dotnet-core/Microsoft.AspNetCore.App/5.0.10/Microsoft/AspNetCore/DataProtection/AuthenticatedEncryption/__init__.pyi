__all__ = ['ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel','ConfigurationModel']
from typing import Tuple, Set, Iterable, List


class ManagedAuthenticatedEncryptorFactory:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def CreateEncryptorInstance(self, key: IKey) -> IAuthenticatedEncryptor: ...
