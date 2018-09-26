#!/bin/bash
#set /p ccomment="Enter Comment: "
#echo "git"
#echo %ccomment%
echo "Please enter a comment"
read name
echo "Your comment is $name"

git add .
git commit -m "$name"
git push
