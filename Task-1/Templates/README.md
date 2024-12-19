The **`templates/`** folder contains the core HTML structure for the frontend of the project. These HTML files will be used by the Flask app to render dynamic content based on the user's interactions with the RAG pipeline. The HTML files are responsible for the layout, user inputs, and displaying results.

#### **1. `index.html`**
The main landing page for the web application. It serves as the entry point for the user to interact with the system.

- **File Upload Section**: Contains a form where the user can upload one or more PDF files. This form will trigger an AJAX request to the backend to process the file.
- **Query Input Section**: A text input field where users can type their natural language queries. After submitting, the system sends the query to the backend to retrieve relevant data from the vector database.
- **Response Display Area**: A section where the results of the query are dynamically displayed. This includes text responses or structured data, such as tables or lists, depending on the type of query and the returned data.
- **Loading Indicator**: Displays a loading message or spinner while the server processes the file upload or query request.
- **Error Handling Area**: If the user uploads an invalid file or submits an empty query, an error message will be displayed in this area.

**Key Elements**:
- Form for file upload and query submission.
- Placeholder for dynamic query results.
- A section for user feedback, such as success or error messages.
- Navigation for basic instructions or help.

#### **2. `file_upload.html`**
This HTML template is specifically designed for the file upload feature. It contains the form for uploading PDF files, along with instructions for the user to ensure they upload the correct file format.

- **File Input Field**: Allows the user to choose and upload PDF files.
- **Submit Button**: Triggers the upload process.
- **Success/Error Messages**: Displays messages based on the success or failure of the file upload.
- **Instructions**: Offers guidance on which files are acceptable for upload (e.g., only PDF files).

**Key Elements**:
- File input to select and upload PDF files.
- Form submission action for handling the file upload.
- Feedback for success or errors during the upload process.

#### **3. `query_input.html`**
This template focuses on handling user queries. It allows the user to enter a query and submit it to the backend for processing.

- **Query Input Field**: A text input field where the user enters their question.
- **Submit Button**: Submits the query to the server for processing.
- **Prompt for Information**: Text that helps users understand what type of queries can be asked (e.g., about the contents of the PDFs).
- **Response Display Area**: Where the query response will be shown once it's retrieved from the backend.

**Key Elements**:
- Text input field for user query.
- Submit button to send the query.
- Dynamic display area for the query response.

#### **4. `comparison_results.html`**
This template is for displaying comparison results between different data points retrieved from multiple PDFs. It formats the results in a structured way, such as a table or bullet points.

- **Table/Chart**: Displays the comparison data between the selected elements from the PDFs.
- **Structured Data**: The data can be presented in columns or rows for easy comparison.
- **Formatting Instructions**: Provides guidance on how the comparison is structured (e.g., by degree type, location, etc.).

**Key Elements**:
- Comparison data displayed in a table or chart.
- Structured layout to show differences or similarities clearly.
- Titles/headers explaining the comparison.

#### **5. `response_display.html`**
This template is responsible for rendering the responses returned from the backend after processing the query. It includes placeholders for displaying the dynamic data retrieved.

- **Dynamic Content Placeholder**: Displays the results that are returned by the backend.
- **Formatting for Data**: Ensures that the response is formatted in a user-friendly way, including textual responses or structured data like tables, lists, or bullet points.

**Key Elements**:
- Placeholder to dynamically inject query responses.
- Formatting logic to ensure the data is presented clearly.
  
### **Conclusion**
The **`templates/`** folder contains HTML files that define the structure and layout for interacting with the RAG pipeline system. These templates ensure that the user can upload files, submit queries, and view responses, with dynamic content rendered based on the backend's processing. By separating the HTML structure into different templates, the system can easily handle file uploads, query processing, and response generation in a modular way.
