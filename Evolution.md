# Productivity Project Evolution

This is a 'productivity' support repository.  
The point is to measure projects development with logs.

## Stage 1

Each project had its file.  

- project-name.yaml

```yaml
logs:
  "YYYY-MM-DD":
    - Task:
        - <string>            # Required list of task descriptions
      Time: "<duration>"      # Required duration(s)
                              # single string with sum of time (e.g. "1h", "30m")
```

Drawbacks: To much mannual editing of text files

## Stage 2

Goal should be to automate this loging so its fast convineinet and one likes to use it. 

### Cli tool to help with loging

File format:

```md
# project-name

## Session 2025-09-03 14:40 - 14:50 0h 10m

- some note
- some note
- some note
```

Requirements:

- I need new script in file C:\Atari-Monk-Art\productivity\scripts\log.py
- Ask for project name
- Check path C:/Atari-Monk-Art/productivity/content/format-2/ if file project-name.md exists
- If file needs to be generated add header '# project-name\n'
- When flag -start is given append '## Session yyyy-mm-dd hh:mm'
- When flag -note is given append note
- When flag -state is given print last session content or given number of them
- When flag -end is given find last record and append - hh:mm xh ym (calculate duration)

---

[Usage](log-usage.md)

### Conversion tool for format 1 -> 2

- I need new script in file C:\Atari-Monk-Art\productivity\scripts\convert.py
- Ask for project name
- Check path C:/Atari-Monk-Art/productivity/content/format-1/ if file project-name.yaml exists proceed else inform no file
- Convert file to format-2.md
- Save file as C:/Atari-Monk-Art/productivity/content/format-2/project-name.md