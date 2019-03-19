'''
Using python's request library, retrieve the HTML of the website you created
that now lives online at <your-gh-username>.github.io/<your-repo-name>

https://mingyyy.github.io/personal_web/index.html

BONUS: extend your python program so that it reads your original HTML file
       and returns True if the HTML from the response is the same as the
       the contents of the original HTML file.
<<<<<<< HEAD
'''
import requests

url = "https://mingyyy.github.io/personal_web/index.html"
r = requests.get(url)
print(r.text)
print(r.status_code == 200)

# bonus: extract all the spaces from both files, check if the clean versions are the same.
