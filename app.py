from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Route to display courses
@app.route('/')
def index():
    try:
        # Load the course data with summaries
        course_data = pd.read_csv('courses_with_summaries.csv')
        return render_template('index.html', courses=course_data.to_dict(orient='records'))
    except FileNotFoundError:
        return "Course data not found. Please run the scraper and summarizer first.", 404

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask web app
