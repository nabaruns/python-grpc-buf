from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Example(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetExampleRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetExampleResponse(_message.Message):
    __slots__ = ("example",)
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    example: Example
    def __init__(self, example: _Optional[_Union[Example, _Mapping]] = ...) -> None: ...

class CreateExampleRequest(_message.Message):
    __slots__ = ("example",)
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    example: Example
    def __init__(self, example: _Optional[_Union[Example, _Mapping]] = ...) -> None: ...

class CreateExampleResponse(_message.Message):
    __slots__ = ("example",)
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    example: Example
    def __init__(self, example: _Optional[_Union[Example, _Mapping]] = ...) -> None: ...
