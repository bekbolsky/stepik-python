import requests

base_url = "https://stepic.org/media/attachments/course67/3.6.3/"

with open("solutions/week-3/dataset_3378_3.txt") as f:
    first_url = f.readline().strip()

r = requests.get(first_url)
answer = r.text.strip()

count = 1
while not answer.startswith("We"):
    r = requests.get(f"{base_url}{answer}")
    answer = r.text.strip()
    count += 1
    print(f"Requesting next file with answer. Requested: {count}")
else:
    final_answer = answer
    print(final_answer)
