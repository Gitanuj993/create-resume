# create-resume


## Components of the projects
1. resume generation
2. authentication
3. database storage




## L1 : Architecture

1. Client submit data : form fills or uploaded file
2. resume generation : file templates , render in  memory
3. return pdf


### . Client submits data

- Structured form data (name, experience, education, skills as JSON) 
- Uploaded file (existing resume/story draft to reformat or rewrite) 

### Backend generates PDF

- Jinja2 to fill an HTML template with the submitted data.
- WeasyPrint (pure Python, easiest to set up) or wkhtmltopdf to convert that HTML/CSS into a PDF.
- Generate the PDF in memory (BytesIO) rather than writing to disk — nothing to clean up afterward, and it's naturally stateless


## File Structure

```txt
resume-backend/
├── main.py              # FastAPI app — the /generate-resume endpoint
├── models.py            # Pydantic schema (ResumeData, Experience, Education)
├── requirements.txt     # Dependencies (fastapi, uvicorn, jinja2, weasyprint, pydantic)
├── sample_request.json  # Example payload for testing
├── README.md            # Setup and run instructions
└── templates/
    └── resume.html      # HTML/CSS layout that gets rendered to PDF```


## Sample Request

```txt
{
  "full_name": "Aarav Sharma",
  "email": "aarav.sharma@example.com",
  "phone": "+91 98765 43210",
  "location": "Indore, India",
  "linkedin": "linkedin.com/in/aaravsharma",
  "summary": "Backend developer focused on Python, building scalable APIs and data pipelines.",
  "skills": ["Python", "FastAPI", "PostgreSQL", "Docker", "REST APIs"],
  "experience": [
    {
      "title": "Backend Developer Intern",
      "company": "TechNova Solutions",
      "location": "Remote",
      "start_date": "Jun 2025",
      "end_date": "Aug 2025",
      "current": false,
      "bullets": [
        "Built REST APIs in FastAPI serving 10k+ daily requests",
        "Reduced query latency by 40% through index optimization"
      ]
    }
  ],
  "education": [
    {
      "degree": "B.Tech in Computer Science",
      "institution": "SGSITS Indore",
      "graduation_date": "2026",
      "gpa": "8.4/10"
    }
  ]
}
```

