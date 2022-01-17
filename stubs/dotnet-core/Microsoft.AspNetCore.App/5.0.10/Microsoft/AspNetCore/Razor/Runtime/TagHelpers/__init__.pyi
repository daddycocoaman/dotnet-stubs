from typing import Tuple, Set, Iterable, List


class TagHelperScopeManager:
    def __init__(self, startTagHelperWritingScope: Action, endTagHelperWritingScope: Func): ...
    def Begin(self, tagName: str, tagMode: TagMode, uniqueId: str, executeChildContentAsync: Func) -> TagHelperExecutionContext: ...
    def End(self) -> TagHelperExecutionContext: ...
