from bs4 import BeautifulSoup
import requests
import pandas as pd
from dateutil import parser

url = "https://en.wikipedia.org/wiki/List_of_North_Korean_missile_tests"
response = requests.get(url)
html = response.text
bs = BeautifulSoup(html, "html.parser")
tables = bs.find_all("table")
wiki_table = tables[1]
wiki_table_rows = wiki_table.find_all("tr")

df = pd.DataFrame(columns=['date', 'content'])

for row in wiki_table_rows:
    try:
        date = row.find_all("th")[0].text
        content = row.find_all("td")[0].text

        date = date.replace('\n', '')
        if ',' not in date:
            datetime_object = parser.parse(date)
        else:
            datetime_object = parser.parse(date)

        df.loc[len(df)] = [datetime_object, content]
    except (IndexError, ValueError) as e:
        print(e)
        pass
    pass

df.to_csv('./timeline.csv')

if __name__ == "__main__":
    pass
