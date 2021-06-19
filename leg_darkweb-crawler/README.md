# DarkWeb Crawler
* Scrape Onion and normal links.
* Save the output in html format in Output folder.

<br/>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<br/>

### Prerequisites

* You will need **Python3** to run this project smoothly. Go to your terminal and execute the following command or visit [Python3](https://www.python.org/download/releases/3.0/) website.

```
[sudo] apt-get install python3 python3-dev
```

* You can install **Tor** by going to their website - https://www.torproject.org/


Python packages can be installed either globally (a.k.a system wide), or in user-space. We do not recommend installing TorScrapper system wide.

Instead, we recommend that you install our system within a so-called “virtual environment” (virtualenv). `virtualenv` allow you to not conflict with already-installed Python system packages (which could break some of your system tools and scripts), and still install packages normally with pip (without sudo and the likes).

To get started with virtual environments, see `virtualenv` installation instructions. To install it globally (having it globally installed actually helps here), it should be a matter of running:

```
[sudo] pip install virtualenv
```
<br/>

## Basic setup

Before you run the Bot make sure the following things are done properly:

* Check tor service

  `service tor status`

  ```bash
  ● tor.service - Anonymizing overlay network for TCP (multi-instance-master)
       Loaded: loaded (/lib/systemd/system/tor.service; enabled; vendor preset: enabled)
       Active: active (exited) since Tue 2021-05-11 07:08:42 KST; 31min ago
      Process: 882 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
     Main PID: 882 (code=exited, status=0/SUCCESS)

* Run tor service
`sudo service tor start`

* Check `torrc` in `/etc/tor/torrc`

  You can find _**ControlPort 9051**_ in `torrc`

  **Uncomment This Part & Check your HashedControlPassword16:XXXX...**

  ```
  # The port on which Tor will listen for local connections from Tor
  # controller applications, as documented in control-spec.txt.
  ControlPort 9051
  # If you enable the controlport, be sure to enable one of these
  # authentication methods, to prevent attackers from accessing it.
  HashedControlPassword 16:XXXX...
  CookieAuthentication 1
  ```

* Give the password inside `HashedControlPassword` file, you need to make yourself.

* Reference by `.gitignore` file in `crawler` directory & `crawl_bot.py`

<br/>

>  Read more about torrc here : [Torrc](https://github.com/ConanKapoor/TorScrapper/blob/master/Tor.md)

<br/>

### Deployment

A step by step series of examples that tells what you have to do to get this project running

* Enter the project directory.
* Copy all the onion and normal links you want to scrape in _onions.txt_

```
[nano]/[vim]/[gedit]/[Your choice of editor] onionlinks.txt
```

* Run TorScrapper.py using Python3

```
[sudo] python3 TorScrapper.py
```

* Check the scraped outputs in Output folder. Look into the codebase and you can edit where to save your files. Currently, it saves into a folder named hacking because the links given are related to that and hence that directory needs to be created beforehand too.

* The code saves one file for each domain and strips out subdomain html text and appends it to the same file which is under the name of the domain.

* The code employs BFS by using a queue to visit related urls from the seed url and a file crawled.txt is maintained for each folder so that same links aren't called again.

* A folder is created for each of the seed urls and all the related URLs are added to it

<br/>

## Built With

* [Python](https://www.python.org/) - Python programming language.
* [Tor](https://www.torproject.org/) - If you don't know about Tor then you probably shouldn't be here :)

<br/>