# -*- coding: utf-8 -*-
import typing

import pytest  # type: ignore

class FakePopen:
    command: typing.Union[typing.List[str], typing.Tuple[str], str]
    def __init__(self, command: typing.Union[typing.Tuple[str], str]) -> None: ...
    def handle(self) -> None: ...

class ProcessNotRegisteredError(Exception): ...

class ProcessDispatcher:
    process_list: typing.List["Process"]
    built_in_popen: typing.Optional[typing.Callable]
    _allow_unregistered: bool
    @classmethod
    def register(cls, process: "Process") -> None: ...
    @classmethod
    def deregister(cls, process: "Process") -> None: ...
    @classmethod
    def dispatch(
        cls,
        command: typing.Union[typing.Tuple[str], str],
        *_: typing.Any,
        **__: typing.Any
    ) -> None: ...
    @classmethod
    def allow_unregistered(cls, allow: bool) -> None: ...

class Process:
    processes: typing.Dict[typing.Union[str, typing.Tuple[str]], FakePopen]
    def __init__(self) -> None: ...
    def register_subprocess(
        self, command: typing.Union[typing.List[str], typing.Tuple[str], str]
    ) -> None: ...
    def __enter__(self) -> "Process": ...
    def __exit__(self, *args: typing.List, **kwargs: typing.Dict) -> None: ...
    def allow_unregistered(cls, allow: bool) -> None: ...

@pytest.fixture
def process() -> Process: ...
