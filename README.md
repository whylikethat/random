# Random Bible Verse Generator
This is a program that generates random bible verses from the New Testament.
You can choose to clone the github repository to a continious integration platform (Jenkins, Travis etc..)
Or you can schedule a task that simply runs the script.sh file. (The SMS service only allows one SMS per day)

## Dependancies
Python:  You can download it from the Microsoft Store on WIndows or by typing python in a terminal on Linux/MAC

# Running on Windows

# Running on Linux
1. Clone the repo 'git clone https://github.com/whylikethat/random.git'
2. 'cd random && chmod +x script.sh'
3. Modify the e-mail information in notification.py to reflect your e-mail service provider (I used SMTP with Gmail)
4. Run the script './script.sh'
   This process only runs the program once, if you want to run it on a schedule, you will need to integrate it with a CI 

* Note: The free SMS service allows up to 78 caracters, that's why there is an e-mail option in case the verse exceeds that length

Make sure that you don't create any shortcuts and you run the script directly in it's original folder.
