# Project History

This is a 'proj-log' repository.  
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
                              # single string with sum of time (e.g. "1h10m", "30m")
```

Drawbacks: To much mannual editing of text files

## Stage 2

Goal should be to automate this loging so its fast convineinet and one likes to use it. 

### Cli tool to help with loging

File format:

```md
# project-name

## Session yyyy-mm-dd hh:mm - hh:mm xh ym

- some note
- some note
- some note
```

Requirements:

- Ask for project name
- Check path C:/Atari-Monk-Art/proj-log/, if file project-name.md exists
- If file needs to be generated, add header '# project-name\n'
- When flag -start is given append '## Session yyyy-mm-dd hh:mm'
- When flag -note is given append note
- When flag -state is given print last session content or given number of them
- When flag -end is given find last record and append - hh:mm xh ym (calculate duration)

---

#### CLI Usage

## Start Session:

```sh
proj_log project-name -start
```

## Add Session Note:

```sh
proj_log project-name -note "bla bla"
```

## End Session: 

```sh
proj_log project-name -end
```
