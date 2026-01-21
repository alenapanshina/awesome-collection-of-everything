# AI-Powered Goals System (2026 Template)

A markdown-based system for managing life, career, and projects with the help of LLMs (Claude, ChatGPT, Cursor).

## 🚀 Getting Started

### 1. The Philosophy
This system is designed for "Context-Aware AI". Instead of chatting with a blank slate, you provide the AI with a structured map of your life (`Vision_2026.md`) and specific deep-dive files for each project.

*   **Vision File** = The Map (What are we doing?)
*   **Project Files** = The Territory (How are we doing it?)
*   **Memory.md** = The Instructions (How should the AI behave?)
*   **Databases** = The Tracker (What exactly needs to happen?)

### 2. Setup Guide

#### Step 1: Initialize Databases
Run the setup scripts to create your empty `goals.db` and `calendar.db`:
```bash
python3 init_goals_db.py
python3 init_calendar_db.py
```

#### Step 2: Define Your Vision
Open `Vision_2026.md`. This is your master list.
- Replace "Category 1" with your actual areas (e.g., "Financial", "Health").
- List your active projects.
- **Link them:** Use relative paths like `[My Project](One-off projects/my-project.md)`.

#### Step 3: Create Goal Files
For each project in your Vision, you need a corresponding markdown file.
1.  Go to `frameworks/project_template.md`.
2.  **Copy** its content.
3.  **Create a new file** in the appropriate folder (e.g., `Pillars/health.md`).
4.  **Paste** the template and fill in the "Strategy", "WOOP", and "Sprint" sections.

#### Step 4: Start Your First Session
Open your AI assistant (Cursor or Claude Project) and send this prompt:

> "Read `Memory.md` and `Vision_2026.md`. I want to plan my week. What do you see as my main priorities?"

---

## 📂 Folder Structure

- **`goals.db` / `calendar.db`**: SQLite databases for task and event tracking.
- **`One-off projects/`**: Projects with a deadline (e.g., "Launch Website", "Buy House").
- **`Pillars/`**: Ongoing systems (e.g., "Health", "Business", "Family").
- **`Side quests/`**: Fun, hobbies, travel, and wishlist items.
- **`frameworks/`**: Educational resources on goal setting (WOOP, Learning Goals).

---

## 🤖 How the AI Uses This

This system includes a `Memory.md` file. This is **system instructions** for the AI. It tells the AI to:
1.  Act as an Executive Coach.
2.  Prioritize ruthlessly (Health > Business > Fun).
3.  Check your specific goal files before giving advice.
4.  **Use the databases** (`goals.db`, `calendar.db`) as the source of truth for tasks.

**Pro Tip:** If you use **Cursor** or **Claude Projects**, you can add `Memory.md` to the "Project Instructions" or "System Prompt" area so it's always active.
