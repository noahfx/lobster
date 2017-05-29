# lobster -- Divide audio files into tracks with a single command
Sometimes we have found an amazing album but it is not divided in a proper way, just a big long song...
with lobster you can retrieve the long audio file (local or download audio from Youtube video) and divide
it into mp3 files and store them into their album directory just with one simple command:

```
~$ lobster --artist="Samsara Blues Experiment" --album="Long Distance Trip" --tracks=/tmp/tracks \ 
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

## Usage

```
~$ lobster -h
usage: lobster [-h] --artist ARTIST --album ALBUM --tracks TRACKS --source
               {local,youtube} --input INPUT --output OUTPUT [--format FORMAT]

Cut audio files with a single command

optional arguments:
  -h, --help            show this help message and exit
  --artist ARTIST, -ar ARTIST
                        Name of the artist of the track this will be used to
                        name the output directory
  --album ALBUM, -al ALBUM
                        Name of the album, this will be used to name the
                        output directory
  --tracks TRACKS, -t TRACKS
                        File containing the information to build the tracks
  --source {local,youtube}, -s {local,youtube}
                        Name of the media file source
  --input INPUT, -i INPUT
                        Path to the source media file
  --output OUTPUT, -o OUTPUT
                        Path to the utput directory
  --format FORMAT       Input media file format
  ``` 

You can install the lobster via the package manager:

```
~$ sudo pip install lobster 
```
