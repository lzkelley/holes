#!/bin/bash

repos=($(awk -F= '{print $1}' rep-folders.txt))
echo ${repos[*]}
cd ..
for repo in ${repos[@]}; do
	cd ${repo}
	pwd
	git reset --hard HEAD
	git clean -f -d
	cd ..
done
