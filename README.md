# CEH-Practical-V13
<details>
  <summary>Module 02: Footprinting and Reconnaissance</summary>

* Lab1: Google Search

| Command | 功能 |
| --- | --- |
| cache: | 顯示 Google 上一次快取的網頁版本 |
| allinurl: | 搜尋網址（URL）中包含所有指定關鍵字的頁面 |
| inurl: | 搜尋網址中包含指定關鍵字的頁面（單一條件） |
| allintitle: | 搜尋網頁標題（title）中含有所有指定關鍵字的頁面 |
| intitle: | 搜尋網頁標題中包含某個關鍵字 |
| inanchor: | 搜尋超連結文字中包含某個關鍵字 |
| allinanchor: | 搜尋超連結（anchor text）中包含所有指定關鍵字的頁面 |
| related: | 找出與某網站相關或類似的網站 |
| info: | 顯示某網站的基本資訊（快取、相似頁面、連結） |
</details>

<details>
  <summary>Module 03: Scanning Networks</summary>

* Lab 1: Host Discovery

```console
nmap -sn -PR [Traget IP Address]
  -sn: disables port scan

  -PR: ARP ping scan
  -PU: UDP ping scan
  -PE: ICMP ECHO ping scan
  -PP: ICMP timestamp ping scan
  -PM: ICMP Address mask ping scan
  -PS: TCP SYN ping scan
  -PA: TCP ACK ping scan
  -PO: IP Protocol ping scan
```

* Lab 2: Port and Service Discovery

```Console
nmap -sT -v [Traget IP Address]
  -v: enables the verbose output (include all hosts and ports in the output)

  -sT: TCP connect/full open scan
  -sS: stealth scan/TCP helf-open scan
  -sX: Xmas scan
  -sM: TCP Maimon scan
  -sA: ACK flag probe scan
  -sU: UDP scan
```
</details>

# kali 基本建置

<details>
  <summary>更新資料庫</summary>

```console
sudo apt update
sudo apt upgrade & sudo apt dist-upgrade
sudo apt autoremove
```
</details>

<details>
  <summary>ssh 遠端登入</summary>

```console
sudo systemctl start ssh
sudo systemctl enable ssh
```
</details>

<details>
  <summary>開機自動進入桌面</summary>

```console
修改文件：sudo nano /etc/lightdm/lightdm.conf
autologin-user=<name>
autologin-user-timeout=0
```
</details>

<details>
  <summary>安裝 python3</summary>

```console
sudo apt-get upgrade python3
sudo apt-get install python3-venv
```
</details>

<details>
  <summary>python 虛擬機</summary>

* 使用user權限設定
```console
mkdir bhp
cd bhp
python3 -m venv venv3
source venv3/bin/activate
pip install lxml
deactivate
```

* 登入虛擬機常用指令
```console
cd bhp
source venv3/bin/activate
deactivate
```
</details>
