import pandas as pd
import re

#data cleaning nasal airflow, thoracic, spo2
#30.05.2024 20:59:00,000; 120
def format_signal(filepath):
    rows=[]
    in_data=False
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line=line.strip()
            if line.lower()=="data:":
                in_data=True
                continue
            if not in_data or not line:
                continue
            parts=line.split(";")
            if len(parts)<2:
                continue
            
            try:
                ts=pd.to_datetime(parts[0].strip(), format="%d.%m.%Y %H:%M:%S,%f")
                val=float(parts[1].strip())
                rows.append((ts, val))
            except:
                continue
    df=pd.DataFrame(rows, columns=["timestamp", "value"])
    df.set_index("timestamp", inplace=True)
    return df


#datacleaning for flow event file
#30.05.2024 23:48:45,119-23:49:01,408; 16;Hypopnea; N1

def format_flow(filepath):
    events=[]
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line=line.strip()
            #30.05.2024     23:48:45,119-   23:49:01,408; 16;Hypopnea; N1
            m=re.match(r"(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2},\d+)-(\d{2}:\d{2}:\d{2},\d+);\s*(\d+);\s*([^;]+);\s*(\S+)",
                line)
            if not m:
                continue
            date_str, start_t, end_t, dur, label, stage=m.groups()
            try:
                start=pd.to_datetime(f"{date_str} {start_t}", format="%d.%m.%Y %H:%M:%S,%f")
                end=pd.to_datetime(f"{date_str} {end_t}", format="%d.%m.%Y %H:%M:%S,%f")
                
                if end<start:
                    end+=pd.Timedelta(days=1)
                events.append({
                    "start": start,
                    "end": end,
                    "duration": int(dur),
                    "label": label.strip(),
                    "stage":stage.strip()
                })
            except:
                continue
    return events


#sleep profile
#30.05.2024 20:59:00,000; Wake

def format_sleep_profile(filepath):
    rows=[]
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            parts=line.split(";")
            if len(parts)<2:
                continue
            parts=line.split(";")
            if len(parts)<2:
                continue
            try:
                ts=pd.to_datetime(parts[0].strip(), format="%d.%m.%Y %H:%M:%S,%f")
                stage=parts[1].strip()
                rows.append((ts, stage))
            except:
                continue
    df=pd.DataFrame(rows, columns=["timestamp", "stage"])
    df.set_index("timestamp", inplace=True)
    return df