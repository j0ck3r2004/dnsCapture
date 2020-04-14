# dnsCapture
# AUTHOR : Vasilis Manthelas [OFFICIAL-WEBSITE](http://j0ck3r2004.000webhostapp.com/)
Python 3 module for capturing dns traffic
# INSTALLATION
- GITHUB
    - ``` git clone https://github.com/j0ck3r2004/dnsCapture/```
# REQUIRMENTS
- Python>=3.8
- scapy
    - windows
    ```sh
    python -m pip scapy
    ```
    - linux
    ```sh 
    pip3 install scapy
    ```
   - dnsCapture folder musst be in the same directory as your program
    ```
    |DIRECTORY-|
    |----------|
    |program.py|
    |dnsCapture|
    ```
# USAGE
- CAPTURE DNS REQUESTS LIVE
    ```python
    import dnsCapture.dnsCapture as dnsCapture
    dns=dnsCapture.DNS_TRAFFIC()
    while True:
        captured=dns.stream('interface',0)
        print(captured)
    ```
- CAPTURE DNS RESPONSES LIVE
    ```python
    import dnsCapture.dnsCapture as dnsCapture
    dns=dnsCapture.DNS_TRAFFIC()
    while True:
        captured=dns.stream('interface',1)
        print(captured)
    ```
- PRINT HELP
    ```python
    import dnsCapture.dnsCapture as dnsCapture
    print(dnsCapture.help())
    ```
- PRINT CREDITS
    ```python
    import dnsCapture.dnsCapture as dnsCapture
    print(dnsCapture.credits())
    ```
