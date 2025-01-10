# Course Search Engine

A Course Search Engine that allows users to search for online courses based on their interests. Using Selenium for web scraping, FAISS for vector search, and Sentence Transformers for text embeddings, this application provides an intelligent and interactive way to find relevant courses. The interface is built using Gradio, offering an intuitive and user-friendly experience.

## 🚀 Features

- **Scrape Courses:** Collect course data (title, description, price, lessons, and image URL) from a specified website using Selenium.
- **Semantic Search:** Search for courses using natural language queries, powered by FAISS and Sentence Transformers.
- **Interactive Interface:** Gradio-based UI for easy interaction and real-time results.
- **Headless Browsing:** Uses headless mode for faster and seamless scraping.

## 🛠️ Tech Stack

### Backend
- **Python:** Core programming language for development.
- **Selenium:** Web scraping and dynamic page interaction.
- **FAISS:** Vector similarity search.
- **Sentence Transformers:** For generating embeddings.

### Frontend
- **Gradio:** Interactive web interface for user input and output.

### Data Management
- **Pandas:** Organizing and processing scraped data.

## 🏗️ Project Structure

```
.
├── app.py                # Main application script
|-- course.json           # Scraped data
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation
```

## 📖 How It Works

### 1. Web Scraping

Selenium is used to scrape course details from the provided URL. The scraped details include:

- Title
- Description
- Number of Lessons
- Price
- Image URL

### 2. Data Preprocessing

The scraped data is saved to a JSON file and can be processed further using Pandas for organization and analysis.

### 3. Embeddings and Search

- **Sentence Transformers** are used to generate vector embeddings for each course.
- **FAISS** builds an efficient vector store for semantic similarity search.

### 4. Gradio Interface

The Gradio interface provides an intuitive search bar for entering queries and displays the most relevant courses with their details.

## 📦 Installation

### Prerequisites
Ensure you have Python 3.8 or later installed on your system.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/NIKHIL-58/smart_search_projects.git
   cd course-search-engine
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open the Gradio interface in your browser:

   The application will provide a local URL (e.g., http://127.0.0.1:7860).

## 📋 Dependencies

The project requires the following Python libraries:

- **Selenium:** For web scraping dynamic content.
- **BeautifulSoup4:** Additional parsing if needed.
- **Pandas:** Data manipulation and organization.
- **FAISS:** Vector similarity search.
- **Sentence Transformers:** Text embeddings.
- **LangChain:** Document and embedding handling.
- **Gradio:** Interactive UI.
- **Webdriver Manager:** For managing browser drivers.

Install all dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 📚 Usage

1. Enter the URL of the course collection page in the script.
2. Run the application to scrape courses and save them to a JSON file.
3. Use the Gradio interface to search for courses using natural language queries.
4. View the results with course details, such as title, price, lessons, and descriptions.

## 🎯 Example

### Input:
```
"Data Science courses under $100"
```

### Output:
```
Title: Data Science Masterclass
Price: $99
Lessons: 50 lessons
Description: Data Science Masterclass Learn from the basics to advanced level.
---
Title: Introduction to Python for Data Science
Price: $89
Lessons: 30 lessons
Description: Learn Python for data science with hands-on projects.
```

## 🖼️ Screenshots

### Gradio Interface

Sample Gradio interface for the Course Search Engine:

![Gradio Interface](path/to/screenshot.png)

## 🏆 Future Enhancements

- Add support for multiple course platforms.
- Integrate user authentication.
- Enable advanced filtering (e.g., by price, rating, or duration).
- Save search results for offline use.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Nikhil Dubey**

- [GitHub](https://github.com/NIKHIL-58)
- [LinkedIn](https://www.linkedin.com/in/nikhil-dubey)
