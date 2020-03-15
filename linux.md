# useful commands
#### getting kernel version of system
~$ uname (-a / -r / -v)(all, release, version)
#### ip information of system
~$ ifconfig
~$ ip addr show eth0 (specific iface)
#### disk space
~$ df -ah (all,human-readble)
#### managing services
~$ service s1 status
~$ systemctl status service
#### size of directory contents on disk
~$ du -sh dirname
#### open ports on system
~$ sudo netstat -tulpn  
#### cpu usage of process
~$ ps aux | grep nginx
~$ top 
~$ htop
#### managing mounts
linux has /mnt in root 
~$ mount (shows existing mounts)
~$ mount /dev/sda2 /mnt (hw addr, mount point)
~$ cat /etc/fstab (mount at boot-time)

