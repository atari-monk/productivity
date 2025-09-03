# zippy-game-engine

## Session 2025-07-22 3h 20m

- Project structure
- Initial setup, vite ts with pnpm
- Converted day-game\dev-tool game-engine code to typescript
- Tested on cross lines scene
- Published npm package
- Cloned Scenelet project and named it as zippy-test
- Linked local pnpm package, with file:../zippy

## Session 2025-08-01 4h 0m

- zippy-shared-lib
- Lib project with shared types
- Initialized project
- config - types in exports prop required
- Published to npm
- Installed 'zippy-shared-lib' to 'zippy'

## Session 2025-08-02 2h 50m

- Optimizing zippy-shared-lib with maintanace prompts
- Zippy-test is a page to test component integration
- zippy-shared-lib, fullscreen-canvas-vanilla, zippy-game-engine
- This is needed to run any project with zippy-game-engine

## Session 2025-08-03 1h 40m

- zippy-shared-lib
- Fix bugs form AI
- Scripts to support prompts generation

## Session 2025-08-04 7h 20m

- zippy-shared-lib
- Cli commands with args for prompt generation
- Refactored prompt script to use file for text data
- Refactoring with maintenance prompt, to point where code is not getting better
- Refactoring with SOLID checker prompt, went from 2 files to 20
- Script with 9 maintanace prompts

## Session 2025-08-05 4h 0m

- zippy-shared-lib
- Made code compile
- Script tool for prompting
- Refactoring with 9 prompts
- Removed 95 % of lib after realizing it was pointless wrappers on browser utils
- zippy
- Update after removed 95% of shared lib

## Session 2025-08-06 1h 50m

- zippy-shared-lib
- Rewiewing, i see, i pretty much wasted 16 hours. I am not sure why this happened. After 3 project with simple game engine, i wanted to optimize them with prompts, document what it is. I had 2 components, canvas and engine. I comunicated them with interface in shared lib. Extracted two shared classes. I was optimizing them with prompts. Events are handled in components, so no need for centralizing it. Wrappers over browser api is just pointless and insane. Classes were removed. I guess i was procrastinating and wanted prompt automation to much. Only thing out of this is scripts for prompting, but it may turn out to be not that usefull. This gives me thouth that a lot of time, best code is removed one. Need clear, measured goals.
- Prepare stable version
- Documentation,
- Fix git history (reset history, 'Initial commit')
- Publish npm package

## Session 2025-08-07 0h 30m

- Fix this file to comply with new format

## Session 2025-08-08 1h 10m

- Documentation with refactoring

## Session 2025-08-09 3h 10m

- Documentation with refactoring

## Session 2025-08-10 2h 0m

- Documentation with refactoring

## Session 2025-08-11 1h 0m

- Documentation with refactoring

## Session 2025-08-12 4h 0m

- Zippy-test
- Made it run after component have been changed
- There is some bug manifesting as weird behavior and crash
- Turned out canvas resizer was looping on itself
- This was imposible to debug in original project, becouse of minified libs that scramble code and make it unreadable
- Monorepo with clone of code of each component was created and build for development, this is better for debuging

## Session 2025-08-19 2h 30m

- Documentation
- Refactored script of producting documentation, its simple now
- Updated code documentation files
- Add usage doc

## Session 2025-08-20 2h 15m

- Documentation for config files
- Its quite hard to document configs and in a consistent way
- Merge zippy-test doc to this doc, no need for separete doc
- Also zippy-shared-lib dosent need to have separete doc, merging

## Session 2025-08-21 1h 0m

- Prepare documentation for zippy-shared-lib
