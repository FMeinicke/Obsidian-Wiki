---
{"publish":true,"cssclasses":""}
---

#qmake/custom-target #qmake/shell_path #qmake/shell_quote

> [!info] Source
> 
> - <https://stackoverflow.com/a/54566034/12780516>
> - <https://doc.qt.io/qt-5/qmake-function-reference.html#shell-path-path>
> - <https://doc.qt.io/qt-6/qmake-advanced-usage.html#adding-custom-targets>

```qmake
python_modules = $$usrlibs/python_modules
DESTDIR = $$python_modules/labbcan

...

# generate a labbcan.pyi stub file to enable type checking and intellisense
# this requires that python is in PATH, and that mypy and PySide6 are installed
win32: generate_stubs.commands = set PYTHONPATH=$$shell_quote($$shell_path($$python_modules)) && stubgen -m labbcan.labbcan --include-private -o $$python_modules
unix: generate_stubs.commands = PYTHONPATH=$$shell_quote($$python_modules) stubgen -m labbcan.labbcan --include-private -o $$python_modules

QMAKE_EXTRA_TARGETS += copy_init_file generate_stubs
QMAKE_POST_LINK += $$copy_init_file.commands && $$generate_stubs.commands
```