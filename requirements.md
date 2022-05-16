## Functional Requirements
1. Login - Chris
2. Logout - Chris
3. Create Account - Josh
4. Delete Account - Josh
5. Add to cart  - Hieu
6. Buy Items  - Jackie
7. Delete Item - Jackie
8. Editing User Profiles - Chris
9. User Ratings - Hieu
10. Add item to seller store - Hieu
11. Find Items - Josh
12. Add pictures for items - Hieu
## Non-functional Requirements
1. Only expected to work on Firefox
2. Multilingual support
3. Transactions are secure
4. The website will respond to the users within 1 second
5. Splash Page
## Use Cases
1. Editing User Profiles
- **Pre-condition:** The user is logged in. The user is on their home page.
- **Trigger:** The user has pressed a button to navigate to the profile editor. 
- **Primary Sequence:**
  
  1. Currently on their home page.
  2. Pressing the profile editor, icon, or background button.
  3. When in the editor write a short bio, in the icon space choose from a selection of icons, or in backgorund choose from a selection of backgrounds.

- **Primary Postconditions:** The user is somewhere in the website (either the shopping viewr or any other page).
- **Alternate Sequence:** 
  
  1. They are any place in the site whilst logged in.
  2. Select drop down menue in the upper right to select profile.
  3. Pressing the profile editor, icon, or background button.
  4. When in the editor write a short bio, in the icon space choose from a selection of icons, or in backgorund choose from a selection of backgrounds.
  
2. Add item to seller store
- **Pre-condition:**  User should be logged in and on the profile page. 
- **Trigger:** The user clicks on 'Sell your items' button. 
- **Primary Sequence:**
  
  1. The user is prompted to input an item name, price, and picture.
  2. The user inputs a name and price into the respective text boxes.
  3. The user uploads a picture by clicking 'Browse...' and selecting an image. 
  4. The user selects 'Add to store'.
  5. The item is now added to the list of items on the items page. 

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
  1. Customer searches for item
  2. Customer adds desired item to their cart
  3. Customer clicks the 'buy item' button
  4. Customer is prompted for their shipping information
  5. Customer is prompted for their payment information
  6. Customer clicks "buy" button
- **Primary Postconditions:**
        - Customer has bought an item       
- **Alternate Sequence:**
  1. Customer searches for item that doesn't exist
  2. Customer is told that item is not in stock
  3. Customer can search for a different item

4. Add to cart
- **Pre-condition:** The user must be logged in and be on the profile page.
- **Trigger:** The user must press the button "View cart".
- **Primary Sequence:**
  
  1. The user is prompted to enter an item's id on the cart page.
  2. The user inputs the desired item's id.
  2. The user selects the "Add to cart" button on that page.
  3. The item will be added to the user's cart and displayed on the cart page.

- **Primary Postconditions:** 

  1. The item is added to the user's cart.
  2. The item is not added if the user is not logged in.

- **Alternate Sequence:**
  
  1. The user is not logged in.
  2. The user selects "Add to cart" on an item's page.
  3. The website displays an error message prompting the user to log in.

5. Rate Items
- **Pre-condition:** The user must be logged in and be on the profile page.
- **Trigger:** The user must press the button "Rate an item".
- **Primary Sequence:**
  
  1. The user is prompted an item's id and a numerical rating.
  2. The user inputs an item id and numerical rating into the respective fields.
  3. The user selects 'Add rating'.
  4. The item's rating will be updated on the items page.

- **Primary Postconditions:**

  1. The item has received a new rating and changes its rating accordingly.
  2. The item's rating does not change because the user is not logged in.

- **Alternate Sequence:**
  1. The user is not logged in.
  2. The user selects "Rate this item" on an item's page.
  3. The website displays an error message prompting the user to log in.

6. Add pictures for items
  - **Pre-condition:** The user must be logged in and have an item listed in the store.
  - **Trigger:** The user must press the button "Add pictures to items".
  - **Primary Sequence:**
    1. The user is logged in.
    2. The user "Adds item to seller store".
    3. The website updates the item to the store.
    4. The user selects "Add picture for items". 
    5. The website allows the user to input a picture for different items.
    6. The website displays picutres for the inputted items.
  
- **Primary Postconditions:**
    1. The item has a new picture.  
    2. The item remains listed without a picture because the user is not logged in.  
  
- **Alternate Sequence:** 
    1. The user is not logged in.  
    2. The user selects "Add pictures to items".  
    3. The system displays an error message asking the user to log in.
