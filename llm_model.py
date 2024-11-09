import openai
import pandas as pd
import os

# Set OpenAI API key (use environment variable for security)
openai.api_key = os.getenv('OPENAI_API_KEY')  # Use your API key securely from environment variables

# Function to generate summary using GPT model
def generate_summary(description):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Or "gpt-4" if you're using GPT-4
            prompt=f"Summarize the following course description:\n\n{description}",
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return "Error generating summary"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Error generating summary"

# Function to summarize all courses
def summarize_courses():
    try:
        # Load the courses from the CSV file
        df = pd.read_csv('courses.csv')

        summaries = []
        for _, row in df.iterrows():
            description = row['description']
            summary = generate_summary(description)
            summaries.append(summary)

        # Add summaries to the dataframe
        df['summary'] = summaries

        # Save the updated CSV with summaries
        df.to_csv('courses_with_summaries.csv', index=False)
        print("Summarization complete. Data saved to 'courses_with_summaries.csv'.")
        return df
    except FileNotFoundError:
        print("Error: 'courses.csv' not found. Please ensure the file is in the correct directory.")
    except Exception as e:
        print(f"An error occurred while summarizing courses: {e}")

if __name__ == "__main__":
    summarize_courses()
