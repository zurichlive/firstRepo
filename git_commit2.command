echo "************************************"
echo "** Welcome to the Imbach Git-Tool **"
echo "Please enter a comment for this version (submit by pressing enter)"
read name
echo "Your comment is: $name"

git add .
git commit -m "$name"
git push
echo "** Thank you for using our tool   **"
echo "************************************"
