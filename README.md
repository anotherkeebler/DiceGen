# Diceware password generator server

This simple python script is used to generate strong but memorable
passphrases.

Get five dice. Roll them and write down the output as a five-digit
number (i.e. 52611). Do that several times. Six iterations is probably
good enough for a master passphrase. Then run the script with your
numbers as the command line:

    ./diceware-picker 13131 55425 41421 31164 42115

    13131 - axiom	awl	backyard
    55425 - stormy	stan	spherical
    41421 - manna	mae	motive
    31164 - gland	gibbs	flatworm
    42115 - mesa	md	nearly

Pick one word from each line to form a phrase you find interesting:

    backyard stan motive flatworm mesa

Mix in punctuation to make it a bit stronger:

    Backyard Stan's motive? flatworm mesa!

That's a fairly strong password. Add some digits or something if you
feel like it.

The wordlists are based on three existing DiceGen lists found online. I
merged them like this:

    paste beale.wordlist.asc diceware.wordlist.asc eff.large.wordlist.asc | cut -f1,2,4,6 > merged.tsv
    
_Notice_ the word lists were copied from the diceware project's page at
http://world.std.com/~reinhold/diceware.html. If you want to be a bit more paranoid, download the
GPG-signed originals from there.

## TODO

* make it fancier looking and more robust
* make it all a single file
