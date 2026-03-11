# Sleep Breathing Irregularity Detection (SRIP Assessment)

## 🔸 Project Overview

This project analyzes physiological signals recorded during sleep to detect
breathing irregularities such as Hypopnea and Obstructive Apnea.
The pipeline covers signal visualization, preprocessing, and labeled dataset creation.

---

## 🔸 Project Structure
```
SRIP/
├── Data/
│   ├── AP01/
│   │   ├── nasal_airflow.txt
│   │   ├── thoracic_movement.txt
│   │   ├── spo2.txt
│   │   ├── flow_events.txt
│   │   └── sleep_profile.txt
│   ├── AP02/
│   ├── AP03/
│   ├── AP04/
│   └── AP05/
│
├── Dataset/
│   └── breathing_dataset.csv
│
├── Visualizations/
│   ├── AP01_visualization.pdf
│   └── AP02_visualization.pdf
│
├── 01_visualization.ipynb
├── 02_create_dataset.ipynb
├── utils.py
├── README.md
└── requirements.txt
```

---

## 🔸 Setup
```bash
pip install -r requirements.txt
```

---

## 🔸 Running the Notebooks

Open in Jupyter Lab and run all cells top to bottom:

**01_visualization.ipynb**
- Loads nasal airflow, thoracic movement, and SpO2 signals
- Overlays annotated breathing events as colored shaded regions
- Draws sleep stage bar at the bottom
- Saves output as PDF to `Visualizations/`
- When prompted enter participant folder path e.g. `Data/AP01`

**02_create_dataset.ipynb**
- Resamples all signals to 4 Hz
- Applies Butterworth bandpass filter (0.17–0.4 Hz)
- Slices signals into 30-second windows with 50% overlap
- Labels each window based on overlap with annotated breathing events
- Saves labeled dataset to `Dataset/breathing_dataset.csv`

---

## 🔸 utils.py — Shared Parsing Functions

| Function | Description |
|---|---|
| `format_signal(filepath)` | Parses nasal airflow, thoracic movement, SpO2 files |
| `format_flow(filepath)` | Parses annotated breathing event files |
| `format_sleep_profile(filepath)` | Parses sleep stage profile files |

---

