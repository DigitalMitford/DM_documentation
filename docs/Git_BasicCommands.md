# Using Git through Command Line
  
*To download a file without cloning or pulling in changes locally, navigate to the file on GitHub and on the right side near the top of the file's content click the button that gives you the "Raw" view of the file. From there you can copy and paste or right click and save.*
  
## Quick reference
* Open terminal / command line shell
* Navigate to repo.
* `git pull`
* Make changes.
* `git status` -- list of changes should be red
* `git add -A` OR `git add .`
* `git status` -- list of changes should be green
* `git commit -m "message here"`
* `git push`
  
## Detailed walk-through

1) The key thing to working with Git is **always knowing where to find your files in the Finder (on Mac) / File Explorer (on Windows) and in the Terminal/Command Line Shell**. So you need to save them in a place where you can easily see them. 
* In the Finder/File Explorer, make yourself a "GitHub" directory that lives inside "Documents" (or on your desktop if that is a more logical place for you). Inside the "GitHub" directory you will clone each of your project repositories.
* In the Terminal/Command Line Shell), you can navigate to your "GitHub" directory from the computer's root by typing:
`cd Documents/GitHub/` if stored in documents or `cd Desktop/GitHub/` if stored on your desktop
**`cd` means "change directories"** and in the above command you are *stepping down* into Documents (or Desktop) and into the GitHub folder. Use **`ls`** to list out the contents of the directory you have stepped down into.

* If you need to **clone** a repository, do so here, because then the new repository will sit as a *child* inside your GitHub directory. Go to the git remote website and get its "Download/Clone" URL by copying it (green icon on right side of the repo's main page). 
Then, in the Terminal/Command Line Shell, type `git clone` and paste in the the URL after that. So it looks like this for our DHClass-Hub:
````
git clone https://github.com/ebeshero/DHClass-Hub.git
````
Hit enter, and watch the lines scroll away in the command line terminal as the repository clones itself on your local computer inside your GitHub directory. 

2) You interact with your local directory the way you would any other. You can drag files into it using the Finder/File Explorer, save files into it, and check in with the remote repository to **pull** new files in.  
So this is what you should do:
Open Terminal/Command Line Shell, and step down into your GitHub directory, and then down into the DHClass-Hub (or desired repo), and check that you are where you want to be **by typing `ls`.** The ls command will **show the contents of the directory** in which you've positioned yourself. You can **`cd`** up or down (cd means change directory), by moving like this:
````
cd ..
````
This moves up to a parent directory.

````
cd directoryName
````
This moves down into a directory. 

* To make sure you're in the right directory, the top level of the DHClass-Hub, also check to see the directory name at the terminal prompt. Yours should look similar to this, and the key part is "DHClass-Hub":
`gbg-wireless-pittnet-150-212-105-8:DHClass-Hub ebb8$ `

Then to pull in any changes from the remote "mothership" repo, type:
````
git pull
```` 

3) When you want to share you local changes to the repo with the remote mothership and other collaborators, you need to **add**, **commit**, and **push** those changes. Here's how you do it:

* Make sure you're in the DHClass-Hub repo at the top level
* Then type:
````
git add .
````
The period means *all* -- as in add *all* new files to be tracked by Git.

* If you type `git status` at this point, you see highlighted in green the new files being added! 
* Now, you need to **commit** those changes. You type the commit, and write a message, because Git *always* makes you document changes to the repo:
````
git commit -m "your detailed commit message should go in here"
````
Think of these commit messages as breadcrumbs for you and others to use in recording your project's progress! Check out our issue on [Effective Git Commit Messages](https://github.com/ebeshero/DHClass-Hub/issues/217).

* Next, you push the commit through, with:
````
git push
````
And gears turn and lines of text whirl on the screen, and your changes go up into the remote "Mothership repo"! You should always check on the web repository to see if your commit went through.  
 
  
  
### Git commands for a Forked Repo workflow
* `git pull upstream master` (This pulls any changes that were made to the original repository since you last synced into your forked repository.)
* Save changes / move files into directory through File Explorer / Finder
* `git status` (shows the differences/changes between the master and your fork/branch -- should be red)
* `git add .` OR `git add -A` (You're adding your changes to your branch.)
* `git status` (To see that you added your changes to your branch -- should be green.)
* `git commit -m "your commit message here"` (Commits your changes to your branch with a message describing changes.)
* `git status` (To see that your commit was successful and your branch is ahead of your remote fork.)
* `git push` (Push your committed changes to your remote fork.)
* Create a pull request on the web repository from your fork to the original repo

