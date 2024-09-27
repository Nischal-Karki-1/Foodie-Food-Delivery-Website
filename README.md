# 🚀 Foodie-Food-Delivery-Website

## What is this project about?
FOODIE is an online food delivery app aimed at providing a seamless ordering experience for customers while allowing restaurant owners to manage their menus and track orders. Built using **React** (MUI library) for the frontend, **Django** for the backend, and **PostgreSQL** as the database, FOODIE addresses common issues with other food delivery platforms by providing a flexible, user-friendly interface for both customers and owners.

## Features

1. **Customer Features**:
   
   - **Combo Meal Creation**: Users can create custom combo meals and save them for future orders.
     
   - **Google Sign-In**: Login using Google accounts.
     
   - **Live Order Updates**: Customers receive live updates on the status of their orders.
     
   - **Customer Feedback**: Users can provide feedback on the food and services.

2. **Owner Features**:
   
   - **Order Management**: Owners can track orders in real-time.
     
   - **Menu Management**: Easily update food categories and items, including pricing, offers, and discounts.
     
   - **Sales Charts**: Owners can track weekly sales and profits using bar and doughnut charts.
     
   - **Order History Export**: Export order history in CSV format for a specified date range.

## Installation

- ### Clone the Project

```bash
git clone https://github.com/Nischal-Karki-1/Foodie-Food-Delivery-Website.git
```
- ### Backend Setup
1. Install the required dependencies:

 ```bash
 pip install -r backend/requirements.txt
 ```
   
2. Run database migrations:

```bash
python manage.py migrate
```
   
3. Start the backend server:

```bash
python manage.py runserver
```
   
4. Set up your email configuration in core/settings.py:

```bash
EMAIL_HOST_USER = '<your-business-gmail>'
EMAIL_HOST_PASSWORD = '<token-gained-for-third-party-app-for-gmail>'
```
   
- ### Frontend Setup
  
1. Navigate to the frontend directory:
      
```bash
cd frontend
```
   
2. Install the required dependencies:
      
```bash
npm install --force
```
   
3. Start the frontend development server:
      
```bash
npm start
 ```

- ### OAuth2.0 Setup
  
1. Go to the Django admin page, and under **DJANGO OAUTH TOOLKIT**, create a new application.
   
2. Copy the Client ID and Client Secret.
   
3. Obtain your Google Client ID.
   
4. Create a ```.env``` file inside the ```frontend``` folder and add the credentials:
   
```bash
# Django OAuth backend credentials
REACT_APP_CLIENT_ID = <your-client-id>
REACT_APP_CLIENT_SECRET = <your-client-secret>

# Google OAuth credentials
REACT_APP_GOOGLE_CLIENT_ID = <your-google-client-id>
```
- ### Running the Application
1. Open two terminals: one for the backend and one for the frontend.

In the first terminal, run the backend server:
```
python manage.py runserver
```

2. In the second terminal, run the frontend:
```
npm start
```

## Screenshots (Narrative Storytelling)
#### Home Page - Foodie
Displays the welcoming interface for the Foodie platform, where users can begin their experience by logging in or signing up.

<div align="center">
    <img src="https://github.com/user-attachments/assets/331a4945-2731-47db-b991-aa94000ad799" alt="Screenshot 2024-09-27 211936" width="562">
    <br><br>
</div>

#### User Registration Page
Allows new users to create an account, enabling them to personalize their food ordering experience on the platform.

<div align="center">
    <img src="https://github.com/user-attachments/assets/f89758d1-0392-4125-8e7d-3d063235fa77" alt="Screenshot 2024-09-27 212010" width="580">
    <br><br>
</div>

#### User Login Page
Provides a secure portal for users to log into the system and access personalized features such as saved food preferences.

<div align="center">
    <img src="https://github.com/user-attachments/assets/bb225a6a-4e1a-47d7-9001-972778af2484" alt="Screenshot 2024-09-27 212032" width="575">
    <br><br>
</div>

#### User Dashboard
Displays a personalized dashboard for users after logging in, showcasing menu items, orders, and account settings.

