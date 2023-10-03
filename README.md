# **Nelkon Finance**
![nelkon_finance_logo](https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/4f0c7288-df4f-4c0f-911a-574a9aa41948)

## Project Overview
<img width="1318" alt="Screenshot 2023-10-03 at 11 52 32" src="https://github.com/Nelkon01/Nelkon-Finance/assets/54297166/3456fe0e-feea-473f-8732-0af0f284687e">

[![Nelkon FInance](https://nelkon-finance-671b974bbd16.herokuapp.com) is a web-based finance management application that helps users take control of their financial lives by providing tools for budgeting, expense tracking, income analysis, and more.

## Key Features

- **Monthly Financial Planning:** Nelkon Finance enables users to plan their income and expenses on a monthly basis. It provides an intuitive interface to set budgets and financial goals for each month.

- **Real-time Data Entry:** Users can input their actual income and expenses for the respective months as soon as the transactions occur. This real-time data entry ensures accurate financial tracking.

- **Interactive Dashboard:** The application boasts a dynamic and user-friendly dashboard that transforms raw financial data into insightful visualizations. Users can analyze their income and spending habits through interactive charts that update in real-time.

## How It Works

1. **Monthly Planning:** Users start by setting up budgets and financial plans for each month, outlining their income sources and expected expenses.

2. **Real-time Tracking:** As financial transactions occur, users can instantly log their actual income and expenses within the app, maintaining an up-to-date financial record.

3. **Data Analysis:** Nelkon Finance provides an interactive dashboard consisting of charts and graphs. Users can select specific months to view, and the charts will update to reflect the chosen data, facilitating a deeper understanding of their financial trends.

## Why Choose Nelkon Finance

- **Empowerment:** Users gain control over their finances by setting clear budgets and tracking income and expenses as they happen.

- **Insightful Analysis:** Users can make informed financial decisions with access to interactive charts and trends that help identify areas for improvement.

- **User-Friendly:** Nelkon Finance offers an intuitive and user-friendly interface, making financial management accessible to everyone.

- **Real-time Updates:** The application ensures that users' financial data is always up-to-date, providing a real-time snapshot of your financial health.


## Table of Contents
<details>
<summary>Click to Expand</summary>

- [UX](#ux)
  * [Strategy](#strategy)
  * [Scope](#scope)
  * [Goals](#goals)
    + [Customer Goals](#customer-goals)
    + [Place Owner Goals](#place-owner-goals)
    + [WebSite Goals](#website-goals)
- [Data Structure](#data-structure)
  * [Database Choice](#database-choice)
  * [Data Models](#data-models)
  * [Collections Data Structure](#collections-data-structure)
    + [Activities](#activities)
    + [Addresses](#addresses)
    + [Countries](#countries)
    + [Events](#events)
    + [Metrics Clicks](#metrics-clicks)
    + [Metrics Page](#metrics-page)
    + [Places](#places)
    + [Reviews](#reviews)
    + [Users](#users)
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
  * [For kids looking for something free to do today in their neighborhood:](#for-kids-looking-for-something-free-to-do-today-in-their-neighborhood)
  * [For places and organizations involved in building the community](#for-places-and-organizations-involved-in-building-the-community)
  * [For site owners hosting a website to store community information](#for-site-owners-hosting-a-website-to-store-community-information)
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

The application should now be running locally. Access it by opening a web browser and navigating to http://localhost:5100.

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
Third image in carousel: <a href="https://www.freepik.com/free-vector/mobile-expense-management-abstract-concept-vector-illustration-charges-control-system-satelite-devices-checking-mobile-network-enterprise-economy-manage-telephony-costs-abstract-metaphor_12083690.htm#query=track%20expenses%20pounds&position=21&from_view=search&track=ais">
Image by vectorjuice</a> on Freepik
