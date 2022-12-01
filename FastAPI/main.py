from fastapi import FastAPI

app = FastAPI()
course_items = [{"course_name": "Python"}, {"course_name": "NodeJS"}, {"course_name": "Machine Learning"}]

@app.get("/courses/")
def read_courses(start: int = 0, end: int = 10):
    return course_items[start : start + end]