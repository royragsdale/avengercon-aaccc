# Setup

## Pre-requisites 

1. Install [vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Optional for offline
  - download `workshop.box`
  - `vagrant box add royragsdale/avengercon-taoccc workshop.box`

## Get the code

```
git clone https://github.com/royragsdale/avengercon-taoccc.git
```

## Start demo box

```
vagrant up
```

<http://192.168.9.9> and `vagrant ssh`

## Services

- picoCTF @ <http://192.168.9.9>
- CTFd @ <http://192.168.9.9:8000>
- user: `ctfadmin`
- pass: `ctfadmin`