<div align="center">
    <img src="https://github.com/user-attachments/assets/97d2980a-e2b2-40c6-8ca5-ab988525d67f" alt="Screenshot 2024-09-27 212134" width="272">
    <br><br>
</div>

#### Food Item Pop-Up: Pizza Selection
Shows a pop-up window detailing the pizza food item, including options to customize, add to cart, or view allergens.

<div align="center">
    <img src="https://github.com/user-attachments/assets/568e6949-7440-4121-a0f2-1ef1a789e30f" alt="Screenshot 2024-09-27 212203" width="501">
    <br><br>
</div>

#### Food Item Pop-Up: Fried Chicken Selection
Another food item pop-up, this time highlighting fried chicken with options to customize and add to the user's cart.

<div align="center">
    <img src="https://github.com/user-attachments/assets/1d6651fa-6c16-490b-aa4a-818a804b916f" alt="Screenshot 2024-09-27 212227" width="381">
    <br><br>
</div>

#### Cart Page
Provides a summary of items added to the cart, allowing users to review and modify their orders before checkout.

<div align="center">
    <img src="https://github.com/user-attachments/assets/850d2753-df7a-49cf-a4dd-5a8bfbcdf4fe" alt="Screenshot 2024-09-27 212244" width="391">
    <br><br>
</div>

#### Checkout Page
The final step in the order process where users confirm payment and delivery details before placing their order.

<div align="center">
    <img src="https://github.com/user-attachments/assets/dfb9d954-8b74-4113-834a-39f996e266e5" alt="Screenshot 2024-09-27 212302" width="328">
    <br><br>
</div>

#### Order Confirmation Message
Displays the confirmation message after the order has been successfully placed, ensuring the user that the order is being processed.

<div align="center">
    <img src="https://github.com/user-attachments/assets/428bf000-9918-492e-9ca5-a3a5b16e441d" alt="Screenshot 2024-09-27 212322" width="343">
    <br><br>
</div>

#### Creating a Combo Meal - Before
Shows the interface before a user creates a custom combo meal, allowing users to mix and match different food items.

<div align="center">
    <img src="https://github.com/user-attachments/assets/03b79419-016b-4687-9c32-6875c0373f97" alt="Screenshot 2024-09-27 212358" width="314">
    <br><br>
</div>

#### Creating a Combo Meal - After
Displays the completed custom combo meal, ready to be added to the cart or saved for future orders.

<div align="center">
    <img src="https://github.com/user-attachments/assets/106e0677-b85c-4251-94af-fbc93e925169" alt="Screenshot 2024-09-27 212439" width="446">
    <br><br>
</div>

#### Login to the Owner Page
Provides restaurant owners a secure login portal to access management tools for their menu and orders.

<div align="center">
    <img src="https://github.com/user-attachments/assets/7784106b-e69f-4e27-a5d8-0988b26e47f5" alt="Screenshot 2024-09-27 212500" width="449">
    <br><br>
</div>

#### Owner Dashboard
The main dashboard for restaurant owners, where they can view real-time updates, manage menus, and track orders.

<div align="center">
    <img src="https://github.com/user-attachments/assets/e97d4b41-ffef-41d3-b088-bef0a4e5b92a" alt="Screenshot 2024-09-27 212521" width="366">
    <br><br>
</div>

#### Order List for the Owner
Displays a list of active and completed orders, providing restaurant owners with detailed information on the order status.

<div align="center">
    <img src="https://github.com/user-attachments/assets/2d30a2f6-5e6d-4e55-9952-fed2d7600577" alt="Screenshot 2024-09-27 212548" width="655">
    <br><br>
</div>

#### Delivery Status Tracking
A series of status updates showing an order's progress, from placement to preparation, shipping, and delivery.

<div align="center">
    <img src="https://github.com/user-attachments/assets/4566fe5d-bd4e-4bcf-b3ee-01cd66d1d47e" alt="Screenshot 2024-09-27 212618" width="602">
    <br><br>
</div>

