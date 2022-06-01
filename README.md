# Scrape the source

The purpose of this program is pull data from some pages that provide useful news about IT.
v1.1


## Usage

If you want to use it normally just run this in the terminal:
```bash
python3 main.py
```

If you are using windows you can create an exe file, but first if you don't have it install Pyinstaller and run:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

## Contributing
Pull requests are welcome. if there is a website you'd like to add just create the file with the name of the website. if you like can enheritance from the BasicActions class just to avoid repeting things such as cleaning the console or getting a response printed, but since websites are pretty unique most of the time you'll have to implement it.
