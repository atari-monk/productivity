# This is a 'productivity' support repository.

The point is to measure projects development with logs.

---

## **Project Structure**

```bash
/productivity
 ├─ content/               # Folder with project logs
 └─ README.md              # This Project Manifesto ✨
```

This should stay intentionally simple, only in text form.  
Each project has its file `project-name.yaml`.

---

## Log Format

Example:

```yaml
logs:
  "2025-07-29":
    - Feature: Project setup
      Task:
        - Fixed blog scripts to categorize and order dev notes
      Time:
        - "1h48m"
        - "1h22m"

  "2025-07-30":
    - Task:
        - Improved test coverage on utility functions
      Time: "45m"
```

Schema:

```yaml
logs:
  "YYYY-MM-DD":
    - Feature: <string>         # Optional
      Task:
        - <string>              # Required list of task descriptions
      Time:                     # Required duration(s)
        - "<duration>"          # List or single string (e.g. "1h", "30m")
```

---