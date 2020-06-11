#!/bin/bash
#
#                                    Eclipse Installation Script
#
# Variables
DIR="$HOME/opt"
DOWNLOADS="$HOME/Downloads"


# Functions
function fill_log {
    if [ -f "eclipse.log" ]          # Check if file install.log exists
    then
        tee -a eclipse.log           # Apends to log file with -a
    else
        tee eclipse.log              # Creates a new log file
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
            echo "2. Installing Eclipse"
            echo "------------------"
            ;;
        3) 
            echo
            echo "3. Updating Eclipse Environment Variables"
            echo "--------------------------------------"
            ;;
    esac
}


function check_dir {
	[ ! -d "$DIR" ] && mkdir -p "$DIR"
}


function install_eclipse {
	cd $DOWNLOADS
	wget -P $DOWNLOADS http://mirror.dkm.cz/eclipse/technology/epp/downloads/release/2020-03/R/eclipse-java-2020-03-R-linux-gtk-x86_64.tar.gz
	tar -xvzf eclipse-java-2020-03-R-linux-gtk-x86_64.tar.gz
	mv ./eclipse $DIR
}


function environment_variables {
	echo 'EC_HOME="'$DIR'/eclipse/eclipse"' >> ~/.bashrc 
	echo 'PATH=$PATH:$EC_HOME' >> ~/.bashrc 
	echo 'alias eclipse=$EC_HOME' >> ~/.bashrc 
	source ~/.bashrc 
}

# End of functions

# Checking
show_progress 1 | fill_log
check_dir | fill_log

# Installing
show_progress 2 | fill_log
install_eclipse | fill_log

# Variables
show_progress 3 | fill_log
environment_variables | fill_log


