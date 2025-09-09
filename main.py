import pandas as pd
from pyweb import pydom
from pyodide.http import open_url
from pyscript import display
from js import console

title = "Pandas (and basic DOM manipulation)"
page_message = "This loads a remote CSV file into a Pandas dataframe and displays it below."
url = "chicago_crime_data.csv"

pydom["div#page-message"].html = page_message
pydom["input#txt-url"][0].value = url

def log(message):
    print(message)
    console.log(message)

def loadFromURL(event):
    pydom["div#pandas-output-inner"].html = ""
    url = pydom["input#txt-url"][0].value
    log(f"Trying to fetch CSV from {url}")
    df = pd.read_csv(open_url(url))
    pydom["div#pandas-output"].style["display"] = "block"
    pydom["div#pandas-dev-console"].style["display"] = "block"
    display(df, target="pandas-output-inner", append="False")