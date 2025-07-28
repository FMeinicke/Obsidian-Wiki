---
{"publish":true,"created":"2025-05-15T09:01:46.466+02:00","modified":"2025-05-26T15:25:01.761+02:00","published":"2025-05-26T15:25:01.761+02:00","cssclasses":""}
---

#python/venv #python/dist-packages #python/site-packages

> [!info] Source
> 
> - <https://stackoverflow.com/a/47842938/12780516>

- by default, python will only have access to the `site-packages` directly installed inside a venv
- if we want to access the packages from the (Linux) system's `dist-packages` that were installed using the system's package manager, there are multiple possible ways
    1. set `PYTHONPATH` to include `/usr/lib/python<VERSION>/dist-packages`
       this has the drawback that now the `dist-packages` take precedence over the `site-packages` from the venv, thus if we have the same package installed in the venv but with a different (usually more recent) version than in the `dist-packages`, python will use the one from the `dist-packages`, which is usually not what we want
    2. create a `.pth` file in the venv's `site-packages` folder that points to the system's `dist-packages`
       this has the advantage, that the venv's packages will be used first and only if python cannot find a package in the venv, it will go looking into the system's `dist-packages`

    ```shell
    echo "/usr/lib/python<VERSION>/dist-packages" > .venv/lib/python<VERSION>/site-packages/dist-packages.pth
    ```

    (the `<VERSION>` has to match, of course, so for Python 3.10, for example, this would read `python3.10` in both cases)