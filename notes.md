## 2025-09-11

- Proj log should be mainly about organizing and tracking time
- Prompts have history with development details
- Plan has definition of tasks
- Talk with ai to guide tactic and strategy
- Define 3 task and switch beetween if that speeds up stuff
- Plan architecture ahead so that SOLID is uphold and after new features refactoring is reduced
---
Ideas:
- Drink counting app
- App about testing game math
- App about testing libs
- Game about learning driving
- Building game
- Garden game

## 2025-09-14

Changes needed in tools, paths:
- There is a problem, when i copy path of a class in VSCode it has \ and that dosent work in json.
- My fix is to use script fix_path that changes \ to /
- Problem, this is to many clicks
---
New fix:
- I may use script to write all paths of project to md file
- Need to update it to ignore dist, .git and node_modules and other files
- Better is just to take src and .ts files
---
Alternative:
- Next step would be to allow prompt script to take file name in project and resolve its path
- But this means new system of handling paths
