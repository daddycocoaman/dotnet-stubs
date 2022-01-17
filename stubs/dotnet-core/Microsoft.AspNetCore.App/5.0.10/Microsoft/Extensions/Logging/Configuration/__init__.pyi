from typing import Tuple, Set, Iterable, List




class ILoggerProviderConfigurationFactory:
    def GetConfiguration(self, providerType: Type) -> IConfiguration: ...


class LoggerProviderOptions:
    def RegisterProviderOptions(services: IServiceCollection) -> None: ...




class LoggingBuilderConfigurationExtensions:
    def AddConfiguration(builder: ILoggingBuilder) -> None: ...
