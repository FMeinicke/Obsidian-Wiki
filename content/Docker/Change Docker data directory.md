---
{"publish":true,"created":"2025-05-20T09:49:14.664+02:00","modified":"2025-05-26T15:25:03.043+02:00","published":"2025-05-26T15:25:03.043+02:00","cssclasses":""}
---


#docker/daemon #rsync

> [!info] Source
> 
> - <https://blog.adriel.co.nz/2018/01/25/change-docker-data-directory-in-debian-jessie/>

- Stop the docker daemon and ensure no docker process is running
  
  ```console
  # systemctl stop docker
  $ ps aux | grep -i docker
  ```
  
- Copy the `/var/lib/docker` tree to the new location
  
  ```console
  # rsync -aPS /var/lib/docker/ /mnt/hdd-tank/docker-data-root
  ```
  
  Be sure to `--exclude` any locally bind-mounted directories.
- Change the directory in the Docker configuration file (`/etc/docker/daemon.json`)
  ```json
  {
    ...
    "data-root": "/mnt/hdd-tank/docker-data-root",
    ...
  }
  ```
  
  Alternatively, create a symlink from `/var/lib/docker` to the new data directory. In this case no change to the configuration file is required.
  
- Restart the docker daemon and verify the new location is being used, and that all containers are running as expected
  
  ```console
  # systemctl start docker
  $ docker info | grep Docker Root Dir
  $ docker ps -a
  ```
  
- If everything is running smoothly for a few days, remove the `/var/lib/docker` tree
  
  ```console
  # rm -rf /var/lib/docker
  ```
