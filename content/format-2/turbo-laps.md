# turbo-laps

## Session 2025-08-21 0h 40m

- Setup project turbo-laps-scenelet (turbo-laps scenes to test features in isolation)
- Used zippy libs
- Added scenes
- Tested locally

## Session 2025-08-22 4h 30m

- Setup project turbo-laps-js (this was before zippy lisbs, version with js code that works somewhat, starting point for prototyping game)
- Generated project 'vite-typescript-template' to speed up setup of this kinf of project
- Setup folder turbo-laps, made it run
- Setup project turbo-lap (full ts game project)
- Prepared elipse and rounded rectangle track scene
- Prepared arrow player scene (used engine input system)
- Extend engine to handle multiple scenes

## Session 2025-08-23 1h 15m

- Removed old logs from fullscreen-canvas-vanilla and zippy-game-engine
- Scene System mode in turbo-laps-scenelet (engine runs one scene or list of scenes)

## Session 2025-08-24 2h 10m

- Added starting-grid scene to turbo-laps-scenelet proj
- Added 2 prompts for next 2 parts
- Failed with track boundary

## Session 2025-08-25 4h 0m

- Prepared prompting proj for coding in this project
- Set up 4 desktops, project, prompting, ai/cli, productivity, go back to 1
- Add track boundary scene
- Position car in starting grid (15m)
- Add road markings scene (25m)
- Add track grass scene (20m)
- Add lap tracker (35m)

## Session 2025-08-26 3h 0m

- Add game score scene (25m)
- Tweak size of track (10m)
- Stop lap tracker and provide interface to start/stop/reset it (40m)
- Menu Scene with title Turbo Laps, 5-Lap Time Trial, description, Start button
- Make Start button switch scene mode to all (1h)

## Session 2025-08-27 4h 0m

- Prompt for new scene - countdown (30m)
- Copy main and scenes form turbo-laps-scenelet to turbo-laps, turn main into game (15m)
- Make turbo-laps-scenelet only about testing single scene and multi scenes for testing feature (55m)
- Implement prompt (20m)
- Test and fix scene (15m)
- Initially turn off car input, turn on after Go - Prompt and implementation in scenelet and game (35m)
- Stop lap tracker when race is over, reset car on starting position (1h10m)

## Session 2025-08-28 4h 50m

- Scene with a canvas rendered button, to restart race (40m)
- Refactor turbo-laps-scenelet, move factory/register functions out of main, scene factory (50m)
- Prompt to refacotr factory and main properly (50m)
- Refactored main to using url params for selection and factory for scene generation/registration (60m)
- Fix factory to create independant instances for tests, integrate continue scene to multi scene test (90m)

## Session 2025-08-29 5h 35m

- Fixed restarting race in test (25m)
- Fixed bug in registerMultiScene (15m)
- Refactor prompting again, remove md, ps1 pairs (to clumsy to use) and define prompts in single ps1 per project file, prompt data model and nice execution helpers (140m)
- Fix sectors in lap tracker (15m)
- Fix prompts and scripts for tools in prompting proj (15m)
- Fix Countdown prompting scripts (10m)
- Countdown should turn on car input on GO, not after GO (20m)
- Run all tests and fix configs and some callbacks (95m)

## Session 2025-08-30 4h 45m

- Copy scenes form scenelet to game (10m)
- Refactor prompting proj, archive old version, prompt model 0.0.1 (2h50m)
- Refactor scene-factory (1h45m)

## Session 2025-08-31 6h 50m

- Thinkig what to do with yt in background (1h)
- Test ElipseTrack, RectangleTrack scene, in isolation as single scene (20m)
- Test ArrowPlayer scene, in isolation as single scene (10m)
- Test TrackBoundary scene, in isolation as single scene (50m)
- Test StartingGrid, in isolation as single scene (30m)
- TrackConfigService singleton extracted and used in scenes (6 scenes) (4h)

## Session 2025-09-01 1h 25m

- Refactor TrackGrass scene to use track config service and test it as single scene in isolation (15m)
- Refactor LapTracker to test it with no dependencies on other scenes (55m)
- Mouse Currsor scene, click to get mouse pos (15m)

## Session 2025-09-02 1h 15m

- Functional multiSceneFactory (25m)
- Add rendering points to Mouse Currsor scene 
- Prompts written (25m) 
- Better prompt system hepled to implement (25m)

## Session 2025-09-04 10:05 - 11:20 1h 15m

- Scene instance factory
- Ai said its nice 3 SOLID factories
- Instance, single scene test, multi scene test, factories

## Session 2025-09-04 13:22 - 13:49 0h 27m

- Refactor next multi scene test

## Session 2025-09-04 13:59 - 14:20 0h 21m

- Refactor next multi scene test

## Session 2025-09-04 16:18 - 17:12 0h 54m

- Refactor next multi scene test
- Acctually 2 done