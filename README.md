# lobster -- Divide audio files into tracks with a single command
Sometimes we have found an amazing album but it is not divided in a proper way, just a big long song...
with lobster you can retrieve the long audio file (local or download audio from Youtube video) and divide
it into mp3 files and store them into their album directory just with one simple command:

```
$ lobster --artist="Samsara Blues Experiment" --album="Long Distance Trip" --tracks=/tmp/tracks \ 
           --source=youtube --input=https://www.youtube.com/watch?v=6vpOHq8bkzA --output=/tmp/
```
Maybe you are wondering where did you specify where to divide the track, all magic happens in the file which 
we send as parameter to the ```--tracks``` argument.
The file ```/tmp/tracks``` looks as follows:
```
Singata Mystic Queen|00:00
Army of Ignorance|11:37
For the Lost Souls|16:12
Center of the Sun|26:11
Wheel of Life|39:18
Double Freedom|43:47

```

You can find an example file under the examples directory.

You can install the lobster via the package manager:

```
$ sudo pip install lobster 
```
