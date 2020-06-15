#!/bin/bash

#                           Java Installation Script
#
#
# Variables

JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
DOWNLOAD_LINK="https://www.oracle.com/webapps/redirect/signon?nexturl=https://download.oracle.com/otn/java/jdk/8u251-b08/3d5a2bb8f8d4428bbe94aed7ec7ae784/jdk-8u251-linux-x64.tar.gz"

# Functions

function fill_log {
    if [ -f "java.log" ]          # Check if file install.log exists
    then
        tee -a java.log           # Apends to log file with -a
    else
        tee java.log              # Creates a new log file
    fi
}


function show_progress {
    case $1 in
        1)
            echo
            echo "2. Installing Java"
            echo "------------------"
            ;;
        2)
            echo
            echo "3. Updating Java Environment Variables"
            echo "--------------------------------------"
            ;;
    esac
}

# Functions

function install_java {
    # Curl supports a large number of protocol calls
    # Curl option flags
    # H: pass on custom headers for cookie
    # -C -: to automatically foind out where/how to resure transfer
    # O: Save file with the same name
    # L: if requested page has moved to different location
    # R: Remote time
    #cd ~/Downloads
    #curl -C - -LR#OH "Cookie: oraclelicense=accept-securebackup-cookie" -k $DOWNLOAD_LINK
    #tar -xvzf jdk-8u251-linux-x64.tar.gz
    sudo apt-get -y install openjdk-8-jdk
}


function environment_variables {
    echo "export JAVA_HOME='"$JAVA_HOME"'" >> ~/.bashrc
    echo "export PATH=$PATH:$JAVA_HOME/bin" >> ~/.bashrc
}


#Installing
show_progress 1 | fill_log
install_java | fill_log

#Variables
show_progress 2 | fill_log
environment_variables | fill_log









