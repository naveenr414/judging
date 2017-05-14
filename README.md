# Things to do
## Grader
* ~~Actually Read the file name~~
    * ~~Currently it relies on input for the file name, and doesn't actually check the file for its name~~
* Write a compiler for C++, Java
* ~~Use a drop down list for the problem name~~
    * ~~Read the list of problems from a file~~
* Create models for submission
* Write each submission to the models
    * Currently, nothing is written to the models
* Write the result of grading to the models
* Create a login system
* Concurrency
    * Run the Grader in the background
        * Do what USACO does, and run the grading in the background, then update
        * Use celery? 
    * Use Channels to allow for realtime update, as soon as grading is done
    * Create a message type system, where the results of all tests are stored
        *  Update the user as soon as a new message is sent
* Use CSS to make it look nice
* Check/Return different types of error (Time Out, Compile Error, Wrong Answer) 

## Clarification System
* Use the message system (as part of the grader) to create clarification system
* Allow for admins to mass send messages
* Create an admin account for the clarification system
    *  Allow for responding/sending mass messages

## Scoreboard
* Create realtime scoreboard
* Do we want to only store the result of each test? 
    * Or do we want to be redundant, and also store the scoreboard somewhere, instead of recalculating
        * Leads to redundancy, as same information is stored twice

## Printing System
* Create a file submission system for printing
* Do we want it to automatically print? 

## Security
* One can enter a faulty Problem Name by not selecting from the list, and then shellcode from there
* One can enter a faulty filename and then shellcode from there
* Some type of password hacking, AKA Hash
* Prevent Users from accessing other files

# How to use
* To add problems, go to Answers/problemList.txt, make sure there's a newline after the last problem
