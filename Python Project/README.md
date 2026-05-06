# 🚦 Traffic Data Analysis System

A command-line Python application for loading, analyzing, filtering, and managing urban traffic data — built as a **1st Year Python Project**.

---

## 📌 Overview

The **Traffic Data Analysis System** is a menu-driven CLI tool that allows users to store and explore traffic records across multiple city locations. It demonstrates core Python concepts including file handling, OOP, NumPy statistics, exception handling, and data structures.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **View Summary** | Displays total record count, all locations, and days present in the dataset |
| 🔍 **Filter Data** | Filter traffic records by day of the week or by location |
| 🔎 **Search Records** | Keyword-based search across location and day fields |
| ➕ **Add Record** | Interactively input and save a new traffic record to the CSV file |
| 📈 **NumPy Analysis** | Statistical breakdown — sum, mean, max, min, std dev for vehicle count and speed |
| 🗂️ **Unique Values** | Lists all unique locations and days, with missing-day detection |

---

## 🧠 Python Concepts Demonstrated

This project was built to showcase fundamental and intermediate Python concepts:

- **Data Structures** — Lists, Tuples, Sets, Dictionaries
- **OOP** — Class definition (`TrafficRecord`), object instantiation, instance methods
- **File Handling** — CSV read, write, and append modes using `csv` module
- **Exception Handling** — `try/except` for `FileNotFoundError`, `ValueError`, and general errors
- **String Methods** — `.strip()`, `.title()`, `.lower()`, `.join()`
- **Loops & Conditionals** — `for`, `while`, `if/elif/else`
- **NumPy** — `np.array`, `np.sum`, `np.mean`, `np.max`, `np.min`, `np.std`, `np.median`
- **Modules** — `os`, `csv`, `numpy`

---

## 📁 Project Structure

```
traffic-analysis/
│
├── traffic_analysis_final.py   # Main application file
├── traffic_data.csv            # Auto-generated sample data file
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x and NumPy installed.

```bash
pip install numpy
```

### Running the Program

```bash
python traffic_analysis_final.py
```

On first run, a sample `traffic_data.csv` file will be automatically created with pre-loaded data.

---

## 🗃️ Sample Data

The program ships with 12 sample records across 4 locations:

| Location | Days Covered | Vehicle Range | Speed Range |
|---|---|---|---|
| MG Road | Mon, Fri, Sat | 180 – 400 | 22 – 45 kmph |
| Ring Road | Mon, Wed, Sun | 200 – 410 | 20 – 55 kmph |
| City Center | Mon, Wed, Fri | 260 – 500 | 15 – 40 kmph |
| Highway 1 | Tue, Thu, Sun | 400 – 600 | 75 – 90 kmph |

---

## 🖥️ Menu Options

```
  ====  TRAFFIC DATA ANALYSIS SYSTEM  ====
  1. View Summary       4. Add Record
  2. Filter Data        5. NumPy Analysis
  3. Search Records     6. Unique Values
  0. Exit
```

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| `numpy` | Statistical analysis of traffic data |
| `csv` | Reading and writing data to CSV files |
| `os` | Checking file existence |

---

## 👨‍💻 Author

**[Kamal Khandelwal]**
1st Year B.Tech(Computer Science)
UPES

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

> *Built with ❤️ as a 1st Year Python Project*
