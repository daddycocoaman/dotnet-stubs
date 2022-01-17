from typing import Tuple, Set, Iterable, List


class IXmlJsonWriterInitializer:
    def SetOutput(self, stream: Stream, encoding: Encoding, ownsStream: bool) -> None: ...
