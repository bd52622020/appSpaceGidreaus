#! /bin/bash
#
#					Python Installation Script
#
# Variables

DIR="$HOME/opt/Python-3.6.9"
DOWNLOADS="$HOME/Downloads"

# Functions

function fill_log {
    if [ -f "python.log" ]          # Check if file install.log exists
    then
        tee -a python.log           # Apends to log file with -a
    else
        tee python.log              # Creates a new log file
    fi
}


function show_progress {
    case $1 in
        1)
            echo
            echo "1. Check dir"
            echo "------------------"
            ;;
        2) 
            echo
            echo "2. Installing Python"
            echo "------------------"
            ;;
	3) 
            echo
            echo "3. Test python"
            echo "--------------------------------------"
            ;;

        4) 
            echo
            echo "3. Set environment variables"
            echo "--------------------------------------"
            ;;
	5) 
            echo
            echo "4. Setting default"
            echo "--------------------------------------"
            ;;
    esac
}


function check_dir {
	[ ! -d "$DIR" ] && mkdir -p "$DIR"
}


function python_install {
	wget -P $DOWNLOADS https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
	cd $DOWNLOADS
	tar zxvf Python-3.6.9.tgz
	cd Python-3.6.9
}


function python_test {
	./configure --prefix="$DIR" --with-zlib=/usr/include
	make
	#make test
	sudo make install
}


function environment_variables {
	echo 'PYTHONPATH="'$DIR'/bin/python3.6"' >> ~/.bashrc
	echo 'export PATH=$PATH:$PYTHONPATH' >> ~/.bashrc
	source ~/.bashrc
}


function python_default {
	### Set Python3.6.9 as default if python2 is installed ###
	if (($1 == 1))
	then
        	sudo update-alternatives --install /usr/bin/python python $HOME"/opt/Python-3.6.9/bin/python3.6" 1
        	sudo update-alternatives  --set python $HOME"s/opt/Python-3.6.9/python3.6"
	fi

}

# End of functions 

# Check directory
show_progress 1 | fill_log
check_dir | fill_log

#
show_progress 2 | fill_log
python_install | fill_log

#
show_progress 3 | fill_log
python_test | fill_log

#
show_progress 4 | fill_log
environment_variables | fill_log

#
show_progress 5 | fill_log
python_default | fill_log

