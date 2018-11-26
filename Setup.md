# Setup

## Get the code

```
git clone https://github.com/royragsdale/avengercon-taoccc.git
```


## Pre-requisites 

1. Install [vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)

## Get the box
  - Plug into switch
    - Statically configure ethernet interface (`10.0.0.[10-200]`)
  - Download box: <http://10.0.0.1/workshop.v3.box>
  - `vagrant box add royragsdale/avengercon-taoccc workshop.v3.box`

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
