### Module 3

<details>
  <summary>Lab 1</summary>

  ```console
  nmap -sn -PR 10.10.10.3-254
  nmap -sn -PU 10.10.10.3-254
  nmap -sn -PE 10.10.10.3-254
  nmap -sn -PP 10.10.10.3-254
  nmap -sn -PM 10.10.10.3-254
  nmap -sn -PS 10.10.10.3-254
  nmap -sn -PA 10.10.10.3-254
  nmap -sn -PO 10.10.10.3-254
  ``` 
</details>

<details>
  <summary>Lab 2</summary>

  ```console
  nmap -sT -v 10.10.1.22
  nmap -sS -v 10.10.1.22
  nmap -sX -v 10.10.1.22
  nmap -sM -v 10.10.1.22
  nmap -sA -v 10.10.1.22
  nmap -sU -v 10.10.1.22
  nmap -sN -T4 -A -v 10.10.1.9
  nmap -sl -v
  nmap -sY -v
  nmap -sZ -v
  nmap -sV
  nmap -A (-O -sV -sC --traceroute)
  ```
</details>

<details>
  <summary>Lab 3</summary>

  ```console
  nmap -A 10.10.1.22
  nmap -O 10.10.1.22
  nmap --script smb-os-discovery.nse 10.10.1.22
  ```
</details>

<details>
  <summary>Lab 4</summary>

  ```console
  Task 1 windows
  ping www.certifiedhacker.com
  ping www.certifiedhacker.com -f -l 1500
  ping www.certifiedhacker.com -f -l 1300
  ping www.certifiedhacker.com -f -l 1473
  ping www.certifiedhacker.com -f -l 1472
  ping www.certifiedhacker.com -i 3
  ping www.certifiedhacker.com -i 2 -n 1
  ping www.certifiedhacker.com -i 3 -n 1
  ping www.certifiedhacker.com -i 4 -n 1
  ```
  ```console
  Task 2 Parrot
  cd Photon
  python3 photon.py -h
  python3 photon.py -u http://www.certifiedhacker.com

  python3 photon.py -u http://www.certifiedhacker.com -l 3 -t 200 --wayback
  ```
  ![Double-click external.txt]()
  ```console
  Task 3
  [Central Ops](https://centralops.net/co/)
  ```
  ```console
  Task 6 Parrot
  cd GRecon
  python3 grecon.py
  certifiedhacker.com
  ```
  ```console
  Task 7 Parrot
  cewl -d 2 -m 5 www.certifiedhacker.com
  cewl -w wordlist.txt -d 2 -m 5 www.certifiedhacker.com
  pluma wordlist.txt
  cewl --help
  ```
</details>

<details>
  <summary>Lab 6</summary>

  ```console
  [Whois Lookup](https://whois.domaintools.com)
  ```
</details>

<details>
  <summary>Lab 7</summary>

  ```console
  Task 1 windows
  nslookup
  set type=a
  www.certifiedhacker.com
  set type=cname
  certifiedhacker.com
  set type=a
  ns1.bluehost.com
  [nslookup](https://www.kloth.net/services/nslookup.php)
  ```
  ```console
  Task 2 Perrot
  [you get signal](https://www.yougetsignal.com)
  cd dnsrecon
  chmod +x ./dsnrecon.py
  ./dnsrecon.py -r 162.241.216.0-162.241.216.255
  ```
  ```console
  Task 3
  [SecurityTrails](https://securitytrails.com)
  ```
</details>

<details>
  <summary>Lab 8</summary>

  ```console
  Task 1
  [arin](https://www.arin.net/about/welcome/region)
  ```
  ```console
  Task 2 windows
  tracert www.certifiedhacker.com
  tracert /?
  tracert -h 5 www.certifiedhacker.com

  Perrot
  traceroute www.certifiedhacker.com
  ```
</details>

<details>
  <summary>Lab 9</summary>

  ```console
  Task 1 Perrot
  cd
  recon-ng
  help
  marketplace install all
  modules search
  workspaces
  workspaces create CEH
  workspaces list
  db insert domains
  show domains
  modules load brute
  modules load recon/domains-hosts/brute_hosts
  run

  back
  modules load recon/domains-hosts/bing_domain_web
  run

  modules load reverse_resolve
  modules load recon/hosts-hosts/reverse_resolve
  run
  show hosts
  back

  modules load reporting/html
  options set FILENAME /home/attacker/Desktop/results.html
  options set CREATOR Jason
  options set CUSTOMER Certifiedhacker Networks
  run
  打開桌面results.html

  cd
  recon-ng
  workspaces create reconnaissance
  modules load recon/domains-contacts/whois_pocs
  options set SOURCE facebook.com
  run
  back
  modules load recon/profiles-profiles/namechk
  options set SOURCE MarkZuckerberg
  run
  back
  modules load reporting/html
  options set FILENAME /home/attacker/Desktop/Reconnaissance.html
  options set CREATOR Jason
  options set CUSTOMER Mark Zuckerberg
  run
  打開桌面Reconnaissance.html

  cd
  recon-ng
  modules load recon/domains-hosts/hackertarget
  options set SOURCE certifiedhacker.com
  run
  ```
</details>
