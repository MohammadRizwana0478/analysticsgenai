import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape (replace with actual URL)
url = 'https://www.example.com/free-courses'  # Replace this with actual course site URL

def scrape_courses():
    # Send request to get the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to store course data
    courses = []

    # Modify these based on the actual HTML structure of the website you're scraping
    course_elements = soup.find_all('div', class_='course-class')  # Adjust the class name as necessary

    for course in course_elements:
        title = course.find('h3').text.strip()  # Modify based on actual HTML structure
        description = course.find('p').text.strip()  # Modify based on actual HTML structure
        link = course.find('a')['href']
        courses.append({
            'title': title,
            'description': description,
            'link': link
        })

    # Save the course data to CSV
    df = pd.DataFrame(courses)
    df.to_csv('courses.csv', index=False)  # Save scraped data to a CSV file
    return df

if __name__ == "__main__":
    scrape_courses()
