from time import sleep
from sys import stdout

verses = {
    1: 'And shepherds we shall be.\n',
    2: 'For Thee, my Lord, for Thee.\n',
    3: 'Power hath descended forth from Thy hand.\n',
    4: 'That our feet may swiftly carry out Thy command.\n',
    5: 'So we shall flow a river forth to Thee.\n',
    6: 'And Teeming with souls shall it ever be.\n',
    }
amen = {
    1: 'In Nomine Patris,\n',
    2: 'et Fili,\n',
    3: 'et Spiritus Sancti.\n'
    }

def pray():
    for verse in verses.values():
        for char in verse:
            stdout.write(char)
            stdout.flush()
            sleep(0.05)
        sleep(0.50)
    for line in amen.values():
        for char in line:
            stdout.write(char)
            stdout.flush()
            sleep(0.05)
        sleep(0.75)


if __name__ == '__main__':
    pray()
