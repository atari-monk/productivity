Write ps1 script to convert big file witch part looks like:

```md
# assets

## Session 2025-07-20 11:16 - 12:16 1h 0m

- Categorized assets in folder

# blender

## Session 2025-09-13 13:20 - 14:13 0h 53m

- Wood storage

# command-box

## Session 2025-08-11 15:33 - 16:48 1h 15m

- Added posts in dev-blog
- Setup project

## Session 2025-08-15 10:36 - 13:16 2h 40m

- It kind of works but i bite on to much that i can chew, ai creeping features in
- Need to only do command object first and then add relation with tag, not both at once
- Fixed MVP doc so it should be doable with no problems now
- App from mvp doc worked, but needs one more run to make it faster
```

To this kind of format

```txt
2025-07-20 09:00 assets
Categorized assets in folder
2025-07-20 10:00
2025-09-13 13:20 blender
Script generating building materials model
2025-09-13 14:13
```
