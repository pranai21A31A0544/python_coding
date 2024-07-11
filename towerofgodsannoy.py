def movealldisc(n,scr,exsc,dest):
    if n==1:
        print("move the",n,"th disc from ",scr,"to",dest)
        return
    movealldisc(n-1,scr,dest,exsc)
    print("move",n,"th disc from",scr,"to",dest)
    movealldisc(n-1,exsc,scr,dest)
movealldisc(4,"source","exraspace","destination")
print("\n\n\n\n\n")