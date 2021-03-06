from typing import Tuple, Set, Iterable, List


class Matrix3D:
    def __init__(self, m11: float, m12: float, m13: float, m14: float, m21: float, m22: float, m23: float, m24: float, m31: float, m32: float, m33: float, m34: float, offsetX: float, offsetY: float, offsetZ: float, m44: float): ...
    @overload
    def Equals(self, value: Matrix3D) -> bool: ...
    @overload
    def Equals(self, o: Object) -> bool: ...
    @property
    def HasInverse(self) -> bool: ...
    @property
    def Identity() -> Matrix3D: ...
    @property
    def IsIdentity(self) -> bool: ...
    @property
    def M11(self) -> float: ...
    @property
    def M12(self) -> float: ...
    @property
    def M13(self) -> float: ...
    @property
    def M14(self) -> float: ...
    @property
    def M21(self) -> float: ...
    @property
    def M22(self) -> float: ...
    @property
    def M23(self) -> float: ...
    @property
    def M24(self) -> float: ...
    @property
    def M31(self) -> float: ...
    @property
    def M32(self) -> float: ...
    @property
    def M33(self) -> float: ...
    @property
    def M34(self) -> float: ...
    @property
    def M44(self) -> float: ...
    @property
    def OffsetX(self) -> float: ...
    @property
    def OffsetY(self) -> float: ...
    @property
    def OffsetZ(self) -> float: ...
    def GetHashCode(self) -> int: ...
    def Invert(self) -> None: ...
    def op_Equality(matrix1: Matrix3D, matrix2: Matrix3D) -> bool: ...
    def op_Inequality(matrix1: Matrix3D, matrix2: Matrix3D) -> bool: ...
    def op_Multiply(matrix1: Matrix3D, matrix2: Matrix3D) -> Matrix3D: ...
    @M11.setter
    def M11(self, value: float) -> None: ...
    @M12.setter
    def M12(self, value: float) -> None: ...
    @M13.setter
    def M13(self, value: float) -> None: ...
    @M14.setter
    def M14(self, value: float) -> None: ...
    @M21.setter
    def M21(self, value: float) -> None: ...
    @M22.setter
    def M22(self, value: float) -> None: ...
    @M23.setter
    def M23(self, value: float) -> None: ...
    @M24.setter
    def M24(self, value: float) -> None: ...
    @M31.setter
    def M31(self, value: float) -> None: ...
    @M32.setter
    def M32(self, value: float) -> None: ...
    @M33.setter
    def M33(self, value: float) -> None: ...
    @M34.setter
    def M34(self, value: float) -> None: ...
    @M44.setter
    def M44(self, value: float) -> None: ...
    @OffsetX.setter
    def OffsetX(self, value: float) -> None: ...
    @OffsetY.setter
    def OffsetY(self, value: float) -> None: ...
    @OffsetZ.setter
    def OffsetZ(self, value: float) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToString(self, provider: IFormatProvider) -> str: ...
