#!/bin/bash

num=$1

if [[ $EUID == 0 ]];

then
	read -p "What user would you like to make? " num
	for usernum in $username
		do useradd -m -s /bin/bash $usernum
	done
exit

fi

// je voert hem uit en dan zegt : do you want to make a new user? 
// als de input yes is dan vraagt ie welke user je wilt maken
// als de input nee is dan vraagt ie of je een user wilt verwijderen
// als daar de input yes dan vraagt ie welke user en zo niet dan exit
