from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Setting up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Sample data for profiles
profiles = [
    {
        "name": "John Doe",
        "position": "CEO",
        "email": "john.doe@example.com",
        "about": "John is the CEO of the company with over 20 years of experience in the industry."
    },
    {
        "name": "Jane Smith",
        "position": "CTO",
        "email": "jane.smith@example.com",
        "about": "Jane is the CTO, leading our technology department with innovative solutions."
    },
    {
        "name": "Emily Johnson",
        "position": "CFO",
        "email": "emily.johnson@example.com",
        "about": "Emily is the CFO, managing the company's finances with precision and care."
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/profiles", response_class=HTMLResponse)
async def read_profiles(request: Request, q: str = Query("", alias="q")):
    filtered_profiles = [profile for profile in profiles if
        q.lower() in profile["name"].lower() or
        q.lower() in profile["position"].lower() or
        q.lower() in profile["email"].lower() or
        q.lower() in profile["about"].lower()
    ]
    return templates.TemplateResponse("profiles.html", {"request": request, "profiles": filtered_profiles, "query": q})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
