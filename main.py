from bs4 import BeautifulSoup
import urllib.request
import json
# providing url
url = "https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/"
# parsing the url html file
html = urllib.request.urlopen(url)
html_parse = BeautifulSoup(html,'html.parser')
# Create a dictionary to store the data
data_dict = {}
# Extract and store headings (h2 elements) and corresponding lists (ul elements)
headings = html_parse.find_all('h2')
for heading in headings:
    heading_text = heading.get_text()
    next_ul = heading.find_next('ul')
    if next_ul:
        list_items = [li.get_text() for li in next_ul.find_all('li')]
        data_dict[heading_text] = list_items

# Convert the dictionary to JSON
json_data = json.dumps(data_dict, indent=4)

# Print the JSON data or save it to a file
print(json_data)
print(data_dict)

with open("output.json", "w") as json_file:
    json_file.write(json_data)