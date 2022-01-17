from typing import Tuple, Set, Iterable, List


class Vector4(ValueType):
    @overload
    def __init__(self, value: Single): ...
    @overload
    def __init__(self, value: Vector3, w: Single): ...
    @overload
    def __init__(self, value: Vector2, z: Single, w: Single): ...
    @overload
    def __init__(self, x: Single, y: Single, z: Single, w: Single): ...
    def Abs(value: Vector4) -> Vector4: ...
    def Add(left: Vector4, right: Vector4) -> Vector4: ...
    def Clamp(value1: Vector4, min: Vector4, max: Vector4) -> Vector4: ...
    @overload
    def CopyTo(self, array: Set(Single)) -> None: ...
    @overload
    def CopyTo(self, array: Set(Single), index: int) -> None: ...
    def Distance(value1: Vector4, value2: Vector4) -> Single: ...
    def DistanceSquared(value1: Vector4, value2: Vector4) -> Single: ...
    @overload
    def Divide(left: Vector4, right: Vector4) -> Vector4: ...
    @overload
    def Divide(left: Vector4, divisor: Single) -> Vector4: ...
    def Dot(vector1: Vector4, vector2: Vector4) -> Single: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, other: Vector4) -> bool: ...
    @property
    def One() -> Vector4: ...
    @property
    def UnitW() -> Vector4: ...
    @property
    def UnitX() -> Vector4: ...
    @property
    def UnitY() -> Vector4: ...
    @property
    def UnitZ() -> Vector4: ...
    @property
    def Zero() -> Vector4: ...
    def GetHashCode(self) -> int: ...
    def Length(self) -> Single: ...
    def LengthSquared(self) -> Single: ...
    def Lerp(value1: Vector4, value2: Vector4, amount: Single) -> Vector4: ...
    def Max(value1: Vector4, value2: Vector4) -> Vector4: ...
    def Min(value1: Vector4, value2: Vector4) -> Vector4: ...
    @overload
    def Multiply(left: Single, right: Vector4) -> Vector4: ...
    @overload
    def Multiply(left: Vector4, right: Vector4) -> Vector4: ...
    @overload
    def Multiply(left: Vector4, right: Single) -> Vector4: ...
    def Negate(value: Vector4) -> Vector4: ...
    def Normalize(vector: Vector4) -> Vector4: ...
    def op_Addition(left: Vector4, right: Vector4) -> Vector4: ...
    @overload
    def op_Division(value1: Vector4, value2: Single) -> Vector4: ...
    @overload
    def op_Division(left: Vector4, right: Vector4) -> Vector4: ...
    def op_Equality(left: Vector4, right: Vector4) -> bool: ...
    def op_Inequality(left: Vector4, right: Vector4) -> bool: ...
    @overload
    def op_Multiply(left: Vector4, right: Vector4) -> Vector4: ...
    @overload
    def op_Multiply(left: Vector4, right: Single) -> Vector4: ...
    @overload
    def op_Multiply(left: Single, right: Vector4) -> Vector4: ...
    def op_Subtraction(left: Vector4, right: Vector4) -> Vector4: ...
    def op_UnaryNegation(value: Vector4) -> Vector4: ...
    def SquareRoot(value: Vector4) -> Vector4: ...
    def Subtract(left: Vector4, right: Vector4) -> Vector4: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToString(self, format: str) -> str: ...
    @overload
    def ToString(self, format: str, formatProvider: IFormatProvider) -> str: ...
    @overload
    def Transform(position: Vector2, matrix: Matrix4x4) -> Vector4: ...
    @overload
    def Transform(position: Vector3, matrix: Matrix4x4) -> Vector4: ...
    @overload
    def Transform(value: Vector4, rotation: Quaternion) -> Vector4: ...
    @overload
    def Transform(value: Vector3, rotation: Quaternion) -> Vector4: ...
    @overload
    def Transform(vector: Vector4, matrix: Matrix4x4) -> Vector4: ...
    @overload
    def Transform(value: Vector2, rotation: Quaternion) -> Vector4: ...
