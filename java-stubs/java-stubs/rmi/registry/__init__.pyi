
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.rmi
import java.rmi.server
import typing



class LocateRegistry:
    @typing.overload
    @staticmethod
    def createRegistry(int: int) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def createRegistry(int: int, rMIClientSocketFactory: typing.Union[java.rmi.server.RMIClientSocketFactory, typing.Callable], rMIServerSocketFactory: typing.Union[java.rmi.server.RMIServerSocketFactory, typing.Callable]) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry() -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(int: int) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(string: typing.Union[java.lang.String, str]) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(string: typing.Union[java.lang.String, str], int: int) -> 'Registry': ...
    @typing.overload
    @staticmethod
    def getRegistry(string: typing.Union[java.lang.String, str], int: int, rMIClientSocketFactory: typing.Union[java.rmi.server.RMIClientSocketFactory, typing.Callable]) -> 'Registry': ...

class Registry(java.rmi.Remote):
    REGISTRY_PORT: typing.ClassVar[int] = ...
    def bind(self, string: typing.Union[java.lang.String, str], remote: java.rmi.Remote) -> None: ...
    def list(self) -> typing.MutableSequence[java.lang.String]: ...
    def lookup(self, string: typing.Union[java.lang.String, str]) -> java.rmi.Remote: ...
    def rebind(self, string: typing.Union[java.lang.String, str], remote: java.rmi.Remote) -> None: ...
    def unbind(self, string: typing.Union[java.lang.String, str]) -> None: ...

class RegistryHandler:
    def registryImpl(self, int: int) -> Registry: ...
    def registryStub(self, string: typing.Union[java.lang.String, str], int: int) -> Registry: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi.registry")``.

    LocateRegistry: typing.Type[LocateRegistry]
    Registry: typing.Type[Registry]
    RegistryHandler: typing.Type[RegistryHandler]
