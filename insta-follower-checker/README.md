# insta-follower-checker

A simple and efficient Python tool to analyze follower relationships using official Instagram data export. This project helps identify non-mutual connections by comparing followers and following lists.

---

## 📌 Overview

`insta-follower-checker` processes JSON data downloaded from Instagram to provide insights into your social connections.

It answers key questions:

* Who doesn’t follow you back?
* Who follows you but you don’t follow back?

---

## 🚀 Features

* Parses official Instagram data export (JSON)
* Identifies non-followers (you follow them, they don’t follow you)
* Identifies fans (they follow you, you don’t follow them)
* Lightweight and beginner-friendly
* No external libraries required

---

## 🗂️ Project Structure

```
insta-follower-checker/
│
├── followers_1.json
├── following.json
├── main.py
└── README.md
```

---

## 📥 Getting Your Instagram Data

1. Open Instagram
2. Go to **Settings → Privacy and Security → Data Download**
3. Request your data in **JSON format**
4. Download and extract the archive
5. Navigate to:

```
connections/followers_and_following/
```

---

## ⚙️ Requirements

* Python 3.x
* No additional dependencies

Check Python installation:

```
python --version
```

---

## ▶️ Usage

1. Place the required files in the project folder:

   * `followers_1.json`
   * `following.json`

2. Run the script:

```
python script.py
```

---

## 📊 Example Output

```
--- Not Following You Back ---
user_a
user_b

--- You Don't Follow Back ---
user_c
user_d
```

---

## ⚠️ Notes

* Instagram may split followers into multiple files:

  * `followers_1.json`, `followers_2.json`, etc.
* Ensure all files are correctly placed in the project directory
* This tool uses only exported data and does not interact with Instagram APIs

---

## 🔮 Future Improvements

* Export results to CSV / Excel
* Add graphical dashboard
* Build web interface (React + FastAPI)
* Add mutual followers analysis

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss improvements.

---

## ✨ Acknowledgment

All data used is obtained from official export provided by Instagram.
