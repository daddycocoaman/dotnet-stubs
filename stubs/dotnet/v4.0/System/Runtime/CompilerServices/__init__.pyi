from typing import Tuple, Set, Iterable, List


class CallSite(Object):
    def Create(delegateType: Type, binder: CallSiteBinder) -> CallSite: ...
    @property
    def Binder(self) -> CallSiteBinder: ...




class CallSiteBinder(Object):
    def Bind(self, args: Set(Object), parameters: ReadOnlyCollection, returnLabel: LabelTarget) -> Expression: ...
    def BindDelegate(self, site: CallSite, args: Set(Object)) -> T: ...
    @property
    def UpdateLabel() -> LabelTarget: ...


class CallSiteHelpers(Object):
    def IsInternalFrame(mb: MethodBase) -> bool: ...


class CallSiteOps(Object):
    pass


class Closure(Object):
    def __init__(self, constants: Set(Object), locals: Set(Object)): ...


class DebugInfoGenerator(Object):
    def CreatePdbGenerator() -> DebugInfoGenerator: ...
    def MarkSequencePoint(self, method: LambdaExpression, ilOffset: int, sequencePoint: DebugInfoExpression) -> None: ...


class DynamicAttribute(Attribute):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, transformFlags: Set(bool)): ...
    @property
    def TransformFlags(self) -> List[bool]: ...


class IRuntimeVariables:
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> Object: ...
    @Item.setter
    def Item(self, index: int, value: Object) -> None: ...


class IStrongBox:
    @property
    def Value(self) -> Object: ...
    @Value.setter
    def Value(self, value: Object) -> None: ...






class RuntimeOps(Object):
    pass


