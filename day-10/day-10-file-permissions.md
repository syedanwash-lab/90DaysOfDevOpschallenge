# Day 10 Challenge

## Files Created

Create empty file devops.txt using touch
Create notes.txt with some content using cat or echo
Create script.sh using vim with content: echo "Hello DevOps"
Verify: ls -l to see permissions

2026  git-help.txt  notes.txt
ls -la
total 16
drwxr-xr-x 2 sandbox sandbox 4096 Jul  1 05:00 .
drwxr-xr-x 3 sandbox sandbox 4096 Jul  1 04:41 ..
-rw-r--r-- 1 sandbox sandbox    0 Jul  1 04:29 devops.txt
-rw-r--r-- 1 sandbox sandbox   49 Jul  1 04:30 notes.txt
-rw-r--r-- 1 sandbox sandbox   32 Jul  1 05:00 scripts.sh

![alt text](image.png)

# Read Files
Read notes.txt using cat
![alt text](day10.1.png)

View script.sh in vim read-only mode - vim -R script.sh

![alt text](day10.2.png)

Display first 5 lines of /etc/passwd using head
![alt text](day10.3.png)

Last five lines
![alt text](day10.4.png)

## Permission Changes

![alt text](day10.png)
![alt text](day10.5.png)
Current permissions :

Devops.txt : -rw-rw-r--

- → indicates it’s a regular file (not a directory or special file).
rw- → (user/owner) → read + write, no execute.
rw- → (group) → read + write, no execute.
r-- → (others) → read only, no write or execute.
Same permissions applied to notes.txt and script.sh.

# Modify Permissions
Make script.sh executable → run it with ./script.sh
![alt text](day10.6.png)

 ./script.sh 
Hello DevOps
sandbox@playground:~/2026/day-10$ 

Set devops.txt to read-only (remove write for all)
![alt text](day10.7.png)

Set notes.txt to 640 (owner: rw, group: r, others: none)
![alt text](day10.8.png)

Create directory project/ with permissions 755
![alt text](day10.9.png)

## Test Permissions
Writing to a read-only file - what happens?
Answer : Writing to a read‑only file normally gives Permission denied. With sudo, you can override and write to the file — but only if the redirection itself is executed with root privileges (using tee or sudo bash -c). Even sudo won’t help if the file is set to immutable (via chattr +i) or mounted on a read‑only filesystem.

Try executing a file without execute permission.
Answer : Executing a file without execute permission gives Permission denied. Even sudo cannot bypass this, because the shell requires the execute bit. However, you can still run the file by explicitly invoking the interpreter (e.g., bash script.sh or python3 script.py).
[before/after for each file]

## Commands Used

touch fname - Creates empty file.
echo "Hello" > fname - Create file with content.
vim fname - Create/open file in Vim.
cat fname - Prints files content.
vim -R fname - Open file in read only mode.
cat /etc/passwd | head -5 - Prints first 5 lines of /etc/passwd.
cat /etc/passwd | tail -5 - Prints last 5 lines of /etc/passwd.
chmod +x fname - Adding executable permission for all(owner,group,others).
chmod -w fname - Removing write permission for all(owner,group,others).
mkdir -m 755 dname - Create directory with permissions(rwx,r-x,r-x).


## What I Learned

Managing files permissions effectively.
Using sudo can override read & write restrictions.
Sudo cannot override execute permission but calling the interpreter directly allows execution.
