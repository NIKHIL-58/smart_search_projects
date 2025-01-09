import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
import gradio as gr
import numpy as np

# Function to scrape course data using Selenium
def scrape_courses_with_selenium(url, limit=50):
    options = Options()
    options.headless = True  # Headless browsing
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "course-card"))
        )
    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return []

    courses = []
    try:
        course_elements = driver.find_elements(By.CLASS_NAME, "course-card")
        for i, course in enumerate(course_elements):
            if i >= limit:
                break
            title = course.find_element(By.CLASS_NAME, "course-card__body").text or "No Title"
            description = course.find_element(By.CLASS_NAME, "course-card__body").text or "No Description"
            lessons = course.find_element(By.CLASS_NAME, "course-card__lesson-count").text or "No Lessons"
            price = course.find_element(By.CLASS_NAME, "course-card__price").text or "No Price"
            image_url = course.find_element(By.TAG_NAME, "img").get_attribute("src") or "No Image"
            
            courses.append({
                "title": title,
                "description": description,
                "lessons": lessons,
                "price": price,
                "image_url": image_url,
            })
    except Exception as e:
        print(f"Error scraping courses: {e}")
    finally:
        driver.quit()
    
    return courses

class SentenceTransformersEmbeddings(Embeddings):
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        # Generates embeddings for a list of documents
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()  # Convert numpy array to list

    def embed_query(self, text):
        # Generates embedding for a single query
        embedding = self.model.encode([text], show_progress_bar=True)[0]
        return embedding.tolist()  # Convert numpy array to list

def main():
    # URL for scraping
    url = "https://courses.analyticsvidhya.com/collections/courses"
    limit = 5  # Number of courses to scrape
    courses = scrape_courses_with_selenium(url, limit)

    if not courses:
        print("No courses found!")
        return

    # Print course information
    for course in courses:
        print(f"Title: {course['title']}, Description: {course['description']}, Price: {course['price']}, Lessons: {course['lessons']}")

    # Convert Data to DataFrame
    df = pd.DataFrame(courses)

    # Combine title and description for embeddings
    df["combined_text"] = df["title"] + " " + df["description"]
    texts = df["combined_text"].tolist()

    # Initialize embedding model
    embedding_model = SentenceTransformersEmbeddings('all-MiniLM-L6-v2')

    # Create Documents for FAISS
    documents = [
        Document(
            page_content=text,
            metadata={"source": f"Course {i+1}", **{k:v for k,v in courses[i].items() if k != 'description'}}
        )
        for i, text in enumerate(texts)
    ]

    # Create FAISS Vector Store
    vector_store = FAISS.from_documents(documents, embedding_model)

    # Define search function
    def smart_search(query):
        docs = vector_store.similarity_search(query, k=2)
        results = []
        for doc in docs:
            result = f"\nTitle: {doc.metadata['title']}\n"
            result += f"Price: {doc.metadata['price']}\n"
            result += f"Lessons: {doc.metadata['lessons']}\n"
            result += f"Content: {doc.page_content}\n"
            results.append(result)
        return "\n---\n".join(results)

    # Create Gradio interface
    iface = gr.Interface(
        fn=smart_search,
        inputs=gr.Textbox(label="Search Courses", placeholder="Enter your search query..."),
        outputs=gr.Textbox(label="Results"),
        title="Course Search Engine",
        description="Search for courses based on your query. The system will return the most relevant matches.",
    )

    # Launch the interface
    iface.launch()

if __name__ == "__main__":
    main()