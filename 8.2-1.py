from urllib.parse import urlparse
from pathlib import Path

url = 'http://test.com/dir1/dir2/dir3/page.html'
page = Path(urlparse(url).path).name
print(page)