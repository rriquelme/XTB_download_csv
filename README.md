# XTB_download_csv
This program is to download data from XTB using their API, data download is turned into a .csv file.

***This program still have some limitations on this version:***
1. Just for demo account.
2. Only download daily data.
3. Just extract one symbol at a time.

## Instructions 
1. Download de .py program.
    * You could just copy all the .py file into your .py file.
    * Or clone de repo.
    
2. Change the initial variables, (lines 1-9):
    * USERNUMBER = "12345678"   ***Your demo account userID or userNumber***
    * PASSWORD = 'password123'   ***Your password***
    * datestr = "Jul 15 21:00:00 2020" ***Date since when you want the data to be extracted***
    * SYMBOL = "US100" ***Symbol that you want to download data***

3. This will create two files:
    * **out.csv**: output data on csv.
    * **symbols.txt**: list of all symbols available to use in the program (first column).

---

This program was made using the API of XTB.

API documentation: http://developers.xstore.pro/documentation/

# TODO
- Calculate real time index
- Create GUI
- Plot data with delay to analize.
