import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://nasa.github.io/nasa-latex-docs/html/examples/table.html"
response = requests.get(url)
# print(response.content)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all LaTeX table elements
latex_elements = soup.find_all(["pre"])
# latex_tables = soup.find_all('table', {'class': 'latex'})
if latex_elements:
    latex_code = [elem.get_text() for elem in latex_elements]
    latex_code = [elem.replace("<span class='k'>","").replace("<span class='na'>","").replace("<span class='nb'>","").replace("</span>","").replace("<pre>","").replace("</pre>","") for elem in latex_code]
else:
    print("No latex code found on the website")

count = 0
for table in latex_code:
    table = str(table)
    print(table)
    if table.startswith("\\begin{table}"):
        # Open the file in write mode

        with open(f"./latex_code/code" + str(count) + ".txt", "w") as file:
            # Write the text to the file
            count += 1
            file.write(table)
    # break

        # print("The string starts with \\begin{table}")
# Find all images related to latex table
# images = soup.find_all('img', {'class': 'latex'})
# print(images)
# for image in images:
    # image_url = image['src']
    # print(image_url)

