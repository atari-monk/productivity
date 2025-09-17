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

## Session 2025-09-05 16:24 - 16:47 0h 23m

- Single Scene Test for Menu scene

## Session 2025-09-05 19:34 - 20:25 0h 51m

- Test of transition form menu to game

## Session 2025-09-05 21:54 - 23:19 1h 25m

- Test for Game Score scene

## Session 2025-09-06 21:51 - 23:09 1h 18m

- Game Factory
- Started, menu and transition to game scenes

## Session 2025-09-07 13:23 - 14:57 1h 34m

- Builder now has inerfaces and validation to set objects relations

## Session 2025-09-07 16:50 - 17:33 0h 43m

- Extend game builder with scenes

## Session 2025-09-07 18:23 - 18:34 0h 11m

- Builder for Countdown

## Session 2025-09-07 18:41 - 18:55 0h 14m

- Builder for LapTracker

## Session 2025-09-07 20:34 - 20:54 0h 20m

- Builder for ContinueBtn

## Session 2025-09-07 22:17 - 22:46 0h 29m

- Builder for GameScore

## Session 2025-09-08 10:39 - 13:38 2h 59m

- Reposition score
- Mark last time in score with red color
- Sound Scene
- Car sprite

## Session 2025-09-08 15:40 - 16:05 0h 25m

- Car sprite rendering

## Session 2025-09-08 17:19 - 18:46 1h 27m

- Sound for car
- Engine

## Session 2025-09-08 20:00 - 20:20 0h 20m

- Car horn sound

## Session 2025-09-08 21:04 - 22:14 1h 10m

- Car crash sound

## Session 2025-09-09 06:56 - 07:02 0h 6m

- Road markings

## Session 2025-09-09 07:05 - 09:03 1h 58m

- Design prompts by prompts

## Session 2025-09-09 09:50 - 11:28 1h 38m

- Implemented configurable lap count

## Session 2025-09-09 11:57 - 12:21 0h 24m

- Fixed Starting Grid

## Session 2025-09-09 12:36 - 14:26 1h 50m

- Reset car when 3s off track

## Session 2025-09-09 15:01 - 15:22 0h 21m

- Toogle Countdown overlay
- Toogle Continue overlay

## Session 2025-09-09 15:28 - 15:49 0h 21m

- TrackBoundary with flags, to use track or track with margins as track border

## Session 2025-09-09 15:53 - 16:08 0h 15m

- Fix road markings

## Session 2025-09-09 16:08 - 16:17 0h 9m

- Sectors of last lap visible in tracker

## Session 2025-09-09 16:20 - 16:29 0h 9m

- Fixed skid sound

## Session 2025-09-09 16:30 - 16:48 0h 18m

- Car dosent turn when not moving

## Session 2025-09-09 16:49 - 17:52 1h 3m

- Block keys off track

## Session 2025-09-09 17:55 - 18:28 0h 33m

- Fix start corss left right to win bug
- Playable car

## Session 2025-09-09 18:29 - 18:49 0h 20m

- Alternative player

## Session 2025-09-09 23:13 - 23:34 0h 21m

- Pondering refactor

## Session 2025-09-10 10:48 - 10:55 0h 7m

- Rename of ArrowPlayer
- Script dosent work for this

## Session 2025-09-10 13:38 - 15:07 1h 29m

- Refactoring Car
- Refactored Car configs to load form json

## Session 2025-09-10 16:30 - 18:51 2h 21m

- Extracted systems from car, Async factories and builders, Move car config loading out of ctor

## Session 2025-09-10 21:49 - 23:31 1h 42m

- Remove async from car ctor

## Session 2025-09-11 11:08 - 12:31 1h 23m

- Drafted 3 tasks (11:32)
- Part of first task done (12:26)

## Session 2025-09-11 13:16 - 13:57 0h 41m

- second part of first task done (13:39)
- third, last part of refactoring car task, time to switch

## Session 2025-09-11 14:36 - 15:14 0h 38m

- started next task, break for lunch (15:14)

## Session 2025-09-11 16:31 - 17:20 0h 49m

- Joystic single scene test

## Session 2025-09-11 18:31 - 20:04 1h 33m

- Joystic with car, controll test, still buggy

## Session 2025-09-11 21:12 - 21:57 0h 45m

- Joystic bug fix

## Session 2025-09-12 21:47 - 22:14 0h 27m

- XY joystic test

## Session 2025-09-13 11:11 - 12:14 1h 3m

- 2 joystick steer car

## Session 2025-09-13 14:56 - 16:13 1h 17m

- plan 3

## Session 2025-09-13 18:11 - 18:46 0h 35m

- plan 4

## Session 2025-09-13 20:01 - 20:11 0h 10m

- plan 5

## Session 2025-09-13 21:01 - 21:34 0h 33m

- plan 6

## Session 2025-09-13 23:05 - 00:25 1h 20m

- plan 7
- failed, touch is not easy, prepare simpler scene

## Session 2025-09-14 10:21 - 10:55 0h 34m

- prompt for plan 1, fail

## Session 2025-09-14 11:16 - 14:34 3h 18m

- it is quite hard to do anything, project got a bit bigger, time to refactor ?
- splited main to 2 clases (12:13)
- refactoring url params, moved functions, rename (12:53)
- refactored to new entity tester, it is setup to test scenes and groups of them, also games (selected groups) (14:34)

## Session 2025-09-14 16:57 - 18:53 1h 56m

- refactoring scene generation from 1 clas with ifs and new to classes with di

## Session 2025-09-14 21:00 - 23:00 2h

- refactoring tester setup, car and car factory stuff quite a lot

## Session 2025-09-15 10:12 - 11:08 0h 56m

- plan 1

## Session 2025-09-15 12:00 - 13:02 1h 2m

- plan 2
- some ai plan failed (12:45)
- next ai seems to fixed problem

## Session 2025-09-15 13:39 - 13:53 0h 14m

- plan 3

## Session 2025-09-15 13:56 - 14:15 0h 19m

- plan 4

## Session 2025-09-15 14:16 - 14:35 0h 19m

- plan 5

## Session 2025-09-15 15:00 - 15:42 0h 42m

- plan 6

## Session 2025-09-15 16:10 - 17:16 1h 6m

- plan 7-11

## Session 2025-09-15 17:48 - 19:58 2h 10m

- plan 12, car sound exception removed, sounds states are a big problem, need extensive debug and refactor

## Session 2025-09-15 22:05 - 23:18 1h 13m

- plan 13

## Session 2025-09-16 13:04 - 15:23 2h 19m

- plan 1, 2

## Session 2025-09-16 16:30 - 17:30 1h

- plan 1, 2

## Session 2025-09-16 22:05 - 23:20 1h 15m

- plan 1, 2

## Session 2025-09-17 11:37 - 14:16 2h 39m

- plan 1

## Session 2025-09-17 16:46 - 17:18 0h 32m

- plan 2

## Session 2025-09-17 18:20 - 19:00 0h 40m

- plan 3