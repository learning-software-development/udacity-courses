import time
import webbrowser

total_breaks = 3
break_count = 0

print("This programm started", time.ctime())
while break_count < total_breaks:
    time.sleep(2*60*60)
    webbrowser.open(
        'https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/zkxk2fwf(v=vs.90)')
    break_count += 1
