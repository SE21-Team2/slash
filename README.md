Demo Video (To be uploaded)

<p align="center"><img width="500" src="./assets/slash.png"></p>

![Python](https://img.shields.io/badge/python-v3.8+-yellow.svg)
![GitHub](https://img.shields.io/github/license/SE21-Team2/slash)
![Github](https://img.shields.io/badge/language-python-red.svg)
![GitHub issues](https://img.shields.io/github/issues-raw/SE21-Team2/slash)
![Github closes issues](https://img.shields.io/github/issues-closed-raw/SE21-Team2/slash)
![Github pull requests](https://img.shields.io/github/issues-pr/SE21-Team2/slash)
![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/SE21-Team2/slash)
[![codecov](https://codecov.io/gh/SE21-Team2/slash/branch/main/graph/badge.svg?token=K0UIYGW138)](https://codecov.io/gh/SE21-Team2/slash)
![Lines of code](https://img.shields.io/tokei/lines/github/SE21-Team2/slash)
![Build Status](https://github.com/SE21-Team2/slash/actions/workflows/python-app.yml/badge.svg)
[![DOI](https://zenodo.org/badge/423285546.svg)](https://zenodo.org/badge/latestdoi/423285546)


Slash is a web application that scrapes the most popular e-commerce websites to get the best deals on the searched items across these websites. 
- **Fast**: With slash, you can save over 50% of your time by comparing deals across websites within seconds
- **Easy**: Slash uses very easy commands to filter, sort and search your items
- **Powerful**: Quickly alter the commands to get desired results

<p align="center">
  <a href="#rocket-getting-started">Getting Started</a>
  ::
  <a href="#card_index_dividers-features">Features</a>
  ::
  <a href="#muscle-whats-new-in-phase-3"> Phase 3 </a>
  ::
  <a href="#earth_americas-whats-next"> Future </a>
  ::
  <a href="#thought_balloon-use-case">Use Case</a>
  ::
  <a href="#page_facing_up-why">Why</a>
  ::
  <a href="#sparkles-contributors">Contributors</a>
  
</p>

---

<img width="959" alt="image" src="https://user-images.githubusercontent.com/32313919/143926845-55c4d285-7528-411a-a531-f8adfda9d2cd.png">

---

:rocket: Getting Started
---
To get started with Slash, follow the instructions in the [Getting Started Guide](https://github.com/SE21-Team2/slash/blob/main/docs/getting_started.md)

:card_index_dividers: Features
---

#### 1. Searching
The main functionality of Slash is to search for products on various sites (currently supports Amazon, Walmart, Etsy). Users can go to the website to see the an item by clicking on the name of the item.
1. Start the application
2. Type the product you would like to search for in the search box
3. Click the search button
![search](https://user-images.githubusercontent.com/32313919/143975603-50c03348-a4d9-49ec-89a0-dada25cb44ba.png)

#### 2. Register Profile and Log In
Users can also register for and log in to a profile to create a wishlist of items.  
**To Register:**  
1. Start the application
2. Click `Log In` in the top right corner
3. Under the `Log In` button, click `Sign Up`
4. Enter a username and password
5. Click `Sign Up`
![signup](https://user-images.githubusercontent.com/32313919/143943237-bf1f067f-de18-4014-94d2-26eb196cf1ce.png)

**To Log In:**  
1. Start the application 
2. Click `Log In` in the top right corner
3. Enter your username and password (Make sure you have registered for a profile as shown above)
4. Click `Log In`
![login](https://user-images.githubusercontent.com/32313919/143945413-9b7c135f-2da9-48bf-a5e0-b9bbee0eca15.png)

#### 3. Create Wishlist
After logging in, users can add search items to their wishlist.
**To Add to Wishlist**
1. Start the application
2. Log in and search for a product
3. Click the `Add to wish list` button on the item you wish to add to your wishlist  
![wishlistAdd](https://user-images.githubusercontent.com/32313919/143987978-0428425a-0037-4117-aebc-5352a5c7b693.png)

**To Remove from Wishlist**
1. Click `Remove from wishlist` button on the item.
You can also remove an item from the wishlist by going to the wishlist (see below).
![wishlistRemove](https://user-images.githubusercontent.com/32313919/143987614-6ca26a33-d0dd-4a31-87ce-1cdca6265aea.png)

**To View the Wishlist**
1. Start the application
2. Log in and click the `View Wishlist` button in the top right corner.
![wishlist](https://user-images.githubusercontent.com/32313919/143987749-ef162758-7937-4c69-a8aa-33a4f6ba6246.png)


#### 4. Sorting
Users can sort the results by price or ratings in ascending or descending order. Sorting is done while getting results from e-commerce websites, so it must be refreshed with each search.
1. Start the application and search for a product
2. In the `Sort By` dropdown, select the desired sorting scheme
3. Click the `Search` button
![sort](https://user-images.githubusercontent.com/32313919/143985749-e5b01cb1-cf22-46a7-837d-3fae4335de79.png)

#### 5.Currency
Users can view the price of the items in various currencies (currently supports USD, EURO, AUD, YUAN, YEN, POUND).
1. Start the application and search for a product
2. In the `Currency` dropdown, select the currency you would like to convert to. The price is converted in the items table.

![currency](https://user-images.githubusercontent.com/32313919/143982280-a736256e-bd59-486a-bf2e-53d79649938a.png)

:muscle: What's New in Phase 3?
---
For a list of specific changes in phase 3, see [Project 3 Changes](https://github.com/SE21-Team2/slash/blob/main/docs/Project3Changes.md).

:earth_americas: Future Scope
---
- Creating ordering and payment functionality for customers to directly order from command line
- Scrape more e-commerce websites for wider range of options 
- Add more parameters such as delivery days to get more information about the product 
- Add functionality to store multiple wishlists from the output generated using the search query 
- Add functionality to edit, delete, rename wishlists 
- Add real time dynamic currency converters for different currencies all around the world

:thought_balloon: Use Case
---
* ***Students***: Students coming to university are generally on a budget and time constraint and generally spend hours wasting time to search for products on Websites. Slash is the perfect tool for these students that slashes all the unnecessary details on a website and helps them get prices for a product across multiple websites.Make the most of this tool in the upcoming Black Friday Sale.
* ***Data Analysts***: Finding data for any project is one of the most tedious job for a data analyst, and the datasets found might not be the most recent one. Using slash, they can create their own dataset in real time and format it as per their needs so that they can focus on what is actually important.

:page_facing_up: Why
---
- In a market where we are spoilt for choices, we often look for the best deals.  
- The ubiquity of internet access has leveled the retail playing field, making it easy for individuals and businesses to sell products without geographic limitation. In 2020, U.S. e-commerce sales, receiving a boost due to the COVID-19 pandemic, grew 44% and represented more than 21% of total retail sales, according to e-commerce information source Internet Retailer.
- The growth of e-commerce has not only changed the way customers shop, but also their expectations of how brands approach customer service, personalize communications, and provide customers choices.
- E-commerce market has prompted cut throat competition amongst dealers, which is discernible through the price patterns for products of major market players. Price cuts are somewhat of a norm now and getting the best deal for your money can sometimes be a hassle (even while online shopping).
- This is what Slash aims to reduce by giving you an easy to use, all in one place solution for finding the best deals for your products that major market dealers have to offer!
- Slash in its current form is for people who have some understanding of python and are comfortable in using the command line interface to interact with systems.
- Future updates aim to encompass a wide variety of users irrespective of their computer knowledge and background.


:sparkles: Contributors
---

### Project 3

<table>
  <tr>
    <td align="center"><a href="https://github.com/TanyaChu"><img src="https://github.com/tanyachu.png" width="75px;" alt=""/><br /><sub><b>Tanya Chu</b></sub></a></td>
    <td align="center"><a href="https://github.com/SteveJones92"><img src="https://github.com/SE21-Team2/slash/blob/main/assets/SteveJones92.png" width="75px;" alt=""/><br /><sub><b>Steven Jones</b></sub></a></td>
    <td align="center"><a href="https://github.com/shikhanair"><img src="https://github.com/SE21-Team2/slash/blob/main/assets/shikhanair.png" width="75px;" alt=""/><br /><sub><b>Shikha Nair</b></sub></a></td>
    <td align="center"><a href="https://github.com/alexsnezhko3"><img src="https://github.com/SE21-Team2/slash/blob/main/assets/alexsnezhko3.png" width="75px;" alt=""/><br /><sub><b>Alex Snezhko</b></sub></a></td>
    <td align="center"><a href="https://github.com/prdhnchtn"><img src="https://github.com/SE21-Team2/slash/blob/main/assets/prdhnchtn.png" width="75px;" alt=""/><br /><sub><b>Pradhan Chetan Venkataramaiah</b></sub></a></td>
  </tr>
</table>

### Project 2
<table>
  <tr>
    <td align="center"><a href="https://github.com/antgad"><img src="https://avatars.githubusercontent.com/u/37169203?v=4" width="75px;" alt=""/><br /><sub><b>Anant Gadodia</b></sub></a></td>
    <td align="center"><a href="https://github.com/AnmolikaGoyal"><img src="https://avatars.githubusercontent.com/u/68813421?v=4" width="75px;" alt=""/><br /><sub><b>Anmolika Goyal</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/shubhangij12"><img src="https://avatars.githubusercontent.com/u/48826459?v=4" width="75px;" alt=""/><br /><sub><b>Shubhangi Jain</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/shreyakarra"><img src="https://avatars0.githubusercontent.com/u/89954066?v=4" width="75px;" alt=""/><br /><sub><b>Shreya Karra</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/srujanarao"><img src="https://avatars.githubusercontent.com/u/6882921?v=4" width="75px;" alt=""/><br /><sub><b>Srujana Rao</b></sub></a><br /></td>
  </tr>
</table>

### Project 1
<table>
  <tr>
    <td align="center"><a href="http://www.shubhammankar.com/"><img src="https://avatars.githubusercontent.com/u/29366125?v=4" width="75px;" alt=""/><br /><sub><b>Shubham Mankar</b></sub></a></td>
    <td align="center"><a href="https://github.com/pratikdevnani"><img src="https://avatars.githubusercontent.com/u/43350493?v=4" width="75px;" alt=""/><br /><sub><b>Pratik Devnani</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/moksh98"><img src="https://avatars.githubusercontent.com/u/29693765?v=4" width="75px;" alt=""/><br /><sub><b>Moksh Jain</b></sub></a><br /></td>
    <td align="center"><a href="https://rahilsarvaiya.tech/"><img src="https://avatars0.githubusercontent.com/u/32304956?v=4" width="75px;" alt=""/><br /><sub><b>Rahil Sarvaiya</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/annie0467"><img src="https://avatars.githubusercontent.com/u/17164255?v=4" width="75px;" alt=""/><br /><sub><b>Anushi Keswani</b></sub></a><br /></td>
  </tr>
</table>
