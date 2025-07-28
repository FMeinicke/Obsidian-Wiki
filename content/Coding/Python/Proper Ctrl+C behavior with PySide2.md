---
{"publish":true,"created":"2025-05-15T09:01:46.732+02:00","modified":"2025-05-26T15:25:02.402+02:00","published":"2025-05-26T15:25:02.402+02:00","cssclasses":""}
---

#qt #qt-for-python #pyside #pyside2

> [!info] Source
>
> - <https://stackoverflow.com/a/11705366/12780516>
> - <https://stackoverflow.com/a/4939113/12780516>

```python
import signal

from PySide2.QtCore import QCoreApplication, QEvent

class CoreApplication(QCoreApplication):
    """needed for proper Ctrl-C behavior (see: https://stackoverflow.com/a/11705366/12780516)"""
    def event(self, event: QEvent) -> bool:
        return super().event(event)

def main():
    handler = None

    def handle_sigint(*args):
        print("handle_sigint")
        global app
        if app is None:
            print("received SIGINT before app was initialized")
            return
        signal.signal(signal.SIGINT, handler)
        app.quit()

    handler = signal.signal(signal.SIGINT, handle_sigint)
    global app
    app = CoreApplication()
    app.startTimer(100)
    app.exec_()


if __name__ == "__main__":
    main()
    print("done")
```

- for PySide6 **on Windows only!**, the only solution that works is to create a custom `CoreApplication` class which overrides `event`, catches `KeyboardInterrupt` in there and then quits the application

```python
from PySide6.QtCore import QCoreApplication, QEvent

class CoreApplication(QCoreApplication):
    """needed for proper Ctrl-C behavior (see: https://stackoverflow.com/a/11705366/12780516)."""

    def event(self, event: QEvent) -> bool:  # noqa: D102
        try:
            return super().event(event)
        except KeyboardInterrupt:
            # NOTE: this only works in a terminal but not in VSCode's debugger
            self.quit()
            return True


def main() -> None:
    """
    Main application entry point.
    """

    if (qapp := QCoreApplication.instance()) is None:
        import sys

        qapp = CoreApplication(sys.argv)
    else:
        # need to use our custom CoreApplication class to handle KeyboardInterrupt
        qapp.__class__ = CoreApplication

    qapp.startTimer(100)

    qapp.exec()


if __name__ == "__main__":
    main()
```

> [!note]- Previous answer
>
> This did not work in combination with a Typer application and I could later not even get this to work on its own in a simple test script.
>
> ```python
> if __name__ == "__main__":
>     class CoreApplication(QCoreApplication):
>         def event(self, event: QEvent) -> bool:
>             return super().event(event)
> 
>     app = CoreApplication([])
> 
>     signal.signal(signal.SIGINT, lambda *a: app.exit())
>     app.startTimer(100)
> 
>     # ...
> 
>     sys.exit(app.exec_())
> ```
>
> - `QCoreApplication.event` has to be re-implemented for some reason otherwise the timer will not work as intended
> - without re-implementation the same can be achieved by using
>
>   ```python
>     timer = QTimer()
>     timer.start(100)  # Let the interpreter run every 100 ms.
>     timer.timeout.connect(lambda: None)
>   ```
>
>   in place of
>
>   ```python
>   app.startTimer(100)
>   ```