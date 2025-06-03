---
{"publish":true,"cssclasses":""}
---

#QObject/moveToThread #QThread

> [!info] Source
> 
> - <https://doc.qt.io/qt-6/qobject.html#moveToThread>

> [!important]
> 
> **An object can only be "pushed" to another thread (i.e., the current thread must be the same as the object's thread), it cannot be "pulled" from an arbitrary thread to the current thread!**


#pyside6 #Q_ARG #Q_RETURN_ARG #QMetaObject/invokeMethod

> [!info] Source
> 
> - lots of trail and error
> - <https://codereview.qt-project.org/c/pyside/pyside-setup/+/408145/18/sources/pyside6/tests/QtCore/qmetaobject_test.py>

- an (over-complicated) example that creates an object in the thread of the `RemoteControl` object

```python
class RemoteControl(QObject):

    __thread: QThread

    def create_object_in_thread(self, object_type: type[_RemoteObjectT], *args, **kwargs) -> _RemoteObjectT:
        """
        Create a RemoteObject derived object in the thread where the RemoteControl object lives.

        Parameters
        ----------
        object_type : type[_RemoteObjectT]
            The type of the object to create
        args : Any
            Positional arguments for the object constructor
        kwargs : Any
            Keyword arguments for the object constructor

        Returns
        -------
        _RemoteObjectT
            The created object
        """

        return self._create_object_in_thread(object_type, args, kwargs)

    @Slot("QVariant", "QVariantList", "QVariantMap", result=QObject)  # type: ignore[arg-type]
    def _create_object_in_thread(self, object_type: type[QObject], args, kwargs) -> QObject:
        """
        Helper function to allow calling `create_object_in_thread()` in another thread via `QMetaObject.invokeMethod()`
        and correctly map `args` and `kwargs` to the QMetaType system and back.
        """

        if QThread.currentThread() != self.__thread:
            obj: QObject = QMetaObject.invokeMethod(
                self,
                "_create_object_in_thread",  # type: ignore[arg-type]
                Qt.ConnectionType.BlockingQueuedConnection,
                Q_RETURN_ARG(QObject),
                Q_ARG("QVariant", object_type),
                Q_ARG("QVariantList", args),
                Q_ARG("QVariantMap", kwargs),
            )
            return obj

        return object_type(*args, **kwargs)
```

- this is, by the way, way too complicated and can be solved by a much simpler implementation

```python
class RemoteControl(QObject):

    __thread: QThread

    def create_object_in_thread(self, object_type: type[_RemoteObjectT], *args, **kwargs) -> _RemoteObjectT:
        """
        Create a RemoteObject derived object in the thread where the RemoteControl object lives.

        Parameters
        ----------
        object_type : type[_RemoteObjectT]
            The type of the object to create
        args : Any
            Positional arguments for the object constructor
        kwargs : Any
            Keyword arguments for the object constructor

        Returns
        -------
        _RemoteObjectT
            The created object
        """

        obj = object_type(*args, **kwargs)
        obj.moveToThread(self.__thread)
        return obj
```