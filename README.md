# Course Search Engine


A **Course Search Engine** that allows users to search for online courses based on their interests. Using Selenium for web scraping, FAISS for vector search, and Sentence Transformers for text embeddings, this application provides an intelligent and interactive way to find relevant courses. The interface is built using **Gradio**, offering an intuitive and user-friendly experience.

---

## 🚀 Features

- **Scrape Courses**: Collect course data (title, description, price, lessons, and image URL) from a specified website using Selenium.
- **Semantic Search**: Search for courses using natural language queries, powered by FAISS and Sentence Transformers.
- **Interactive Interface**: Gradio-based UI for easy interaction and real-time results.
- **Headless Browsing**: Uses headless mode for faster and seamless scraping.

---

## 🛠️ Tech Stack

### Backend
- **Python**: Core programming language for development.
- **Selenium**: Web scraping and dynamic page interaction.
- **FAISS**: Vector similarity search.
- **Sentence Transformers**: For generating embeddings.

### Frontend
- **Gradio**: Interactive web interface for user input and output.

### Data Management
- **Pandas**: Organizing and processing scraped data.

---

## 🏗️ Project Structure

```plaintext
.
├── app.py                # Main application script
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation (this file)
```

---

## 📖 How It Works

### 1. Web Scraping
![Scraping Icon](https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/000000/external-web-scraping-digital-marketing-flaticons-lineal-color-flat-icons.png)
- Selenium is used to scrape course details from the provided URL.
- The scraped details include:
  - **Title**
  - **Description**
  - **Number of Lessons**
  - **Price**
  - **Image URL**

### 2. Data Preprocessing
- The scraped data is converted into a Pandas DataFrame.
- Titles and descriptions are combined to create a single searchable text field.

### 3. Embeddings and Search
![Search Icon](https://img.icons8.com/external-justicon-lineal-color-justicon/64/000000/external-search-seo-justicon-lineal-color-justicon.png)
- Sentence Transformers are used to generate vector embeddings for each course.
- FAISS builds an efficient vector store for semantic similarity search.

### 4. Gradio Interface
- Provides an intuitive search bar for entering queries.
- Displays the most relevant courses with their details.

---

## 📦 Installation

### Prerequisites
Ensure you have Python 3.8 or later installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/course-search-engine.git
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
   - The application will provide a local URL (e.g., `http://127.0.0.1:7860`).

---

## 📋 Dependencies

The project requires the following Python libraries:

- **Selenium**: For web scraping dynamic content.
- **BeautifulSoup4**: Additional parsing if needed.
- **Pandas**: Data manipulation and organization.
- **FAISS**: Vector similarity search.
- **Sentence Transformers**: Text embeddings.
- **LangChain**: Document and embedding handling.
- **Gradio**: Interactive UI.
- **Webdriver Manager**: For managing browser drivers.

Install all dependencies using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## 📚 Usage

1. Enter the URL of the course collection page in the script.
2. Run the application to scrape courses and index them in FAISS.
3. Use the Gradio interface to search for courses using natural language queries.
4. View the results with course details, such as title, price, lessons, and descriptions.

---

## 🎯 Example

### Input:
"Data Science courses under $100"

### Output:
```plaintext
Title: Data Science Masterclass
Price: $99
Lessons: 50 lessons
Content: Data Science Masterclass Learn from the basics to advanced level.
---
Title: Introduction to Python for Data Science
Price: $89
Lessons: 30 lessons
Content: Learn Python for data science with hands-on projects.
```

---

## 🖼️ Screenshots

![Gradio Interface](https://img.icons8.com/color/96/000000/search.png)

*Sample Gradio interface for the Course Search Engine.*

---

## 🏆 Future Enhancements

- Add support for multiple course platforms.
- Integrate user authentication.
- Enable advanced filtering (e.g., by price, rating, or duration).
- Save search results for offline use.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Your Name**

[![GitHub](https://img.icons8.com/fluent/48/000000/github.png)](https://github.com/your-username)
[![LinkedIn](https://img.icons8.com/fluent/48/000000/linkedin.png)](https://linkedin.com/in/your-profile)


