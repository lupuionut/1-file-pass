# 1-file-pass
Basic password manager. It keeps your passwords encrypted, using scrypt. Makes use of a master password for listing/password encryption.

The GUI is built using PyQt library.

What you can do:
* add a new entry containing url, username, password and extra info
* list all entries
* filter entries by username/url
* copy to clipboard a certain password
* remove an entry from the database

## Instructions
Download repo. Navigate to directory. Run **make install**. Run the executable from dist folder.
```bash
cd /path/to/1-file-pass
make install
./dist/1fpass
```

When you first execute the program, it will automatically generate a .db
file where all your entries will get stored. When you add a new entry,
you will be asked for a database password (the master password). If it's the first time, this master password is not set, so whatever you use will become your database password, in order to list all your entries or add new entry.

## Screenshots

![Dashboard](https://i.imgur.com/cVB2tFs.png)

![Adding a new password](https://i.imgur.com/91prdme.png)

![Display passwords](https://i.imgur.com/OPS8tQJ.png)
