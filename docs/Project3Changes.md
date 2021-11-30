# Project 3 Changes
See [project 2 documentation](#project-2-documentation) for previous command-line functionalities.

### Web App
The project was previously a command-line tool which made it less convenient to use and less accessible to the average user who may not have experience with command-line operations. To improve this, we have created a web app that wraps around the original tool and provided a better User Interface. The frontend UI includes a search bar, inputs for the number of results, currency, and sort by options, and a table to show the list of results. In the table, users can directly click on the item name to go to the product web page and add the item to their wishlist.

### REST API
Along with the web app, we have created REST API endpoints so that the tool can be more extendable and accessible. Future contributors can create their own interface such as a browser extension to interact with the tool. See the [REST API Descriptions](https://github.com/SE21-Team2/slash/blob/main/docs/restapi_descriptions.md) document for more details.

### Enhanced Profile Creation and Wishlist
Version 2 of Slash included the `Full Version` that allowed users to log in with their email address and create a wishlist. In project 3, we created a more sophisticated log in and authentication system with username and password and required users to register for a profile before logging in. The frontend UI also made it easier for users to view, add, remove items from their wishlist. This is implemented with connection to the database as described later in this document. 

### Sorting Logic Updates
Previously, it is possible for users to specify the number of items to return. The tool would return that number of items for _each_ website and we thought that this would be confusing to the user. Instead, we decided to just return the specified number (_num_) of items in the overall search. For the default search, it would attempt to return a fraction of _num_ for each website for a total of the given number. For the sorted searches, it would retrieve the specified number of items for each website and then sort the values. It would then only return the top _num_ values of the sorted list.

### Scrape Item Image
With the web app and user interface, the tool can now show an image of the item. This can better allow users to compare the items across sites and determine if they want the item. 

### Cloud Deployment
The app can now be run through a Heroku dyno, allowing for better bot up-time and consistency and removing the inconvenience of forcing someone to run the bot locally on their own computer.

### Database
Previously, all persistent data was stored in local files and each action would overwrite the entirety of data files. However, this approach suffers at scale, where datasets are large and operations are done frequently and concurrently. We transitioned persistent storage to use a PostgreSQL instance hosted through the Heroku cloud platform, to solve these issues. This also improves on the profile creation functionality so users can login to the wep app and view their saved wishlists.


# Project 2 Documentation (CLI features replaced by Web API in Project 3)

:golf: Flags and Command Line Arguments 
---
Currently the tool supports the following flags and command line arguments. These flags and arguments can be used to quickly filter and guide the search to get you the best results very quickly.

| Arguments | Type | Default | Description                                                                                  |
|-----------|------|---------|----------------------------------------------------------------------------------------------|
| --search  | str  | None    | The product name to be used as the search query                                              |
| --num     | int  | 3       | Maximum number of products to search                                                         |
| --sort    | str  | re      | Sort results by relevance (re) or by price (pr)                                              |
| --des     | bool | -       | Set boolean flag if results should be sorted in non-increasing order                         |
| --csv     |      | -       | Save results as CSV                                                                          |
| --full    | str  | F       | T for full version of app; F for mini version of app                                         |
| --link    |      |         | Show links in the table                                                                      |
|--currency | str  |         | Display the amount in specified currency(inr, euro, aud, yuan, yen, pound)                   |
 
:card_index_dividers: Some Examples
---

#### 1. Searching
```--search```  accepts one argument string which it uses to search and scrape the requested products on 
the e-commerce websites. So, to use this, run the python script followed by the --search argument and the 
search string. The search string should be in double quotes if it have two or more words. Example:
```
For Mac
python3 slash.py --search "socks"

For Windows
python slash.py --search "socks"
```
```
             timestamp                                    title   price                                     link  website rating
0  04/11/2021 13:09:36  CelerSport Ankle Athletic Running So...  $12.70  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
1  04/11/2021 13:09:36  CelerSport 6 Pack Men's Ankle Socks ...  $15.95  www.amazon.com/gp/slredirect/picasso...   amazon    4.7
2  04/11/2021 13:09:36  Men's Athletic Ankle Socks 8 Pairs T...  $22.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
3  04/11/2021 13:09:39  Hanes Women's Cool Comfort Ankle Soc...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
4  04/11/2021 13:09:39  Hanes Women's Cool Comfort Crew Sock...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
5  04/11/2021 13:09:39  AND1 Men's Cushion No Show Socks, 12...  $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart    4.6
6  04/11/2021 13:09:40  Follkee Women's Alpaca Wool Socks Pe...  $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
7  04/11/2021 13:09:40  Alpaca Socks | GoWith 2 Pairs Cozy W...  $19.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
8  04/11/2021 13:09:40                  Great White Shark Socks  $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
```

#### 2. Sorting
```--sort``` accepts one or more arguments that determine how the tool sorts and filters the requested products
after scraping. The first value is used to initially sort and filter the results of the scraping. The arguments
following the first one are not required but will be used to further sort the filtered results. Example:
```
For Mac
python3 slash.py --search "socks" --sort ra

For Windows
python slash.py --search "socks" --sort ra
```
```
           timestamp                                       title    price   website      rating 
 0  03/11/2021 21:42:53  Hanes Women's Cool Comfort Ankle Socks, ...  $10.97   walmart         4.2 
 1  03/11/2021 21:42:53  Hanes Women's Cool Comfort Crew Socks, 1...  $10.97   walmart         4.2 
 2  03/11/2021 21:42:53  Hanes Mens FreshIQ Ankle Cushion Socks, ...  $13.46   walmart         4.2 
 3  03/11/2021 21:42:51  10 Pairs Ankle Socks No Show Sock Low-Cu...  $11.95   amazon          4.3 
 4  03/11/2021 21:42:50  Mens Cushioned Work Socks 10 Pairs           $12.10   amazon          4.5 
 5  03/11/2021 21:42:50  Women's 6-Pack Performance Cotton Cushio...  $17.70   amazon          4.5 
 6  03/11/2021 21:42:54  PDF Crikey Crocodile Socks Knit Animal S...  7.50     Etsy            4.5 
 7  03/11/2021 21:42:54  5socks /set -  Cotton Women's Socks          16.00    Etsy            5   
 8  03/11/2021 21:42:54  Follkee Women's Alpaca Wool Socks Perfec...  18.49    Etsy            5   

```
#### 3. Sort Order
The ```--des``` flag can be set to sort the requested products in a non-increasing order. This flag will be 
actually used when coupled with ```--sort```. Example:
```
For Mac
python3 slash.py --search "socks" --sort pr --des

For Windows
python slash.py --search "socks" --sort pr --des
```
```
           timestamp                                   title        price    website  rating   

 0  04/11/2021 13:18:30                                                        Etsy                
 1  04/11/2021 13:18:30                                                        Etsy                
 2  04/11/2021 13:18:30                                                        Etsy                
 3  04/11/2021 13:18:27  6-pk. Performance Cotton Crew Socks Size...  $34.38   amazon     4.7      
 4  04/11/2021 13:18:27  Men's 10 Pairs Cotton Moisture Control H...  $25.49   amazon     4.7      
 5  04/11/2021 13:18:27  Men's Dri-Tech Comfort Crew Sock             $25.45   amazon     4.8      
 6  04/11/2021 13:18:29  AND1 Men's Cushion No Show Socks, 12 Pac...  $11.47   walmart    4.6      
 7  04/11/2021 13:18:29  Hanes Women's Cool Comfort Ankle Socks, ...  $10.97   walmart    4.2      
 8  04/11/2021 13:18:29  Hanes Women's Cool Comfort Crew Socks, 1...  $10.97   walmart    4.2      
```

#### 4. Result length
The maximum number of results that are scraped from each website can be set using the ```--num``` argument. It accepts
an integer value ```n``` and then returns ```n``` results from each website. Note that tool returns a maximum of 
the value of ```n``` and the number of results on the webiste. By default this value is set to 3. Example:
```
For Mac
python3 slash.py --search "socks" --num 5

For Windows
python slash.py --search "socks" --num 5
```
```
              timestamp                                    title   price                                     link  website rating
0   04/11/2021 13:13:33  CelerSport 6 Pack Men's Ankle Socks ...  $15.95  www.amazon.com/gp/slredirect/picasso...   amazon    4.7
1   04/11/2021 13:13:33  CelerSport Ankle Athletic Running So...  $12.70  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
2   04/11/2021 13:13:33  Men's Athletic Ankle Socks 8 Pairs T...  $22.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
3   04/11/2021 13:13:33  CelerSport 6 Pack Men's Athletic Cre...  $18.95  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
4   04/11/2021 13:13:33    Women's 10-Pair Value Pack Crew Socks   $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...   amazon    4.7
5   04/11/2021 13:13:36  Hanes Women's Cool Comfort Ankle Soc...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
6   04/11/2021 13:13:36  Hanes Women's Cool Comfort Crew Sock...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
7   04/11/2021 13:13:36  AND1 Men's Cushion No Show Socks, 12...  $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart    4.6
8   04/11/2021 13:13:36  Gildan Adult Men's Performance Cotto...  $10.00  www.walmart.comhttps://wrd.walmart.c...  walmart    4.3
9   04/11/2021 13:13:36  Hanes Women's Cool Comfort No Show S...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.4
10  04/11/2021 13:13:37  Follkee Women's Alpaca Wool Socks Pe...  $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
11  04/11/2021 13:13:37  Alpaca Socks | GoWith 2 Pairs Cozy W...  $19.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
12  04/11/2021 13:13:37                  Great White Shark Socks  $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
13  04/11/2021 13:13:37  Miss June’s| 1 Pair Cashmere Wool bl...  $15.00  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
14  04/11/2021 13:13:37  Customized Dog Socks - Put Your Cute...   $8.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
```

#### 5.Currency
```--currency``` provides basic currency conversion for different currencies like INR, EURO, AUD, YUAN, YEN and POUND.

Example:
```
For Mac
python3 slash.py --search "socks" --currency "inr"

For Windows
python slash.py --search "socks" --currency "inr"

```

![image](https://user-images.githubusercontent.com/48826459/140242430-0d7d2707-095a-4a2d-86a7-c5e91b88d725.png)



#### 6. Main Menu 
```--full``` command is used to display the complete menu for the project. If the argument passed is "T", the Full version of the app will be displayed. If the argument passed is "F", the mini version of the app is displayed.

Example:

##### 1) When argument "F" is passed : 
```
For Mac
python3 slash.py --search "socks" --full "F"

For Windows
python slash.py --search "socks" --full "F"

```
```
             timestamp                                    title   price                                     link  website rating
0  04/11/2021 16:10:02  Men's 6 Pack Everyday Kit Cushioned ...  $12.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
1  04/11/2021 16:10:02  Compression Athletic Crew Socks (6 P...  $19.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.4
2  04/11/2021 16:10:02  CelerSport 6 Pack Women's Ankle Runn...  $15.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
3  04/11/2021 16:10:05  Hanes Women's Cool Comfort Ankle Soc...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
4  04/11/2021 16:10:05  Hanes Women's Cool Comfort Crew Sock...  $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
5  04/11/2021 16:10:05  AND1 Men's Cushion No Show Socks, 12...  $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart    4.6
6  04/11/2021 16:10:06  Follkee Women's Alpaca Wool Socks Pe...  $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
7  04/11/2021 16:10:06  Alpaca Socks | GoWith 2 Pairs Cozy W...  $19.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
8  04/11/2021 16:10:06                  Great White Shark Socks  $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
```

##### 2) When argument "T" is passed :
```
For Mac
python3 slash.py --search "socks" --full "T"

For Windows
python slash.py --search "socks" --full "T"

```

###### 2.a) The output window asks for user information in order to store the data in the database. It also displays the menu for the user. The user can select the product which             he/she wishes to search, check the existing list and see the currency conversion.

```
C:\Anant\NCSU\GITHUB\slash\src>python slash.py --full T
Welcome to Slash!
Please enter the following information:
Name: Anant
Email: agadodi@ncsu.edu
Welcome  Anant
Select from following:
1. Search new product
2. See exiting list
3. See Currency Conversion
4. Exit
```
##### 2.b) If the user inputs 1 i.e. Search new product, the command ```--search``` will be used. The product which the user wishes to search for needs to be entered. 


```
1
Enter name of product to Search: socks
```
```
               timestamp                                    title       price                                     link  website rating
0    04/11/2021 12:24:24  CelerSport Ankle Athletic Running So...      $12.70  www.amazon.com/gp/slredirect/picasso...   amazon    4.8
1    04/11/2021 12:24:24  CelerSport 6 Pack Men's Ankle Socks ...      $15.95  www.amazon.com/gp/slredirect/picasso...   amazon    4.7
2    04/11/2021 12:24:24  Men's 6 Pack Everyday Kit Cushioned ...      $12.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.6
3    04/11/2021 12:24:24  Compression Athletic Crew Socks (6 P...      $19.99  www.amazon.com/gp/slredirect/picasso...   amazon    4.4
4    04/11/2021 12:24:24    Women's 10-Pair Value Pack Crew Socks       $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...   amazon    4.7
5    04/11/2021 12:24:24  Men's Dri-tech Moisture Control Crew...      $14.99  www.amazon.com/Dickies-Multi-Pack-Dr...   amazon    4.7
6    04/11/2021 12:24:24  Women's Performance Heel Tab Athleti...      $14.99  www.amazon.com/Saucony-Womens-Perfor...   amazon    4.8
7    04/11/2021 12:24:24       Mens Cushioned Work Socks 10 Pairs      $12.10  www.amazon.com/Fruit-Loom-Everyday-S...   amazon    4.5
8    04/11/2021 12:24:24  CelerSport Ankle Athletic Running So...      $12.70  www.amazon.com/CelerSport-Ankle-Athl...   amazon    4.8
9    04/11/2021 12:24:24  mens Dual Defense Cushioned Socks - ...      $11.97  www.amazon.com/Fruit-Loom-Cushion-De...   amazon    4.7
10   04/11/2021 12:24:24  mens Athletic Cushioned Crew Socks (...      $18.99  www.amazon.com/adidas-Mens-Athletic-...   amazon    4.7
11   04/11/2021 12:24:25  Hanes Women's Cool Comfort Ankle Soc...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
12   04/11/2021 12:24:25  Hanes Women's Cool Comfort Crew Sock...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.2
13   04/11/2021 12:24:25  AND1 Men's Cushion No Show Socks, 12...      $11.47  www.walmart.comhttps://wrd.walmart.c...  walmart    4.6
14   04/11/2021 12:24:25  Gildan Adult Men's Performance Cotto...      $10.00  www.walmart.comhttps://wrd.walmart.c...  walmart    4.3
15   04/11/2021 12:24:25  Hanes Women's Cool Comfort No Show S...      $10.97  www.walmart.com/ip/Hanes-Women-s-Coo...  walmart    4.4
16   04/11/2021 12:24:25  Avia Women's Performance Flatknit Lo...       $9.97  www.walmart.com/ip/Avia-Women-s-Perf...  walmart      5
17   04/11/2021 12:24:25  Athletic Works Men's Ankle Socks 12 ...       $9.97  www.walmart.com/ip/Athletic-Works-Me...  walmart    4.4
18   04/11/2021 12:24:25  Athletic Works Men's Crew Socks 12 Pack       $9.97  www.walmart.com/ip/Athletic-Works-Me...  walmart    4.5
19   04/11/2021 12:24:25  Hanes Women's Cool Comfort Sport Ank...  From $8.97  www.walmart.com/ip/Hanes-Women-s-Com...  walmart    4.5
20   04/11/2021 12:24:25  Hanes Women's Cool Comfort No Show S...  From $5.99  www.walmart.com/ip/Hanes-Women-s-Com...  walmart    4.5
21   04/11/2021 12:24:26  Follkee Women's Alpaca Wool Socks Pe...      $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
22   04/11/2021 12:24:26  Alpaca Socks | GoWith 2 Pairs Cozy W...      $19.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
23   04/11/2021 12:24:26                  Great White Shark Socks      $11.95  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
24   04/11/2021 12:24:26  Miss June’s| 1 Pair Cashmere Wool bl...      $15.00  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
25   04/11/2021 12:24:26  Custom Face Socks w Text, Personaliz...       $7.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
26   04/11/2021 12:24:26  Customized Dog Socks - Put Your Cute...       $8.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
27   04/11/2021 12:24:26  Follkee Women's Alpaca Wool Socks Pe...      $18.49  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
28   04/11/2021 12:24:26  Custom Pet Socks - Dog Socks For Men...       $9.88  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
29   04/11/2021 12:24:26  PDF Knitting Pattern Crikey Crocodil...       $7.50  www.Etsy.comhttps://www.etsy.com/lis...     Etsy    4.5
30   04/11/2021 12:24:26  5 PAIRS of Cashmere Wool Blend Socks...      $34.36  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
31   04/11/2021 12:24:26  Custom Pet Socks, Dog Socks, Pup Soc...       $7.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
32   04/11/2021 12:24:26  Warm & Cozy Cupcake Socks, Sleeping,...       $4.99  www.Etsy.comhttps://www.etsy.com/lis...     Etsy      5
```


Once the product list is displayed, the user is given the option to choose whether to save in the product or if he or she wished to open the browser and check the link.


```
Enter 1 to save product to list
2 to open link in browser
else enter any other key to continue
1
Enter row number of product to save: 4
```

Here, as the user entered 1, the product is saved in the list.

```
             timestamp                                  title  price                                     link website rating
4  04/11/2021 12:24:24  Women's 10-Pair Value Pack Crew Socks  $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...  amazon    4.7
```
```
Select from following:
1. Search new product
2. See exiting list
3. See Currency Conversion
4. Exit
2
```
##### 2.c) Now that we know that there is an element in the list, we can select the "See existing List" option. 
```   
   timestamp                                  title  price                                     link website  rating
0  04/11/2021 12:24:24  Women's 10-Pair Value Pack Crew Socks  $8.79  www.amazon.com/Hanes-Womens-Crew-Whi...  amazon     4.7
```

With the list output, the user is also giventhe option to choose whether to delete the item from the list or to open the link for the product.

```
Select from the following:
1. Delete item from list
2. Open link in Chrome
3. Continue
2

Enter row number to open in chrome: 0

![image](https://user-images.githubusercontent.com/48826459/140417153-365d93d4-df64-4658-a016-eadcabeebf89.png)
```
```
Select from following:
1. Search new product
2. See exiting list
3. See Currency Conversion
4. Exit
4
Thank You for Using Slash
```

#### 7. Save products in csv
```--csv``` command is used to save the complete list of the searched product in a csv format.
```--cd``` command here is used to change the directory for the csv file.
Example:
```
For Mac
python3 slash.py --search "socks" --csv --cd C:\Anant\NCSU\slash_test_csv

For Windows
python slash.py --search "socks" --csv --cd C:\Anant\NCSU\slash_test_csv

```
```
CSV Saved at:  C:\Anant\NCSU\slash_test_csv
File Name: C:\Anant\NCSU\slash_test_csv\socks211104_1223.csv
```

![image](https://user-images.githubusercontent.com/48826459/140409684-a352f30a-9b01-4369-a044-f166eab42630.png)
