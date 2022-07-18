import pandas as pd
import re

def getStockCode(str):
    if len(str) < 5 : return ""
    str5 = str[0:5]
    if re.fullmatch(str5, "\d\d\d\d\d") : return ""
    return str5

def getQuantity(str):
    if str == "" : return "0"
    #if str.isnumeric() == False : return "0"
    if int(str) < 0 : return "0"
    return str

def getUnitPrice(str):
    if str == "" : return "0"
    #if str.isnumeric() == False : return "0"
    if float(str) < 0 : return "0"
    return str

def getCustomerID(str):
    if str == "" : return "99999"
    return str

input_file_name = "data_cus_test.csv"
#input_file_name = "data_cus.csv"
output_file_name = "gen.csv"

# open file stream
csv_input = pd.read_csv(filepath_or_buffer = input_file_name, encoding="utf-8", header = 0, sep = ",")
csv_output = open(output_file_name, "w")

# get indeies
df = pd.DataFrame(csv_input)
idx_invoice_no = df.columns.get_loc("InvoiceNo")
idx_stock_code = df.columns.get_loc("StockCode")
idx_description = df.columns.get_loc("Description")
idx_quantity = df.columns.get_loc("Quantity")
idx_invoice_date = df.columns.get_loc("InvoiceDate")
idx_unit_price = df.columns.get_loc("UnitPrice")
idx_customer_id = df.columns.get_loc("CustomerID")
idx_country = df.columns.get_loc("Country")

#df = pd.DataFrame(csv_input)

header = ",".join(df.columns)# + "Stack"
csv_output.write(header)
csv_output.write("\n")

for line in df.values:
    val_invoice_no = line[idx_invoice_no]
    val_stock_code = line[idx_stock_code]
    val_description = line[idx_description]
    val_quantity = line[idx_quantity]
    val_invoice_date = line[idx_invoice_date]
    val_unit_price = line[idx_unit_price]
    val_customer_id = line[idx_customer_id]
    val_country = line[idx_country]

    # update values
    val_stock_code = getStockCode(val_stock_code)
    val_quantity = getQuantity(val_quantity)
    val_unit_price = getUnitPrice(val_unit_price)
    val_customer_id = getUnitPrice(val_customer_id)

    # generate a new line
    csv_output.write(str(val_invoice_no) + ",")
    csv_output.write(str(val_stock_code) + ",")
    csv_output.write(str(val_description) + ",")
    csv_output.write(str(val_quantity) + ",")
    csv_output.write(str(val_invoice_date) + ",")
    csv_output.write(str(val_unit_price) + ",")
    csv_output.write(str(val_customer_id) + ",")
    csv_output.write(str(val_country) + "\n")

csv_output.close()
