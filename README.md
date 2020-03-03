# Install
##
```
pip install git+https://github.com/tomekstrzeszkowski/ms_client.git
```
### Development
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
