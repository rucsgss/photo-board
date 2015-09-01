Photo board
===========

Setup
-----

Create list(s) of people in separate text files for each section in
the photo board (e.g., PhD students, MS students, etc.). The file
should contain one person per line, in the following format:

    unique-id[display-name]

If the `display-name` is omitted, the `unique-id` will be used
instead.

Photos should be placed in the `photos` directory, with a filename
that matches `unique-id` (plus an extension). PNG files seem to work
better with LaTeX than JPG. If a photo cannot be found, the blank
profile image (`noun_project_419.eps`) will automatically be used
instead.

The title for the photo board is in `make-photoboard-tex.py` --
replace "Your Title Here" with the title you like. The groups of
people are defined in `main` of the same file, as follows:

    groups = [
        ["Group 1", "group1.txt"],
        ["Group 2", "group2.txt"]]

The first field is the title that will be displayed on the photo
board, and the second is the filename that lists the people in that
group, as described above.

You may need to adjust `numcolumns` and `numrows`, as well as possibly
some of the spacing, font sizes, paper size, etc., in that file to
make everything fit the way you want.

Building
--------

Run the following:

    make clean
    make

This should generate a `photoboard.pdf` file with the finished photo
board.
