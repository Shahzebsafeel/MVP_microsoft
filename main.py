from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from pydantic import BaseModel

app = FastAPI()


app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

@app.get("/")
async def read_root():
    
    with open("frontend/build/index.html") as f:
        html_content = f.read()
        
        
        css_style = """
        <style>
            /* Basic Styles */
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
            }

            /* Main Container */
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                text-align: center;
            }

            /* Title */
            h1 {
                font-size: 3rem;
                color: #4CAF50;
                text-transform: uppercase;
                letter-spacing: 2px;
            }

            /* Form Styles */
            form {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 20px;
            }

            input[type="text"] {
                padding: 10px;
                margin-right: 10px;
                font-size: 1.2rem;
                border: 2px solid #ccc;
                border-radius: 5px;
                width: 300px;
            }

            button {
                padding: 10px 20px;
                font-size: 1.2rem;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            button:hover {
                background-color: #45a049;
            }

            /* Career Recommendation Styles */
            .recommendation {
                font-size: 1.5rem;
                margin-top: 20px;
                color: #555;
            }

            .recommendation strong {
                font-size: 1.7rem;
                color: #4CAF50;
            }
        </style>
        """
        
        
        html_content = html_content.replace('</head>', f'{css_style}\n</head>')
        
        return HTMLResponse(html_content)

career_data = {
    "AI": {"role": "Data Scientist", "skills": ["Python", "Machine Learning", "Data Analysis", "AI", "Deep Learning"]},
    "Web Development": {"role": "Frontend Developer", "skills": ["HTML", "CSS", "JavaScript", "React", "Vue"]},
    "Embedded Systems": {"role": "Embedded Systems Engineer", "skills": ["C", "Microcontrollers", "Embedded Software", "RTOS"]},
    "Mobile Development": {"role": "Mobile App Developer", "skills": ["Java", "Swift", "React Native", "Flutter"]},
    "Cloud Computing": {"role": "Cloud Solutions Architect", "skills": ["AWS", "Azure", "Google Cloud", "DevOps", "Terraform"]},
    "C++": {"role": "C++ Developer", "skills": ["C++", "Algorithms", "Data Structures", "Multithreading"]},
    "Java": {"role": "Java Developer", "skills": ["Java", "Spring Framework", "JPA", "Hibernate"]},
    "Excel": {"role": "Data Analyst", "skills": ["Excel", "Data Visualization", "Pivot Tables", "Data Cleaning"]},
    "Power BI": {"role": "Power BI Developer", "skills": ["Power BI", "DAX", "Power Query", "Data Modeling"]},
    "MySQL": {"role": "Database Administrator", "skills": ["MySQL", "SQL", "Database Design", "Indexing", "Normalization"]},
}

class UserInput(BaseModel):
    skill: str

@app.post("/recommend")
def recommend_career(user_input: UserInput):
    
    recommendations = []
    
    for field, data in career_data.items():
        if user_input.skill.lower() in ', '.join(data['skills']).lower():
            recommendations.append(f"Consider becoming a {data['role']}! You should focus on learning: {', '.join(data['skills'])}")
    
    if recommendations:
        return {"recommendation": recommendations}
    else:
        return {"recommendation": "No career match found for this skill, try a different one!"}
