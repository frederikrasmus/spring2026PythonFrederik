import os
import requests
import webbrowser

def download_site():
    # setup
    base_url = "https://itakea.github.io/e24_swa/"
    page_file = "py_intro_3.html"
    folder_name = "downloaded_site"

    # opret mappe
    os.makedirs(folder_name, exist_ok=True)

    # hent HTML
    print(f"Henter {page_file}...")
    response = requests.get(base_url + page_file)
    html_content = response.text

    # Vi henter alt som kommer efter href ved hjælp af split
    split_html = html_content.split('href="')

    # Find custom.css
    css_relative_path = ""
    for part in split_html:
        if "custom.css" in part:
            css_relative_path = part.split('"')[0]
            break

    if css_relative_path:
        print(f"Fandt css sti: {css_relative_path}")

        # Hent css filen
        css_url = base_url + css_relative_path
        css_response = requests.get(css_url)

        local_css_name = "style.css"
        with open(os.path.join(folder_name, local_css_name), 'w', encoding='utf-8') as f:
            f.write(css_response.text)

        # RETTELSE: Denne linje skal ud af 'with open' blokken for at gemme HTML rigtigt
        html_content = html_content.replace(css_relative_path, local_css_name)
        print("CSS downloadet og HTML opdateret")

    else:
        print("Kunne ikke finde CSS filen i html")

    # Gem HTML filen
    local_html_path = os.path.join(folder_name, "index.html")
    with open(local_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Åben i browser
    full_path = os.path.abspath(local_html_path)
    print(f"åbner {full_path}...")
    webbrowser.open('file://' + full_path)

if __name__ == "__main__":
    download_site()