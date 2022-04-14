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
1. Use Case Name (should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit 
amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore 
magna aliqua.
- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis 
nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea 
commodi consequatur. 
- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>
- **Primary Postconditions:** <can be a list or short description> 
- **Alternate Sequence:** <you can have more than one alternate sequence to 
describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...
- **Alternate Sequence <optional>:** <you can have more than one alternate sequence
to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...
2. Use Case Name (Should match functional requirement name)
   ...
3. Add item to seller store
   **Pre-condition:** User must be logged in
   
   **Trigger:** Customer selects " add items to shop" option

   **Primary Sequence:** 
   1:System allows user to place item into shop
   2:Customer adds description of item 
   3:Customer sets price of item
   4:System lists item on website for sale
   5:Customer logs out

   **Alternate Sequence:**
   2.Customer sells illegal item
      a.System displays warning message to customer
      b.System flags customer

   **Post-condition:** 
   -Customer's item is listed in the shop
   -Customer receives money when item is bought
    OR
   -Customer fails to list item on shop
   -System doesn't update and shop remains the same
