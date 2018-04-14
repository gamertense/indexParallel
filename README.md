Implemented from "Information Retrieval" class. This program indexes all .txt files in docs folder in parallel. The two posting lists (or inverted indexes) are stored in RAM waiting for searching terms such as "brother" and "water" to do an AND operation, which gives the docID both "brother" and "water" appear.

# Requirements
- [Python 3.5.2 or 3.6.5](https://www.python.org/)
- [XAMPP](https://www.apachefriends.org/)

## Python libraries
- matplotlib
- numpy

# Usage
## Install required libraries
You can install required libraries by typing
```
sudo pip3 install matplotlib
```
> Normally, the above command also installs numpy.

## Install XAMPP on Ubuntu 16.04
1. Download [XAMPP for Linux](https://www.apachefriends.org/index.html)
2. Go to */home/ {username} /Downloads* or where you downloaded XAMPP into. Right-click > Open in Terminal and type the following commands.
```
sudo su
chmod +x xampp-linux-x64-7.2.3-0-installer.run
./xampp-linux-x64-7.2.3-0-installer.run
```
3. Finish the installation process.
4. Start Apache server using XAMPP Control Panel. In case you accidentally close the program and have no idea where to open it again, open terminal and type
`sudo /opt/lampp/lampp start
`
to start all servers or
`
sudo /opt/lampp/lampp startapache
`
to start only Apache server.
5. Copy our project to */opt/lampp/htdocs*. For example, */opt/lampp/htdocs/ourproject*.
6. Note that by default */opt/lampp/htdocs* directory can't be executed. `chmod 777 opt/lampp/htdocs` command is needed to give permission. 

## See it in action
1. Navigate your browser to *localhost/ourproject*
2. Type two terms you want to search and hit search button.
3. The output will appear below the search button along with a benchmark graph.


> Note: Work best on Ubuntu 16.04. We tried running on Windows 10 and it gave us the incorrect benchmark results (serial was faster than parallel).
