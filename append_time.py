__author__ = 'Mike Konarski'
# This module contains some useful functions for appending time to strings.
import datetime

def add_date_time_to_filename(filename):
    if "." in filename:
        dot = filename.find(".")
        return filename[:dot] + "_" + str(datetime.datetime.now()).replace(" ", "_") + filename[dot:]
    else:
        return filename + "_" + str(datetime.datetime.now()).replace(" ", "_")

if __name__ == "__main__":
    print add_date_time_to_filename("filename")
    print add_date_time_to_filename("filename.txt")
