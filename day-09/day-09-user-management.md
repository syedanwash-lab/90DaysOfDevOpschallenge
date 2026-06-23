# Day 09 Challenge – Linux User & Group Management

## Objective

Today's goal was to practice Linux user and group management through hands-on challenges involving:

* User creation
* Group management
* Shared directory permissions
* Team collaboration setup

---

# Task 1: Create Users

## Commands Used

```bash id="uz6tsd"
sudo useradd -m tokyo
sudo useradd -m berlin
sudo useradd -m professor

sudo passwd tokyo
sudo passwd berlin
sudo passwd professor
```

## Verification

```bash id="yfqvx8"
cat /etc/passwd | grep -E 'tokyo|berlin|professor'
ls /home
```

---

# Task 2: Create Groups

## Commands Used

```bash id="f3szjc"
sudo groupadd developers
sudo groupadd admins
```

## Verification

```bash id="2fdkbx"
cat /etc/group | grep -E 'developers|admins'
```

---

# Task 3: Assign Users to Groups

## Commands Used

```bash id="5fyqfi"
sudo usermod -aG developers tokyo
sudo usermod -aG developers,admins berlin
sudo usermod -aG admins professor
```

## Verification

```bash id="wkv41h"
groups tokyo
groups berlin
groups professor
```

---

# Task 4: Shared Directory Setup

## Commands Used

```bash id="fsfjlwm"
sudo mkdir -p /opt/dev-project
sudo chgrp developers /opt/dev-project
sudo chmod 775 /opt/dev-project
```

## Test File Creation

```bash id="vtzrzm"
sudo -u tokyo touch /opt/dev-project/tokyo-file.txt
sudo -u berlin touch /opt/dev-project/berlin-file.txt
```

## Verification

```bash id="6zcxhn"
ls -ld /opt/dev-project
ls -l /opt/dev-project
```

---

# Task 5: Team Workspace

## Commands Used

```bash id="c0jlbj"
sudo useradd -m nairobi
sudo passwd nairobi

sudo groupadd project-team

sudo usermod -aG project-team nairobi
sudo usermod -aG project-team tokyo

sudo mkdir -p /opt/team-workspace
sudo chgrp project-team /opt/team-workspace
sudo chmod 775 /opt/team-workspace
```

## Test File Creation

```bash id="y9zlkr"
sudo -u nairobi touch /opt/team-workspace/nairobi-file.txt
```

## Verification

```bash id="mhb8hm"
ls -ld /opt/team-workspace
ls -l /opt/team-workspace
```

---

# Users & Groups Created

## Users

* tokyo
* berlin
* professor
* nairobi

## Groups

* developers
* admins
* project-team

---

# Group Assignments

| User      | Groups                   |
| --------- | ------------------------ |
| tokyo     | developers, project-team |
| berlin    | developers, admins       |
| professor | admins                   |
| nairobi   | project-team             |

---

# What I Learned Today

1. How Linux manages users and groups for secure access control.

2. How shared group permissions allow multiple users to collaborate on the same directory.

3. How to use commands like `usermod`, `chmod`, `chgrp`, and `groups` in real-world DevOps scenarios.

4. How Linux file permissions directly impact team workflows and system security.

5. How to test user access using `sudo -u` to simulate different users.

---

# Real-World DevOps Use

This type of user and permission management is commonly used in:

* Shared development servers
* CI/CD environments
* Multi-user Linux systems
* Production infrastructure management

---

# Conclusion

Today’s challenge helped me understand practical Linux administration tasks that are important for DevOps and system engineering roles.