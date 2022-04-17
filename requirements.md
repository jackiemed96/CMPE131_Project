## Functional Requirements
1. Login //Chris
2. Logout //Chris
3. Create new account //Josh
4. delete account //Josh
5. Add to cart  //Hieu
6. Buy items  //Jackie
7. Splash page //Jackie
8. User profiles //Chris
9. User ratings //Hieu
10. Add item to seller store //Josh
11. Find items  //Hieu
12. Add pictures for items //Jackie
## Non-functional Requirements
1. Only expected to work on Firefox
2. Multilingual support
3. Transactions are secure
4. The website will respond to the users within 1 second
## Use Cases
1. User Profiles
- **Pre-condition:** The user is logged in. The user is on their home page.
- **Trigger:** The user has moved from their home page to the profile viewer. 
- **Primary Sequence:**
  
  1. Entering their home page.
  2. Pressing the profile button.

- **Primary Postconditions:** The user is somewhere in the website (either the shopping viewr or any other page).
- **Alternate Sequence:** 
  
  1. They are any place in the site whilst logged in.
  2. Select drop down menue in the upper right to select profile.
  
2. Add item to seller store
- **Pre-condition:**  User should be logged in. 
- **Trigger:** The user has moved from a page to the listing maker. 
- **Primary Sequence:**
  
  1. Entering their home page.
  2. Pressing the make a listing button.

- **Primary Postconditions:** The user is in their profile page.
- **Alternate Sequence:**
  
  1. Hover over the drop down menue in the upper right.
  2. Select the make a listing option.

- **Alternate Sequence:**
  
  1. The user is in the shop.
  2. The user can select to list their own item which is similar.

3. Buy items
- **Pre-condition:** 
  1. Having an account
  2. Being logged in
  3. Finding the desired item
- **Trigger:** 
  1. Customer clicks 'buy item' button
- **Primary Sequence:**
  1. Customer logs into account
  2. Customer searches for item
  3. Customer adds desired item to their cart
  4. Customer clicks the 'buy item' button
  5. Customer is prompted for their shipping information
  6. Customer is prompted for their payment information
  7. Customer clicks "buy" button
- **Primary Postconditions:**
        - Customer has bought an item       
- **Alternate Sequence:**
  1. Customer searches for item that doesn't exist
  2. Customer is told that item is not in stock
  3. Customer can search for a different item

4. Add to cart
- **Pre-condition:** The user must be logged in and be on the item's page.
- **Trigger:** The user must press the button "Add to cart".
- **Primary Sequence:**
  
  1. The user is logged in.
  2. The user is on the page with their desired item.
  3. The user selects the "Add to cart" button on that page.
  4. The item will be sent to the user's cart.
  5. The website displays the message "Add to cart successfully".

- **Primary Postconditions:** 

  1. The item is added to the user's cart.
  2. The item is not added if the user is not logged in.

- **Alternate Sequence:**
  
  1. The user is not logged in.
  2. The user selects "Add to cart" on an item's page.
  3. The website displays an error message prompting the user to log in.

5. User ratings
- **Pre-condition:** The user must be logged in and be on an item's page.
- **Trigger:** The user must press the button "Rate this item".
- **Primary Sequence:**
  
  1. The user is logged in.
  2. The user is on the page of an item.
  3. The user selects the "Rate this item" button on that page.
  4. The website displays a message promping the user to input a number rating.
  5. The user inputs a number.
  6. The website displays the message "Rating received"

- **Primary Postconditions:**

  1. The item has received a new rating and changes its rating accordingly.
  2. The item's rating does not change because the user is not logged in.

- **Alternate Sequence:**
  1. The user is not logged in.
  2. The user selects "Rate this item" on an item's page.
  3. The website displays an error message prompting the user to log in.
