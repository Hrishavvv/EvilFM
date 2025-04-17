<div align="center">
  <img src="https://github.com/user-attachments/assets/37e951c4-5bb2-498f-b3cb-d8ff0f393bb5" alt="Evil FM" style="max-width: 60%; width: 60%; height: auto;">
  <h2>A Python Script for Managing Last.fm Scrobbles</h2>
</div>

**EvilFM** is a Python-based utility that leverages the Last.fm API to programmatically manage music scrobbles. With this tool, users can automate scrobbling tracks to their Last.fm profile, specifying the artist, track, and number of scrobbles as needed.

---

## Disclaimer

This software is provided "as-is" without any warranties, express or implied, including but not limited to warranties of merchantability or fitness for a particular purpose. The author(s) are not liable for any damages or losses resulting from the use of this software, including direct, indirect, incidental, or consequential damages. By using EvilFM, you acknowledge that you do so at your own risk.

---

## Prerequisites

To use EvilFM, you will need:

- A Last.fm account with API credentials (API Key, API Secret, Username, and Password).
- Python 3.x installed on your system.
- Git installed for cloning the repository.
- Basic knowledge of command-line or terminal operations.

---

## Getting Started

### Step 1: Obtain Last.fm API Credentials

- Navigate to the Last.fm API account creation page.
- Sign up or log in to acquire your API Key, API Secret, Username, and Password.
- Store these credentials securely for use in the script configuration.

<div align="center">
  <img src="https://github.com/user-attachments/assets/2e1f7599-4006-45f1-8e58-de8fe17b35a3" alt="Last.fm API" style="max-width: 50%; width: 50%; height: auto;">
</div>

---

### Step 2: Clone the Repository

#### For Windows

1. **Install Python** (skip if already installed):
   - Download the Python installer from [python.org](https://www.python.org/).
   - Run the installer and ensure Python is added to your system PATH.

2. **Install Git** (skip if already installed):
   - Refer to [Git installation guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

3. **Clone the repository:**

```bash
git clone https://github.com/Hrishavvv/EvilFM.git
```

#### For Linux (Debian/Ubuntu)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Hrishavvv/EvilFM.git
```

#### For Termux

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/Hrishavvv/EvilFM.git
```

---

### Step 3: Configure the Script

1. Navigate to the EvilFM directory:

```bash
cd EvilFM
```

2. Open `evil.py` in a text editor:

- **Windows:** Use Notepad or VS Code.
- **Linux/Termux:** Use nano:

```bash
nano evil.py
```

3. Update the following lines with your Last.fm API credentials:

```python
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
```

<div align="center">
  <img src="https://github.com/user-attachments/assets/67c4bcfc-7073-4591-b7ba-e5a06c6e126c" alt="API Credentials" style="max-width: 60%; width: 60%; height: auto;">
</div>

4. At the end of `evil.py`, set your scrobble preferences:

```python
ARTIST = "YOUR_ARTIST"
TRACK = "YOUR_TRACK"
SCROBBLE_COUNT = YOUR_SCROBBLE_COUNT
```

<div align="center">
  <img src="https://github.com/user-attachments/assets/285c7e54-f7e4-4907-936e-222c986dce1d" alt="Scrobble Parameters" style="max-width: 60%; width: 60%; height: auto;">
</div>

5. Save and exit:
- In nano, press `Ctrl+O`, then `Enter` to save, and `Ctrl+X` to exit.

---

### Step 4: Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

---

### Step 5: Run the Script

Execute to begin scrobbling:

#### Windows:

```bash
python evil.py
```

#### Linux/Termux:

```bash
python3 evil.py
```

<div align="center">
  <img src="https://github.com/user-attachments/assets/9f05cd3a-3460-4d0b-90d2-48286156109a" alt="Script Execution" style="max-width: 60%; width: 60%; height: auto;">
</div>

---

## Troubleshooting

- **API Errors:** Double-check your credentials and ensure your Last.fm account is active.
- **Dependency Issues:** Reinstall packages:

```bash
pip install -r requirements.txt
```

- **Script Won't Run:** Make sure Python and Git are correctly installed and in your system PATH.

---

## Contributing

We welcome contributions to enhance EvilFM! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

Please ensure your code follows the project's coding standards and includes appropriate documentation.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
