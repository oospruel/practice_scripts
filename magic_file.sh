#!/usr/bin/bash

clock=10

touch poof
#creates poof file
echo "poof file created"
while
	[ -f poof ] && [ $clock -ge 1 ]
#while poof exist & clock greater then 1
do
	clock=$(($clock -1))
echo "poof still exist, but will be deleted in $clock"
sleep 0.5
#subtract 1 from the clock
done

rm poof ; echo "poof deleted"

