# Random Bible Verse Generator
This is a program that generates random bible verses from the New Testament.
You can choose to clone the GitHub repository to a continuous integration platform (Jenkins, Travis etc..)
Or you can schedule a task that simply runs the script.sh file. (The SMS service only allows one SMS per day but you can replace the code in script.sh with your own SMS provider's API)

## Dependencies
Python:  You can download it from the Microsoft Store on Windows or by typing python in a terminal on Linux/MAC

# Running on Windows

# Running on Linux
1. Clone the repository:
```
git clone https://github.com/whylikethat/random.git
```
2. Then go into the repository and make the script executable
```
  cd random && chmod +x script.sh
```
2. Modify the e-mail information in notification.py to reflect your e-mail service provider (I used SMTP with Gmail)
3. Run the script:
```
   make text
```
4. Cleanup with:
```
   make clean
```
   This process only runs the program once, if you want to run it on a schedule, you will need to integrate it with [CI ](https://www.google.com/search?q=continous+integration+platforms&oq=continous+integration+platforms&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMggIAhAAGBYYHjIICAMQABgWGB4yCAgEEAAYFhgeMgoIBRAAGAgYDRgeMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoFMgYICBAuGEAyBggJEEUYOdIBCDQ5NDNqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8)

* Note: The free SMS service allows up to 78 characters, that's why there is an e-mail option in case the verse exceeds that length. You can use the SMS service of your choice and integrate it into the script.sh

Make sure that you don't create any shortcuts and you run the script directly in it's original folder.
