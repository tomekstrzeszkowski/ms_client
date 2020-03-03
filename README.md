# Install
##
```
pip install git+https://github.com/tomekstrzeszkowski/ms_client.git
```
### Development installation
Clone and open the repository
```
git clone https://github.com/tomekstrzeszkowski/ms_client ms_client && cd $0
```
Then install it using:
```
pip install -e .
```

# Config
```
export XSTARZ_MARKETSCAN_URL='..'
export XSTARZ_MARKETSCAN_ACCOUNT='..'
```
# Usage
```
import client

c = client.Client('RunScan')
print(c.post('''
{
    "Engine": "MARSE",
    "ScanType": 1,
    ...
}
'''
))

```
