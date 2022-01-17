__all__ = ['Metadata']
from typing import Tuple, Set, Iterable, List


class IJsonOnDeserialized:
    def OnDeserialized(self) -> None: ...


class IJsonOnDeserializing:
    def OnDeserializing(self) -> None: ...


class IJsonOnSerialized:
    def OnSerialized(self) -> None: ...


class IJsonOnSerializing:
    def OnSerializing(self) -> None: ...


class JsonAttribute(Attribute):
    pass


class JsonConstructorAttribute(JsonAttribute):
    def __init__(self): ...


class JsonConverter(Object):
    def CanConvert(self, typeToConvert: Type) -> bool: ...




class JsonConverterAttribute(JsonAttribute):
    def __init__(self, converterType: Type): ...
    def CreateConverter(self, typeToConvert: Type) -> JsonConverter: ...
    @property
    def ConverterType(self) -> Type: ...


class JsonConverterFactory(JsonConverter):
    def CreateConverter(self, typeToConvert: Type, options: JsonSerializerOptions) -> JsonConverter: ...


class JsonExtensionDataAttribute(JsonAttribute):
    def __init__(self): ...


class JsonIgnoreAttribute(JsonAttribute):
    def __init__(self): ...
    @property
    def Condition(self) -> JsonIgnoreCondition: ...
    @Condition.setter
    def Condition(self, value: JsonIgnoreCondition) -> None: ...


class JsonIgnoreCondition:
    Never = 0
    Always = 1
    WhenWritingDefault = 2
    WhenWritingNull = 3


class JsonIncludeAttribute(JsonAttribute):
    def __init__(self): ...


class JsonKnownNamingPolicy:
    Unspecified = 0
    CamelCase = 1


class JsonNumberHandling:
    Strict = 0
    AllowReadingFromString = 1
    WriteAsString = 2
    AllowNamedFloatingPointLiterals = 4


class JsonNumberHandlingAttribute(JsonAttribute):
    def __init__(self, handling: JsonNumberHandling): ...
    @property
    def Handling(self) -> JsonNumberHandling: ...


class JsonPropertyNameAttribute(JsonAttribute):
    def __init__(self, name: str): ...
    @property
    def Name(self) -> str: ...


class JsonPropertyOrderAttribute(JsonAttribute):
    def __init__(self, order: int): ...
    @property
    def Order(self) -> int: ...


class JsonSerializableAttribute(JsonAttribute):
    def __init__(self, type: Type): ...
    @property
    def GenerationMode(self) -> JsonSourceGenerationMode: ...
    @property
    def TypeInfoPropertyName(self) -> str: ...
    @GenerationMode.setter
    def GenerationMode(self, value: JsonSourceGenerationMode) -> None: ...
    @TypeInfoPropertyName.setter
    def TypeInfoPropertyName(self, value: str) -> None: ...


class JsonSerializerContext(Object):
    @property
    def Options(self) -> JsonSerializerOptions: ...
    def GetTypeInfo(self, type: Type) -> JsonTypeInfo: ...


class JsonSourceGenerationMode:
    Default = 0
    Metadata = 1
    Serialization = 2


class JsonSourceGenerationOptionsAttribute(JsonAttribute):
    def __init__(self): ...
    @property
    def DefaultIgnoreCondition(self) -> JsonIgnoreCondition: ...
    @property
    def GenerationMode(self) -> JsonSourceGenerationMode: ...
    @property
    def IgnoreReadOnlyFields(self) -> bool: ...
    @property
    def IgnoreReadOnlyProperties(self) -> bool: ...
    @property
    def IncludeFields(self) -> bool: ...
    @property
    def PropertyNamingPolicy(self) -> JsonKnownNamingPolicy: ...
    @property
    def WriteIndented(self) -> bool: ...
    @DefaultIgnoreCondition.setter
    def DefaultIgnoreCondition(self, value: JsonIgnoreCondition) -> None: ...
    @GenerationMode.setter
    def GenerationMode(self, value: JsonSourceGenerationMode) -> None: ...
    @IgnoreReadOnlyFields.setter
    def IgnoreReadOnlyFields(self, value: bool) -> None: ...
    @IgnoreReadOnlyProperties.setter
    def IgnoreReadOnlyProperties(self, value: bool) -> None: ...
    @IncludeFields.setter
    def IncludeFields(self, value: bool) -> None: ...
    @PropertyNamingPolicy.setter
    def PropertyNamingPolicy(self, value: JsonKnownNamingPolicy) -> None: ...
    @WriteIndented.setter
    def WriteIndented(self, value: bool) -> None: ...


class JsonStringEnumConverter(JsonConverterFactory):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, namingPolicy: JsonNamingPolicy, allowIntegerValues: bool): ...
    def CanConvert(self, typeToConvert: Type) -> bool: ...
    def CreateConverter(self, typeToConvert: Type, options: JsonSerializerOptions) -> JsonConverter: ...


class JsonUnknownTypeHandling:
    JsonElement = 0
    JsonNode = 1


class ReferenceHandler(Object):
    def CreateResolver(self) -> ReferenceResolver: ...
    @property
    def IgnoreCycles() -> ReferenceHandler: ...
    @property
    def Preserve() -> ReferenceHandler: ...




class ReferenceResolver(Object):
    def AddReference(self, referenceId: str, value: Object) -> None: ...
    def GetReference(self, value: Object) -> Tuple[str, bool]: ...
    def ResolveReference(self, referenceId: str) -> Object: ...
