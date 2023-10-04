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


### Design Choices


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
