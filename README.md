##Goal:

The associated repository is used to scrape data from coinmarketcap.com, parses it, and runs a SKLearn linear regression on variables to test the relationship between volitility and volume.

##Usage

1. Run the program named HW1_Request. It will insert HTML files into the html_files folder.

2. Run the HW1_Parsing program; after a few minutes, it will combine the data from the HTML folders into the parsed_files folder
into a csv file named coinmarketcap_dataset_0422_cleaned.

3. In the parsed_files folder, open HW1_Machine_Learning_Linear. Run this python program to test the data. Test size is automatically
set to .25 and random state is automatically set to 0. The program will output the predictions, then the r2 score, and then a
scatterplot in the parsed_files folder. The scatterplot will appear as a PNG file labled prediction and target test on their respective
axis.

