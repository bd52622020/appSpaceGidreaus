#! /bin/bash

                                            ###Install dependencies ###

# Functions

function fill_log {
    if [ -f "dependencies.log" ]          # Check if file install.log exists
    then
        tee -a dependencies.log           # Apends to log file with -a
    else
        tee dependencies.log              # Creates a new log file
    fi
}


function show_progress {
    case $1 in
        1)
            echo
            echo "1. Updating System"
            echo "------------------"
            ;;
        2) 
            echo
            echo "2. Installing curl"
            echo "------------------"
            ;;
        3) 
            echo
            echo "3. Installing tar"
            echo "------------------"
            ;;
    esac
}


function update_system {
	sudo apt-get update
	sudo apt-get install zlib1g-dev
	sudo apt --yes upgrade          # Specifying yes to upgrade to avoid interuptions
}


function install_curl {
	sudo apt --yes install curl # Using curl to download Java package
}


function install_tar {
	sudo apt --yes install tar
}

# End of functions

# Updating
show_progress 1 | fill_log
update_system | fill_log

# Installing curl
show_progress 2 | fill_log
install_curl | fill_log

# Installing tar
show_progress 3 | fill_log
install_tar | fill_log



