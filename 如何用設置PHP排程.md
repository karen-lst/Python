## 設置PHP排程
- 在服務器中設置一個排程，動作為bat檔。bat內容為：
```
@echo off
start /min /d "C:\Program Files\Internet Explorer" iexplore.exe http://192.168.65.232/backupcode/device_update_warning.php
```