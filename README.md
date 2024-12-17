# Messengers-and-notes
網路程式設計專題作品

## 環境設定
請先安裝 Python  
建議先在此專案中建立一個 .venv 虛擬環境  
執行以下套件安裝：
```
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install flask-login
pip3 install flask-socketio
```
在資料庫新增預設資料：
```
python .\util\addData.py
```
要啟動伺服器請輸入：
```
python app.py
```