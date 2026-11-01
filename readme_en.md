# Wish simulator for Honkai: Star Rail
Simulator for Honkai: Star Rail for a numerous amount of pulls. Translated into Russian and English, works for HSR version 2.4+ (Moze release).

## How it works

### 1. Decide whether you want to track certain characters
Application can track certain four-stars' constellations. You can choose three characters from the list on chosen language, that you can get when inputting `0` into name field. Other characters will mark as non-banner and will have separate chances for drop. Constellations are written into file `4starconstellations.txt` and set as 0. This can be modified manually. Selection is accessed if `1` is entered on respective input and after 5-star constellation input.

### 2. Enter configuration
Enter amount of pulls you have, pity for 4 and 5 star, constellations for 5 star characters, names of certain banner 4-stars (if you have chosen to track them) and constellations for them, available pulls in shop for stardust, and available stardust and starglitter on the start of simulation. If incorrect data is provided, respective parameter is set on default (absence for characters and `0` for all other parameters).

### 3. See the result
After simulation certain information is visible:
1. Amount of pulls w/ converted starglitter and stardust
2. 4 and 5 star pity
3. Constellations for 4 and 5 star
4. Total earned starglitter and stardust
5. How many additional pulls are bought via starglitter and stardust
6. List of constellations for non-banner 4-stars

## Changing settings
Program relies on `.txt` files with all the information, that are located in `data` folder. Via these files language and starting constellations for 4-star can be changed. **NOTICE:** files, that are responsible for constellations and names 4-star characters, **must** have 22 lines in them. Removing or adding additional lines may result in an incorrect simulation. If you want to set a starting constellation for a non-banner 4-star, find the line number where its name is written and replace the constellation number with respective line number.