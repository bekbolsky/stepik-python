import requests

url = "https://stepic.org/media/attachments/course67/3.6.2/899.txt"

r = requests.get(url.strip())
content = r.text.splitlines()

count = 0
for line in content:
    count += 1

print(count)
# можно и так
print(len(content))
