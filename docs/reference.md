# API Reference
*[< Index](index.md)*

# Table of Contents
*Note:* If clicking on these doesn't work, try using your browser's find 
feature. (usually `Ctrl-F` on Windows)

1. [`Client`](reference.md#class-Client)
2. [Base structures](reference.md#BASE-STRUCTURES)
3. [Submission classes](reference.md#SUBMISSION-CLASSES)
4. [Misc. classes](reference.md#MISC-CLASSES)

# *class* `Client`
Your "portal" to GameBanana. Implements multiple getter coroutines for different
types of submissions found on GameBanana. 

**IMPORTANT:** This is the only class you have to initialize by yourself, all
the other classes are created internally by the wrapper and are not meant to be
created by the user.

## *await* `Client.get_blog(id)`

### Arguments
`id` : `int` - ID of the blog to get.
### Returns
[`Blog`](reference.md#class-Blog) - The retrieved blog.

## *await* `Client.get_concept(id)`

### Arguments
`id` : `int` - ID of the concept to get.
### Returns
[`Concept`](reference.md#class-Concept) - The retrieved concept.

## *await* `Client.get_effect(id)`

### Arguments
`id` : `int` - ID of the effect to get.
### Returns
[`Effect`](reference.md#class-Effect) - The retrieved effect.

## *await* `Client.get_gamefile(id)`

### Arguments
`id` : `int` - ID of the gamefile to get.
### Returns
[`Gamefile`](reference.md#class-Gamefile) - The retrieved gamefile.

## *await* `Client.get_gui(id)`

### Arguments
`id` : `int` - ID of the GUI to get.
### Returns
[`GUI`](reference.md#class-GUI) - The retrieved GUI.

## *await* `Client.get_map(id)`

### Arguments
`id` : `int` - ID of the map to get.
### Returns
[`Map`](reference.md#class-Map) - The retrieved map.

## *await* `Client.get_prefab(id)`

### Arguments
`id` : `int` - ID of the prefab to get.
### Returns
[`Prefab`](reference.md#class-Prefab) - The retrieved prefab.

## *await* `Client.get_project(id)`

### Arguments
`id` : `int` - ID of the project to get.
### Returns
[`Project`](reference.md#class-Project) - The retrieved project.

## *await* `Client.get_question(id)`

### Arguments
`id` : `int` - ID of the question to get.
### Returns
[`Question`](reference.md#class-Question) - The retrieved question.

## *await* `Client.get_request(id)`

### Arguments
`id` : `int` - ID of the request to get.
### Returns
[`Request`](reference.md#class-Request) - The retrieved request.

## *await* `Client.get_script(id)`

### Arguments
`id` : `int` - ID of the script to get.
### Returns
[`Script`](reference.md#class-Script) - The retrieved script.

## *await* `Client.get_skin(id)`

### Arguments
`id` : `int` - ID of the skin to get.
### Returns
[`Skin`](reference.md#class-Skin) - The retrieved skin.

## *await* `Client.get_sound(id)`

### Arguments
`id` : `int` - ID of the sound to get.
### Returns
[`Sound`](reference.md#class-Sound) - The retrieved Sound.

## *await* `Client.get_spray(id)`

### Arguments
`id` : `int` - ID of the spray to get.
### Returns
[`Spray`](reference.md#class-Spray) - The retrieved spray.

## *await* `Client.get_texture(id)`

### Arguments
`id` : `int` - ID of the texture to get.
### Returns
[`Texture`](reference.md#class-Texture) - The retrieved texture.

## *await* `Client.get_thread(id)`

### Arguments
`id` : `int` - ID of the thread to get.
### Returns
[`Thread`](reference.md#class-Thread) - The retrieved thread.

## *await* `Client.get_tool(id)`

### Arguments
`id` : `int` - ID of the tool to get.
### Returns
[`Tool`](reference.md#class-Tool) - The retrieved tool.

## *await* `Client.get_tutorial(id)`

### Arguments
`id` : `int` - ID of the tutorial to get.
### Returns
[`Tutorial`](reference.md#class-Tutorial) - The retrieved tutorial.

## *await* `Client.get_ware(id)`

### Arguments
`id` : `int` - ID of the ware to get.
### Returns
[`Ware`](reference.md#class-Ware) - The retrieved ware.

## *await* `Client.get_wip(id)`

### Arguments
`id` : `int` - ID of the WiP to get.
### Returns
[`WiP`](reference.md#class-WiP) - The retrieved WiP.

# BASE STRUCTURES

# *class* `Author`
Represents an author of a submission. You can get this through the `.author`
property of any submission object. (or any object that inherts from 
`BaseSubmission`)

# *class* `Game`
Represents a game on GameBanana. You can get this through the `.game` or 
`.partOf` property of any submission object. (or any object that inherts from 
`BaseSubmission`)

# *class* `BaseSubmission`
The most basic form of a submission on GameBanana. All submission classes
inherit from this class.

### Properties
`author` : [`Author`](reference.md#class-Author) - The submitter.

`partOf`/`game` : [`Game`](reference.md#class-Game) - The game the submission 
was made for.

`name` : `str` - The name of the submission.

`type` : `str` - The name of the type of the submission.

`image` : `str` - The URL of the submission's image. (if any)

`thumbnail` : `str` - The URL of the submission's thumbnail image. (again, if 
any)

`likes` : `int` - The amount of likes the submission received. (can be `None`!)

`views` : `int` - The amount of views the submission received.

`posts` : `int` - The amount of posts (replies) the submission received.

`added` : `datetime` - The time of the submission's creation.

`modified` : `datetime` - The time when the submission was last modified.

# SUBMISSION CLASSES

# *class* `Blog`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Castaway`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Concept`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Effect`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Gamefile`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `GUI`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Map`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*does* implement unique properties.

### Properties
`version` : `str` - The map's version.

# *class* `Prefab`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Project`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and *does* 
implement unique properties.

### Properties
`completion` : `int` - The completion percentage.

`dev_state` : `str` - The development state.

`finished_url` : `str` - The URL of the finished work.

`wip_count` : `str` - The amount of WiPs in this project.

`file_count` : `str` - The amount of files in this project.

# *class* `Question`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Request`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and *does* 
implement unique properties.

### Properties
`deadline` : `datetime` - The request's deadline.

`resolution` : `str` - The request's resolution.

`resolutionMessage` : `str` - The resolution message.

# *class* `Script`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Skin`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Sound`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Spray`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Texture`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any unique properties.

# *class* `Thread`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and 
*doesn't* implement any other functionality or properties.

# *class* `Tool`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and *does* 
implement unique properties.

### Properties
`download` : `str` - The download URL.

`homepage` : `str` - The tool's homepage URL.

# *class* `WiP`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and *does* 
implement unique properties.

### Properties
`dev_state`/`state` : `str` - The development state.

`is_private` : `bool` - `True` if the WiP is private.

`finished_work` : [`FinishedWork`](reference.md#class-FinishedWork) - The
finished work.

`added` : `datetime` - The time of the WiP's creation.

# *class* `Tutorial`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and *does* 
implement unique properties.

### Properties
`difficulty` : `str` - The tutorial's difficulty.

# *class* `Ware`
Inherits from [`BaseSubmission`](reference.md#class-BaseSubmission) and *does* 
implement unique properties.

### Properties
`ware_type` : `str` - The ware's type.

# MISC. CLASSES

# *class* `FinishedWork`
Represents finished work of a WiP.

### Properties
`on_gamebanana` : `list[`[`WorkOnGB`](reference.md#WorkOnGB)`]` - Finished work 
on GameBanana.

`remote` : `list[str]` - URLs of finished work outside GameBanana.

# *class* `WorkOnGB`
Represents a finished work of a WiP on GameBanana.

### Properties
`name` : `str` - The name of the work.

`profile` : `str` - The URL of the work.