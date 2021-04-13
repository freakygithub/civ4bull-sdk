# civ4bull-sdk
Originally forked from dguenms/beyond-the-sword-sdk

Adding BULL assets on top and merging the makefiles

Setup directions can be found on this thread: https://forums.civfanatics.com/threads/the-easiest-way-to-compile-a-new-dll.608137/

# Custom Combat
- Gives the player more options to customize the game how they think it should be
- Built on top of BUG+BULL and compatible with BAT so you don't miss out on their features, and can add it to your own BULL-based mod


## Installation
- Install BUG+BULL
- Download the code repo as a zip file - https://github.com/freakygithub/civ4bull-sdk/tree/civ4-custom-combat-master
- Backup the things from these next steps as you go... just in case
- Replace BULL's CvGameCoreDLL.dll (wherever you have it installed) with CvGameCoreDLL.dll from the zip file 
  - For BAT, the DLL is in My Games\beyond the sword\MODS\BAT Mod 4.1\Assets\
- Copy CustomAssets from the zip to your CustomAssets folder (for me, ...My Games\beyond the sword\CustomAssets)
  - For BAT, copy to My Games\beyond the sword\MODS\BAT Mod 4.1\Assets
- Copy BugUserSettings from the zip to Bug's UserSettings folder (for me, ...My Games\beyond the sword\BUG Mod\UserSettings)
  - For BAT, copy to \My Games\beyond the sword\MODS\BAT Mod 4.1\Assets\Config
- Open Civ4 and start a game
- Open BUG menu (ctrl+shift+O) and play around with new settings :) You might have to re-update these when you load a game (for now), but with less RNG, you should need fewer reloads anyway.

## Current Custom Combat Features
- Maximum combat round limit (Allows combat to be less lethal)
- Global combat damage multiplier (makes results more consistent)
- Remove metal requirement for metal-based units
- Adjustable bonus damage promotion to melee units for having access to copper/iron (e.g. +20% strength for copper and +40% for iron) 
  - If you change the damage bonuses mid-game, it will only affect newly built units
## Future Custom Combat Goals
- Stack limit size
- Siege units ignore defender retaliation (boolean)
  - Exception for other siege units (boolean)
  - Siege collateral damage has a chance to miss each unit
- Land units can beseige/blockage tiles around a city
  - Adjust land siege radius
