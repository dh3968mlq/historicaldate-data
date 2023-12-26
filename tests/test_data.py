# At present these tests will run only if historicaldata is where it's expected to be...
# Which may mean only when both historicaldate-data and historicaldate are submodules of a common project

import sys
import glob
import pandas as pd
import datetime

# -- General idea: improves chances of tests and Sphinx builds working if this is included as a submodule
def add_submodule(path):
    if f"./{path}" not in sys.path:
        sys.path.insert(0,f"../{path}") # -- Needed for Sphinx builds, usually run in the docs subdirectory
        sys.path.insert(0,f"./{path}")  # -- For normall running. Add second so it will go first in the search order
add_submodule("hdtimelines")

from hdtimelines import pltimeline

def test1():
    lfiles = glob.glob("**/data/**/*.csv", recursive=True)
    for filename in lfiles:
        if "Playwrights" in filename or True:  # Allow easy focus on a problematic file
            lowfolder = filename.split("/")[-2]
            if lowfolder != "reference_tables":
                df = pd.read_csv(filename, na_filter=False)
                pltl = pltimeline.plTimeLine()
                try:
                    pltl.add_topic_from_df(df, title=filename,
                                    study_range_start=datetime.date(1000,1,1), study_range_end=datetime.date(2100,12,31))
                except Exception as inst:
                    print(f"Failed on {filename}")
                    raise

    assert True