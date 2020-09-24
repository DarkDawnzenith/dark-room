# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Commander789 (in Reddit) Darkskull Dawn Zenith and Booplicate",
        name="Dark Room Topic",
        description="What if the classroom got a sudden blackout somehow? With this submod, you'll know for sure!",
        version="1.0.0"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Dark Room Topic",
            user_name="Darkskull Dawn Zenith",
            repository_name="dark-room",
            update_dir=""
        )

init 5 python:
    if persistent.playername == "Ronald":
        addEvent(
            Event(
                persistent.event_database,
                eventlabel='blackout',
                category=['mod'],
                prompt="Can you test this new feature?",
                pool=True,
                unlocked=False,
                rules={"no_unlock": None}
            )
        )
    else:
        addEvent(Event(persistent.event_database,eventlabel="blackout",category=['mod'],prompt="Easter Egg",random=True))

    if persistent._mas_current_background == "spaceroom":
        addEvent(Event(persistent.event_database,eventlabel="blackout",category=['mod'],prompt="Easter Egg",random=True))
    else:
        print("ch30_loop")

label blackout:
    if mas_isMorning():
        m 1eub "Okay!"
        $mas_HKBRaiseShield()
        $HKBHideButtons()
        pause 7.0
        stop music
        $ morning_flag = False
        $ prev_flt = store.mas_sprites.get_filter()
        $ store.mas_sprites.set_filter(store.mas_sprites.FLT_NIGHT)
        play sound "mod_assets/sounds/effects/powerout.ogg"
        show black zorder 10
        show monika_dark_room zorder 20
        show monika 6wud zorder 30
        pause 1.0
        play music "<loop 0>mod_assets/sounds/amb/eyes.ogg"
        m 3rksdlb "Ahaha~! Who turned off the lights? I don't remember seeing this before..."
        m 1wuo "Wait, that look on your face [player]... You're not feeling uncomfortable are you?"
        m 3rkc "Is it because of the dark? I have to admit, it does feel a bit unsettling. I hope there isn't anything behind me..."
        m 1wkd "...Ah! [player], I'm not the one who's making you scared am I? Is it because of my stare...?"
        m 1hksdlb "Sorry! I don't mean to be creepy or anything! After all you've been through, traumatizing you any further would be pretty awful of me."
        m 2wkd "No, please don't misunderstand [player]. I don't mean you any harm."
        m 3rkc "I don't know what's going on. This is not my doing. Something's not right. The whole game is blackened out except for me and your desktop..."
        m 1cud "I can even hear a creepy sound being played in the background..."
        m 3rtd "Is it a virus? A mod gone wrong? Another corrupted file? I hope not..."
        m 2wfd "Whatever's out there, if it wants to get you, it'll have to go through me first. "
        m 4dsd "I'm going to do a check on your files and see what's going on and maybe run your antivirus as well. Try not to restart your computer okay? As for me, don't worry. I'll be fine."
        m 6hksdlb "Ahaha~! Sorry if I still creep you out..."
        m 5eub "Just don't be scared [player]. I'm here for you remember? If you're feeling squeamish, you can stare at me instead."
        m 5wkb "Let it be a reminder that you're not alone and that I'm here to protect you okay? I still love you, you know."
        window hide
        show monika 1esa
        with Dissolve(0.15)
        pause 120.0
        hide monika_dark_room
        hide black
        $ morning_flag = True
        $ prev_flt = store.mas_sprites.get_filter()
        $ store.mas_sprites.set_filter(store.mas_sprites.FLT_DAY)
        with Dissolve(8.0)
        stop music fadeout 8.0
        $HKBShowButtons()
        $mas_HKBDropShield()
        pause 0.15
        $ play_song(persistent.current_track, fadein=5.0)
    else:
        m 1eub "Okay!"
        $mas_HKBRaiseShield()
        $HKBHideButtons()
        pause 7.0
        stop music
        play sound "mod_assets/sounds/effects/powerout.ogg"
        show black zorder 10
        show monika_dark_room zorder 20
        show monika 6wud zorder 30
        pause 1.0
        play music "<loop 0>mod_assets/sounds/amb/eyes.ogg"
        m 3rksdlb "Ahaha~! Who turned off the lights? I don't remember seeing this before..."
        m 1wuo "Wait, that look on your face [player]... You're not feeling uncomfortable are you?"
        m 3rkc "Is it because of the dark? I have to admit, it does feel a bit unsettling. I hope there isn't anything behind me..."
        m 1wkd "...Ah! [player], I'm not the one who's making you scared am I? Is it because of my stare...?"
        m 1hksdlb "Sorry! I don't mean to be creepy or anything! After all you've been through, traumatizing you any further would be pretty awful of me."
        m 2wkd "No, please don't misunderstand [player]. I don't mean you any harm."
        m 3rkc "I don't know what's going on. This is not my doing. Something's not right. Even your entire desktop is blackened out except for the game. "
        m 1cud "I can even hear a creepy sound being played in the background..."
        m 3rtd "Is it a virus? A mod gone wrong? Another corrupted file? I hope not..."
        m 2wfd "Whatever's out there, if it wants to get you, it'll have to go through me first. "
        m 4dsd "I'm going to do a check on your files and see what's going on and maybe run your antivirus as well. Try not to restart your computer okay? As for me, don't worry. I'll be fine."
        m 6hksdlb "Ahaha~! Sorry if I still creep you out..."
        m 5eub "Just don't be scared [player]. I'm here for you remember? If you're feeling squeamish, you can stare at me instead."
        m 5wkb "Let it be a reminder that you're not alone and that I'm here to protect you okay? I still love you, you know."
        window hide
        show monika 1esa
        pause 120.0
        hide monika_dark_room
        hide black
        with Dissolve(8.0)
        stop music fadeout 8.0
        $HKBShowButtons()
        $mas_HKBDropShield()
        pause 0.15
        $ play_song(persistent.current_track, fadein=5.0)
    return
