#!/bin/bash

if test "$USER" != 'root' ; then
	echo you are not loggeg in as root, you are $USER
fi

if [ $(id -u) -gt 9 ]; then
	echo "the number $(id -u) is greater than 9!"
fi

if grep "^${USER}:" /etc/passwd &> /dev/null ; then
	echo "${USER} is a local user on the system."
else
	echo "${USER} is not a local user."
fi

read -p 'Enter your first and last name:' FIRST LAST
echo $FIRST $LAST
