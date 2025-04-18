import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

async def connect():
    global conn
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASS, database=DB_NAME, host=DB_HOST)


async def get_courses_id(c_id):
    courses = await conn.fetch('SELECT * FROM centre_course WHERE category_id = $1', c_id)

    return courses

async def get_category():
    return await conn.fetch('SELECT * FROM centre_category')

async def get_courses():
    return await conn.fetch('SELECT * FROM centre_course')

async def get_lessons_id(course_id):
    lessons = await conn.fetch('SELECT * FROM centre_lesson WHERE course_id = $1', course_id)

    return lessons

