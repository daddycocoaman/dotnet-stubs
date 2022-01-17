from typing import Tuple, Set, Iterable, List


class BigInteger(ValueType):
    @overload
    def __init__(self, value: int): ...
    @overload
    def __init__(self, value: UInt32): ...
    @overload
    def __init__(self, value: Int64): ...
    @overload
    def __init__(self, value: UInt64): ...
    @overload
    def __init__(self, value: Single): ...
    @overload
    def __init__(self, value: float): ...
    @overload
    def __init__(self, value: Decimal): ...
    @overload
    def __init__(self, value: Set(Byte)): ...
    @overload
    def __init__(self, value: ReadOnlySpan, isUnsigned: bool, isBigEndian: bool): ...
    def Abs(value: BigInteger) -> BigInteger: ...
    def Add(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def Compare(left: BigInteger, right: BigInteger) -> int: ...
    @overload
    def CompareTo(self, obj: Object) -> int: ...
    @overload
    def CompareTo(self, other: BigInteger) -> int: ...
    @overload
    def CompareTo(self, other: UInt64) -> int: ...
    @overload
    def CompareTo(self, other: Int64) -> int: ...
    def Divide(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    def DivRem(dividend: BigInteger, divisor: BigInteger) -> Tuple[BigInteger, BigInteger]: ...
    @overload
    def Equals(self, other: Int64) -> bool: ...
    @overload
    def Equals(self, other: UInt64) -> bool: ...
    @overload
    def Equals(self, other: BigInteger) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def IsEven(self) -> bool: ...
    @property
    def IsOne(self) -> bool: ...
    @property
    def IsPowerOfTwo(self) -> bool: ...
    @property
    def IsZero(self) -> bool: ...
    @property
    def MinusOne() -> BigInteger: ...
    @property
    def One() -> BigInteger: ...
    @property
    def Sign(self) -> int: ...
    @property
    def Zero() -> BigInteger: ...
    def GetBitLength(self) -> Int64: ...
    def GetByteCount(self, isUnsigned: bool) -> int: ...
    def GetHashCode(self) -> int: ...
    def GreatestCommonDivisor(left: BigInteger, right: BigInteger) -> BigInteger: ...
    @overload
    def Log(value: BigInteger) -> float: ...
    @overload
    def Log(value: BigInteger, baseValue: float) -> float: ...
    def Log10(value: BigInteger) -> float: ...
    def Max(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def Min(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def ModPow(value: BigInteger, exponent: BigInteger, modulus: BigInteger) -> BigInteger: ...
    def Multiply(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def Negate(value: BigInteger) -> BigInteger: ...
    def op_Addition(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def op_BitwiseAnd(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def op_BitwiseOr(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def op_Decrement(value: BigInteger) -> BigInteger: ...
    def op_Division(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    @overload
    def op_Equality(left: UInt64, right: BigInteger) -> bool: ...
    @overload
    def op_Equality(left: BigInteger, right: Int64) -> bool: ...
    @overload
    def op_Equality(left: BigInteger, right: BigInteger) -> bool: ...
    @overload
    def op_Equality(left: Int64, right: BigInteger) -> bool: ...
    @overload
    def op_Equality(left: BigInteger, right: UInt64) -> bool: ...
    def op_ExclusiveOr(left: BigInteger, right: BigInteger) -> BigInteger: ...
    @overload
    def op_Explicit(value: Single) -> BigInteger: ...
    @overload
    def op_Explicit(value: Decimal) -> BigInteger: ...
    @overload
    def op_Explicit(value: BigInteger) -> Decimal: ...
    @overload
    def op_Explicit(value: BigInteger) -> Byte: ...
    @overload
    def op_Explicit(value: BigInteger) -> Int64: ...
    @overload
    def op_Explicit(value: BigInteger) -> SByte: ...
    @overload
    def op_Explicit(value: BigInteger) -> Int16: ...
    @overload
    def op_Explicit(value: BigInteger) -> UInt16: ...
    @overload
    def op_Explicit(value: BigInteger) -> int: ...
    @overload
    def op_Explicit(value: BigInteger) -> UInt32: ...
    @overload
    def op_Explicit(value: BigInteger) -> Single: ...
    @overload
    def op_Explicit(value: BigInteger) -> float: ...
    @overload
    def op_Explicit(value: BigInteger) -> UInt64: ...
    @overload
    def op_Explicit(value: float) -> BigInteger: ...
    @overload
    def op_GreaterThan(left: BigInteger, right: Int64) -> bool: ...
    @overload
    def op_GreaterThan(left: BigInteger, right: BigInteger) -> bool: ...
    @overload
    def op_GreaterThan(left: BigInteger, right: UInt64) -> bool: ...
    @overload
    def op_GreaterThan(left: Int64, right: BigInteger) -> bool: ...
    @overload
    def op_GreaterThan(left: UInt64, right: BigInteger) -> bool: ...
    @overload
    def op_GreaterThanOrEqual(left: BigInteger, right: Int64) -> bool: ...
    @overload
    def op_GreaterThanOrEqual(left: BigInteger, right: UInt64) -> bool: ...
    @overload
    def op_GreaterThanOrEqual(left: Int64, right: BigInteger) -> bool: ...
    @overload
    def op_GreaterThanOrEqual(left: BigInteger, right: BigInteger) -> bool: ...
    @overload
    def op_GreaterThanOrEqual(left: UInt64, right: BigInteger) -> bool: ...
    @overload
    def op_Implicit(value: SByte) -> BigInteger: ...
    @overload
    def op_Implicit(value: Byte) -> BigInteger: ...
    @overload
    def op_Implicit(value: int) -> BigInteger: ...
    @overload
    def op_Implicit(value: UInt32) -> BigInteger: ...
    @overload
    def op_Implicit(value: Int64) -> BigInteger: ...
    @overload
    def op_Implicit(value: UInt64) -> BigInteger: ...
    @overload
    def op_Implicit(value: UInt16) -> BigInteger: ...
    @overload
    def op_Implicit(value: Int16) -> BigInteger: ...
    def op_Increment(value: BigInteger) -> BigInteger: ...
    @overload
    def op_Inequality(left: BigInteger, right: Int64) -> bool: ...
    @overload
    def op_Inequality(left: BigInteger, right: UInt64) -> bool: ...
    @overload
    def op_Inequality(left: BigInteger, right: BigInteger) -> bool: ...
    @overload
    def op_Inequality(left: UInt64, right: BigInteger) -> bool: ...
    @overload
    def op_Inequality(left: Int64, right: BigInteger) -> bool: ...
    def op_LeftShift(value: BigInteger, shift: int) -> BigInteger: ...
    @overload
    def op_LessThan(left: BigInteger, right: BigInteger) -> bool: ...
    @overload
    def op_LessThan(left: BigInteger, right: Int64) -> bool: ...
    @overload
    def op_LessThan(left: Int64, right: BigInteger) -> bool: ...
    @overload
    def op_LessThan(left: BigInteger, right: UInt64) -> bool: ...
    @overload
    def op_LessThan(left: UInt64, right: BigInteger) -> bool: ...
    @overload
    def op_LessThanOrEqual(left: BigInteger, right: UInt64) -> bool: ...
    @overload
    def op_LessThanOrEqual(left: Int64, right: BigInteger) -> bool: ...
    @overload
    def op_LessThanOrEqual(left: BigInteger, right: BigInteger) -> bool: ...
    @overload
    def op_LessThanOrEqual(left: BigInteger, right: Int64) -> bool: ...
    @overload
    def op_LessThanOrEqual(left: UInt64, right: BigInteger) -> bool: ...
    def op_Modulus(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    def op_Multiply(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def op_OnesComplement(value: BigInteger) -> BigInteger: ...
    def op_RightShift(value: BigInteger, shift: int) -> BigInteger: ...
    def op_Subtraction(left: BigInteger, right: BigInteger) -> BigInteger: ...
    def op_UnaryNegation(value: BigInteger) -> BigInteger: ...
    def op_UnaryPlus(value: BigInteger) -> BigInteger: ...
    @overload
    def Parse(value: str) -> BigInteger: ...
    @overload
    def Parse(value: str, style: NumberStyles) -> BigInteger: ...
    @overload
    def Parse(value: str, provider: IFormatProvider) -> BigInteger: ...
    @overload
    def Parse(value: str, style: NumberStyles, provider: IFormatProvider) -> BigInteger: ...
    @overload
    def Parse(value: ReadOnlySpan, style: NumberStyles, provider: IFormatProvider) -> BigInteger: ...
    def Pow(value: BigInteger, exponent: int) -> BigInteger: ...
    def Remainder(dividend: BigInteger, divisor: BigInteger) -> BigInteger: ...
    def Subtract(left: BigInteger, right: BigInteger) -> BigInteger: ...
    @overload
    def ToByteArray(self) -> Set(Byte): ...
    @overload
    def ToByteArray(self, isUnsigned: bool, isBigEndian: bool) -> Set(Byte): ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToString(self, provider: IFormatProvider) -> str: ...
    @overload
    def ToString(self, format: str) -> str: ...
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str: ...
    def TryFormat(self, destination: Span, format: ReadOnlySpan, provider: IFormatProvider) -> Tuple[bool, int]: ...
    @overload
    def TryParse(value: str) -> Tuple[bool, BigInteger]: ...
    @overload
    def TryParse(value: ReadOnlySpan) -> Tuple[bool, BigInteger]: ...
    @overload
    def TryParse(value: str, style: NumberStyles, provider: IFormatProvider) -> Tuple[bool, BigInteger]: ...
    @overload
    def TryParse(value: ReadOnlySpan, style: NumberStyles, provider: IFormatProvider) -> Tuple[bool, BigInteger]: ...
    def TryWriteBytes(self, destination: Span, isUnsigned: bool, isBigEndian: bool) -> Tuple[bool, int]: ...


class Complex(ValueType):
    def __init__(self, real: float, imaginary: float): ...
    def Abs(value: Complex) -> float: ...
    def Acos(value: Complex) -> Complex: ...
    @overload
    def Add(left: float, right: Complex) -> Complex: ...
    @overload
    def Add(left: Complex, right: float) -> Complex: ...
    @overload
    def Add(left: Complex, right: Complex) -> Complex: ...
    def Asin(value: Complex) -> Complex: ...
    def Atan(value: Complex) -> Complex: ...
    def Conjugate(value: Complex) -> Complex: ...
    def Cos(value: Complex) -> Complex: ...
    def Cosh(value: Complex) -> Complex: ...
    @overload
    def Divide(dividend: Complex, divisor: Complex) -> Complex: ...
    @overload
    def Divide(dividend: Complex, divisor: float) -> Complex: ...
    @overload
    def Divide(dividend: float, divisor: Complex) -> Complex: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, value: Complex) -> bool: ...
    def Exp(value: Complex) -> Complex: ...
    def FromPolarCoordinates(magnitude: float, phase: float) -> Complex: ...
    @property
    def Imaginary(self) -> float: ...
    @property
    def Magnitude(self) -> float: ...
    @property
    def Phase(self) -> float: ...
    @property
    def Real(self) -> float: ...
    def GetHashCode(self) -> int: ...
    def IsFinite(value: Complex) -> bool: ...
    def IsInfinity(value: Complex) -> bool: ...
    def IsNaN(value: Complex) -> bool: ...
    @overload
    def Log(value: Complex) -> Complex: ...
    @overload
    def Log(value: Complex, baseValue: float) -> Complex: ...
    def Log10(value: Complex) -> Complex: ...
    @overload
    def Multiply(left: Complex, right: Complex) -> Complex: ...
    @overload
    def Multiply(left: Complex, right: float) -> Complex: ...
    @overload
    def Multiply(left: float, right: Complex) -> Complex: ...
    def Negate(value: Complex) -> Complex: ...
    @overload
    def op_Addition(left: Complex, right: float) -> Complex: ...
    @overload
    def op_Addition(left: float, right: Complex) -> Complex: ...
    @overload
    def op_Addition(left: Complex, right: Complex) -> Complex: ...
    @overload
    def op_Division(left: Complex, right: float) -> Complex: ...
    @overload
    def op_Division(left: float, right: Complex) -> Complex: ...
    @overload
    def op_Division(left: Complex, right: Complex) -> Complex: ...
    def op_Equality(left: Complex, right: Complex) -> bool: ...
    @overload
    def op_Explicit(value: BigInteger) -> Complex: ...
    @overload
    def op_Explicit(value: Decimal) -> Complex: ...
    @overload
    def op_Implicit(value: Int16) -> Complex: ...
    @overload
    def op_Implicit(value: int) -> Complex: ...
    @overload
    def op_Implicit(value: Int64) -> Complex: ...
    @overload
    def op_Implicit(value: UInt16) -> Complex: ...
    @overload
    def op_Implicit(value: UInt64) -> Complex: ...
    @overload
    def op_Implicit(value: SByte) -> Complex: ...
    @overload
    def op_Implicit(value: Byte) -> Complex: ...
    @overload
    def op_Implicit(value: Single) -> Complex: ...
    @overload
    def op_Implicit(value: float) -> Complex: ...
    @overload
    def op_Implicit(value: UInt32) -> Complex: ...
    def op_Inequality(left: Complex, right: Complex) -> bool: ...
    @overload
    def op_Multiply(left: Complex, right: Complex) -> Complex: ...
    @overload
    def op_Multiply(left: Complex, right: float) -> Complex: ...
    @overload
    def op_Multiply(left: float, right: Complex) -> Complex: ...
    @overload
    def op_Subtraction(left: float, right: Complex) -> Complex: ...
    @overload
    def op_Subtraction(left: Complex, right: float) -> Complex: ...
    @overload
    def op_Subtraction(left: Complex, right: Complex) -> Complex: ...
    def op_UnaryNegation(value: Complex) -> Complex: ...
    @overload
    def Pow(value: Complex, power: Complex) -> Complex: ...
    @overload
    def Pow(value: Complex, power: float) -> Complex: ...
    def Reciprocal(value: Complex) -> Complex: ...
    def Sin(value: Complex) -> Complex: ...
    def Sinh(value: Complex) -> Complex: ...
    def Sqrt(value: Complex) -> Complex: ...
    @overload
    def Subtract(left: Complex, right: Complex) -> Complex: ...
    @overload
    def Subtract(left: Complex, right: float) -> Complex: ...
    @overload
    def Subtract(left: float, right: Complex) -> Complex: ...
    def Tan(value: Complex) -> Complex: ...
    def Tanh(value: Complex) -> Complex: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToString(self, provider: IFormatProvider) -> str: ...
    @overload
    def ToString(self, format: str) -> str: ...
    @overload
    def ToString(self, format: str, provider: IFormatProvider) -> str: ...
