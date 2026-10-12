strings = [
    "http://example.com",
    "https://secure.com",
    "http://google.com/search",
    "ftp://files.server.ru",
    "http://my-site.org/page",
    "just some text",
    "https://python.org",
    "http://localhost:8000",
    "www.wikipedia.org",
    "http://api.service.io/v1/data",
    "HTTP://uppercase.com",
    "mailto:user@mail.ru",
    "http://",
    "https://github.com/user/repo",
    "random string here",
]

vi = [s for s in strings if s.startswith("http://")]
print(vi)