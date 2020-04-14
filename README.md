# dnsCapture
# AUTHOR : Vasilis Manthelas [OFFICIAL-WEBSITE](http://j0ck3r2004.000webhostapp.com/)
Python 3 module for capturing dns traffic
# INSTALLATION
- GITHUB
    ```sh 
    $ git clone https://github.com/j0ck3r2004/dnsCapture/
    ```
- PyPi
    - Windows
    ```sh
    $ pip3 install dnsCapture
    ```
    - Linux
    ```sh 
    $ python3 -m pip install dnsCapture
    ```
# REQUIRMENTS
- python
    | VERSION | RUNS |
    | ------ | ------ |
    | 2.7 | `TRUE` |
    | 3.8 | `TRUE` |
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
    `DNS_TRAFFIC(IFACE,type) | IFACE(string) = your interface, type(1byte) = request(0) or response(1) `
- CAPTURE DNS REQUESTS LIVE
    ```python
    import dnsCapture.dnsCapture as dnsCapture
    dns=dnsCapture.DNS_TRAFFIC()
    while True:
        captured=dns.stream('interface',0)
        print(captured)
    ```
    [RETURNING]
    | NAME | VALUE | MEANING |
    | ------ | ------ | ------ |
    | src | 'x.x.x.x' | localhost |
    | dst | 'x.x.x.x' | DNS |
    | url | 'https://X.X' | requested url |
    
- CAPTURE DNS RESPONSES LIVE
    ```python
    import dnsCapture.dnsCapture as dnsCapture
    dns=dnsCapture.DNS_TRAFFIC()
    while True:
        captured=dns.stream('interface',1)
        print(captured)
    ```
    [RETURNING]
    | NAME | VALUE | MEANING |
    | ------ | ------ | ------ |
    | src | 'x.x.x.x' | DNS |
    | dst | 'x.x.x.x' | localhost |
    | url | 'https://X.X' | requested url |
    | ip  | 'x.x.x.x' | requested url's ip |
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