#### Add Item Page for Owners
Allows restaurant owners to add new food items or categories, updating the menu in real time for customers.

<div align="center">
    <img src="https://github.com/user-attachments/assets/ce9b0fc6-a1c9-48ed-a6ba-d8095d25f2b4" alt="Screenshot 2024-09-27 212718" width="291">
    <br><br>
</div>

#### Adding a New Category: Biryani
Shows the interface where owners can add new food categories, such as Biryani, to the menu.

<div align="center">
    <img src="https://github.com/user-attachments/assets/5143b48d-290f-4947-a78f-7d8941ca688c" alt="Screenshot 2024-09-27 212737" width="287">
    <br><br>
</div>

#### Adding a New Food Item: Chicken Biryani
Demonstrates the process of adding a specific item, like Chicken Biryani, under a newly created food category.

<div align="center">
    <img src="https://github.com/user-attachments/assets/db7de3f5-eccb-4c8b-9846-ac7f52bbc98f" alt="Screenshot 2024-09-27 212755" width="419">
    <br><br>
</div>

#### New Category Added to the Owner Page
Displays the newly created category on the owner’s menu management page.

<div align="center">
    <img src="https://github.com/user-attachments/assets/188b89f9-a3f6-46ef-84cd-59ee54d4b867" alt="Screenshot 2024-09-27 212821" width="429">
    <br><br>
</div>

#### New Food Item Added to the Owner Page
Shows the newly added food item, Chicken Biryani, under the Biryani category in the owner’s management system.

<div align="center">
    <img src="https://github.com/user-attachments/assets/d660ff94-a019-4120-8e73-a48539a41e14" alt="Screenshot 2024-09-27 212841" width="275">
    <br><br>
</div>

#### New Category Displayed on the User Page
The user interface showing the newly added Biryani category in the customer’s menu view.

<div align="center">
    <img src="https://github.com/user-attachments/assets/0ed63ec8-3cb3-47e3-a091-4c0ef95c63ac" alt="Screenshot 2024-09-27 212931" width="414">
    <br><br>
</div>

#### New Menu Item Displayed on the User Page
Shows the Chicken Biryani item within the Biryani category, visible to customers.

<div align="center">
    <img src="https://github.com/user-attachments/assets/6bcd413c-4487-4834-922b-459c938cd70d" alt="Screenshot 2024-09-27 212949" width="280">
    <br><br>
</div>

#### Offer for Food Item: Chicken Biryani
Displays the promotion or discount offered on Chicken Biryani, as seen by both customers and owners.

<div align="center">
    <img src="https://github.com/user-attachments/assets/c613c862-963e-47ce-95f2-7c2cd58729ab" alt="Screenshot 2024-09-27 213003" width="365">
    <br><br>
</div>

#### Owner's Order History Page
Allows restaurant owners to review past orders and download reports on sales and earnings.

<div align="center">
    <img src="https://github.com/user-attachments/assets/cbe29b3f-88e2-47bf-9b96-1dc10a5160e9" alt="Screenshot 2024-09-27 213023" width="485">
    <br><br>
</div>

#### Customer Review Submission
Shows the interface where customers can submit reviews for the food they’ve ordered.

<div align="center">
    <img src="https://github.com/user-attachments/assets/f3c7ee4e-98e1-4820-8445-7b99ec7667ea" alt="Screenshot 2024-09-27 213042" width="364">
    <br><br>
</div>

#### Customer Care Page for Owners
Provides tools for restaurant owners to manage customer reviews and respond to feedback.

<div align="center">
    <img src="https://github.com/user-attachments/assets/c75e1a87-92aa-4b4c-9650-54b8634fe6aa" alt="Screenshot 2024-09-27 213102" width="461">
    <br><br>
</div>

#### Customer Review Wall on User Page
Displays customer reviews on the user page, providing feedback and ratings on food items.

<div align="center">
    <img src="https://github.com/user-attachments/assets/c7408dcb-4dfa-43ab-8a28-18d4e5a64c5c" alt="Screenshot 2024-09-27 213129" width="455">
    <br><br>
</div>


