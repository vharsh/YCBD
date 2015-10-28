import win32clipboard

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
if 'youtube' in data:
    print (data)
    
