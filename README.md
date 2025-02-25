<div align="center">
  <img src="https://github.com/user-attachments/assets/37e951c4-5bb2-498f-b3cb-d8ff0f393bb5" alt="Evil FM" style="max-width: 60%; width: 60%; height: auto;">
</div>

<div align="center">
  <h2>A Python script to manipulate Last.fm scrobbles!</h2>
</div>

## Disclaimer

This project is provided "as-is" without any warranty or guarantee of any kind, either express or implied, including but not limited to the implied warranties of merchantability or fitness for a particular purpose. The author(s) of this project are not liable for any damages, losses, or other consequences that may arise from the use of this software, including but not limited to direct, indirect, incidental, or consequential damages.

By using this software, you agree to do so at your own risk.

## How To Use

### Getting a Last.fm API account
Click [here](https://www.last.fm/api/account/create) and make an account and get the API key, API secret and Username.

 <img src="https://github.com/user-attachments/assets/2e1f7599-4006-45f1-8e58-de8fe17b35a3" alt="Evil FM" style="max-width: 50%; width: 50%; height: auto;">

## Cloning the repository

### For Windows

_Installing python on your system (skip this if you have it installed already)_

Download the python installer from [here.](https://www.python.org/downloads/windows/)

Run the installer and after installing python open up cmd.

Type the following one by one (_Make sure you have git installed on your system if not [check this.](https://www.simplilearn.com/tutorials/git-tutorial/git-installation-on-windows)_):
```bash
git clone https://github.com/Hrishavvv/EvilFM.git/
```

## Open the EvilFM folder and open the ```evil.py``` file in a text editor.
Go to these lines and replace it with your original Last.fm API key, API Secret, Username and Password

![image](https://github.com/user-attachments/assets/67c4bcfc-7073-4591-b7ba-e5a06c6e126c)

Find these lines at the end of the code and update it accordingly to the artist and the track name and the number of times you want to scrobble it

![image](https://github.com/user-attachments/assets/285c7e54-f7e4-4907-936e-222c986dce1d)

## Usage 
Open cmd/(terminal in Linux) and go to the drive the ```EvilFM``` folder is in and type the following :
```bash
cd EvilFM
```
```bash
pip install -r requirements.txt
```
```bash
python evil.py
```
![image](https://github.com/user-attachments/assets/9f05cd3a-3460-4d0b-90d2-48286156109a)

## For Linux/Termux :

#### Same process for cloning and using the script on Linux, I haven't mentioned the steps of cloning the repo in Linux seperately in details but you can just follow this if you're confused.

### To install python and git in ``Debian/Ubuntu`` :
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Hrishavvv/EvilFM.git
```

*Open the evil.py file and change the required things in the code (as mentioned above for Windows)*

``Run this after you have updated the code``
```bash
cd EvilFM
pip install -r requirements.txt
python3 evil.py
```

### For ``Termux`` :
```bash
apt update && apt upgrade -y
apt install python git -y
git clone https://github.com/Hrishavvv/EvilFM.git
```
*Open the evil.py file and change the required things in the code (as mentioned above for Windows)*

``Run this to open the nano text edtitor in Termux``
```bash
cd EvilFM
nano evil.py
```

``Run this after you have updated the code``
```bash
pip install -r requirements.txt
python3 evil.py
```
<img src="https://github.com/user-attachments/assets/fce73b54-de4c-4000-91af-b95ee594c897" alt="Evil FM" style="max-width: 40%; width: 40%; height: auto;">

