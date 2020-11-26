# Autoayuda
Autoayuda module for Conecta

# Requirements
In order for the module to run properly the following depdendencies are required
- Python 3.6 (on a virtual environment)
- Python pip 20.1.1
- zoom.us account, api key and secret
- google account

# Installation steps
1 - Verify that the OS version is ubuntu 16 or higher. 

2 - Create a directory in which the app will be installed (i.e.: /var/www/)

3 - Install git:

    ~: sudo add-apt-repository ppa:git-core/ppa

    ~: sudo apt update

    ~: sudo apt-get install git

4 - Clone autoayuda repository:

    ~: git clone https://github.com/ocideos/autoayuda.git

5 - Inside the prevoius folder, install a Python 3.6 or greater virtual environment:

    ~: [python | python3 | python3.6 | python3.x] -m venv venv

5 - Inside the prevoius folder, activate the virtual environment:

    ~: source ./venv/bin/activate

6 - Inside the previous folder upgrade pip and install all PiP applications:

    ~: pip install --upgrade pip
    ~: pip install git+https://github.com/ocideos/zoomus.git
    ~: pip install git+https://github.com/ocideos/google-calendar-simple-api.git

# Credits
- zoomus for their great videocall platform
- prschmid for his excellent zoomus python client
- google for a great videocall platform
- kuzmoyev for his great google calendar api python client
