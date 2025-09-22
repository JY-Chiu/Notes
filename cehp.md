### CEHP

<details>
  <summary>使用NMAP掃描網路</summary>
  
  ``` console
  nmap -sn 10.10.10.*
  nmap -sn 10.10.10.* --packet-trace
  nmap -sn scanme.nmap.org --packet-trace
  ```
</details>

<details>
  <summary>使用NMAP掃描主機</summary>

  ```console
  nmap 10.10.10.9
  nmap 10.10.10.9 --reason
    最常用的1000個端口/usr/share/nmap/nmap-services
  nmap 10.10.10.9 -p-
  nmap 10.10.10.16 -sU -p53,137-139,161,1900,5353
  nmap -p80 10.10.10.*
  nmap -p80 10.10.10.2,10,13 --reason
  nmap -p80 10.10.10.* --open
  ```
</details>

<details>
  <summary>使用NMAP識別作業系統與服務</summary>

  ```console
  nmap 10.10.10.16 -O
  nmap 10.10.10.16 -sV
  nmap 10.10.10.16 -sVC -p445,3389
  nmap 10.10.10.16 -sV -O -sC -Pn -p445,3389,389,3268
    for windows
  ```
</details>

<details>
  <summary>列舉常見網路服務</summary>

  ```console
  nmap -sU -p161 --open 10.10.10.*
  nmap -sU -p161 -sC 10.10.10.*
  snmp-check 10.10.10.16
  nmap -sU -p161 --script snmp-win32-users 10.10.10.16
  nbtscan 10.10.10.1-254
  enum4linux 10.10.10.16
  hydra -L win32-users.txt -P /usr/share/wordlists/nmap.lst smb://10.10.10.16
  hydra -l jason -P /usr/share/wordlists/nmap.lst smb://10.10.10.16
    smb可換rdp
  enum4linux -u martin -p apple -a 10.10.10.16
    -a可替換-S -U -P
  python3 -m pip install --upgrade impacket
  crackmapexec smb 10.10.10.16 -u martin -p apple --shares
  ```
</details>
