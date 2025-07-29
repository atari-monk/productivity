# This is a 'productivity' support repository.

The point is to measure projects development with logs.

## **Project Structure**

```bash
/productivity
 ├─ content/               # Folder with project logs
 └─ README.md              # This Project Manifesto ✨
```

This should stay intentionally simple, only in text form.

## Log Format

### ✅ **Single Time Range (One Session)**

```yaml
logs:
  "2025-07-24":
    - Feature: Test Toogle Button component
      Task:
        - Splitting wood before this, teached me a lesson
        - Separate pickaroo test project
        - Test for toogle button
      Agent: Human and LLM Chat
      Start: "13:44"
      Stop: "14:57"
```

### ✅ **Multiple Sessions (Time Ranges as List)**

```yaml
logs:
  "2025-07-29":
    - Feature: Project setup
      Task:
        - Fixed blogs (scripts) to categorize and order dev notes
      Agent: Human, LLM Chat, Copilot
      Sessions:
        - Start: "09:50"
          Stop: "11:38"
        - Start: "12:51"
          Stop: null
```

## Git Commits

Minimal commit messages:
- `Initial setup`
- `Update`
- `Custom message`

Detailed history is intentionally not maintained.
