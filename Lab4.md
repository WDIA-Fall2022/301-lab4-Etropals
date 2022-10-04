# Lab 4

Unless you did some programming before, do not attempt to write the code before the lecture.

1. Connect to your raspberry Pi using `ssh`.

2. Install the SenseHat emulator using the command

   ```
   sudo apt-get update
   sudo apt-get install python3-sense-emu python-sense-emu-doc sense-emu-tools -y
   ```

3. Bookmark the SenseHat browser emulator on your laptop: `https://trinket.io/sense-hat`

4. In the file `Lab4.py`, modify the `trinket_logo()` function so that the colours G,Y,B,O are sent as arguments to the function with default values.

5. Test the code `Lab4.py` with your modification in the trinket emulator.

6. Do the same with the functions `raspi_logo()`, `plus(),` `equals()` and `heart().`

7. Based on the functions created steps 4 and 6, create a function `elephant()` with arguments and default values to display an elephant on the SenseHat. The elephant pattern can be found in the file `elephant.py`

8. Create a function `getUserChoice()`. The function displays the following menu:

   ```
   What do you want to display (0. to exit):
   
   1. Logo
   2. Plus sign
   3. Equals sign
   4. Raspberry
   5. Heart
   6. Elephant
   0. Exit
   
   ```

   The function must validate the user input as an `integer` using a loop and a `try except` block and then returns the `integer` value

9. Modify the main program (lines 94 to 98 in the original `Lab4.py` program) to:

   - Call the function `getUserChoice()` to display the menu and get the user's choice
   - Process the user input and display the appropriate item on the Sense Hat
   - Repeat the process until the user decides to quit (option 0)

10. Test your code on the raspberry Pi. You will need to replace the line 

    `from sense_hat import SenseHat` with `from sense_emu import SenseHat`

    Once finished, commit the file `Lab4.py` to GitHub.
