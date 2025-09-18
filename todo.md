Write ps1 script to convert big file witch snippet looks like:

```md
# assets

## Session 2025-07-20 1h 0m

- Categorized assets in folder

# blender

## Session 2025-09-13 13:20 - 14:13 0h 53m

- Script generating building materials model
```

To this

```txt
2025-07-20 09:00 assets
Categorized assets in folder
2025-07-20 10:00
2025-09-13 13:20 blender
Script generating building materials model
2025-09-13 14:13
```

So where there is only duration we must convert it to time based notation

Make it chronological (md is not)
I dont trust regex, can it be done without it ?