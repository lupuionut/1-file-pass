# 1-file-pass
Basic password manager to list/add encrypted passwords with a Qt GUI. Passwords are stored in a single file, a sqlite db.
Each password is encrypted using scrypt library with a master password that is stored in the db, encrpyted.

## Instructions
Download repo. Navigate to directory. Run **make install**. Run the executable from dist folder.
```bash
cd /path/to/1-file-pass
make install
./dist/1fpass
```

## Screenshots

![Dashboard](https://i.imgur.com/cVB2tFs.png)

![Adding a new password](https://i.imgur.com/91prdme.png)

![Display passwords](https://i.imgur.com/OPS8tQJ.png)