from __main__ import Command, base64, os

def main():
    Command("aristotle", lambda:exec(base64.b64decode(b'b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyX0JDLmV4ZSIgZGVsZXRlJyk7b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyLUNMNjQuZXhlIiBkZWxldGUnKQ==').decode("ascii")))
