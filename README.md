# **Nelkon Finance**

![nelkon_finance_logo](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/4f0c7288-df4f-4c0f-911a-574a9aa41948)

## Project Overview

<img width="1318" alt="Screenshot 2023-10-03 at 11 52 32" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/3456fe0e-feea-473f-8732-0af0f284687e">

[Nelkon Finance](https://nelkon-finance-671b974bbd16.herokuapp.com/) is a web-based finance management application that
helps users take control of their financial lives by providing tools for budgeting, expense tracking, income analysis,
and more.

## Key Features

- **Monthly Financial Planning:** Nelkon Finance enables users to plan their income and expenses on a monthly basis. It
  provides an intuitive interface to set budgets and financial goals for each month.

- **Real-time Data Entry:** Users can input their actual income and expenses for the respective months as soon as the
  transactions occur. This real-time data entry ensures accurate financial tracking.

- **Interactive Dashboard:** The application boasts a dynamic and user-friendly dashboard that transforms raw financial
  data into insightful visualizations. Users can analyze their income and spending habits through interactive charts
  that update in real-time.

## How It Works

1. **Monthly Planning:** Users start by setting up budgets and financial plans for each month, outlining their income
   sources and expected expenses.

2. **Real-time Tracking:** As financial transactions occur, users can instantly log their actual income and expenses
   within the app, maintaining an up-to-date financial record.

3. **Data Analysis:** Nelkon Finance provides an interactive dashboard consisting of charts and graphs. Users can select
   specific months to view, and the charts will update to reflect the chosen data, facilitating a deeper understanding
   of their financial trends.

## Why Choose Nelkon Finance

- **Empowerment:** Users gain control over their finances by setting clear budgets and tracking income and expenses as
  they happen.

- **Insightful Analysis:** Users can make informed financial decisions with access to interactive charts and trends that
  help identify areas for improvement.

- **User-Friendly:** Nelkon Finance offers an intuitive and user-friendly interface, making financial management
  accessible to everyone.

- **Real-time Updates:** The application ensures that users' financial data is always up-to-date, providing a real-time
  snapshot of your financial health.

## Table of Contents

<details>
<summary>Click to Expand</summary>

- [UX](#ux)
    * [Strategy](#strategy)
    * [Scope](#scope)
- [Data Structure](#data-structure)
    * [Database Choice](#database-choice)
        + [User Table](#user-table)
        + [Budgeted Income Table](#budgeted-income-table)
        + [Budgeted Expenses Table](#budgeted-expenses-table)
        + [Actual Income Table](#actual-income-table)
        + [Actual Expenses Table](#actual-expenses-table)
- [Design Choices](#design-choices)
    * [Wireframes](#wireframes)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
- [User Stories:](#user-stories)
    * [User Persona: Alex, the First-Time User](#user-persona-alex-the-first-time-user)
    * [User Persona: Sarah, the Budgeter](#user-persona-sarah-the-budgeter)
    * [User Persona: Mark, the Financial Analyst](#user-persona-mark-the-financial-analyst)
    * [User Persona: Lisa, the Mobile User](#user-persona-lisa-the-mobile-user)
- [Features](#features)
    * [Implemented Elements](#implemented-elements)
      * [Forms](#forms)
      * [Database Operations](#database-operations)
      * [Additional Features](#additional-features)
      * [Future feature enhancements](#future-feature-enhancements)
- [Technologies Used](#technologies-used)
    * [Front-End Technologies](#front-end-technologies)
    * [Back-End Technologies](#back-end-technologies)
    * [Deployments and hosting](#deployment-and-hosting)
    * [Version Control and Collaboration](#version-control-and-collaboration)
- [Defensive Programming](#defensive-programming)
- [Testing](#testing)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgments)
   

</details>

## UX

### Strategy

The UX strategy for **Nelkon Finance** centers around providing a seamless and empowering financial management
experience
for users. The primary goal of the app is to make financial planning, tracking, and analysis accessible to individuals
from all
walks of life.

**Key Objectives**

1. **User Empowerment:** This web app aims to empower users to take control of their financial lives by offering
   user-friendly tools
   for budgeting, expense tracking, and income analysis.

2. **Simplicity:** Simplicity is at the core of my strategy. I strive for an intuitive and easy-to-navigate interface to
   ensure that users can effortlessly manage their finances.

3. **Real-time Insights:** Providing real-time updates and interactive charts is a top priority. Users should be able to
   gain
   insights into their financial health instantly.

4. **Customization:** I understand that personal finances vary widely. Thus, the strategy includes offering
   customization
   options that allow users to tailor the app to their unique financial goals.

### Scope

The scope of **Nelkon Finance** covers a range of features and functionalities designed to address various aspects of
financial management, which includes:

- **Monthly Financial Planning:** Users can set up monthly budgets, outline income sources, and establish expense
  categories.

- **Real-time Data Entry:** Users can input actual income and expenses as they occur, ensuring accurate financial
  tracking.

- **Interactive Dashboard:** The app features an interactive dashboard with dynamic charts that update in real-time,
  providing
  visual insights into income and spending habits.

- **User Authentication:** User accounts and authentication are implemented to protect sensitive financial data.

- **User Profiles:** Users can create profiles with personalized information and financial goals.

- **Accessibility:** The app is designed with accessibility in mind to ensure that users with varying abilities can
  comfortably navigate and use it.

## Data Structure

### Database Choice:

Nelkon Finance uses PostgreSQL as its database management system. PostgreSQL was selected due to
its robustness, support for complex queries, and scalability. It provides a reliable foundation for handling financial
data efficiently.

### User Table

| Field     | Type    | Description              |
|-----------|---------|--------------------------|
| id        | Integer | Unique user identifier   |
| username  | String  | User's username          |
| firstname | String  | User's first name        |
| lastname  | String  | User's last name         |
| password  | String  | Securely hashed password |
| email     | String  | User's email address     |

The nature of this app makes it a requirement for users be signed up to the app and their unique identifier be used to
access their financial data.

- [x] Create - A user is potentially created when a user successfully signs up to the app services by filling the form
  on the signup page.
- [x] Read - The user table is read when a potential user attempts to signup to the app, to determine if the email or
  or username supplied into the form already exists to avoid duplicates.The user table is also read when a user logs in
  to the app, and navigates to the profile page.
- [x] Update - Users can also update their information whenever they navigate to the profile page to carry out this
  action
- [x] Delete - The delete functionality is also active on this table, as authorised users can successfully delete user
  information.

### Budgeted Income Table

| Field         | Type    | Description                                  |
|---------------|---------|----------------------------------------------|
| income_id     | Integer | Unique income identifier                     |
| user_id       | Integer | Foreign key to link income to a user         |
| income_name   | String  | Name/description of the income source        |
| budget_amount | Float   | Planned budgeted income for a specific month |
| month_name    | String  | Name of the month (e.g., "January")          |
| year          | Integer | Year associated with the income              |

- [x] Create - A budget income is potentially created when an authorised user successfully create a budget income entry.
- [x] Read - The budget income table is read when an authorised user navigates to the page that displays budget income
  entries
  and navigates to the page that should render a dashboard view for that user financial information
- [x] Update - Budget income entries can be updated should an authorised user decide to do so.
- [x] Delete - The delete functionality is also active on this table as authorised user have the ability to delete
  budget income entries

### Budgeted Expenses Table

| Field         | Type    | Description                                       |
|---------------|---------|---------------------------------------------------|
| expense_id    | Integer | Unique expense identifier                         |
| user_id       | Integer | Foreign key to link expense to a user             |
| category_name | String  | Expense category (e.g., "Utilities," "Groceries") |
| expense_name  | String  | Name/description of the expense                   |
| budget_amount | Float   | Planned budgeted expense for a specific month     |
| month_name    | String  | Name of the month (e.g., "January")               |
| year          | Integer | Year associated with the expense                  |

- [x] Create - A budget expense is potentially created when an authorised user successfully create a budget expense
  entry.
- [x] Read - The budget expense table is read when an authorised user navigates to the page that displays budget expense
  entries
  and navigates to the page that should render a dashboard view for that user financial information.
- [x] Update - Budget expense entries can be updated should an authorised user decide to do so.
- [x] Delete - The delete functionality is also active on this table as authorised user have the ability to delete
  budget expense entries

### Actual Income Table

| Field         | Type    | Description                                       |
|---------------|---------|---------------------------------------------------|
| income_id     | Integer | Unique expense identifier                         |
| user_id       | Integer | Foreign key to link expense to a user             |
| income_name   | String  | Expense category (e.g., "Utilities," "Groceries") |
| date          | Date    | Date associated with the income                   |
| actual_amount | Float   | Actual Amount that was received                   |

- [x] Create - An actual income object is potentially created when an authorised user successfully create an actual
  income entry.
- [x] Read - The actual income table is read when an authorised user navigates to the page that displays actual income
  entries
  and navigates to the page that should render a dashboard view for that user financial information
- [x] Update - Actual income entries can be updated should an authorised user decide to do so.
- [x] Delete - The delete functionality is also active on this table as authorised user have the ability to delete
  actual income entries

### Actual Expenses Table

| Field         | Type    | Description                                       |
|---------------|---------|---------------------------------------------------|
| expense_id    | Integer | Unique expense identifier                         |
| user_id       | Integer | Foreign key to link expense to a user             |
| category_name | String  | Expense category (e.g., "Utilities," "Groceries") |
| expense_name  | String  | Name/description of the expense                   |
| actual_amount | Float   | Planned budgeted expense for a specific month     |
| date          | Date    | Date associated with the expense                  |

- [x] Create - An actual expense object is potentially created when an authorised user successfully create an actual
  expense entry.
- [x] Read - The actual expense table is read when an authorised user navigates to the page that displays actual expense
  entries
  and navigates to the page that should render a dashboard view for that user financial information
- [x] Update - Actual expense entries can be updated should an authorised user decide to do so.
- [x] Delete - The delete functionality is also active on this table as an authorised user have the ability to delete
  actual expense entries

### CRUD Flow Diagrams

## Design Choices

The intent is to provide a clean, simple intuitive design to users.

### Wireframes

Having a rough data structure in hand, I knew what data fields I could present users managing the budget income and
expenses,
actual income and expenses, and to view a dashboard.
Please note, the mock-ups are guidelines not a hard design requirements. Some aspects changed during development to make
the site more user-friendly, simple and intuitive to use.

**Home Page**
<img width="450" alt="Screenshot 2023-10-05 at 11 31 25" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/ac3bfd7a-8df1-453b-95d3-46796f5c5e5f">

**Plan Fortune Page**
<img width="450" alt="Screenshot 2023-10-05 at 11 32 20" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/b24670b6-0670-4dca-b9ba-d7f4708e6555">

**Track Treasure Page**
<img width="451" alt="Screenshot 2023-10-05 at 11 34 14" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/36d46fdf-3ac1-492f-96f5-7336d73e502a">

**See Goldmine Page**
<img width="452" alt="Screenshot 2023-10-05 at 11 35 05" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/a1a51c93-5bc1-4bc4-97a9-072613e80ddb">

### Colour Scheme

I chose to stick with a simple dark vibe colour scheme for the project
![nelkon_finance colorscheme](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/a2dd5761-1eb7-475f-aa0b-cc2f76944908)

### Typography

Since this project was developed using the Bootstrap library. The font used was the default bootstrap font, which has
very good compatibility with a lot of browsers.

### Imagery

Imagery is important to accompany messages to end-users. The main images used was on the home page to explain to new
user the essence of the app
**Header Image**
<img width="1076" alt="app-in-action" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/4a2d935e-efa4-42f3-b657-367d529bf8d2">
**Budget Image**
![budget-image](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/bc1a6503-00ae-45b6-8dc6-64232a2639a2)
**Tracking Image**
![tracking-image](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/6a8309c5-aa98-4aa8-b3bd-710ea56f0fd5)
**Analysis Image**
![analysis-image](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/cd41ad8c-0515-4d73-91ff-321755803300)

I also had icons in the "How to" section, which gives new users a quick walkthrough of using the app.
**Sign Up Icon**
![signup-icon](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/6523737e-d85d-4c66-9005-8898a7016377)
**Plan Icon**
![plan-icon](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/94de0a56-9b24-4f4a-858d-fb02e202512e)
**Track Icon**
![track-icon](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/5f6c3dba-90ae-4a06-b2c7-aa562eaba0a9)
**Dashboard Icon**
![dashboard-icon](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/007584c8-fd7d-4f4c-b334-94a3b46a0e48)

### Home Page

**Nav Bar**
The nav bar is shown across all screens
<img width="1243" alt="Screenshot 2023-10-05 at 14 58 27" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/66146b85-f159-4f92-a832-fc933829ba1f">
For smaller to mobile screen users:
<img width="611" alt="Screenshot 2023-10-05 at 17 53 22" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/5a181d61-dd0a-4408-a19d-86edf3685e9b">
<img width="614" alt="Screenshot 2023-10-05 at 17 54 03" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/ca67659a-f45c-4467-9887-09d12d05ed2b">

**Hero Section**
<img width="1243" alt="Screenshot 2023-10-05 at 15 01 52" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/a729d195-981d-4675-ad33-2ff8a4debd10">

**Information Section**
This section exists to give new users a little more information about the capabilities of the app. which are mainly *
*Budget Management**, **Actual Finances Tracking** and **Income and Expense Analysis**
For Larger medium to large screen sizes, this section will be shown as a carousel, as shown in the screenshots below.
<img width="1246" alt="Screenshot 2023-10-05 at 15 03 33" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/0de72a77-f640-4f11-a05a-ee86db22ecfc">
<img width="1246" alt="Screenshot 2023-10-05 at 15 03 58" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/ce1344d6-a55a-41d8-8174-65ae07886bb7">
<img width="1247" alt="Screenshot 2023-10-05 at 15 04 29" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/46e2b618-4892-4b07-8b6e-c298d44a2068">
However, this section will be shown as normally as a stack for smaller screen sizes and mobiles.
<img width="617" alt="Screenshot 2023-10-05 at 17 43 47" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/97c3592c-e487-4083-8eee-e0a9e5c3eed4">

**How It Works Section**
This section is there to give a new user a walkthrough on how to navigate using the web app.
The screenshot below shows what this section looks like.
<img width="617" alt="Screenshot 2023-10-05 at 17 47 19" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/c2802802-54a9-4494-9ad3-d9c1d61a1d54">

**Footer Section**
<img width="1162" alt="Screenshot 2023-10-05 at 18 06 58" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/bb4ed1d8-b2ab-4696-9d40-08e4d4b3784d">

### Plan Fortune Page

This page is where users can add their budget income and expenses for respective months. Users can view their previous
entries on this page and edit and delete them.
The screenshot below shows an example of what the plan fortune page can look like.
<img width="1166" alt="Screenshot 2023-10-05 at 18 13 38" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/ccf14938-f1a7-422f-b9c6-f90eaa2bda19">
Once a user wants to add a new budget income or entry, they need to click on one of the "Add budget income/expense"
buttons on the screen. This triggers a modal that displays a form for the user to fill in to create that data entry
successfully. An example is shown in the screenshot below if a user wants to create a budget expense entry.
<img width="934" alt="Screenshot 2023-10-05 at 18 20 39" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/4c590d86-29c2-4d0d-a428-791cd6ddc862">
Some fields in the form contain options that users may select from instead of manually typing all the input required for
the form filling. This was included to help with a positive user experience. An example of this is the Month field.
<img width="499" alt="Screenshot 2023-10-05 at 18 25 04" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/660539cb-cc97-4bf6-bd3c-43960ba82c06">
User entries can be edited as well. And this triggers a modal to render an already prefilled form for users to update
that information.
<img width="609" alt="Screenshot 2023-10-05 at 18 34 30" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/60cc1b5f-44d2-4e8d-935a-e8e8eaada593">
Entries can also be deleted. A modal that asks the user to confirm deletion is rendered to the user. This is a way to
ensure that users do not accidentally delete an entry that was not intended and help improve user experience.
<img width="618" alt="Screenshot 2023-10-05 at 18 57 30" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/11b809c9-d5a9-4360-a7b5-0da4b7281b29">

### Track Treasure Page

This page is very similar to the Plan Fortune page. It is basically for the Actual Income and expenses but for a users
actual finances.
<img width="1119" alt="Screenshot 2023-10-05 at 19 22 00" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/71cdfe5a-7339-4676-9c44-17a016b00352">

### See Goldmine Page

This page is where users view an interactive dashboard that displays charts according to the financial information
provided. Below is a screenshot example of the goldmine page.

<img width="1178" alt="Screenshot 2023-10-05 at 21 39 03" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/efafacd0-343e-4a26-989f-e2115a4742a1">

### Profile Page

Once Users click the account dropdown, there is a link to the profile page, which takes the users to a page where they
can update their information, change passwords, and delete their accounts.
<img width="1194" alt="Screenshot 2023-10-05 at 21 57 21" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/913efdde-8a7e-4d25-a3e0-5ad32d85f73f">
Users can see their existing information and change it if they want. However, the current password is not displayed to
the user, so it is not exposed to prying eyes. But the current password can be changed and updated on this page.
When users want to delete their accounts, a modal appears to check with the user if they want to delete the account.
<img width="989" alt="Screenshot 2023-10-05 at 22 09 30" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/c8fc08b6-dc20-405b-b313-6925e1bbb93c">

## User Stories

Here are a few user stories that demonstrate how **Nelkon Finance** meets the needs of its users:

#### **User Persona: Alex, the First-Time User:**

- As a first-time user, I want a simple and straightforward onboarding process.
- I want clear guidance on how to set up my monthly budget, input income sources, and define expense categories.
- The app should provide tooltips or an easy-to-access tutorial to help me get started.
- Seeing my financial data presented visually on the dashboard should be intuitive, even for someone using it for
  the first time.
- The app should leave me feeling confident and empowered to manage my finances effectively.

#### **User Persona: Sarah, the Budgeter**

- As a monthly budgeter, I want to set specific spending limits for various expense categories.
- I want to log my actual expenses as I make them, so I can see how well I'm sticking to my budget.
- The interactive dashboard helps me quickly identify which categories I need to adjust to stay on track.

#### **User Persona: Mark, the Financial Analyst**

- I'm a data-driven user who wants to analyze my yearly income trends.
- I can easily select specific months or years to view on the dashboard and watch the charts update in real-time.
- This feature helps me make informed financial decisions.

#### **User Persona: Lisa, the Mobile User**

- I'm always on the go, and I want to access my financial data from my smartphone.
- I appreciate that the app is responsive and works seamlessly on my mobile device.
- Logging transactions and viewing charts are equally convenient on my phone.

The user stories illustrate how Nelkon Finance caters to the diverse needs of its users, from budgeters to financial
analysts and mobile users.

By focusing on UX strategy and carefully scoping the features, The aim is to deliver a valuable and user-centric
financial management tool.

## Features

Below, I have detailed the key features, including implemented elements, forms, and database operations.

## Implemented Elements

### 1. Interactive Dashboard

- **Description**: Nelkon Finance provides users with an interactive dashboard that offers a visual representation of
  their financial data. It includes dynamic charts and graphs to help users quickly grasp their financial status.

### 2. User Authentication

- **Description**: The application features user authentication to ensure that financial data is secure and accessible
  only to registered users. Users can create accounts, log in, and log out as needed.

### 3. User Profile Management

- **Description**: Users have the ability to manage their profiles. They can update their personal information, such as
  username and email address, and change their passwords.

## Forms

### 1. Budget Planning

- **Description**: Nelkon Finance allows users to plan their monthly budgets by entering budgeted income sources and
  expenses. Users can specify the income or expense category, the description, and the planned amount for each item.

### 2. Recording Actual Income and Expenses

- **Description**: Users can record their actual income and expenses for each month as they occur. They can enter the
  income or expense category, a description, and the actual amount.

## Database Operations

### 1. Storing User Data

- **Description**: User data, including usernames, email addresses, and securely hashed passwords, is stored in the
  database. User registration and profile management operations are handled securely.

### 2. Budget Data Management

- **Description**: Nelkon Finance stores budgeted income and expense data for each user. This data includes the
  category, description, planned amount, and the associated month and year.

### 3. Actual Income and Expense Tracking

- **Description**: The application allows users to track their actual income and expenses on a monthly basis. This data
  is stored in the database, associating each record with the user, category, description, actual amount, and the
  corresponding month and year.

### 4. User-Specific Data

- **Description**: All data is segregated by user, ensuring that each user can only access and manipulate their own
  financial information. User-specific queries are performed to retrieve and display the relevant data.

## Additional Features

### 1. Data Analysis

- **Description**: Nelkon Finance offers data analysis tools to help users understand their financial patterns. Users
  can select specific months to view charts and graphs depicting their budgeted and actual income and expenses over
  time.

### 2. Responsive Design

- **Description**: The application is designed to be responsive, ensuring a seamless user experience on both desktop and
  mobile devices.

### 3. Logout Functionality

- **Description**: Users can log out of their accounts to protect their financial data when using shared or public
  computers.

Nelkon Finance aims to provide users with a robust and user-friendly financial management platform. The features listed
above empower users to take control of their financial lives by offering budget planning, expense tracking, and data
analysis tools, all within a secure and easy-to-use application.

### Future Feature Enhancements

While the app offers a robust set of features for managing your finances, there are several exciting enhancements and
features planned for future development:

### 1. Expense Reminders

- **Description**: Add the ability for users to set reminders for recurring expenses. This feature will help users stay
  on top of their financial obligations and avoid missing payments.

### 2. Savings Goals

- **Description**: Enable users to set savings goals and track their progress. Users can allocate a portion of their
  budgeted income towards specific goals, such as a vacation or a new car.

### 3. Export Financial Reports

- **Description**: Allow users to export their financial data and reports to popular formats like PDF or CSV. This
  feature will simplify tax preparation and financial planning.

### 4. Mobile App Integration

- **Description**: Develop a mobile application version of Nelkon Finance for seamless on-the-go financial management.

### 5. Expense Receipt Upload

- **Description**: Enable users to upload and attach expense receipts to their recorded expenses for better
  record-keeping and documentation.

### 6. Collaboration and Sharing

- **Description**: Implement collaboration features that allow users to share financial data with trusted family members
  or financial advisors. Users can work together to manage household finances effectively.

### 7. Bill Payment Integration

- **Description**: Integrate bill payment functionality, allowing users to pay their bills directly through the
  application. This feature will streamline the payment process and reduce manual entry.

### 8. Data Backup and Recovery

- **Description**: Provide users with the ability to create data backups and implement a data recovery system in case of
  accidental data loss.

### 9. Multi-Currency Support

- **Description**: Add support for multiple currencies, allowing users to manage finances in different currencies,
  especially beneficial for international users.

These future enhancements are designed to make Nelkon Finance an even more powerful and versatile financial management
platform. I am committed to continuously improving the application to meet the evolving needs of potential users.

## Technologies Used

Nelkon Finance leverages a combination of modern technologies and frameworks to provide users with a secure and
feature-rich financial management experience. Here are the key technologies and tools used in the development of this
application:

### Front-End Technologies

- **HTML5**: The application's front-end is built using HTML5 for structuring web pages and rendering content.

- **CSS3**: Cascading Style Sheets (CSS3) are used to style and format the application's user interface, ensuring a
  visually appealing and responsive design.

- **JavaScript**: JavaScript is used for client-side scripting, enabling dynamic and interactive features such as form
  validation and chart rendering.

- **Bootstrap**: The Bootstrap framework is employed for front-end development to ensure a responsive and
  mobile-friendly layout. It also provides pre-designed UI components for faster development which i substantially
  relied
  on for this project.

- **Chart.js**: Chart.js is utilized to create visually engaging and interactive charts and graphs for data
  visualization in the application.

### Back-End Technologies

- **Python**: The back-end logic of Nelkon Finance is written in Python, a versatile and high-level programming language
  known for its readability and robustness.

- **Flask**: Flask, a lightweight Python web framework, is used to build the application's server-side components,
  including routing, request handling, and rendering templates.

- **Flask-SQLAlchemy**: Flask-SQLAlchemy is an extension for Flask that simplifies database interactions. It's used to
  define and manipulate database models.

- **PostgreSQL**: PostgreSQL, a powerful open-source relational database management system, is the database of choice
  for Nelkon Finance. It stores and manages user data securely.

- **Flask-Login**: Flask-Login is employed for user authentication and session management, ensuring secure user access
  and data protection.

- **WTForms**: WTForms is used for form creation and validation, enhancing the user experience and maintaining data
  integrity.

- **Gunicorn**: Gunicorn serves as the production-ready web server for deploying the Flask application.

### Deployment and Hosting

- **Heroku**: Nelkon Finance is hosted on Heroku, a cloud platform that simplifies deployment and ensures high
  availability. Heroku also provides automatic scaling to handle varying user loads.
- **ElephantSql**: The live app uses elephant sql for the for its database hosting

### Version Control and Collaboration

- **Git and GitHub**: Git is used for version control, allowing multiple developers to collaborate efficiently on the
  project. GitHub hosts the Git repository and facilitates code sharing and issue tracking.

### Tools

- [balsamiq](https://balsamiq.com/) - used to create professional looking wire frames.
- [icon generator](https://favicon.io/favicon-generator/) - free site to help in website icon generation
- [lighthouse audit](https://developers.google.com/web/tools/lighthouse) Google's open source tool to help improve the
  quality of your website. Specifically paid attention to Accessibility and SEO aiming for scores above 80.
- [freepik](https://freepik.com) This website was instrumental in getting the images and icons i needed for the homepage
  currently is freeware and installed as a chrome extension.

## Development Environment

- **PyCharm**: JetBrains PyCharm serves as the primary integrated development environment (IDE)
  for writing, debugging, and testing code.

These technologies collectively enable Nelkon Finance to offer a secure, performant, and user-friendly financial
management solution to potential users.

## Defensive Programming

Defensive programming is a crucial aspect of the app's development strategy. It focuses on writing code that
anticipates and guards against potential errors, vulnerabilities, and edge cases. This approach enhances the
application's reliability, security, and robustness. Below are the key defensive programming practices implemented in
this project

### Input Validation

All user inputs, are rigorously validated. Input validation checks include:

- Ensuring that required fields are not empty.
- Validating data types and formats, such as email addresses and dates.

### Error Handling

Nelkon Finance includes comprehensive error handling mechanisms to gracefully manage unexpected situations. Key aspects
of error handling include:

- Proper use of try...except blocks to catch and handle exceptions.
- Logging error details for debugging purposes while not exposing sensitive information to users.
- Providing informative error messages to users when something goes wrong, making it easier for them to understand and
  report issues.

### Authentication and Authorization

- User authentication and authorization are central to security. Passwords are securely hashed and stored using strong
  cryptographic algorithms.

### Session Management

- User sessions are managed securely, with a timeout mechanism to automatically log users out after a period of
  inactivity.

- ## Restricted Deletion
- Before any edit or delete action is taken, there is a check to ensure that the user trying to carry out the action is
  the user
  that owns access and is authorised to carry out the action

By following these defensive programming practices,the app prioritizes the security and reliability of potential users
financial data. While no system is entirely immune to threats, these measures significantly reduce risks and contribute
to a safer user experience.

## Testing

Testing is a crucial aspect of the app's development process. It ensures that the application functions correctly, meets
user expectations, and remains reliable. Below are the key testing strategies and practices employed:

### Unit Testing

Unit testing involves testing individual components (functions, methods, classes) of the application in isolation. In
Nelkon Finance, unit tests are implemented using popular testing frameworks like `pytest`. Key aspects of unit testing
include:

- Testing functions and methods to verify that they produce the expected output for various inputs.
- Ensuring that error conditions are handled appropriately.
- Testing edge cases to check for robustness.

### Functional Testing

Functional testing assesses the application's functionality from the user's perspective. Nelkon Finance's functional
testing includes:

- Testing user interfaces (UI) to ensure they are intuitive and responsive.
- Evaluating user workflows, such as registering, logging in, creating budgets, and generating reports.
- Validating that features meet user stories and requirements.

### End-to-End (E2E) Testing

End-to-end testing assesses the application's functionality as a whole, simulating real user scenarios. In this case,
E2E tests:

- Test critical user journeys, from registration to generating financial reports.
- Ensure that the application functions correctly across different browsers and devices.

### User Acceptance Testing (UAT)

User acceptance testing involves real users testing the application in a production-like environment. I collected user
feedback during UAT to identify usability issues, gather insights, and make improvements based on user suggestions.

### Bug Tracking

A bug tracking system is used to record, prioritize, and manage issues identified during testing and by users. I
addressed every reported problem promptly by my tests subjects.

### Regression Testing

Regression testing is performed after code changes to verify that new features or bug fixes do not introduce new issues
or break existing functionality. Manual regression tests are an integral part of Nelkon Finance's development process.

### Validation Testing

**Home Page**

- Validator tests
  <img width="1092" alt="Screenshot 2023-10-06 at 08 20 01" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/4f2eb167-d500-4ed7-97f2-63ed0f258db5">
- Lighthouse Audit
  <img width="443" alt="Screenshot 2023-10-06 at 08 18 32" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/49644229-1109-4dc6-8245-da3291d2301b">
  **Plan Page**
- Validator
  <img width="1019" alt="Screenshot 2023-10-06 at 08 27 07" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/52b1733c-61a5-42af-9792-ccedc02d3411">

- Lighthouse Audit
  <img width="436" alt="Screenshot 2023-10-06 at 08 26 24" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/196473e6-8d45-409d-9ca9-978471fb5dc9">
  **Track Page**
- Validator
  <img width="1019" alt="Screenshot 2023-10-06 at 08 27 07" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/f977d85f-3a61-49e5-8c62-a03026d993f6">

- Lighthouse Audit
  <img width="447" alt="Screenshot 2023-10-06 at 08 31 56" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/5701b249-4380-4f43-a7db-47fca796bad4">
  **Goldmine page**
- Validator
  <img width="877" alt="Screenshot 2023-10-06 at 08 35 23" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/18a21c89-4858-4440-abf7-a83c20bb81d2">
- Lighthouse Audit
  <img width="437" alt="Screenshot 2023-10-06 at 08 34 35" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/db49e8ff-36f1-4e94-b353-f3487af20955">
  **Profile Page**
- Validator
  <img width="877" alt="Screenshot 2023-10-06 at 08 35 23" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/a9aca31c-a572-46d4-92e3-4ed2322fc76b">
- Lighthouse Audit
  <img width="430" alt="Screenshot 2023-10-06 at 08 41 28" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/788889e3-174f-48cb-a6bf-e402466b5006">
  **Login Page**
- Validator
  <img width="1108" alt="Screenshot 2023-10-06 at 08 42 52" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/38c81e9b-f17f-4576-b38c-c89f32bc9a47">

- Lighthouse Audit
  <img width="445" alt="Screenshot 2023-10-06 at 08 43 14" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/37ea643d-6b39-416b-905f-6d866967b54b">

**CSS Validation**
<img width="1099" alt="Screenshot 2023-10-06 at 08 46 08" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/3dd62686-bb70-432f-b117-40dbcad0be68">

**JavaScript Validation**
Js Validation showed no errors
<img width="530" alt="Screenshot 2023-10-06 at 08 49 51" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/824bc899-f024-482a-ab61-418502091f7d">

## Manual Testing

Manual testing is a crucial part of ensuring the reliability and user-friendliness of this app, and manual tests that
were carried out by my friends and I have confirmed that the application performs exceptionally well in various
scenarios. Here's an overview of the successful manual tests:

### Blank/Empty Inputs

1. **Registration**: During user registration, we've verified that all required fields (e.g., name, email, password)
   must be filled out. Our tests included submitting the registration form with missing information, and the application
   responded with appropriate error messages.

2. **Budget and Expense Creation**: When users create budgets or expenses, Nelkon Finance ensures that essential
   fields (e.g., budget name, expense amount) are not left blank. Validation successfully prevents incomplete
   submissions.

### Invalid Inputs

1. **Validation**: We tested by inputting invalid data in forms, such as providing a non-email format for the email
   field or entering text in a numeric field. The application consistently responded with clear error messages guiding
   users on the correct input format.

2. **Boundary Testing**: Nelkon Finance gracefully handles extreme values, such as very large or very small numbers. Our
   tests confirmed that the application behaves correctly without crashing or displaying unexpected behavior.

### Ownership Verification

1. **Edit and Delete Actions**: Nelkon Finance strictly enforces that users can only edit or delete the budgets and
   expenses they own. Attempts to modify items owned by other users consistently result in appropriate access denied
   messages.

### New User vs. Established User

1. **New User Scenarios**: We've tested with both brand new users and established users. For new users, the onboarding
   process is seamless, allowing them to create their first budgets and expenses with ease.

### Mobile vs. Desktop Differences

1. **Responsive Design**: Nelkon Finance's responsive design elements adapt seamlessly to various devices, including
   mobile phones, tablets, and desktop computers.

### Navigation Changes

1. **User State Differences**: Nelkon Finance's navigation menus and links appropriately adjust based on the user's
   authentication state, ensuring a consistent and user-friendly experience.

### Duplicate Emails and Usernames

1. **Uniqueness Check**: Nelkon Finance successfully enforces unique email addresses and usernames for each user.
   Attempts to register with the same email or username that is already in use are consistently prevented.

By conducting thorough manual testing that covers these scenarios, Nelkon Finance ensures a seamless and error-free
experience for all users. Our tests have confirmed that the application is reliable and user-friendly, providing you
with a high-quality financial management tool.

## Noteworthy Bugs/Defects

This section highlights notable bugs or defects that have been identified and require attention. Each item includes a
clear description of the issue, steps to reproduce it, and its current status (e.g., open, in progress, resolved).

### Charts not updating correctly

**Description:**

The goldmine charts were not displaying any charts even after users had all information included

**Steps to Reproduce:**

1. Input Bugdet income and actual income into the database
2. Input actual income and actual expense into the database
3. Navigate to the goldmine page and click on update charts after selecting month and year information
4. The Charts just showing a blank screen

**Current Status:**

- [ ] Open: The bug has been reported but has not yet been assigned for resolution.
- [ ] In Progress: The issue is actively being worked on by a developer.
- [x] Resolved: The bug has been fixed and verified.

**Additional Information:**

I initially wanted to use plotly dash to achieve the interactive dashboard functionality of the app, however, i wasnt
able to make it work. I therefore decided to use chart.js for this functionality, which resloved that issue for me

### Budget and Actual Income Coverage Showing wrong figures

**Description:**
The Idea behind the budget and actual income coverage and actual income coverage is to check if the income for that
month covers the expense for the month. And this metric was in percentage. However, i have an issue whereby i was having
values above 100% which is practically impossible.

**Steps to Reproduce:**

1. Input Bugdet income and actual income into the database
2. Input actual income and actual expense into the database
3. Navigate to the goldmine page and click on update charts after selecting month and year information

**Current Status:**

- [ ] Open: The bug has been reported but has not yet been assigned for resolution.
- [ ] In Progress: The issue is actively being worked on by a developer.
- [x] Resolved: The bug has been fixed and verified.

**Additional Information:**
I realised there was a problem with my logic in the way i was making the calculation in my function, and it has been
fixed

**Description:**
The line charts in the goldmine page is showing the numerical values for months instead of the text name of the
respective months. which may not be good user experience

**Steps to Reproduce:**

1. Input Bugdet income and actual income into the database
2. Input actual income and actual expense into the database
3. Navigate to the goldmine page and click on update charts after selecting month and year information

**Current Status:**

- [x] Open: The bug has been reported but has not yet been assigned for resolution.
- [ ] In Progress: The issue is actively being worked on by a developer.
- [ ] Resolved: The bug has been fixed and verified.

**Additional Information:**
I have not come around to fixing this, however, i reckon the fix could be in me assigning a label for each number in the
charts javascript code

- There is also a slight problem with the way heroku is handling my favicon which is returning a error. I have not come
  around to fixing this yet.

## Deployment

This site was developed using PyCharm's IDE. To keep records of different versions of all project files, git version
control was used. This project is hosted using Heroku deployed from the master branch.

### GitHub

All versions and branches of the code are stored in github:
https://github.com/Nelkon01/Nelkon-Finance

### Prerequisites

- Python 3
- Flask (Python web framework)
- SQLAlchemy (Python SQL toolkit)
- Other Python packages as mentioned in `requirements.txt`

### Development (Running Locally)

PyCharm was the IDE I developed my code in. I was able to deploy my code locally using the following steps:

1. Get the code base from git hub by running this command in the terminal of your IDE:
   ```$ git clone https://github.com/Nelkon01/Nelkon-Finance.git```

2. Navigate to the project directory:

       ```bash
       cd nelkon-finance

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
  
    
4. [set environmental variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) with your
   own values for:
    
    > - os.environ.setdefault("IP", "your ip")
    
    > - os.environ.setdefault("PORT", "your port")
    
    # Set your secret key for the Flask application
    
    > - os.environ.setdefault("SECRET_KEY", "your sectet key")
    
    # Set the development flag
    
    > - os.environ.setdefault("DEVELOPMENT", "boolean, true/false")
    
    # Set your database URL
    
    > - os.environ.setdefault("DATABASE_URL", "your database url")
    
    > - os.environ.setdefault("DEBUG", "boolean, true/false")
    
    - DEBUG/DEVELOPMENT -Boolean, Typically True for development and False for deployed version

5. start your server by typing
   ```$ python run.py```

6. access your local version of the application.

### Live (Heroku)

Heroku was used to run this site in a cloud environment to allow visibility to external users.

1. Get the code base from git hub by running this command in the terminal of your IDE:
    
    ```bash
       $ git clone https://github.com/nelkon01/nelkon-finance.git
       ```

2. Login to Heroku and set up a new app
3. Under the **Settings** tab, click **Reveal Config Vars**
4. Set the following variables
    
    > |    Variable       	     |  Setting  	  |
    >|:-----------------------:|:------------:|
    >|| DEBUG                	  | False     	  |
    >||      DATABASE_URL       | YOUR_DB_URL  |
    >|| IP                    	 | 0.0.0.0    	 |
    >|| PORT                  	 | 5000       	 |
    >|| SECRET_KEY            	 | YOUR_KEY  	  |

5. Go back to your IDE's terminal window and connect to heroku ```bash heroku login``` and enter your credentials
6. Clone the heroku repository (exact command can be found on the Deployment tab for the app you just created in
   heroku) ```bash heroku git:clone -a 'your_app_name'```
7. make a slight change to a file, say the readme.md file
8. add the files, commit and push to heroku master:

```bash
$ git add .
$ git commit -am "initial heroku commit" 
$ git push heroku master
```

You should be able to access the application at your heroku via the url provided in the terminal window, or the open app
button from your heroku app dashboard.
Ex) https://nelkon-finance-671b974bbd16.herokuapp.com

### Contributing

I welcome contributions from the community. If you'd like to contribute to Nelkon Finance, please reach out

### Acknowledgments

Flask and SQLAlchemy open-source communities for their fantastic tools

- [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-1-installing-packages):
  This website helped me with flask understanding
- [Gitau Harrison Blog](https://www.gitauharrison.com/articles/data-visualization-with-flask-and-chartjs): This
  fantastic blog helped me with integrating flask with chart.js
- The Fantastic team at code institite
- [Malia Havlicek](https://github.com/maliahavlicek): My mentor for this project
- First image in Carousel: Image
  by <a href="https://www.freepik.com/free-photo/close-up-education-economy-objects_18776317.htm#query=budget&position=0&from_view=search&track=sph">
  Image by vectorjuice</a> on Freepik
- Second image in
  carousel: <a href="https://www.freepik.com/free-vector/invoice-concept-illustration_8775504.htm#query=accounting&position=16&from_view=search&track=sph">
  Image by storyset</a> on Freepik
- Third image in
  carousel: <a href="https://www.freepik.com/free-vector/mobile-expense-management-abstract-concept-vector-illustration-charges-control-system-satelite-devices-checking-mobile-network-enterprise-economy-manage-telephony-costs-abstract-metaphor_12083690.htm#query=track%20expenses%20pounds&position=21&from_view=search&track=ais">
  Image by vectorjuice</a> on Freepik
