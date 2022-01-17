from typing import Tuple, Set, Iterable, List


class WebRenderer(Renderer):
    def __init__(self, serviceProvider: IServiceProvider, loggerFactory: ILoggerFactory, jsonOptions: JsonSerializerOptions, jsComponentInterop: JSComponentInterop): ...
