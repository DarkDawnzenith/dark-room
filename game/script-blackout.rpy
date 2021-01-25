# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Commander789 Darkskull Dawn Zenith and Booplicate",
        name="Dark Room Topic",
        description="What if the classroom got a sudden blackout somehow? With this submod, you'll know for sure!",
        version="1.0.4"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Dark Room Topic",
            user_name="DarkDawnZenith",
            repository_name="dark-room",
            update_dir=""
        )

init -1 python: 
    mas_background_def = MASFilterableBackground(
        "submod_dark_room",
        "Dark Room",
        
        # mapping of filters to MASWeatherMaps
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_dark_room_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_dark_room_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_dark_room_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_dark_room_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_dark_room_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_dark_room_night_snow",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_dark_room_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_dark_room_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_dark_room_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_dark_room_snow_ss",
            }),
        ),

        # filter manager
        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        unlocked=False,
        entry_pp=store.mas_background._def_background_entry,
        exit_pp=store.mas_background._def_background_exit,
    )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="blackout",
            category=['mod'],
            prompt="{i}Turn off the lights.{/i}",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.ENAMORED or mas_aff.LOVE, None)
        )
    )

label blackout:
    if mas_isMorning():
        $mas_HKBRaiseShield()
        $HKBHideButtons()
        stop music
        $ morning_flag = False
        $ prev_flt = store.mas_sprites.get_filter()
        $ store.mas_sprites.set_filter(store.mas_sprites.FLT_NIGHT)
        play sound "mod_assets/sounds/effects/powerout.ogg"
        show black zorder 10
        show monika_dark_room zorder 20
        show monika 6wud zorder 30
        show vignette
        pause 1.0
        play music "<loop 0>mod_assets/sounds/amb/eyes.ogg"
        m 3rksdlb "Ahaha~! Who turned off the lights? I don't remember seeing this before..."
        m 1wuo "Wait, that look on your face [player]... You're not feeling uncomfortable are you?"
        m 3rkc "Is it because of the dark? I have to admit, it does feel a bit unsettling. I hope there isn't anything behind me..."
        m 1wkd "...Ah! [player], I'm not the one who's making you scared am I? Is it because of my stare...?"
        m 1hksdlb "Sorry! I don't mean to be creepy or anything! After all you've been through, traumatizing you any further would be pretty awful of me."
        m 2wkd "No, please don't misunderstand [player]. I don't mean you any harm."
        m 3rkc "I don't know what's going on. This is not my doing. Something's not right. The whole game is blacked out except for me and your desktop..."
        m 1cud "I can even hear a creepy sound being played in the background..."
        m 3rtd "Is it a virus? A mod gone wrong? Another corrupted file? I hope not..."
        m 2wfd "Whatever's out there, if it wants to get you, it'll have to go through me first. "
        m 4dsd "I'm going to do a check on your files and see what's going on and maybe run your antivirus as well. Try not to restart your computer okay? As for me, don't worry. I'll be fine."
        m 6hksdlb "Ahaha~! Sorry if I still creep you out..."
        m 5eub "Just don't be scared [player]. I'm here for you remember? If you're feeling squeamish, you can stare at me instead."
        m 5wkb "Let it be a reminder that you're not alone and that I'm here to protect you okay? I still love you, you know."
        window hide
        show monika 1esa
        with Dissolve(0.50)
        pause 181.72
        $HKBShowButtons()
        $ morning_flag = True
        $ prev_flt = store.mas_sprites.get_filter()
        $ store.mas_sprites.set_filter(store.mas_sprites.FLT_DAY)
        hide monika_dark_room
        hide black
        hide vignette
        with Dissolve(8.0)
        stop music fadeout 4.0
        pause 4.0
        $mas_HKBDropShield()
        $ play_song(persistent.current_track, fadein=4.0)
    else:
        $mas_HKBRaiseShield()
        $HKBHideButtons()
        stop music
        play sound "mod_assets/sounds/effects/powerout.ogg"
        show black zorder 10
        show monika_dark_room zorder 20
        show monika 6wud zorder 30
        show vignette
        pause 1.0
        play music "<loop 0>mod_assets/sounds/amb/eyes.ogg"
        m 3rksdlb "Ahaha~! Who turned off the lights? I don't remember seeing this before..."
        m 1wuo "Wait, that look on your face [player]... You're not feeling uncomfortable are you?"
        m 3rkc "Is it because of the dark? I have to admit, it does feel a bit unsettling. I hope there isn't anything behind me..."
        m 1wkd "...Ah! [player], I'm not the one who's making you scared am I? Is it because of my stare...?"
        m 1hksdlb "Sorry! I don't mean to be creepy or anything! After all you've been through, traumatizing you any further would be pretty awful of me."
        m 2wkd "No, please don't misunderstand [player]. I don't mean you any harm."
        m 3rkc "I don't know what's going on. This is not my doing. Something's not right. The whole game is blacked out except for me and your desktop..."
        m 1cud "I can even hear a creepy sound being played in the background..."
        m 3rtd "Is it a virus? A mod gone wrong? Another corrupted file? I hope not..."
        m 2wfd "Whatever's out there, if it wants to get you, it'll have to go through me first. "
        m 4dsd "I'm going to do a check on your files and see what's going on and maybe run your antivirus as well. Try not to restart your computer okay? As for me, don't worry. I'll be fine."
        m 6hksdlb "Ahaha~! Sorry if I still creep you out..."
        m 5eub "Just don't be scared [player]. I'm here for you remember? If you're feeling squeamish, you can stare at me instead."
        m 5wkb "Let it be a reminder that you're not alone and that I'm here to protect you okay? I still love you, you know."
        window hide
        show monika 1esa
        with Dissolve(0.50)
        pause 181.72
        $HKBShowButtons()
        hide monika_dark_room
        hide black
        hide vignette
        with Dissolve(8.0)
        stop music fadeout 4.0
        pause 4.0
        $mas_HKBDropShield()
        $ play_song(persistent.current_track, fadein=4.0)
    return

image monika_dark_room = ConditionSwitch(
    persistent._mas_current_background == "spaceroom", "dark_space",
    persistent._mas_current_background == "submod_background_Den", "dark_den",
    persistent._mas_current_background == "submod_background_Furnished_spaceroom1", "dark_furnish1",
    persistent._mas_current_background == "submod_background_Furnished_spaceroom2", "dark_furnish2",
    persistent._mas_current_background == "submod_background_Furnished_spaceroom3", "dark_furnish3",
    persistent._mas_current_background == "submod_background_Kitchen", "dark_kitchen"
    )

image dark_space = "mod_assets/location/spaceroom/spaceroom-d.png"
image dark_den = "mod_assets/location/Den V1.1/den1.1-d.png"
image dark_furnish1 = "mod_assets/location/Spaceroom V1.1/V1.1-d.png"
image dark_furnish2 = "mod_assets/location/Spaceroom V2.2/V2.2-d.png"
image dark_furnish3 = "mod_assets/location/Spaceroom V3.1/V3.1-d.png"
image dark_kitchen = "mod_assets/location/Kitchen/kitchen-d.png"
