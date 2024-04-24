# DS2 Labs

If you encounter some `UnicodeDecodeError` on any program of mine on Windows, that is usually due to some `open(...)` line of code
To fix that, add `encoding='utf-8'` inside the `open()` function
Example: `open('myfile.txt', 'r')` becomes `open('myfile.txt', 'r', encoding='utf-8')`

Linux automatically does that by default but Windows being the son of a ..., does not.
