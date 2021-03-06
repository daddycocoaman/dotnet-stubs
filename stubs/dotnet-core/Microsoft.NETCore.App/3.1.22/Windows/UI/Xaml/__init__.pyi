__all__ = ['Automation','Markup','Media']
from typing import Tuple, Set, Iterable, List


class CornerRadius:
    @overload
    def __init__(self, uniformRadius: float): ...
    @overload
    def __init__(self, topLeft: float, topRight: float, bottomRight: float, bottomLeft: float): ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, cornerRadius: CornerRadius) -> bool: ...
    @property
    def BottomLeft(self) -> float: ...
    @property
    def BottomRight(self) -> float: ...
    @property
    def TopLeft(self) -> float: ...
    @property
    def TopRight(self) -> float: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(cr1: CornerRadius, cr2: CornerRadius) -> bool: ...
    def op_Inequality(cr1: CornerRadius, cr2: CornerRadius) -> bool: ...
    @BottomLeft.setter
    def BottomLeft(self, value: float) -> None: ...
    @BottomRight.setter
    def BottomRight(self, value: float) -> None: ...
    @TopLeft.setter
    def TopLeft(self, value: float) -> None: ...
    @TopRight.setter
    def TopRight(self, value: float) -> None: ...
    def ToString(self) -> str: ...


class Duration:
    def __init__(self, timeSpan: TimeSpan): ...
    def Add(self, duration: Duration) -> Duration: ...
    def Compare(t1: Duration, t2: Duration) -> int: ...
    @overload
    def Equals(self, duration: Duration) -> bool: ...
    @overload
    def Equals(self, value: Object) -> bool: ...
    @overload
    def Equals(t1: Duration, t2: Duration) -> bool: ...
    @property
    def Automatic() -> Duration: ...
    @property
    def Forever() -> Duration: ...
    @property
    def HasTimeSpan(self) -> bool: ...
    @property
    def TimeSpan(self) -> TimeSpan: ...
    def GetHashCode(self) -> int: ...
    def op_Addition(t1: Duration, t2: Duration) -> Duration: ...
    def op_Equality(t1: Duration, t2: Duration) -> bool: ...
    def op_GreaterThan(t1: Duration, t2: Duration) -> bool: ...
    def op_GreaterThanOrEqual(t1: Duration, t2: Duration) -> bool: ...
    def op_Implicit(timeSpan: TimeSpan) -> Duration: ...
    def op_Inequality(t1: Duration, t2: Duration) -> bool: ...
    def op_LessThan(t1: Duration, t2: Duration) -> bool: ...
    def op_LessThanOrEqual(t1: Duration, t2: Duration) -> bool: ...
    def op_Subtraction(t1: Duration, t2: Duration) -> Duration: ...
    def op_UnaryPlus(duration: Duration) -> Duration: ...
    def Subtract(self, duration: Duration) -> Duration: ...
    def ToString(self) -> str: ...


class DurationType:
    Automatic = 0
    TimeSpan = 1
    Forever = 2


class GridLength:
    @overload
    def __init__(self, pixels: float): ...
    @overload
    def __init__(self, value: float, type: GridUnitType): ...
    @overload
    def Equals(self, oCompare: Object) -> bool: ...
    @overload
    def Equals(self, gridLength: GridLength) -> bool: ...
    @property
    def Auto() -> GridLength: ...
    @property
    def GridUnitType(self) -> GridUnitType: ...
    @property
    def IsAbsolute(self) -> bool: ...
    @property
    def IsAuto(self) -> bool: ...
    @property
    def IsStar(self) -> bool: ...
    @property
    def Value(self) -> float: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(gl1: GridLength, gl2: GridLength) -> bool: ...
    def op_Inequality(gl1: GridLength, gl2: GridLength) -> bool: ...
    def ToString(self) -> str: ...


class GridUnitType:
    Auto = 0
    Pixel = 1
    Star = 2


class LayoutCycleException:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class Thickness:
    @overload
    def __init__(self, uniformLength: float): ...
    @overload
    def __init__(self, left: float, top: float, right: float, bottom: float): ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, thickness: Thickness) -> bool: ...
    @property
    def Bottom(self) -> float: ...
    @property
    def Left(self) -> float: ...
    @property
    def Right(self) -> float: ...
    @property
    def Top(self) -> float: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(t1: Thickness, t2: Thickness) -> bool: ...
    def op_Inequality(t1: Thickness, t2: Thickness) -> bool: ...
    @Bottom.setter
    def Bottom(self, value: float) -> None: ...
    @Left.setter
    def Left(self, value: float) -> None: ...
    @Right.setter
    def Right(self, value: float) -> None: ...
    @Top.setter
    def Top(self, value: float) -> None: ...
    def ToString(self) -> str: ...
