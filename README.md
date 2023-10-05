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
    * [Data Models](#data-models)
    * [Nelkon Finance Data Structure](#nelkon-finance-data-structure)
        + [User Table](#user-table)
        + [Budgeted Income Table](#budgeted-income-table)
        + [Budgeted Expenses Table](#budgeted-expenses-table)
        + [Actual Income Table](#actual-income-table)
        + [Actual Expenses Table](#actual-expenses-table)
    * [CRUD Flow Diagrams](#crud-flow-diagrams)
- [Design Choices](#design-choices)
    * [Wireframes](#wireframes)
        + [Content Considerations](#content-considerations)
    * [Surface:](#surface)
        + [Color Choice](#color-choice)
        + [Typography](#typography)
        + [Image Choice](#image-choice)
            - [Home Page](#home-page)
            - [Activity Icons](#activity-icons)
            - [Input Icons](#input-icons)
            - [Header Image](#header-image)
            - [Modals and Errors](#modals-and-errors)
            - [Loading Giff](#loading-giff)
        + [Design Elements](#design-elements)
        + [Animations & Transitions](#animations--transitions)
- [User Stories:](#user-stories)
    * [User Persona: Alex, the First-Time User](#user-persona-alex-the-first-time-user)
    * [User Persona: Sarah, the Budgeter](#user-persona-sarah-the-budgeter)
    * [User Persona: Mark, the Financial Analyst](#user-persona-mark-the-financial-analyst)
    * [User Persona: Lisa, the Mobile User](#user-persona-lisa-the-mobile-user)
- [Features](#features)
    * [Implemented Features](#implemented-features)
        + [Structural](#structural)
        + [Common Elements](#common-elements)
        + [Forms](#forms)
        + [Database Operations](#database-operations)
        + [API Integration](#api-integration)
        + [Metrics](#metrics)
    * [Features Left to Implement](#features-left-to-implement)
        + [Features Deferred from original plan](#features-deferred-from-original-plan)
        + [User Roles & Permissions](#user-roles--permissions)
        + [Place Administrator Dashboard](#place-administrator-dashboard)
        + [External User Adult Dashboard](#external-user-adult-dashboard)
        + [External User Minor Dashboard](#external-user-minor-dashboard)
        + [Content Admin Dashboard](#content-admin-dashboard)
        + [Site Admin Dashboard](#site-admin-dashboard)
        + [More Sophisticated Attendance Tracking](#more-sophisticated-attendance-tracking)
        + [API Integrations](#api-integrations)
        + [Switch to Relational Database](#switch-to-relational-database)
        + [Ease of Use Enhancements](#ease-of-use-enhancements)
    * [Project Tracking](#project-tracking)
- [Technologies Used](#technologies-used)
    * [Programming languages](#programming-languages)
    * [Framework & Extensions](#framework--extensions)
    * [Fonts](#fonts)
    * [Tools](#tools)
    * [APIs](#apis)
- [Defensive Programming](#defensive-programming)
    * [Form Validation:](#form-validation)
    * [Cross Site Forgery Protection](#cross-site-forgery-protection)
    * [XSS Protection](#xss-protection)
    * [Restricted Deletion](#restricted-deletion)
- [Testing](#testing)
    * [Validation Testing](#validation-testing)
    * [Unit Testing](#unit-testing)
    * [Cross Browser/ Cross Device Verification](#cross-browser-cross-device-verification)
    * [Cross Site Scripting and Forgery](#cross-site-scripting-and-forgery)
    * [Accessibility Testing](#accessibility-testing)
    * [Regression Testing](#regression-testing)
    * [Automated Testing](#automated-testing)
    * [Defect Tracking](#defect-tracking)
        + [Noteworthy Bugs](#noteworthy-bugs)
        + [Outstanding Defects](#outstanding-defects)
- [Deployment](#deployment)
    * [GitHub](#github)
    * [Requires](#requires)
    * [Development (Running Locally)](#development-running-locally)
    * [Live (Heroku)](#live-heroku)
- [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

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

### Data Structure

#### Database Choice:

Nelkon Finance uses PostgreSQL as its database management system. PostgreSQL was selected due to
its robustness, support for complex queries, and scalability. It provides a reliable foundation for handling financial
data efficiently.

## Data Models

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
- [x] Delete - The delete functionality is also active on this table, as authorised users can successfully delete user information.

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

Having a rough data structure in hand, I knew what data fields I could present users managing the budget income and expenses,
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
Since this project was developed using the Bootstrap library. The font used was the default bootstrap fonts which has very good compatibility with a lot of browsers.

### Imagery
Imagery is important to accompany messages to end-users. The main images used was in the home page to explain to new user the essence of the app
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




### User Stories

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

## About

Nelkon Finance is designed to simplify personal finance management. With this application, users can:

- **Plan Fortune:** Create and manage budgets for income and expenses to achieve financial goals.
- **Track Treasure:** Effortlessly track actual income and expenses to gain insights into spending habits.
- **See Goldmine:** Analyze income sources and expense areas with interactive charts for financial planning.

## Features

- **Budget Management:** Create and manage budgets for different income sources and expense categories.
- **Actual Finances Tracking:** Easily track actual income and expenses over time.
- **Income and Expense Analysis:** Visualize income and expense trends with interactive charts.
- **User Profiles:** Users can create and edit their profiles.
- **Security:** User authentication and authorization with secure password storage.

## Getting Started

Follow these instructions to set up and run Nelkon Finance on your local machine.

### Prerequisites

- Python 3.x
- Flask (Python web framework)
- SQLAlchemy (Python SQL toolkit)
- Other Python packages as mentioned in `requirements.txt`

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/nelkon-finance.git

2. Navigate to the project directory:

       ```bash
       cd nelkon-finance

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    Set up the database:
4. Set Up Database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
5. Start the application:
    ```bash
    flask run

The application should now be running locally. Access it by opening a web browser and navigating
to http://localhost:5100.

### Usage

- Register or log in to your account.
- Use the "Plan Fortune" feature to create budgets for income and expenses.
- Track your actual income and expenses with the "Track Treasure" feature.
- Analyze your financial situation over time using the "See Goldmine" feature.
- Edit your user profile by clicking on "Account" in the navigation bar.

### Contributing

I welcome contributions from the community. If you'd like to contribute to Nelkon Finance, please reach out

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

The development team at Nelkon Finance
Flask and SQLAlchemy open-source communities for their fantastic tools

First image in Carousel: Image
by <a href="https://www.freepik.com/free-photo/close-up-education-economy-objects_18776317.htm#query=budget&position=0&from_view=search&track=sph">
Image by vectorjuice</a> on Freepik
Second image in
carousel: <a href="https://www.freepik.com/free-vector/invoice-concept-illustration_8775504.htm#query=accounting&position=16&from_view=search&track=sph">
Image by storyset</a> on Freepik
Third image in
carousel: <a href="https://www.freepik.com/free-vector/mobile-expense-management-abstract-concept-vector-illustration-charges-control-system-satelite-devices-checking-mobile-network-enterprise-economy-manage-telephony-costs-abstract-metaphor_12083690.htm#query=track%20expenses%20pounds&position=21&from_view=search&track=ais">
Image by vectorjuice</a> on Freepik
