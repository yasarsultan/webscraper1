from bs4 import BeautifulSoup
import pandas as pd
import requests
import html5lib


def main():
    # gethering data and storing html in text format
    url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
    html_data = requests.get(url).text

    # Parsing using beautifulsoup
    soup = BeautifulSoup(html_data, "html.parser")

    # making a dataframe
    data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

    # transforming and loading data into dataframe 
    for row in soup.find_all("tbody")[0].find_all("tr"):
        columns = row.find_all("td")
        if columns:
            name = columns[1].text
            clean = columns[2].text.replace(columns[2].text[1], columns[2].text[0])
            market_cap = clean[1:-1]
            data = data._append({"Name": name, "Market Cap (US$ Billion)":market_cap}, ignore_index = True)
        

    file = "bank_market_assets.csv"
    data.to_csv(file)

main()


