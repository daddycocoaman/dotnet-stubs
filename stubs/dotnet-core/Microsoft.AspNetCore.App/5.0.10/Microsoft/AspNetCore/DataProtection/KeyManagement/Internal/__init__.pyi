from typing import Tuple, Set, Iterable, List


class CacheableKeyRing:
    pass


class DefaultKeyResolution:
    pass


class ICacheableKeyRingProvider:
    def GetCacheableKeyRing(self, now: DateTimeOffset) -> CacheableKeyRing: ...


class IDefaultKeyResolver:
    def ResolveDefaultKeyPolicy(self, now: DateTimeOffset, allKeys: Iterable[IKey]) -> DefaultKeyResolution: ...


class IInternalXmlKeyManager:
    def CreateNewKey(self, keyId: Guid, creationDate: DateTimeOffset, activationDate: DateTimeOffset, expirationDate: DateTimeOffset) -> IKey: ...
    def DeserializeDescriptorFromKeyElement(self, keyElement: XElement) -> IAuthenticatedEncryptorDescriptor: ...
    def RevokeSingleKey(self, keyId: Guid, revocationDate: DateTimeOffset, reason: str) -> None: ...


class IKeyRing:
    @property
    def DefaultAuthenticatedEncryptor(self) -> IAuthenticatedEncryptor: ...
    @property
    def DefaultKeyId(self) -> Guid: ...
    def GetAuthenticatedEncryptorByKeyId(self, keyId: Guid) -> Tuple[IAuthenticatedEncryptor, bool]: ...


class IKeyRingProvider:
    def GetCurrentKeyRing(self) -> IKeyRing: ...
