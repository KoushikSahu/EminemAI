# EminemAI

Creates Eminem style lyrics and converts them to audio in the voice of Eminem

## Example output produced (Warning: NSFW!):

```
She loves me!
Can you hear me? I aint got time
I need you to shut your mouth
Shut up, bitch!
You know how many times I gotta say a word
And I just say it once
And thats all you gots to see
Yo, this is what it sounds like in my brain
Much as I fight to restrain
I have the right to remain violent
Any rhyme that I say can and will be used against you
Icicle veins, micsll get slain
Like they were strangled with bicycle chains
You’re gonna have to come identify the remains
Wait, what?
I said my head is twisted like a bread tie
Cant get a fuckin word in edgewise
Success overnight like a red-eye
Dressed like a Jedi at a Best Buy on the Westside of Dallas
In a laser tag vest and a racin jacket
```
https://user-images.githubusercontent.com/39738439/218961539-1362e6a4-2588-47ba-8cf6-d67f4b4f1ea8.mp4

## Usage:

To produce lyrics and convert them to audio run:
```
python src/main.py
```

To get the options that can be set while running the above command run `python src/main.py -h`:
```
usage: Generate eminem lyrics using a LLMs [-h] [-l MAXLENGTH]

options:
  -h, --help            show this help message and exit
  -l MAXLENGTH, --maxlength MAXLENGTH
                        Maximum length of lyrics to generate
```

## TODOs:

- [ ] Add pipeline to upload soundcloud playlist with a cadence
- [ ] Use transfer learning to train own model on Eminem lyrics dataset
