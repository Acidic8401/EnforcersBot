import discord


def find(name, hacker, crasher, rwt, tracker, scammer):
    if hacker == True:
        hackflag = ":white_check_mark:"
    else:
        hackflag = "❌"
    if crasher == True:
        crashflag = ":white_check_mark:"
    else:
        crashflag = "❌"
    if rwt == True:
        rwtflag = ":white_check_mark:"
    else:
        rwtflag = "❌"
    if tracker == True:
        trackflag = ":white_check_mark:"
    else:
        trackflag = "❌"
    if scammer == True:
        scamflag = ":white_check_mark:"
    else:
        scamflag = "❌"
    em = discord.Embed(
        title=f"**Data for:** {name}",
        description=
        f"`Hacker:` {hackflag} \n `Crasher:` {crashflag} \n `RWTer:` {rwtflag} \n `Tracker:` {trackflag} \n `Scammer:` {scamflag}",
        color=discord.Color.random())
    return em

def deepfind(name, hacker, crasher, rwt, tracker, scammer, proofurl):
    if hacker == True:
        hackflag = ":white_check_mark:"
    else:
        hackflag = "❌"
    if crasher == True:
        crashflag = ":white_check_mark:"
    else:
        crashflag = "❌"
    if rwt == True:
        rwtflag = ":white_check_mark:"
    else:
        rwtflag = "❌"
    if tracker == True:
        trackflag = ":white_check_mark:"
    else:
        trackflag = "❌"
    if scammer == True:
        scamflag = ":white_check_mark:"
    else:
        scamflag = "❌"
    
    em = discord.Embed(
        title=f"**Data for:** {name}",
        description=
        f"`Hacker:` {hackflag} \n `Crasher:` {crashflag} \n `RWTer:` {rwtflag} \n `Tracker:` {trackflag} \n `Scammer:` {scamflag}",
        color=discord.Color.random())
    proof = f"https://{proofurl}"
    if "jpg" in proof or "png" in proof:
        em.set_image(url=proof)
    else:
        em.add_field(
            name="**Proof**",
            value=f"`Proof URL:` {proof}"
        )
    return em