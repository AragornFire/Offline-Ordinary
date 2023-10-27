# Offline-Ordinary
So far, there is one ordinary, 'majorOrdinary.txt', and one search file, 'search.py'.

'majorOrdinary' compiles blazons from several armorials (more to be added, ideally every armorial) in the following format:
CODECODE - blazon - First Last - Source Note

The code is a string of eight characters in base 64, that is: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
The first two characters of these codes encode the tradition, such as: EN for English, SC for Scottish, FR for French, ES for Spanish, PO for Portuguese, etc.
The remaining six characters are used for each armiger.

Blazons are always lowercase and are standardized by a style sheet currently not completed. This is to allow people who wish to search for a particular blazon to find it by knowing the to-be-made style sheet and inferring what they ought to search from it. These are exclusively of the shield.

The names are currently the trickiest to standardize, especially with earlier armigers, where the spelling is not standardized. The best attempt is made, however, like several 'Guillaume's in early English rolls having their names changed to 'William'.

The source is the most common name for the armorial from which the blazon is sourced. Blazons are ordered in the file by tradition, then by source, then by position within the source.

Notes are little symbols placed at the end of the entry to point out something unique about the blazon. So far, there is *, which indicated the blazon cannot be standardized, ?, which means there is likely something wrong with the entry, and !, which means the entry must be revisited (!!!!! means the entry essentially cannot work because of a major flaw, like a half-finished blazon).

'search.py' is split into four sections, variable declaration, function declaration, main, and comments. It uses the termcolor library to color the output.

Variable declaration holds the name of the current ordinary and the colors used by the functions to color the output for aesthetics.

Function declaration holds the functions searchOrdinary(search_list) (which does a standard search through the file, outputting every line that contains every element in search_list), searchOrdinaryExcl(include_list,exclude_list) (which prints every line containing all elements of include list and none from exclude_list), help() (which gives a small rundown on all commands), ask(command) (which prints an explanation of the given command), setOrdinary(new_file) (which sets the current ordinary to new_file), changeColors(codec,blazonc,namec,sourcec) (which changes the colors of the output text based on the input), and begin() (which prints the introductory text).

Main just contains a call to begin().

Comments contains notes on how to write entries in 'majorOrdinary.txt'.
