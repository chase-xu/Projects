import requests
from bs4 import BeautifulSoup
import smtplib
URL = "https://www.amazon.ca/dp/B0792P6SFD/ref=ods_gw_d_bts19_dt_xpl2_ca_en?pf_rd_p=1ce93cef-3c3b-4723-a30b-fefa525273a0&pf_rd_r=04J9CH5QMBX3QJ9EHVGT"
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}   ##dictionary
page = requests.get(URL, headers = headers) #import data from web page
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_dealprice").get_text()

print(price)