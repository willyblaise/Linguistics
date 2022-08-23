#!/bin/env bash


if [[ $# < 2 ]]
then
	echo 'Usage: enter start date and end date in format YYYYMMDD'
	exit 10
fi

end_date=$1
start_date=$2

#let DIFF=($(date +%s -d 20221207)- $(date +%s -d 20220817))/86400
let DIFF=($(date +%s -d $end_date)- $(date +%s -d $start_date))/86400

echo $DIFF days until 12-07-2022
