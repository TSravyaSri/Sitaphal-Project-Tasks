# RAG Pipeline Web Interface - CSS & JavaScript

This repository contains the CSS and JavaScript files for the web interface of the **Retrieval-Augmented Generation (RAG) pipeline** project. The frontend interacts with the backend to handle tasks such as file uploads, query processing, and displaying results retrieved from the RAG pipeline.

## Overview

The **CSS** and **JavaScript** files are responsible for the layout, styling, and dynamic functionality of the web pages. These files ensure that the user interface is visually appealing, responsive, and interactive.

---

## CSS Files

The **CSS** files are located in the `static/css/` folder. They define the styling and appearance of the web pages.

### Files

- **`styles.css`**
  - This file contains the primary styling for the web interface, including layout, typography, and colors.
  - **Key Features**:
    - **General Styles**: Basic layout, background colors, and font settings.
    - **Responsive Design**: Ensures that the page is usable across devices (desktop, tablet, mobile).
    - **Form Styles**: Customizes the appearance of input fields, buttons, and forms for file uploads and query submission.
    - **Error and Success Messages**: Adds visual cues for displaying success or error messages to the user.
    - **Loading Indicators**: Styles for displaying a loading spinner or progress bar while data is being processed.

### How to Modify

- You can adjust the layout and colors by editing the `.css` classes.
- For adding new sections (e.g., custom pop-ups or modals), you can define new styles in this file.

---

## JavaScript Files

The **JavaScript** files are located in the `static/js/` folder. They handle the dynamic behavior of the web interface, including making API calls, managing form submissions, and rendering results.

### Files

- **`script.js`**
  - This file contains the logic for the following tasks:
    - **File Upload Handling**: Sends the uploaded PDF files to the backend for processing using AJAX.
    - **Query Handling**: Submits the user's query (text) to the backend and handles the response for displaying it dynamically.
    - **Error Handling**: Captures errors (such as invalid file uploads or empty queries) and displays appropriate messages to the user.
    - **Loading States**: Manages loading indicators during file uploads or query processing.
    - **Dynamic Content Rendering**: Once the backend processes the query, this script injects the response into the HTML page.

### How to Modify

- You can modify the event handlers for file uploads or query submissions to customize the interactions.
- The AJAX logic can be updated if the API endpoint changes or if additional features are added (e.g., showing results in a specific format like tables or charts).
- The script is designed to handle responses dynamically, meaning it will automatically update the page content without a full reload.

---

## How to Use

1. **CSS**:
   - Ensure that the `styles.css` file is linked to the HTML files inside the `<head>` tag.
   - Any custom styles can be added to the CSS file.

2. **JavaScript**:
   - Link the `script.js` file in your HTML template right before the closing `</body>` tag.
   - Modify the `script.js` file to customize the form submission, error handling, or dynamic data rendering as per the application's requirements.

---

## File Structure

