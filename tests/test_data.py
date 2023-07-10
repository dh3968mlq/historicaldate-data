import sys
import glob
import pandas as pd

hdroot = "/svol1/pishare/users/pi/repos/historicaldate"
sys.path.append(hdroot)
from historicaldate import hdpl

def test1():
    lfiles = glob.glob("data/**/*.csv", recursive=True)
    for filename in lfiles:
        lowfolder = filename.split("/")[-2]
        if lowfolder != "reference_tables":
            df = pd.read_csv(filename, na_filter=False)
            pltl = hdpl.plTimeLine()
            try:
                pltl.add_event_set(df, title=filename)
            except Exception as inst:
                print(f"Failed on {filename}")
                raise

    assert True