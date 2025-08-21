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
    - Task:
        - Fixed blog scripts to categorize and order dev notes
        - Published
      Time: "1h48m"
```

Schema:

```yaml
logs:
  "YYYY-MM-DD":
    - Task:
        - <string>            # Required list of task descriptions
      Time: "<duration>"      # Required duration(s)
                              # single string with sum of time (e.g. "1h", "30m")
```

---