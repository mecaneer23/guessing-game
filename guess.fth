require random.fs

: input
    ." Guess a number between 0 and 9: "
    key
    dup 48 - swap
    emit
    cr ;

: main
    10 random \ wonky - often returns 0
    begin
        input
        over over < if ." Too high!" else
        over over > if ." Too low!" else
        ." You guessed it!" 100 swap
        then then
        drop cr
        dup 100 = until
        drop drop ;

main
cr bye