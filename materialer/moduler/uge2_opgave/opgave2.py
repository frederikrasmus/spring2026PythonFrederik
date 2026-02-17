import subprocess
import os

#Klon repo
print('Kloner Repo...')
subprocess.run(["git", "clone", "https://github.com/python-elective-kea/spring2024.git"])

#Definér sti til index.html
html_sti = os.path.join("spring2024", "docs", "index.html")

#Åben fil i browser
print(f"Åbner {html_sti} i browser...")

# 'nt' som er windows, os.startfile svarer til at dobbeltklikke på fil
if os.name == 'nt':
    os.startfile(html_sti)
else:
    subprocess.run(["open", html_sti])
