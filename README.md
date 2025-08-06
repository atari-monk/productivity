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

example:

```yaml
logs:
  "2025-07-24":
    - Feature: Test Toogle Button component
      Task:
        - Splitting wood before this, teached me a lesson
        - Separate pickaroo test project
        - Test for toogle button
      Agent: Human, LLM Chat
      Start: "13:44"
      Stop: "14:57"
```

scheme:

```yaml
logs:
  "2025-07-29":
    - Feature:
      Task:
        - 
      Agent: Human, LLM Chat
      Start: ""
      Stop: null
```

### ✅ **Multiple Sessions (Time Ranges as List)**

example:

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

scheme:

```yaml
logs:
  "2025-07-29":
    - Feature:
      Task:
        - 
      Agent: Human, LLM Chat
      Sessions:
        - Start: ""
          Stop: null
```
