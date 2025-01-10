import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gradio as gr


# Function to scrape course data using Selenium
def scrape_courses_with_selenium(url, output_file="course.json"):
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
        for course in course_elements:
            try:
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
                print(f"Error extracting a course: {e}")

    except Exception as e:
        print(f"Error scraping courses: {e}")
    finally:
        driver.quit()

    # Save scraped data to JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=4)

    return courses

# Function to search for courses in the JSON file
def search_course_by_title(query, input_file="course.json"):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            courses = json.load(f)

        # Perform case-insensitive search
        results = [course for course in courses if query.lower() in course["title"].lower()]
        if not results:
            return "No matching courses found."

        output = []
        for course in results:
            result = f"<div style=\"margin-bottom: 20px;\">\n"
            result += f"<img src=\"{course['image_url']}\" alt=\"{course['title']}\" style=\"width:300px;height:auto;\">\n"
            result += f"<p><strong>Title:</strong> {course['title']}</p>\n"
            result += f"<p><strong>Lessons:</strong> {course['lessons']}</p>\n"
            result += f"<p><strong>Price:</strong> {course['price']}</p>\n"
            result += f"<p><strong>Description:</strong> {course['description']}</p>\n"
            result += "</div>\n"
            output.append(result)

        return "\n---\n".join(output)

    except FileNotFoundError:
        return f"Error: The file {input_file} was not found."
    except Exception as e:
        return f"Error: {e}"


# Main function to scrape and search
if __name__ == "__main__":
    # URL for scraping
    url = "https://courses.analyticsvidhya.com/pages/all-free-courses"

    # Scrape and save data to JSON
    print("Scraping courses...")
    scrape_courses_with_selenium(url)
    print("Scraping completed. Data saved to course.json.")

    # Define Gradio interface for searching
    def gradio_search(query):
        return search_course_by_title(query)

    iface = gr.Interface(
        fn=gradio_search,
        inputs=gr.Textbox(label="Search Courses", placeholder="Enter course title..."),
        outputs="html",
        title="Course Search Engine",
        description="Search for courses by title from the scraped data stored in course.json.",
    )

    iface.launch()
