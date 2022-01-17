from typing import Tuple, Set, Iterable, List


class Extensions(Object):
    @overload
    def Ancestors(source: Iterable[T]) -> Iterable[XElement]: ...
    @overload
    def Ancestors(source: Iterable[T], name: XName) -> Iterable[XElement]: ...
    @overload
    def AncestorsAndSelf(source: Iterable[XElement]) -> Iterable[XElement]: ...
    @overload
    def AncestorsAndSelf(source: Iterable[XElement], name: XName) -> Iterable[XElement]: ...
    @overload
    def Attributes(source: Iterable[XElement]) -> Iterable[XAttribute]: ...
    @overload
    def Attributes(source: Iterable[XElement], name: XName) -> Iterable[XAttribute]: ...
    def DescendantNodes(source: Iterable[T]) -> Iterable[XNode]: ...
    def DescendantNodesAndSelf(source: Iterable[XElement]) -> Iterable[XNode]: ...
    @overload
    def Descendants(source: Iterable[T]) -> Iterable[XElement]: ...
    @overload
    def Descendants(source: Iterable[T], name: XName) -> Iterable[XElement]: ...
    @overload
    def DescendantsAndSelf(source: Iterable[XElement]) -> Iterable[XElement]: ...
    @overload
    def DescendantsAndSelf(source: Iterable[XElement], name: XName) -> Iterable[XElement]: ...
    @overload
    def Elements(source: Iterable[T]) -> Iterable[XElement]: ...
    @overload
    def Elements(source: Iterable[T], name: XName) -> Iterable[XElement]: ...
    def InDocumentOrder(source: Iterable[T]) -> Iterable[T]: ...
    def Nodes(source: Iterable[T]) -> Iterable[XNode]: ...
    @overload
    def Remove(source: Iterable[XAttribute]) -> None: ...
    @overload
    def Remove(source: Iterable[T]) -> None: ...
