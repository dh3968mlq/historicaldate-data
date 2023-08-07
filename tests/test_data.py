import sys
import glob
import pandas as pd
import datetime

sys.path.append("historicaldate")
#from historicaldate import hdpl
try:
    import historicaldate.hdpl as hdpl
except:
    import historicaldate.historicaldate.hdpl as hdpl

def test1():
    lfiles = glob.glob("**/data/**/*.csv", recursive=True)
    for filename in lfiles:
        if "Playwrights" in filename or True:  # Allow easy focus on a problematic file
            lowfolder = filename.split("/")[-2]
            if lowfolder != "reference_tables":
                df = pd.read_csv(filename, na_filter=False)
                pltl = hdpl.plTimeLine()
                try:
                    pltl.add_event_set(df, title=filename,
                                    study_range_start=datetime.date(1000,1,1), study_range_end=datetime.date(2100,12,31))
                except Exception as inst:
                    print(f"Failed on {filename}")
                    raise

    assert True