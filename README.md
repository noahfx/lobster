# lobster -- Split audio files into tracks with a single command
Sometimes we have found an amazing album but it is not splittedd in a proper way, just a big long song...
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

## Usage

But if you do not want to an input file or write all those arguments, There is
wizard mode for you, run lobster as Wizard and forgot about all the above syntax

```
$ lobster -m wizard

<lobster>  (\/) (°,,,°) (\/) -- woop woop woop
<lobster>  Enter artist name: Gorilla Pulp  
<lobster>  Enter album name: Heavy Lips
<lobster>  Enter the source y=Youtube|l=local: [Y/l]
<lobster>  Enter Video URL: https://www.youtube.com/watch?v=W1vY6qVTqkM
<lobster>  Enter the destination directory: /tmp
<lobster>  Enter Number of tracks: 8
<lobster>  Enter Track Number 1 Name: Bless The Moon
<lobster>  Enter Time where Track 1 starts: (e.g: 04:20) 00:00
<lobster>  Enter Track Number 2 Name: In your waters
<lobster>  Enter Time where Track 2 starts: (e.g: 04:20) 04:34
<lobster>  Enter Track Number 3 Name: The Witches Twirl
<lobster>  Enter Time where Track 3 starts: (e.g: 04:20) 8:07
<lobster>  Enter Track Number 4 Name: Heavy Lips
<lobster>  Enter Time where Track 4 starts: (e.g: 04:20) 12:04
<lobster>  Enter Track Number 5 Name: Cactus Killer
<lobster>  Enter Time where Track 5 starts: (e.g: 04:20) 18:14
<lobster>  Enter Track Number 6 Name: Prey On Your Mind
<lobster>  Enter Time where Track 6 starts: (e.g: 04:20) 22:37
<lobster>  Enter Track Number 7 Name: The Low Song
<lobster>  Enter Time where Track 7 starts: (e.g: 04:20) 27:18
<lobster>  Enter Track Number 8 Name: Ape Eyes
<lobster>  Enter Time where Track 8 starts: (e.g: 04:20) 32:48
<lobster>
 information:
 artist: Gorilla Pulp
 album: Heavy Lips
 source: youtube
 input: https://www.youtube.com/watch?v=W1vY6qVTqkM
 output: /tmp
 name: Bless The Moon poisition: 1
 initial time: 00:00

---------------
 name: In your waters
 poisition: 2
 initial time: 04:34

---------------
 name: The Witches Twirl 
 poisition: 3 
 initial time: 8:07 
 
---------------
 name: Heavy Lips 
 poisition: 4 
 initial time: 12:04 
 
---------------
 name: Cactus Killer 
 poisition: 5 
 initial time: 18:14 
 
---------------
 name: Prey On Your Mind 
 poisition: 6 
 initial time: 22:37 
 
---------------
 name: The Low Song 
 poisition: 7 
 initial time: 27:18 
 
---------------
 name: Ape Eyes 
 poisition: 8 
 initial time: 32:48 
 
---------------

Is the above information correct: [Y/n]


```

## Usage for Nerds

```
$ lobster -h
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
  --mode MODE, -m MODE  Launch Lobster in Wizard or Command mode,`wizard` will
                        launch the Wizard mode, `cmd` will lauch Command mode,
                        `cmd` is the current default
  ```

You can install the lobster via the package manager:

```
$ sudo pip install lobster 
```
