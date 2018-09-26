echo "Welcome to the Imbach Git-Tool"
echo "Please enter a comment for this version"
read name
echo "Your comment is $name"

git add .
git commit -m "$name"
git push
