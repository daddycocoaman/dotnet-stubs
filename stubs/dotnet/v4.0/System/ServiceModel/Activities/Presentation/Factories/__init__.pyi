from typing import Tuple, Set, Iterable, List


class ReceiveAndSendReplyFactory(Object):
    def __init__(self): ...
    def Create(self, target: DependencyObject) -> Activity: ...


class SendAndReceiveReplyFactory(Object):
    def __init__(self): ...
    def Create(self, target: DependencyObject) -> Activity: ...
