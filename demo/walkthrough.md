
sudo shell_manager status
sudo shell_manager package /vagrant/examples/read-and-print
sudo dpkg -i aci-read-and-print-p1-0-0.deb

sudo shell_manager status
sudo shell_manager deploy read-and-print
