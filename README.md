## Technical Analysis Project
A Python program which performs technical analysis on stocks.
## Setup
* Clone the repository from https://github.com/Alpha249/TechnicalAnalysis.
* Run `pip install -r requirements.txt` to install all the required dependencies.
## Usage
* Open the `main.py` file.
* Add all your stock `tickers` in the `portfolio` variable. 
* This program only work for stocks listed in India.
* Run `python main.py` in the terminal and follow all the prompts.
* Allowed arguments for periods are: `“1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”` 
* Allowed arguments for interval are: `“1m”, “2m”, “5m”, “15m”, “30m”, “60m”, “90m”, “1h”, “1d”, “5d”, “1wk”, “1mo”, “3mo”`
    * **`1m` data is only for available for last 7 days** 
    * **Data interval `<1d` for the last 60 days**
## *End*
