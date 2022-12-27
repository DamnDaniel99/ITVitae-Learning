#!/bin/bash

read -p $"How would you like to be greeted? "$'\n' GREETED
echo ${GREETED}, ${1}
