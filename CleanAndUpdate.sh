#!/bin/bash

#want to make sure it stops on errors so nothing has a chance to somehow get messed up

set -e

#Keeping user informed
echo "Updating and Cleaning System"

#want to upgrade, update then start cleaning cause may have orphaned programs or programs not in main repository
sudo apt full-upgrade -yy
sudo apt update
sudo apt autoremove -yy
sudo apt autoclean

#informing user of completion
echo "Finished Updating and Cleaning System"