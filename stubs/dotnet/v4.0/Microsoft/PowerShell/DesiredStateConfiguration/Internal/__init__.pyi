from typing import Tuple, Set, Iterable, List


class DscClassCache:
    def ClearCache() -> None: ...
    def ClearImplicitlyImportedFlagFromResourceInClassCache(module: PSModuleInfo, cimClass: CimClass) -> None: ...
    def DebugModeShouldHaveOneValue() -> ErrorRecord: ...
    def DisabledRefreshModeNotValidForPartialConfig(resourceId: str) -> ErrorRecord: ...
    def DuplicateResourceIdInNodeStatementErrorRecord(duplicateResourceId: str, nodeName: str) -> ErrorRecord: ...
    def GenerateMofForType(type: Type) -> str: ...
    def GetBadlyFormedExclusiveResourceIdErrorRecord(badExclusiveResourcereference: str, definingResource: str) -> ErrorRecord: ...
    def GetBadlyFormedRequiredResourceIdErrorRecord(badDependsOnReference: str, definingResource: str) -> ErrorRecord: ...
    def GetCachedClassByFileName(fileName: str) -> List: ...
    def GetCachedClassByModuleName(moduleName: str) -> List: ...
    def GetCachedClassesForModule(module: PSModuleInfo) -> List: ...
    def GetCachedKeywords() -> Collection: ...
    def GetDSCResourceUsageString(keyword: DynamicKeyword) -> str: ...
    def GetFileDefiningClass(className: str) -> List: ...
    def GetLoadedFiles() -> Set(str): ...
    def GetPullModeNeedConfigurationSource(resourceId: str) -> ErrorRecord: ...
    def GetResourceMethodsLinePosition(moduleInfo: PSModuleInfo, resourceName: str) -> Tuple[bool, Dictionary, str]: ...
    def GetStringFromSecureString(value: SecureString) -> str: ...
    @overload
    def ImportCimKeywordsFromModule(module: PSModuleInfo, resourceName: str) -> Tuple[bool, str]: ...
    @overload
    def ImportCimKeywordsFromModule(module: PSModuleInfo, resourceName: str, functionsToDefine: Dictionary) -> Tuple[bool, str]: ...
    @overload
    def ImportCimKeywordsFromModule(module: PSModuleInfo, resourceName: str, functionsToDefine: Dictionary, errors: Collection) -> Tuple[bool, str]: ...
    def ImportClasses(path: str, moduleInfo: Tuple, errors: Collection, importInBoxResourcesImplicitly: bool) -> List: ...
    def ImportClassResourcesFromModule(moduleInfo: PSModuleInfo, resourcesToImport: ICollection, functionsToDefine: Dictionary) -> List: ...
    @overload
    def ImportInstances(path: str) -> List: ...
    @overload
    def ImportInstances(path: str, schemaValidationOption: int) -> List: ...
    @overload
    def ImportScriptKeywordsFromModule(module: PSModuleInfo, resourceName: str) -> Tuple[bool, str]: ...
    @overload
    def ImportScriptKeywordsFromModule(module: PSModuleInfo, resourceName: str, functionsToDefine: Dictionary) -> Tuple[bool, str]: ...
    @overload
    def Initialize() -> None: ...
    @overload
    def Initialize(errors: Collection, modulePathList: List) -> None: ...
    def InvalidConfigurationNameErrorRecord(configurationName: str) -> ErrorRecord: ...
    def InvalidLocalConfigurationManagerPropertyErrorRecord(propertyName: str, validProperties: str) -> ErrorRecord: ...
    def InvalidValueForPropertyErrorRecord(propertyName: str, value: str, keywordName: str, validValues: str) -> ErrorRecord: ...
    @overload
    def LoadDefaultCimKeywords() -> None: ...
    @overload
    def LoadDefaultCimKeywords(functionsToDefine: Dictionary) -> None: ...
    @overload
    def LoadDefaultCimKeywords(errors: Collection) -> None: ...
    @overload
    def LoadDefaultCimKeywords(modulePathList: List) -> None: ...
    @overload
    def LoadDefaultCimKeywords(errors: Collection, cacheResourcesFromMultipleModuleVersions: bool) -> None: ...
    def LoadResourcesFromModule(scriptExtent: IScriptExtent, moduleSpecifications: Set(ModuleSpecification), resourceNames: Set(str), errorList: List) -> None: ...
    def MissingValueForMandatoryPropertyErrorRecord(keywordName: str, typeName: str, propertyName: str) -> ErrorRecord: ...
    def PsDscRunAsCredentialMergeErrorForCompositeResources(resourceId: str) -> ErrorRecord: ...
    def UnsupportedValueForPropertyErrorRecord(propertyName: str, value: str, keywordName: str, validValues: str) -> ErrorRecord: ...
    def ValidateInstanceText(instanceText: str) -> None: ...
    def ValueNotInRangeErrorRecord(property: str, name: str, providedValue: int, lower: int, upper: int) -> ErrorRecord: ...


class DscRemoteOperationsClass:
    def ConvertCimInstanceToObject(targetType: Type, instance: CimInstance, moduleName: str) -> Object: ...
