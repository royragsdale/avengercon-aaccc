# Errata

Commands and details worth remembering.

### Enable static downloads

```
        location ~ /static {
            root   /usr/share/nginx/html;
            types        { }
            default_type application/octet-stream;
        }
```

### Host the box

For download on a local network

```
docker run --rm -it -p 80:80 -v $(pwd):/usr/share/nginx/html:ro nginx
```

### Package the box

[Reference](https://scotch.io/tutorials/how-to-create-a-vagrant-base-box-from-an-existing-one)

```
sudo dd if=/dev/zero of=/EMPTY bs=1M
sudo rm -f /EMPTY
cat /dev/null > ~/.bash_history && history -c && exit
```

```
vagrant package --output workshop.box
```
