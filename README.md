# equable-destruction
> v. 20230217

> author: @southwickIO
<br>

## Overview
### This app is under development.
 Evercookie related research and scripts to find evercookies.
<br>

Research was framed around [OP's creation](https://github.com/samyk/evercookie).
<br>

## Script Order
```mermaid
graph LR
A[evercookie.py] -- 1 --> B(FindHTMLCookies.py)
A[evercookie.py] -- 2 --> C(FindLocalShareObjects.py)
A[evercookie.py] -- 3 --> D(FindIsolatedStorage.py)
A[evercookie.py] -- 4 --> E(FindSessionStorage.py)
A[evercookie.py] -- 5 --> F(FindLocalStorage.py)

G[leveldb-dump.py] --> E(FindSessionStorage.py)
G[leveldb-dump.py] --> F(FindLocalStorage.py)

B(FindHTMLCookies.py) ----> H[SpreadsheetHandler.py]
E(FindSessionStorage.py) ----> H[SpreadsheetHandler.py]
F(FindLocalStorage.py) ----> H[SpreadsheetHandler.py]


```

## Script Descriptions
 1. FindHTMLCookies.py - Checks for simple HTML cookies from Chrome and Firefox. Apt and Snap examples.
 2. LocalShareObjectFinder.py - Checks for the presence of LSOs, but doesnt print to spreadsheet since LSOs are deprecated.
 3. FindIsolatedStorage.py - Supposed to check for the presense of Isolated Storage. It was a Silverlight feature and there is no indication that Edge uses this.
 

## Dependencies
 1. openpyxl
 2. leveldb (if using helpful repositories)
 3. PyQt5 (if using helpful repositories)

## Notable file paths (Ubuntu 22.04)
1. ~/.config/google-chrome/\<profile\>/Cookies
2. /snap/firefox/common/.mozilla/firefox/\<profile\>.default/
3. ~/.config/google-chrome/\<profile\>/LocalStorage
4. ~/.config/microsoft-edge/\<profile\>/LocalStorage

## evercookie.py useage
 1. All scripts are written for Ubuntu file system.
 2. All scripts are written for one profile/user.
 3. Chromium related browsers were installed with dpkg
 4. Firefox was installed with snap
 5. Review each script before first runtime and make changes as needed.
 6. evercookie.py needs to be run as sudo if you want LocalShareObjectFinder.py to have permissions to check everywhere for LSO objects. Otherwise, its just looking for user LSO objects.

## Helpful Repositories
1. [markmckinnon/Leveldb-py](https://github.com/markmckinnon/Leveldb-py) - LevelDB viewer and dumper

## Tasks
- [x] evercookie.py (Main)
- [x] Standard HTTP Cookies
- [x] Flash Local Shared Objects
- [ ] Silverlight Isolated Storage
- [ ] CSS History Knocking
- [ ] Storing cookies in HTTP ETags (Backend server required)
- [ ] Storing cookies in Web cache (Backend server required)
- [ ] HTTP Strict Transport Security (HSTS) Pinning (works in Incognito mode)
- [ ] window.name caching
- [ ] Internet Explorer userData storage
- [ ] HTML5 Session Storage <-----
- [ ] HTML5 Local Storage <-----
- [ ] HTML5 Global Storage <-----
- [ ] HTML5 Database Storage via SQLite
- [ ] HTML5 Canvas (Backend server required)
- [ ] HTML5 IndexedDB
- [ ] Java JNLP PersistenceService
- [ ] Java exploit CVE-2013-0422
- [ ] Update FindHTMLCookies.py to include Microsoft Edge
- [ ] Port for Windows and MacOS

## Resources
1. [View, edit, and delete cookies in Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/storage/cookies)
2. [Microsoft Edge Developers](https://learn.microsoft.com/en-us/microsoft-edge/developer/)
3. [Chrome Developers](https://developer.chrome.com/docs/)
4. [Chromium Developers](https://www.chromium.org/developers/)
5. [Firefox Developers](https://developer.mozilla.org/en-US/)
6. [Microsoft Edge Developers: Store data on the device](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/offline)
7. [Chromium Session Storage and Local Storage](https://www.cclsolutionsgroup.com/post/chromium-session-storage-and-local-storage)
8. [Hang on! That’s not SQLite! Chrome, Electron and LevelDB](https://www.cclsolutionsgroup.com/post/hang-on-thats-not-sqlite-chrome-electron-and-leveldb)
9. [Microsoft Developes: Isolated Storage](https://learn.microsoft.com/en-us/dotnet/standard/io/isolated-storage)
