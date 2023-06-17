"""
main.py
"""
from alert import AlertAnnouncement

def main():
    alertancmt = AlertAnnouncement()
    alertancmt.crawling_announcement()
    alertancmt.send_mail()

if __name__=="__main__":
    main()