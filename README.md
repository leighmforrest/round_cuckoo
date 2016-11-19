# Round Cuckoo

a Swiss-style Tournament Database

by [Leigh Michael Forrest](http://leighmforrest.github.io)

[https://github.com/leighmforrest/round_cuckoo](https://github.com/leighmforrest/round_cuckoo)

---

## Installation

### Install VirtualBox
Download the appropriate installation at `https://www.virtualbox.org/wiki/Downloads` and install it per vendor instructions.

### Install Vagrant
Download Vagrant at `https://www.vagrantup.com/downloads.html` After install, run this command in the terminal: `vagrant -v` and make sure a version number is displayed.

### Clone git Repository

Clone the code repository with the following command on the terminal:
`git clone https://github.com/leighmforrest/round_cuckoo.git round_cuckoo`

### Run the Virtual Machine

Be sure you `cd` into the root directory of the code, and be sure you have a file called `Vagrantfile` in your repository.

Run these commands in the terminal:

`vagrant up`

`vagrant ssh`

__Note: in OSX, there may be issues with curl embedded in Vagrant. If this is so, run this line: `sudo rm -rf /opt/vagrant/embedded/bin/curl`__

### Run the Database

To run the database, run these lines in the terminal (prompts are in bold):
__$__ `psql`

__vagrant=>__ `\i tournament.sql`

__vagrant=>__ `\q`

### Unit Test the API

To run the unit tests, run this command in the terminal: `python tournament_test.py` The code should be all clear.

### Use the API

You can now use the functions in __test.py__ To use it in a shell jam session, be sure to enter `import tournament` before you are ready to use the functions.

### Quit the VM

To quit the Virtual Machine, __control-D__ and when the main prompt is displayed, enter this code in the terminal: `vagrant halt`
