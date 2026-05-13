# The script of the game goes in this file.

init:
    define mc = Character("mc")
    define nill = Character("????")
    define r1 = Character("Ran | Remora", color="#5c88ac")
    define r2 = Character("Hapi | Remora", color="#5c88ac")
    define r3 = Character("Anju | Remora", color="#5c88ac")
    define r4 = Character("Alice | Remora", color="#5c88ac")
    define r5 = Character("Wendy | Remora", color="#5c88ac")
    define l = Character("Sasha | Lemon Shark", color="#7d4938")
    define o = Character("Reign| Orca", color="#4e4f65")
    define m = Character("Keira | Moray Eel", color="#8b5493")
    define p = Character("Lilith | Giant Phantom Jellyfish", color="#90525f")
    define a = Character("Styx | Anglerfish", color="#6b5c9b")
    #colour are ideas though i think it might be better to not bother.

    #backgrounds
    #character sprites
        #remora
            image r = Image("")
            image r = Image("")
            image r = Image("")
            image r = Image("")

        #lemon shark
    image l1 = Image("")   #neutral
    image l2 = Image("")   #grin
    image l3 = Image("")   #confused
    image l4 = Image("")   #concerned
      
        #orca
    image o1 blush advert = Image("")   #neutral
    image o2 blush advert = Image("")
    image o3 blush advert = Image("")
    image o4 blush advert = Image("")
       
        #moray eel
    image m1 blush advert = Image("")
    image m2 blush advert = Image("")
    image m3 blush advert = Image("")
    image m4 blush advert = Image("")
       
        #giant phantom jellyfish
    image p1 blush advert = Image("")
    image p2 blush advert = Image("")
    image p3 blush advert = Image("")
    image p4 blush advert = Image("") 
            #blushing        
        image p1 blush = Image("")
        image p2 blush = Image("")
        image p3 blush = Image("")
        image p4 blush = Image("")
      
         #angler fish
    image a1 = Image("")   #neutral
    image a2 = Image("")   #raised brow
    image a3 = Image("")   #amused
    image a4 = Image("")   #pissed


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene sunlight
    scene twilight
    scene midnight
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy



label intro
#more for the ending but what if ur the only one who can see them as 'people' and you're sent in cus mc just has a way with fish?
# like ur borderline crazy :3
# added it so it is implied that others see them as just a their normal sea cretin but you can acc see n yap to em.
    "Yapper yapper put your fucking name here prick. literally change this to fit the context however yu want cus ima cry if i do anymore tippytaps."

    $ mc = renpy.input("Your Name is...", length=25)
   
    $ mc = mc.strip()
    
    if mc == "":
        $ mc="MC"

label next_part:
    "And your name is [mc], you can confirm?"
    menu:
        "Yes":
            pass
        "This doesn't seem right...":
            jump intro
    "Good. Seems like you aren't all that out of sorts today."
    "Unlike how you usually are..."
    "Well, since you have your special little way with sea creatures, how about you do something a little different for us this time around."

 #n carry on yapper yapper. but like, we wanted it to go bzztt, this ur job btw. repeat ur name? ok good, bet. fuck off to the goolags cunt


label remora intro
    "A face suddenly appears, staring up at you with wide, expant eyes. You stumble slightly as you try to regain both your footing and composure."
    mc "Woah!"
    nill "Wow, you're new, aren't you?"
    mc "Is it that obvious? Uhh..."
    nill "It's pretty obvious, yeah!"
    r3 "I'm Anju, by the way! Hehes!"
    mc "Anju? I'm [mc]. It's uh, nice to meet you?"
    r3 "It's been a while since we've had a new diver around."
    r3 "But you're a little different, aren't you?"
    r3 "I've never been able to talk to one before!"
    "Before you could answer, another pops up behind her, brows furrowed."

    nill "Anju, what are you..." #r1
    nill "..." #r1
    nill "Oh! A new face, a new face!" #2
    nill "...Who's that?" #4
    nill "Seems like new company." #5
    nill "And they can talk to us just fine...? Isn't that weird...?" #4
    mc "Oh god! Uh, there are five of you?"
    nill "Obviously." #r1
    r3 "This is [mc]. [mc], this one is-"
    r2 "I'm Hapi! Nice to meet ya!"
    r3 "...Yep. And here's Alice."
    r4 "..."
    r4 "Hi..."
    r5 "And I'm Wendy."
    r1 "...It's Ran."
    mc "R-right! Wow- uh-"
    mc "All those names... It's sort of diffcult to remember."
    r5 "Oh, it's alright. It will stick."
    mc "Uhh so you're Hapi... and you are... Al- wait no-"
    r3 "Is it really that hard to remember? Hmm..."
    r2 "Well you know the saying!"
    r2 "There {i}are{/i} plenty of fish in the sea! It's not like it's easy to remember all of em!"
    r1 "We're not in the sea."
    r2 "Well- I- I know that!"
    r2 "In the dome! There's a lot of us!"
    r1 "I think we're getting distracted from the fact that the human is probably here for a reason."
    r5 "Well it can't be for us. We've already had people come in today." 
    r3 "Hmm? I mean, I never got the chance to ask..."
    r1 "What? We're talking about you, you know. Aren't you going to tell us?"
    mc "Well, I'm supposed to be going to the Midnight Dome and bring supplies to them."
    r1 "The Midnight Dome? Shouldn't there be two people for that job?"
    r2 "Oh no..."
label lemon shark intro
    nill "So here's where you all went?"
    nill "You don't usually leave my sight unless... aah?"
    mc "Hello? It's nice to meet you?"
    nill "Who?"
    r5 "This is [mc]. They're supposed to be heading to the Midnight Dome."
    nill "...Aren't you a strange one?"
    l "Well, [mc]. You can just call me Sasha!"
    r2 "Or puppy!"
    r3 "Pups if you really wanna annoy him!"
    mc "Pups?"
    l "Quiet, you two! It's everytime!"
    r1 "...! Oh..."
label orca intro
    "A heavy, looming shadow sweeps over, your heart nearly skipping a beat as you turn around to face the source of your discomfort."
    "Besides you, Sasha lets out an agitated huff, clearly unhappy to see the man"
    l "Great, just what we needed."
    l "Can't keep yourself away from me, huh?"
    l "It hasn't even been a minute."
    o "... It's rude to swim off during a conversation."
    o "Besides... swimming off to bother a human?"
    o "Dont' tell me you're doing all this on purpose?"
    l "The hell are you talking about..."
    mc "Uh, hi? I'm [mc], it's good to meet you!"
    mc "I don't think I've ever met so many animals all in the first hour."
    o "{i}It{/i} can understand?"
    r2 "Haha, he called them {i}it{/i}!!"
    r5 "It's rude to laugh, Hapi."
    l "Reign, don't be an ass."
    mc "For an Orca..."
    mc "Well for some reason... I thought you'd be bigger..."
    o "Bigger?"
    mc "Well, not bigger but... Maybe more scary?"
    o "Oh, so I'm not scary enough for you?"
    l "Ignore him. He's just messin around."
    r1 "You say that Sasha but he's always coming over here and starting fights..."
    r2 "I think a food contest should do it!"
    r3 "Dont you mean a hunting contest?"
    r2 "Hm? Same thing!"
    r4 "...or a fight. To show who's better."
    l "I really don't want to do that..."
    r2 "But we have to decide the winner somehow..."
    r3 "Then maybe a quiz? Those are fun!"
    o "No way. I'm not doing that."
    r2 "What! Come on, why not?!"
    o "Every quiz done by your girls get rigged from the start. I ain't entertaining that."
    r2 "That's so unfair!"
    r5 "But if [mc] is the judge, then it won't be so unfair?"
    r5 "How about it."
    o "..."

label quiz shark and orca
    r3 "How about... when we think of a question, that will be directed to the both of you!"
    r3 "Sasha can answer first, and Orca after. That way it really does feel like a match!"
    r3 "...What do we think?"
    o "How would the little human be a judge then, if that's how we'll be doing it?"
    r3 "Well..."
    r5 "They get to decide on who's better, based on the facts. Isn't that the best way to do it?"
    r2 "Woah, yeah! I like that!"
    l "Well, I have no complaints."
    o "Of course you wouldn't. All you know how to do is go along with everything, don't you?"
    l "H-hey! That ain't true at all!"
    r2 "Yeah! He doesn't {i}always{/i} go along with {i}everything{/i}!"
    r1 "Loud..."
    r4 "Are you mad Sasha gets to go first..?"
    l "Pff- yeah! Just because I'm better than you! Nerd."
    o "In what way did you come to that conclusion..?"
    l "Can't hear ya' over how jealous you are."
    o "Sigh. Let's get this over with."
    o "...Can already feel a headache coming on..."
    r2 "The first question!"
    r2 "Hmmmm..."
    r3 "..."
    r3 "How about the reasons for their name?"
    r2 "What? Their reason for being called Sasha? How am I supposed to know that..."
    r1 "Their {i}other{/i} name. You know, their species?"
    r2 "Oh! Haha, I knew that!"
        #Q1 Their namee
        menu:
            "Where do Lemon Sharks get their name?"
            "Natural Camoflage":
                l "Why is this sorta embarrassing..."
                r3 "Uh, huh! It's because Lemon sharks can blend into the sand!"
                r3 "But their colours also change with age. That was also a right answer!"
                o "Adding multiple answers now?"
                r2 "It's allowed!"
            "Their colour changes with age":
                r3 "That's right!"
                l "Yeah. As pups lemon sharks are {i}pretty{/i} yellow to start with."
                l "Obviously as time goes by, our colour tends to turn more into a greyish-brown?"
                r5 "You still have that yellow tint though."
                r3 "Oh but the other reason is because of natural camoflage. Lemon sharks can blend into the send easily so..."

            "They taste like lemons":
                r2 "Hehe! Lemons!"
                l "God..."
                r3 "Sorry, I had to slip in a fun one!"
                r3 "The actually reasoning for their names though is because of the fact that their colour changes with age and how lemon sharks can blend into the sand!"
                o "Pff, you should've seen how {i}yellow{/i} Sasha was as a pup."
                r4 "...I wish I could see..."
                r2 "Reign always gets to know more about Sasha! It's so not fair!"
                o "...How is that in my control?"

        menu:
            "Where do Orcas get their name?"
            "That's the noise they make":
                r2 "BAHAHA! That's a great one!"
                r4 "Heh...It {i}is{/i} pretty funny."
                o "...like a seal?"
                o "Real funny."
                o "Keep your girls in check, blondie."
                l "Wha, me?! They're just playing."
                o "Orcas are referred to large-bellied pots or casks. In this sense, whales."
                l "Despite you not even being a whale?"
                o "...Exactly right."
                r4 "Orcas aren't whales...?"
                o "We're dolphins."
                r4 "Oh... that as pretty cool..."
                r2 "Alice! You're siding with the wrong team!"
                r4 "A-ah, my bad."
            "Big like orc":
                r2 "Woaha, so fitting!"
                o "..."
                o "Real nice."
                r5 "Well, it is quite accurate."
                l "I'm so proud."
                o "The real meaning of my name, since you are to be the judge..."
                o "And obviously because this has been rigged from the start. Ah-hem."
                r4 "He's talking about us..."
                o "The real meaning is a latin translation for large-bellied pots or casks."
                o "In my sense, it would be... whales. Despite not even being a whale."
                l "Oh, that's right. You guys are dolphins, aren't ya?"
                l "No wonder you're so messed up!"
                o "...are you trying to pick a fight?"
                l "What, me? No... never!"
                l "I have no idea what you're talkin about!"
            "Large-bellied whale":
                o "Which is ironic since Orca's aren't even whales, we're dolphins."
                mc "What I'm trying to figure out is how 'large-bellied whale' would be related to the name?"
                o "It's because in latin, Orca refers to a large-bellied pot or cask. It's just to describe the appearance of my species, more than anything."
                l "Isn't it also part of that one underworld deity? Humans seem to love that sorta thing."
                l "Orcus or something."
                o "...Orcinus is derived from the Roman underworld deity Orcus, yes."
                o "It translates to 'the kingdom of the dead' or 'belonging to orcus'."
                r5 "I didn't think you paid attention to that kind of thing?"
                o "..."
                l "I... I don't! It just stuck with me!"
                l "Don't give me that look..."
                o "Uh huh? Aren't we supposed to be competing against each other?"
                o "But here you are, proving that I'm better once again."
                l "I will never do anything nice for you, ever!"

        #Q2 types of orcas and sharks
        r4 "How about the types of Sharks and Orcas?"
        r3 "That's good, yeah-"
        r2 "What? No way that's so boring!"
        r2 "I was thinking along the lines of..."
        r1 "Something to do with food, probably."
        r2 "Wha?! How'd you find that out?!"
        r1 "Told ya."
        r5 "We should have 1 question each to ask to make this fair."
        r5 "Otherwise, this may take all day."
        r1 "Yeah Hapi. And you can't just say it's {i}boring{/i} and move on."
        r2 "But {i}you{/i} do that to me all the time!"
        r1 "...And?"
        r2 "Okay, fine! But I'm asking the next question!"
        r5 "Alice? That's your queue to ask your question."
        r4 "Ah, okay..."
        r4 "How many species of sharks and orcas are there?"
        menu:
            "How many species of sharks are there?"
            "Around 200":
                r4 "Uh..."
                r1 "Are you serious right now?"
                r2 "Even {i}I{/i} know that much!"
                mc "I panicked! It's hard to keep up."
                l "Let's take a step back, yeah?"
                l "Not everyone knows everything about sharks, come on girls."
                r2 "Well they {i}should{/i}!"
                o "God, such little suck ups..."
                o "...Quite literally"
                r5 "Because we're suckerfish?"
                l "There are approximately 500 to over 550 different species of shark that are known right now."
                l "So... a little more than 200."
            "Around 400":
                r3 "Oh, you were close!"
                o "Though evidently not close enough."
                r2 "It's still close!"
                r4 "Ah... so, yes. The approximated amount is 500 to over 550 species of shark that are currently known."
                r4 "So you were really close. Thank god."
                r2 "It ain't that serious... who cares if they're close, it's a dumb question!"
                l "Be nice, Hapi. The question was good."
                r2 "How is this supposed to with beating Reign!"
                l "Well the more of me, the cooler, right? Numbers don't lie!"
                r2 "Well... if you phrase it like that, I guess..."
                o "..."
                o "How about my turn now?"
            "Around 500":
                r2 "Uh-huh! There are approximately 500 to over 550 species of shark that are currently known!"
                r4 "It's really cool..."
                r2 "Not as cool as Sasha though!"
                r4 "Oh, yeah! Not as cool as Sasha!"
            "Around 820": #
                r1 "Why specifically did you choose 820?"
                r4 "Oh... I just wanted to mix it up a little..."
                r4 "...Was that not good?"
                r1 "N-no. It was good."
                r4 "Really?"
                r4 "I'm glad..."
                r5 "... and the correct answer, Alice?"
                r4 "Oh, right! It was over 500!"
                r4 "There are approximately 500 to over 550 species of shark that are known currently."
                l "Great job, Alice."
                r4 "Hehe..."
            "How many species of orcas are there?"
            "1 type":
                o "So you are aware of my game, hm?"
                o "But yes, all orcas are classified as one species. Though we do have at least 10 different 'ecotypes'."
                o "It would be a whole ramble to explain it though."
                l "The jist of it though is that worldwide different orcas have different appearances, diets and behaviours. Real weird, huh?"
                l "But they're still classed as just one species... I don't get it at all."
                r2 "Sasha, no! You're not supposed to be helping the enemy!"
                l "H-huh? Oh, my bad!"
                l "Ignore me! Uh- all orcas are the same and suck!"
                o "Pff... idiot."
                o "How about we move on, yeah?"
            "Near 5":
                o "There is only one species of orca."
                o "...What? You look surprised. Didn't expect it?"
                l "Well {i}I{/i} think they're just being lazy with it!"
                l "Different appearances, diets and behaviours of Orcas across the world but it's an 'ecotype' not a species?"
                l "Stuuupidd ~"
                r4 "Um... wasn't this supposed to be a competition?"
                r5 "Yup."
                r1 "That's right. Though you know Sasha..."
                l "Ack! That's right!"
                l "Forget I even said anything!"
            "Around 8": 
                o "Nice try, but just there's just one."
                o "One species and 10 different 'ecotypes'. It's a whole pain to explain but supposedly, they has been suggested potential reclassification of this."
                l "They sure are taking their damn time with that, god."
                o "It isn't too big of a deal. It's not like it effects us in anyway."
                l "I guess not but still..."
                l "I'd  be annoyed. I know that much."
            "At least 10":
                o "There are at least 10 different 'ecotypes' we have worldwide. However orcas are all classified as one species."
                l "Which personally, I don't think makes sense! It's-"
                o "It's a whole lot of explaining, that's what it is. We'd be talking all day if we went through all the different types there are."
                l "You have a point but..."
                l "Fine! Let's move on."

        #Q3 what do they eat. and how they get by
        r2 "Well it's finally my turn!"
        r2 "Okay, okay! Are you ready? Drum roll, please!"
        r2 "...What do lemon sharks eat! And uh- orcas!"
        r5 "The question never changed? That's funny."
        r3 "Well you know her..."
        l "This one is a little..."
        r2 "You don't like it?"
        l "N-no, I like it..."
        r1 "Of course he likes it. Just that the answer is obvious."
        r2 "We'll see about that! I said lemon sharks, not just any shark!"

        menu:
            "What do Lemon Sharks eat?"
            "Humans":
                r2 "Naahhh. But you know what that does mean?"
                r2 "That you're in great hands and you should totally choose Sasha and agree with how he's so much better!"
                o "..."
                r2 "What?"
                o "Do you by any chance think I eat humans?"
                r2 "Huh? Obviously! Like at the size of you!"
                o "Good lord..."
                l "R-right, who wants to go next?"

            "Fish":
                l "Well... yes? That's out primary diet."
                r2 "...And? You have to keep going puppy!"
                l "Uh, there's not much else to say though?"
                l "We primarily eat bony fish, stinrays, crustacans and mollusks..."
                l "Though some lemon sharks consumer smaller sharks and seabirds..."
                r2 "You do?!"
                l "I don't, no. But others may?"
                l "...This includes young lemon sharks. Unfortunately."
                r1 "Well... Sasha may have lost this contest."
                r2 "You don't know this! Maybe [mc] thinks it's cool! Right, [mc]?"
                mc "Well... that's for you to find out."
                r2 "The anticipation! Nooo!!"
            "Large Marine Mammals":
                r2 "Nope! Though other sharks tend to, don't they?"
                l "Ah... yeah sometimes."
                r2 "But {i}our{/i} Sasha is the sweetest and would never!"
                r2 "See, isn't he just so much better than Reign?"
                r1 "As you can probably tell... the obvious answer was fish."
                r2 "This is a set up for something great you hear me, great!"   
        menu:
            "What do Orcas eat?"
            "Humans":
                r1 "Did you really just reuse the same questions"
                r2 "I don't know what Reign likes to eat? Why would I care?"
                r1 "Sigh..."
                o "Well, on a positive note. Your assumptions only strengthen my case."
                o "I believe there have been not a single case of a wild orca eating humans."
                o "As I say... we're picky and prefer fish. There's not much else."
                r2 "Wah! Really, is that true?!"
                l "Well, yeah? I've only seen him eat fish so it checks out."
                r2 "He could be decieving you, Sasha! You can't trust him!"
                l "Uhh... I'm not sure that's his strong point."
                o "Hmph... loud."
            "Fish":
                r3 "This may have been an obvious question..."
                r2 "You think so? Hmm..."
                r2 "I think you're right, I should've added more choices..."
                o "Well you say that but orcas actually have quite selective eating, and of course this depends on the ecotype of an orca..."
                o "Mainly we do eat fish, salmon especially... though we don't typically go for marine mammals like seals..."
                o "Much less anything bigger."
                r2 "Wow, that's it? I though you would've ate sharks or something."
                o "..." 
                # THE BLUSHING SPRITE!!!!!! PLEEAAASSEESE HERE BLUSH HERE !!!
                l "Don't look at me like that... stupid..."
            "Large Marine Mammals":
                r2 "See! Scary big man eat big mammals!"
                r2 "This is why we {i}have{/i} to put all our points into Pups!"
                o "We do not do that."   
                o "We have very specific and selective tastes that really... depends on the orca."
                o "I personally prefer fish. Like the majority do."
                r2 "Wow, boo! Boring!"
                l "Calm down. I think my head's starting to spin..."


        #Q4 The types of behaviour in them socially. r5
        r5 "I'd like to, since I have a good one."
        r5 "Ah-hem. How about... the types of behaviour in lemon sharks!"
        r5 "Specifically, in the social aspect"
        l "Oh no, I know exactly where you plan to go with this..."
        o "...?"
        r5 "And the social behaviours of orcas too, of course."
        menu:
            "What type of social behaviours do sharks show?"
            "Cooperative Hunting":
                r5 "Ah, yep! Lemon sharks are known for forming groups where they hunt together!"
                r5 "..."
                r5 "Honestly, you chose the most boring one. Um..."
                l "Hey..."
                r5 "I guess... you would also forage and inspect reefs together? It's mainly group hunting, co-operative foraging and learning from eachother really."
            "Social learning":
                r5 "Well if I'm going to be real, they're all the right answer."
                r2 "Oh, I like how you're thinking!"
                o "Of course it was going to end up like this..."
                r5 "Now, now! Let's not get ahead of ourselves..."
                r5 "As we all know, lemon sharks are one of the few sharks that aren't solitary!"
                r5 "They're actually known for forming long-term friendships based on preference and the ability to learn from each other."
                l "Yeah, yeah! What do you expect when we grow up in small groups..."
                o "You were always pretty close to your mother..."
                l "Wah! And my siblings too! There were 15 of us!"
                l "Of course that would've been the case."
                r1 "So a momma's boy, huh? Why is that not surprising?"
                l "Yeah, yeah... god i knew this was coming"
            "Mating rituals":
                l "What! Why that one of all things?!"
                mc "In all honesty, I couldn't help but be curious."
                r5 "I had a feeling you were going to pick this one!"
                l "Please, can we skip this one?"
                o "Really? I think we should continue."
                r5 "First up, courting! Sharks have this weird think when they're courting someone they interested in, they bite them?"
                r5 "Usually it would be their pectoral fins, their flanks and back."
                r2 "Woah, so aggressive..."
                l "I want to die."
                r5 "Though when they mate, they swim side by side! Or parallel to eachother! The concept is so very cute!"
                l "Why did I agree to this..."
                r5 "Ah, but I heard Lemon sharks are polyandrous so they mate with multiple partners!"
                o "Excuse me?"
                r4 "Oh, he's done it now..."
                r1 "Jesus."
                l "Females do! Female lemon sharks! It's to have more litter."
                l "Hey, don't look at me like that!"
                o "...Hmph."
                l "Are you seriously mad at me? Hey!"
               
            o "So the other questions were right as well?"
            r5 "That's right! Are you mad?"
            o "Mad isn't what I'd go for. It's more... I'm tired."
            r5 "Hm... then let's finish this up."

        menu:
            "What type of social behaviours do orcas show?"
            "Cooperative Hunting":
                r5 "I knew at least this much." 
                o "Well, just like sharks obviously orcas work in a team to hunt. That's just a known fact."
                o "Not only that but it's common to share prey within the group as a way to... strengthen bonds."
                o "We also have different roles for different members of the group though... it's a lot to explain."
                r2 "I feel like... We're giving Reign too much appeal. It feels like we're losing."
                o "Maybe you are? Can't handle a little competition?"
                r2 "Excuse me?! I started this whole idea!"
                r3 "...What?"
            "Complex Social Structures":
                o "Oh? So you know about that?"
                r5 "Well... I was hoping you'd explain. I have the jist in my head but it's a little hard to..."
                o "Where should I start?"
                o "It's a matriachal leadership. Pods consists of an elder female, her sons and daughter and the offsprings of her daughters."
                r1 "So it's just like... a family?"
                o "Pretty much. Resident Orcas often stay with their mothers for their entire lives, though mine..."
                o "Ah-hem. But the whole structure is based on dominance, discipline and the ability to resolve conflict..."
                r4 "Wow, it sounds so complicated..."
                l "Sounds like a pain..."
                o "We're disciplined from mothers or other adults though when it comes to asserting dominance in the social hierarchy..."
                o "There is a lot of tail slaps, head-butts and raking..."
                o "We're very physically on hands with eachother."
                l "..."
                l "Should I be concerned by the future if I keep getting on your nerves...?"
                o "Don't be stupid."
                l "Phew!"
                r1 "Lovebirds..."

            "Communication with other Orcas":
                r5 "So... I heard orcas have different dialects? And I think..."
                o "Yes... and ultural traditions. Each pod has different ways of speaking..."
                o "Clicks, whistles, pulsed calls... You could say they are passed down through generations, sort of like a 'family badge'."
                o "Hunting strategies, vocalizations and social habits are also taught to younger generations."
                r3 "It does make sense, since orcas are dolphins... I feel like I shouldn't be surprised."
                l "I never realised you knew so much about this kinda thing."
                r5 "I dont really. It's more small things you hear about."
                l "Yeah?"    
        
        o "So you intended on all the answers being right?"
        r5 "I may have, yes. Since you and Sasha are quite close..."
        r5 "Let's not fight so much, yeah?"
        o "..."
        r1 "Well I suppose it's my turn next. Let's get this over with."
        
        #Q5 The biggest difference between a shark and a orca. r1
        #include the best way to deter
        r1 "What would be the biggest difference between sharks and orcas?"
        r3 "Hm? Are you changing it up?"
        r1 "Yup. This is going to be our last one."
        menu:
            "The biggest difference between sharks and orcas?"
            "Their senses":
                r1 "...Correct."
                r1 "Orca's cannot smell and rely on their hearing to hunt."
                l "They can't? Oh my god I'm the worst!"
                l "I never knew..."
                o "It's a thing for all dolphins. With rely on our hearing... and echolocation for help."
                l "So when you would tell me I stunk, you were lying?!"
                r3 "That's your biggest concern?"
                r1 "Meanwhile sharks rely on scent during their hunts."
                r2 "I would've said appearance, personally."
                r1 "...We know."
                r1 "That would've been too obvious so I thought to leave it out."
                r1 "In the end, the only judge here on who's better...is [mc]."
            "Hunting strategies":
                r1 "No... the way they hunt are pretty similar. Targeting the most nutritious parts of their prey and..."
                r1 "Both sharks and orcas use their stealth to frequently attack prey from below."
                l "You've been watching us? That's so embarrassing..."
                o "You're all joined at the hip most of the time, how do you not notice?"
                l "I get busy, okay! Or side tracked!"
                r5 "I guess it isn't surprising given the size and speed of them..."
                r4 "Sounds like an easy life..."
                l "You say that as if I don't feed you!"
                r1 "Are we done now? I think you're all forgetting that [mc] has business to take care of."
                r4 "Oh... you're right."
                r3 "We have kept you for a while..."
            "Global Range"
                r1 "This one was... quite obviously the wrong answer."
                r1 "Both sharks and orcas are found in nearly every ocean in the world."
                o "It's called cosmopoolitan distribution. Though it isn't all that interesting."
                l "I guess it comes with the title of being apex predators? I wonder if that's it..."
                o "Maybe. But the right answer I'm assuming was our senses. Isn't that right?"
                l "Huh? It is?"
                r1 "...you mean you hadn't noticed? Orcas cant' smell. I'm pretty sure all dolphins can't..."
                l "I... feel like I'm being gaslit here. There's no way..."
                l "Have you been tricking me this entire time! Reign!"
                r5 "Oh wow, first names?"
                o "Out of all the things I've lied to you about, this is the one that bothers you the most?"
                l "That depends on the lie, obviously!"
                l "And you lying... about me stinking! That makes no sense!"
                r2 "H-huh? He said that?"
                r5 "Oh, I remember this."
                r3 "When was this...?"
                o "...Your reactions were...amusing."
                l "So cruel!"
                r1 "Well, if you two are done bickering, we're finished now."
                r3 "Already? Awh..."
                r1 "Have you all forgotten that [mc] has places to be?"
                l "You do have a point..."
                r5 "So considerate, even if it's in your own special way, huh?"
                
    r5 "Was there anything else you were curious about?"
    mc "I mean, I've always been curious on whether sharks actually enjoy pets?"
    mc "There are so many videos online but..."
    o "Not gonna answer an honest question from the heart, blondie?"
    l "Ugh... "
    l "We like em', yeah..."
    l "Dun' mean you should have any ideas bout it though!"
    mc "Awh, I can't?"
    l "Wha?! You... you mean you actually want to?"
    r1 "Oh, they do."
    r5 "Well this is... different."
    r2 "This is amazing."
    l "You can't be serious..."
    mc "I mean, you don't have to! I just wanted to at least try it once in my life."
    l "No... it's alright you can."
    l "But just a little, alright?"
    o "Wow, you cheatin' on me now?"
    l "Shut up! We are {i}not{/i} dating!"


#reveals the point system and number of right answers. though that part doesn't matter.
#mc makes the choice on who wins. 
#r2 decides to make it a majority vote. cus dis whole thing is rigged n
#sasha is gonn deemed the coolest no matter what, the outcome would've always been the same

#b4 they fuck off to the twilight zone... i rlly don't have the energy to finish dis :'D UUAUAHGGHHH
# but basically the boyfriends argue.

r2 "Leave him alone you big meanie! Go away!"
r2 "Away, away!"
o "Annoying little brats..."
l "...Let's take this elsewhere."
r2 "W-what! You can't just leave!"


label twilight zone
    "The dizzying force of the currents slams into you, propelling you forward and into the threshold of the next dome until the pressure finally relents."
    "Your eyes easily lock onto the two figures nearby."
    mc "God, my head is spinning..."
    o "Oh? Our persistent little diver followed."
    l "Don't be weird..."
    l "They were headin' this way before you showed up."
    l "Maybe if you paid attention, you would've known!"
    o "And now you're expecting me to predict your conversations? Such a pain."
    l "I... that's... no..."    
    o "So you're here for the next zone ahead?"
    o "The only reason divers go down there is to..."
    l "Ah, food! You're carryin food, aint it!"
    o "Calm down, you."
    mc "I... it's not alot though? And I don't think I'm allowed to hand out what I do have..."
    o "Of course you aren't, but we're not asking."
    l "Though we are friends now, so you should totally give us... well, just a little bite?"
    l "Come on!"

label moray eel intro
    nill "Who the hell..."
    l "Ach! No one's here, not anyone at all."
    l "...It's Keira!"
    o "...I see that."
    m "I recognize that annoying voice from anywhere."
    l "A-annoying?!"
    l "Reign... My voice isn't annoying, right! Right?"
    o "...Ah-hem..."
    l "What the hell is wrong with you..."
    l "Not funny!"
    m "And you..."
    m "...You're new, aren't you?"
    l "[mc] is not food, Keira! They're just carryin' it!"
    m "Quit that. You should know better than to annoy me by now."
    l "..."
    l "Yeah..."
    o "..."
    m "I'm asuming these two are being a bother?"
    mc "Something like that."
    m "Never seem to learn their damn lessons, huh?"
    m "And over something like food? Come on now."
    l "That's not it at all! Come on [mc], tell her!"
    l "We were just playing around, quizzin' the new fella..."
    l "The usual... friendly friend stuff!"
    mc "Oh, yeah. Though you did side track me a little..."
    l "Ack! I know..." 
    m "A quiz though? Hmm..."
    mc "I mean, I really should be getting going. Just because this is my first time down here and..."
    mc "It was only supposed to be a quick in and out task."
    m "It always is a quick in and out when it comes to the midnight dome."
    m "Though, I'm sure you have a little time to spare, no?"
    m "I did help you out afterall. Don't you think I'm deserving of a reward?"
    o "When did you ask for rewards?"
    m "When pretty little divers started coming down with the ability to actually talk to us, Reign."
    m "Though I'm sure that's why they sent them down to the Midnight Dome in the first place."
    m "So how about it? Up for another quiz?"
    l "I don't really think you have a choice in this, [mc]."

label quiz moray eel
#Q1       answer is over 800
    m "Shall we start with a vague one?"
menu:
    "How many species of Eels are there?"
    "Around 120":
        l "120? Come on, even I know that much..."
        m "You live in the waters though, Sasha. There's no reason not to practice a little more humbleness."
        l "Should I just die..."
        m "But yes, Sasha is right. The number is a lot more than... 120 of us."
        l "...Are you ignoring me?"
        m "Though if you were thinking specifically Moray Eels... Haha."
        m "You'd still be wrong. Since there are over 200 known species when it comes to us Moray Eels."
        l "M'can't believe this!"
        o "..."
        o "When did you get that scar?"
        l "Huh? Where?"
        o "...There."
        m "You two really can't help yourself, can you..."
        m "Sigh."

    "Over 500":
        #block of code to run
    "Over 800":
        m "However there are over 200 known species of Moray Eels that are divided over..."
        m "I'd like to say roughly 15 to 16 different genera, found worldwide."
    "Over 1000":
        #block of code to run
    
    l "Can I ask something I always wondered?"
    m "...Shoot."
    l "Is the jaw thing... something all eels have?"
    mc "The jaw thing? What's the jaw thing?"
    l "You don't know? They've got like... two jaws!"
    m "How did our conversation divert to this of all things?"
    mc "It doesn't look like you have two jaws..."
    m "It's in my throat. Would you like a demonstration?"
    menu:
        "Actually, yes!":
            mc "Oh, actually yeah! You mean it?"
            l "What?! No! You don't mean it!"
            l "Everytime I see it... ugh I good, thanks!"
            m "Yes, yes. I'll keep my jaws to myself."
            m "[mc], yes? We'll schedule that for a later date."
            l "God... what's wrong with everyone here..."
            o "This is what I get for going along with your whims."
            l "Shut up you."
            l "I don't see you doing anything to help..."
            m "Enough fighting, boys. We have guests."
            o "...Hardly."
            m "Allow me to continue."

        "No, not really...":
            mc "No, not really..."
            l "Haha...thank god."
            o "Didn't want to be the demonstration today?"
            l "Absolutely not. Never again."
            mc "You... she demonstrated on you?"
            l "...I don't wanna talk about it..."

    m "You're a fun one."
    mc "I... thank you?"
    o "We got off topic."
    m "We did."
    m "Ah-hem."
    m "So... while most of us share the same jaw structure... Moray eels use it differently."
    m "Unlike other fish, we aren't able to create suction to swallow food."
    m "A second jaw allows us to... let's just say, 'drag' our prey into our esophagus."
    o "Still wish to see it?"
    l "That's what I'm saying..."
    mc "Then how do other eels do it?"
    m "Well... if I told you now, I'd give you the answer to one of our upcoming questions."
    o "A good thing you asked. It gives ya a huge head start."
    mc "Okay... so eels have the same jaw structure but it isn't used the same way..."
    mc "Hmm..."
    l "Well, Keira? What's the next one?"
    m "Ah. Right."
        
#Q2          only fishes, octopuses and crustaceans r right
    m "Moray Eels are opportunistic feeders, but what do you think would be our favourite choice of a meal?"
    o "..."
    o "Pff..."
    l "That's so-"
    m "Shut it."
    m "Or do you intend to ruin all my fun?"
    "Sasha pouts, crossing his arms but saying nothing futher. Reign just looks off at nothing in particular, though he had an amused expression on his face."
    menu:
        "What do Moray Eels eat in the environment?"
        "Plant matter, algae, seaweed or seagrass.":
            m "Oh, absolutely not."
            m "That would do nothing for me, I wouldn't even entertain the thought."
            mc "Not even other eels?"
            m "Eels besides from me, you mean?"
            m "Depends on the eel. Moray Eels on the other hand are carnivores."
            m "Anything very small or plant based does nothing for us."
            o "Out of all the options, you went with that one."
            o "Interesting choice..."
            l "Honest, I thought Moray Eels would eat anything."
            m "Like yourself?"
            l "Kinda, yeah..."
        "Smaller fish, cleaner organisms.":
            m "Well, I suppose? Though we're not picky... we do care about the size and shape of our prey a lot more than we let on..."
            m "I'm not sure whether I should give you that one..."
            l "Really? Thought there ain't a wrong answer to this one." 
            m "Well what we 'dislike' is anything too difficult to catch, really."
            m "The smaller the fish, the more annoying. Especially with such bad eyes... It really would be more of a bother than anything."
            m "That and we don't eat cleaner fish."
            l "Oh yeah! You don't, do ya?"
            l "Forgot about that..."
        "Fishes, octopuses and crustaceans.":
            m "There you go."
            m "This was an easier one to answer."
            m "Though god, I'm getting hungry at the thought..."
            o "Well good thing our little diver has some on hand."
            m "Lets not. Food for the midnight dome is hardly filling anyways."
            m "Nor is it satisfying in the least. They can keep their scraps."
            o "...You do make a point."
            mc "What? That's really all it would've taken for you to back off?"
            mc "You can't be serious..."
            o "It's a reasoning I can accept."
            l "M'hungry..."
        "Larger prey":
            o "When you look back, the right answer is obvious."
            m "It is, yes. But I'm not expecting our little diver here to know everything about every creature to exsist in this dome."
            o "...can't relate."
            m "Of course {i}you{/i} can't."
            m "I am sorry to disappoint but that is most definitely not what I would choose as 'quality' prey."
            m "Though I am flattered, in a way."
            m "Anything too large for my bite, I'm not all that interested in consuming."
            m "And while I am classified as a top predator, it's important to understand that I can be preyed on myself, especially by larger sharks, barracudas, even sea snakes..."
            m "Though it would be unwise for them to try."
            l "God, I get shivers just thinking about it..."
        
        m "Now a good follow up question to that..."
        l "Y'know, I thought {i}our{/i} questions were hard. This though."
        l "This is just mean..."
        m "Oh really? How so? Please do elaborate."
        l "Well I- Uh-!"
        l "Y-you know I'm bad with big words!"
        o "Pff..."
        l "Hey now..."
        l "Who're you laughin' at? So mean man..."
        m "Big words like... elaborate?"
        l "Shut up! All of you! Ugh..."
        l "M'never gonna talk again, I swear..."  
        m "...We'll move on."
 #Q3      scent is the only one that's right here.
    m "Then here's a good one. How do you think Moray Eels hunt?"
    l "Oh."
    l "I'm actually not all that sure if you'd get this one..."
    menu:
        "How do Moray Eels hunt?"
        "Social Hunting":
            m "Some eels do so, yes. Moray eels on the other hand... very rarely."
            m "More specifically Electric Eels tend to use that as a tactic."
            m "It's tactless but... gets the job done I suppose."
            o "Electric Eels. They work in groups to coorindate attacks, don't they?"
            m "They do, yes. They form groups of up to 100 and synchronize high voltage shocks to overwhelm prey."
            l "...remind me to never get on the bad side eels in general"
            o "You think you'll need a reminder after this?"
            l "Not really... I think this'll be ingrained into my memory forever..."
        "Choice 2":
            #block of code to run
        "High-Speed Chase":
            m "Definitely not a tactic I've tried before."
            m "Nor one I intend too..."
            l "To be honest, I'd freak out of a Moray Eel charging at me then anything else down 'ere!"
            m "The point is, prey would freak out if they saw me."
            m "And I wouldn't exactly be able to see nothin'..."
            m "Oh well. Ah-hem, but the correct answer would be that Moray Eels use their heightened sense of smell."
            m "What we can't see, we smell."
            m "And we absolutely use this to our advantage."
        "Scent":
            #block of code to run
            m "If you hadn't gathered already, my eyes certainly don't do me any justice."
            m "It's either we Moray Eel hide in rocks and strike when prey happen to get too close or..."
            m "When it's at night. With my poor eyesight, it doesn't matter to me whether it's night or day."
            m "And due to that, I rely mainly on my incredibly developed sense of smell to hunt."
            l "Sneaking up on sleeping fish..."
            m "Got something to say?"
            l "..."
            l "Course not..."

     m "We're nearing the end of the quiz, just a couple more."

    #Q4       shrimp & groupers are correct answers
    menu:
        "Moray Eels have a mutualistic relationship with what creature?" 
        "Shrimp":
            m "That's right. Moray Eels share a mutualistic relationship with cleaner shrimp."
            m "They will clean our teeth and eyes, providing a grooming service of sorts."
            m "And in return we give them essentially a free meal from whatever's left over."
            m "Gross... but it sure as hell practical."

        "Choice 2":
            #block of code to run
        "Choice 2":
            #block of code to run
        "Groupers":
            m "Interesting choice. Moray Eels specifically engage in this sort of...truce."
            m "Despite our solitary repuation, we are occasionally known to participate in or form cooperative hunts alongside Groupers"
            o "I do recall seeing this once before."
            m "Our roles in hunting are complimentary."
            m "Moray Eels are specialized for hunting inside tight, rocky structures whereas Groupers are fast open-water predators."
            m "It only makes sense to team up every now and then, when the situation calls for it..."
            l "Thought it was just shrimp that you guys are chill with, to be fair."
            m "Cleaner Shrimps too- they often clean our eyes and the inside of our mouths."
            m "It's to prevent infection. And in return, they get a safe meal from whatever's left over on our teeth."
            m "It's all based on convenience."
            l "Huh. Maybe I should give that a try..."
            l "Though who would I..."
            o "...?"
            l "Ack... N-nevermind!"
            l "Today is dragging on way longer than I had hoped!"
            m "This will be the last question then."
        
    #Q5     bite & blood are correct answers
        m "Now, let's bring back something we were talking about before."
        m "In what sense am I dangerous?"
        l "Haha... I wonder."
    menu:
        "What is the most dangerous thing that Moray Eels use to their advantage?"
        "Biting":
            l "God, please don't remind me."
            m "You can't say you didn't deserve it."
            l "Hey! I was just a little pup! I didn't know any better!"
            l "Hell, I could've died!"
            l "Infact, I nearly did!"
            mc "That's very... it's a lot to take in."
            mc "Though surely it couldn't have been that bad?"
            o "Oh, it really was."
            o "This is one of the few times Sasha isn't exaggerating ."
            o "I on the other hand..."
            o "Let's just say that biting one also isn't this best of ideas..."
            o "Though how was I supposed to know Moray Eels had poisonous blood. A heads up would've save everyone a little less agony."
            m "What can I say? Serves you right."
            mc "So you've both made this mistake?"
            mc "Wowzers. I had expected that much from Sasha but, you Reign?"
            o "...It was a lack of judgement on my behalf."
            mc "I see. Though surely for Sasha, if he had just gotten bit- wouldn't it be the same as maybe a shark bite?"
            l "Hah! I'd rather an Orca bite me."
            o "...yeah? We can arrange that."
            l "Shut up. Your bites hurt way less, so yeah!"
            m "Woah, even doubling down. Haha."
            m "There is a reason."
            m "Not only do we have incredibly sharp and hooked teeth, but the infection risk is pretty damn high!"
            l "I can't believe you're explaining this so proudly..."
            o "Maybe we should stop there, before Sasha becomes more of a nuisance than just a whiny puppy."
            m "Agreed."
        "Electricity":   
            m "Electricity? Oh no, not at all."
            m "I thought you would have realised... Moray Eels don't produce any electricity. Hence our way of hunting and the use of our jaws..."
            m "You're very much thinking of electric eels. Though the funny thing about are that electric eels aren't true eels."
            l "They aren't?! My head hurts..."
            m "They're a type of knife fish. Appearance wise though, I suppose the title of an eel suits them fine enough."
            o "Where's this understanding when it comes to us?"
        "Blood":
            o "Don't remind me."
            m "Exactly right. One bite into me and he'd be ill for weeks. My blood would be considered poisonous to... well any animal."
            m "Perfect for when a bigger prey thinks to fight back."
            m "I'm very sure that if you were to bite into me [mc], you'd end up completely dead!"
            mc "Haha... good thing I have no intention of doing that."
            o "..."
            mc "Reign? You alright?"
            o "I'm fine."
            l "Reign's just mad that he tried picking a fight with her long ago and suffered for it."
            o "You're forgetting yourself. Don't forget that you've been bitten."
            o "In the end it's all the same. Biting or getting bit, what's really the difference?"
            l "I was young! Really young! You can't fault me on that!"
            mc "I'm surprised you aren't all at each others throat."
            m "Well, no hard feelings. This was a long time ago."
            m "And sometimes things must be learnt the hard way. Especially for a creature so stubborn..."
            o "Yeah, yeah. I get it."
        "Choice 2":
            #block of code to run
    
    l "So... what now?"
    o "Sigh..."
    l "W-what?"
    m "Not much. [mc] is expected to go into the midnight dome."
    o "You're awfully calm about all of this."
    l "Yeah! Heard you got into a scrap over a meal not to long ago!"
    m "...Did you really think I wanted the food all for myself? Ridiculous."
    l "I-is it?"
    o "... I don't believe it one bit."
    m "What? I just don't wanna have to deal with the freaks over in that zone. The less annoyances the better."
    m "Whether you believe me is your own choice."
    o "And we're apart of that 'annoyance'?"
    m "The hell do you think?"
    m "You."
    mc "Me?"
    m "Who else? Where's your light?"
    mc "Oh... it's here."
    m "Keep it out and keep it on. The deeper you delve from her on our will only get more dark."
    l "You've met some of the creatures of that dome, right? Are you sure it's gonna..."
    m "Realistically, they wont be a bother. They're aware of the consequences."
    l "...right..."
    l "W-well, are you all ready?"
    l "Got everything your light, food, uh..."
    o "Your breathing equipment."
    l "Your breathing equipment!"
    mc "I... yeah I've got everything. There shouldn't be any issues."
    mc "Just a quick in and out!"
    l "And we'll wait for you when you come back!"
    o "..."
    l "Reign!"
    o "What? Uh..."
    o "Right. We'll wait around."
    l "You suck at this."
    m "The currents are strong so remember to have that torch tight around your wrist."
    m "There should be a safety strap, just there."
    mc "Thanks! I'll be heading off then, okay?"
    l "Be safe and make it quick!"
    o "Puppy's grown attached?"
    l "Ugh! Don't wanna hear that from you."
    
    #n maybe a paragraph of delving further into the dome before reaching the current part?


label phantom jellyfish intro
    "The currents leading towards the final dome weren't exactly a surprise this time. Still, the anticipation didn't make the pitch blackness of the midnight dome any less stressful."
    mc "I hope the torch holds out..." 
    "You grip the torch a little tigher as you sweep the light around, searching for any sign of movement."

    nill "Oh...hello?"
    "You recoil, the suddenness of the voice catching you completely off guard. It seemed she was just as startled as you were."
    nill "Oh, god! I'm so sorry!"
        menu:
            "I never meant to scare you!"
            "It's okay, it was an accident.":
                mc "No, no! I..."
                mc "It's okay, really! I know you didn't mean to."
                nill "Really? I'm so glad..."
                nill "Still, I'm sorry I///"
                mc "Did you... were you expecting someone else?"
                nill "Expecting someone? No, not at all..."
                nill "I was more curious..."
            "I wasn't scared of you.":
                mc "Don't worry, I wasn't scare of you!"
                nill "I... you weren't? Really? Do you promise?"
                mc "Really. I was just startled. This is my first time doing this, so..."
                nill "Oh, I know it is!"
    nill "Still, I'm sorry for... you know..."
    nill "It was wrong for me to appear out of nowhere."
    mc "Can I ask, uh... who are you? Or uh, what?"
    nill "Hmm? Me?"
    nill "Ah... you can't tell, really?"
    mc "S-sorry...I-"
    p "No, no! It's alright, really."
    p "I'm Lilith. Or maybe you could call me Lily? For short."
    mc "Lilith? That's such a pretty name I should've expected it, really."
    mc "It suits you well. I'm [mc]."
    p "Well that is my name."
    p "Haha, [mc]? [mc], [mc]! That's so fun to say!"
    p "I do hope that maybe..."
    p "Maybe we can be friends? I-if you want to of course!"
    p "It's not like you have to... it's just because no one really talks to me much outside my dear brotula..."
    mc "Brotula?"
    p "Oh, yes! Our sweet little Pelagic Brotula!"
    p "She's like a daughter to me... the only one who keeps me company really."
    p "Divers are... they're afraid of me."
    p "Though I can't say I blame them..."
    p "..."
        menu:
            p "...can we?"
            "We can be friends":
                p "S-sorry? I think I misheard..."
                mc "I... would very much like to be your friend. You seem sweet."
                mc "I'd love to be your friend, really."

            "Will you help me if I am?":
                #block of code to run

            "Will you hurt me if I won't?"
                p "Will I hurt you...?"
                p "Never! I... of course not..."
            
    p "S-so... I'm guessing you're down here to replenish the food of this zone."
    mc "Oh, how did you know?"
    p "There's no other reason for divers to come down here, other than for that, silly"
    p "It's far too dark. Which is why you also keep mindful or anything here that glows besides from that torch of yours, okay?"
    p "I mean it... the creatures here- they're harmless, really!"
    p "Just don't get on their bad side..."
    mc "Yeah, I've been told the same. I'll be sure to keep that in mind."
    p "You have?"
    mc "Yeah, from the others... uhh..."
    mc "The other creatures from the different zones. 
    have been friendly for the most part. They're definitely an interesting bunch."
    p "Oh I wouldn't know... I don't think they like me too much anyways."
    mc "That's completely my bad. I was just curious."
    p "So you all... just talked together? That seems nice."
    mc "It was mainly just bickering and quizzing-"
    p "Oh! A quiz? I've never taken part in a quiz before..."
    p "That sounds so fun!"
    p "So lucky, I wish I had people around to do that sort of thing with..."
    mc "..."
    mc "Would you like to do one then? A quiz?"
    p "Wow, you mean it?"
    p "Uh-huh! I'd love to!"
    p "This feels so proper, wow! I can't believe I actually get to participate in a quiz- and with a friend!"
    p "Could I be dreaming?"
    mc "No dreaming! This is all really happening."
    
label quiz phantom jellyfish
    p "Then... then shall we start the quiz?"
    mc "Well..."
    mc "I'm ready when you are!"
    p "Haha, god where to even begin?"
    p "For the first one... hmm something easy might be good..."
    #Q1
    p "I'm referred to by a specific nickname! What did you think that might be?"
        menu:
            "What am I nicknamed?"
            "Psychdelic Medusa":
                "Nope, not me!"
                "That'"
            "Alarm Jellyfish":
                "I gave you quite a hard one to go off on, huh? I think I got a little too excited..."
                "Alarm Jellyfish are actually the nickname of the Atolla Jellyfish."
                "You might see her around down here!"
            "Phantom of the Deep"
                p "Hehe, I completely made that up by the way!"
                p "Though my nickname is similar. Giant Phantom Jellyfish are called the Ghost of the Ocean."
                p "I dont really like the nick name all that much but... what can you do."
                mc "I think it's quite a pretty name though? It has a certain charm to it."
                p "You... think so? I see..."
                p "Maybe you're right..."
                p "Ah-hem! N-next up!"
            "Ghost of the Ocean"
                p "That's how the divers tend to refer to me as! It's so rude..."
                mc "Do you think so?"
                menu:
                    "Do you think so?"
                    "I think it's charming":
                        "From how i view it..."
                        "I think it's" 
                    "Choice 2":
                        #block of code to run             
    #Q2
    p "And do you think the scientific name for my species could be?"
    menu:
        "What's the scientific name for the Giant Phantom Jellyfish?"
        "Chrysaora Fuescescens":
            p "Chrysaora Fuescescens are Compass Jellyfish."
            p "They're called that because of they sorta look like a compass card!"
            p "Or so I've heard... I've never actually met one before."
            p "Anyways, the right answer was that I am a Stygiomedusa Gigantea!"
            p "An impressive name, don't you think?"
        "Stygiomedusa Gigantea":
            p "Yup! I'm the only one."
            p "We're extemerly rare, I'm pretty sure there have only been around 115 to 125 recorded sightings in the last century?"
            p "Something like that? Aren't I so cool?!"
        "Turritopsis Dohrnii"
            p "Haha, no! I'm what you'd call Stygiomedusa Gigantea."
            p "Turritopsis Dohrnii are Immortal Jellyfish. They're known for their ability to revert to a polypstate."
            p "To keep it short, they can reverse its life cycle. So instead of dying, it shrinks and reassorbs itself!"
            p "Crazy, huh?"
        "Chrysaora Achlyos"
            p "Ah, the one who is nicknamed the Black Sea Nettle. A close one, and we're even somewhat similar in... well a lot of things!"
            p "In colour, size and not to mention, they're also quite rare as well..."
            p "Though they have a much larger apetite. I would not want to get stung by one of those!"
            p "Anyways. The correct answer is that I'm a Stygiomedusa Gigantea!"
            p "A rather cool name, if I do say so myself!"
    #Q3
    p "Now, how many species do you think are in the Stygiomedusa family?"
    p "You'll be surprised!"
    menu:
        "Say Statement"
        "0":
            p "Huh? None?"
            p "S-sorry, maybe I wasn't clear before um..."
            p "I'm of the Stygiomesdua family. The correct answer from the last question was Stygiomedusa Gigantea, remember?"
            p "B-but it's okay though! The answer is there's only one."
        "1":
            p "Yup! Just me!"
            p "Tehe! You could tell I'm that special?"
            p "You flatter me, really."
        "3":
            p "It's a good guess but no... it's actually just one!"
            p "That's usually not the case though, right? I'm not surprised you thought it would be more, haha."
            p "I'm still sort of surprised by it myself? Ah- but next up!-"
        "8":
            p "Aha... that many?"
            p "I mean... that was a good try! Really!"
            p "I'm actually the only one though."
            p "It sounds a little lonely saying it aloud but... I take pride it in being that way."
            p "It feels more special, I think!"
            p "But enough of all that, next up..."
    #Q4
    p "Where do you think my kind are commonly found?"
    menu:
        "Where are Giant Phantom Jellyfish commonly found?"
        "Sunlight Zone":
            p "H-huh? I can't tell if you're joking..."
            p "The point of a quiz is to actually put in effort! It's no fun if you're guessing all the wrong answers!"
            p "Hmph!"
        "Twilight Zone":
            p "Yup! That's a trick question."
            p "It's both the ocean's midnight and twilight zone!"
            p "Did you choose this one just to catch my reaction?"
        "Midnight Zone":
            p "It's pretty obvious, huh? Since this is a reflection of the Midnight Zone."
            p "I did kinda give you a trick question. You can find me in the Twilight Zone too."

    #Q5
    p "The Giant Phantom Jellyfish shares a symbiotic relationship with what fish?"
    p "Now I did mention this before so I hope you've actually been paying attention to me..."
    p "T-though I know you've had a long day so..."
    p "I won't take it to heart."
    menu:
        "What fish does the Giant Phantom Jellyfish share a symbiotic relationship with?"
        "Choice 1":
            #block of code to run
        "Lanternfish":
            p "You just chose Lanternfish because you knew they were deep-sea fish, didn't you?"
            p "But no, the correct answer would be the Pelagic Brotula. Remember?"
            p ""
        "Stygno Brotula":
            p "I tricked you a little there! The correct answer is actually the Pelagic Brotula."
            p "Stygnobrotula... Well an easier name for them are just Black Brotula."
            p "They occupy reefs to freshwater caves, though you do tend to see them venture a lot deeper than they should be."
            p "Though they do the same thing, as cleaner fish."
            p "My Brotula, Pelagic Brotula's are adapted to survive the high pressure, near-frezzing temperatures and permanent dark of the midnight zone."
        "Pelagic Brotula":
            p "Correct! So you really were listening to me?"
            p "In the ocean, Giant Phantom Jellyfish have a sort of co-relation with the Pelagic Brotula."
            p "We offer them shelter within our bell and in return, they rid us of any parasites!"
    #Q6
    p "Giant Phantom Jellyfish have long arms, our 'tentacles' if it makes things easier."
    p "Though that phrasing isn't entirely accurate in my case. Maybe appenages would be more appropriate..?"
    p "How long do you think these arms can grow to?"
    menu:
        "How long can a Giant Phantom Jellyfish's arms grow to?"
        "5 metres":
            p "You underestimate me! Come on!"
            p "It's 10 metres! My arms can reach up to 33ft in length, thank you!"
        "8 metres"
            p "Not quite, but close! Really close, actually."
            p "Ours grow to about 10 metres, so it reaches to 33ft in length.""
        "10 metres":
            p "Are you sure you aren't cheating? I can't believe you got that right..."
            p "But yeah! Our arms can grow up to 10 metres, which are 33ft in length."
        "15 metres":
            p "God, that would be so cool! I think if I tried hard enough I actually could reach to 15..."
            p "O-oh, don't mind me! Our arms can actually grow to up to 10 metres."
    p "That makes me the largest invertebrate predator in the ocean!"
    p "Though I shouldn't brag, really. I wouldn't want to scare you away..."
    p "Ah-hem!"
    #Q7
    p "Given how long these arms are... how do you think I capture prey?"
    p "I'm give you a hhuuuugge hint, by the way!"
    menu:
        "How do Giant Phantom Jellyfish capture prey?"
        "Trawling with long tentacles":
            p "Awh, I thought it was obvious."
            p "No... that's more for... species like the Lion's Mane Jellyfish! They drag their tentacles behind them, just like a fishing net to snare fish!"
            p "Or really, anything that drifts by."
            p "For us though... our arms are called 'oral arms'. So we hoist up what gets tangled into our arms to our mouths and that's how we eat."
        "Stings them with their arms":
            p "Well, that's the most common method that many Jellyfish are equipped to do... given they have stinging cells."
            p "Which I do not. Mine can't pierce prey or inject toxins, they simply capture."
            p "And because of the length of my arms, we can move things up and into my mouth."
        "Bioluminescence"
            p "That is how most deep sea creatures lure their prey."
            p "And while I do emit a faint light that may attract prey... that's not how I capture them."
            p "The length of my arms allows me to move anything all the way up and into my mouth!"
        "Hoists prey into their mouth"
            p "Exactly right!"
            p "I don't have a stinging cells to hunt and paralyse like most other Jellyfish can, so instead..."
            p "They get tangled into my arms where I can move them right up and into my mouth!"
    #Q8
    p "And with that little piece of information, what food do you think I eat?"
    menu:
        "Say Statement"
        "Choice 1":
            #block of code to run
        "Zooplankton and small fish":
            #yeah idfk. this is the right answer tho :3
        
    #Q9
    p "Hmm..."
    p "I have one more question I want to ask you, but..."
    p "It's a little... ahhh how should I do this?"
    p "Okay, okay! I'm taking too long! Um..."
    p "How do you think... my kind give birth?"
    p "A-and don't tease me about it! I'm already such as mess..."
    menu:
        "How do Giant Phantom Jellyfish give birth?"
        "Live young":
            p "Wow, that's a really impressive guess!"
            p "A-hem! Unless it wasn't a guess...then..."
            p "Ignore me! Sorry! Um, yes!"
            p "Giant Phantom Jellyfish are different from others because we're viviparous."
            p "This just means if I were to, I'd give birth to live young."
            p "This might sound a little absurd but it would develop inside my bell before detaching from inside my hood and swimming right out of my mouth!"
            p "In many ways, I don't really align with most other Jellyfish. Or sea creature in general."
        "Asexually":
            p "This is how the majority of jellyfishes reproduce. Adult jellyfish release their eggs and sperm the form larvae and settle on any nearby surface."
            p "Then they essentially grow into polyps that clone themselves and evntually bud off as baby jellyfish! Ain't that cute?"
            p "My way of birthing, live birth is a lot... less cute though?"
            p "W-well, if I were to give birth! Our young would develop inside our bells before deataching itself from inside my hood and swim out of my mouth."
            p "A lot more... unconventional. But I think thats pretty neat!"
        "Or trick question, immortality!"
            p "Nope! Did I catch you off guard?"
            p "So some species like the immortal jellyfish can revert from their grown stage- the medusa stage and back to a polyp stage."
            p "Where they would be just a blob floating around till they grow up again in around... 3-4 weeks?"
            p "For me, well if I were too..."
            p "We give birth to live young, where they would develop inside my bell before deataching and leaving through my mouth! "
            
    mc "You know, I always did wonder how. Learn something new everyday, huh?"
    p "God, I'm so embarrassed... m'think I should've left that question out but..."
    p "Haha! That was so much fun, wow!"
    p "It's been so long since I've had such a great time... talking!"
    p "Thank you for the company... and taking part in all this, well it really means a lot to me."
    p "A-hem! I've held you up for a while and... well I'm sure the pitch darkness in this dome isn't the most pleasant."
    p "How about I help you? Since you've done so much for me..."

    p "...just feel for a moment. We're not too far from the entrance to this dome, all you have to do is feel the current."
    p "There you go! It's just that way. As long as you trust yourself in where the current is pulling you in, you'll be able to find exactly where you're going."      
    
    "She pauses, thinking over something before deciding to give in."
    p "H-here! This is for you, [mc]"

    "She carefully places something into your palm, seeming pleased by herself. It was a beaded bracelt with a large teardrop shaped gemstone dangling from the front."
    "It seemed to be a smooth clear quart of sorts - exactly like the ones that adorned her ears and neck."
    mc "They're so pretty but... what is this? I've never seen anything like it before..."
    p "These are called Phantom Quartz. Red Phantom Quartz."
    p "It's quite fitting, no? They're awfully special to me so I do hope you keep this gift safe."
    mc "That's very kind of you. I don't feel as I though I deserve such a sudden gift..."
    p "You're a very dear friend to me. You know... it's been pretty lonely for me down here."
    p "So from the bottom of my heart, I'm so glad you stayed and played along my request."
    p "Thank you."
    p "And... you can take it as a claim of sorts? Hehe..."
    "I place these around my wrist, tightening the thread around my wrist."
    p "Will you be off then?"
    menu:
        "I better be, yes.":
            p "Ah... I see..."
            p "I wish you could've stayed longer. Get back safe, dear."
        "I wish I could stay longer.":
            p "I wish the same."
            p "But we should hold that thought... my dear brotula will wonder where I've gone off too..."
            p "Next time, for sure? Will you stay a little longer?"
            mc "I promise."
            p "I'll see you then, then. Stay safe, my dear."
                

label angler fish
    "Without Lilith hear as a guide, the darkness felt more suffocating. Your hands sweep through the void, feeling for the pull of the current as you push forward."
    mc "Nearly there..."
    "Suddenly, a flicker of light pierces through the darkness, catching your eyes and drawing you closer."
    "Before you could even process the glow, a face lunges out from the shadows."
    nill "Boo!"
    mc "!!!!"
    "A sharp jagged grin staring down at you as you recoil, scrambling backwards through the water."
    mc "T-the hell..."
    nill "Is that any way to greet someone? Good lord you humans are all too dramatic."
    nill "And by the gods do you look like such a tasty looking treat! Did they send you down here as my reward? You know, for being so good lately?"
    mc "I... I'm just here for... refills. I brought actual food from-"
    nill "Yeah, yeah. I can see that much."
    nill "Though, shouldn't you have been told how unsafe it is to linger?"
    nill "No one has stayed for as long as you have."
    mc "I mean, yes that was my intention but-"
    nill "But you're still here? Why?"
    mc "Because I was held up!"
    nill "...Haha, I knew that already. I'm already well aware."
    nill "I could here your bickering from miles away, don't you worry."
    mc "..."
    nill "What? Got something to say?"
    mc "I... don't think so?"
    nill "Hm... A shame. How dull."
    mc "[mc]."
    nill "What?"
    mc "My name. It's [mc]..."
    nill "Okay? I don't particularly care..."
    nill "..."
    nill "Sigh. It's Styx, yeah?"
    mc "Styx? I've never heard anything like it before."
    a "Well I expect you to remember it regardless."
    a "Though I suppose you wont have to if I eat you, huh?"
    a "Hmph."
    a "Now what was it I was saying before..."
    a "Ah! That it's quite a bold move for a human to linger around these parts."
    mc "I know, but there was this woman and..."
    a "Yes. I did hear..."
    mc "You... heard?"
    a "Well, I heard your little quiz."
    a "And let's just say I found myself curious."
    a "Voices travel far in these parts. Especially such, excitable ones."
    a "I wonder who caught your interest for you to linger down here for so long..."
    a "But enough about that. Entertain me!"
    mc "Entertain you? I'm not sure I quite understand."
    a "Must I really rephrase myself? Sigh..."
    a "For me to allow you to leave here unscathed, you will entertain me, yes?"
    mc "I... like another quiz?"
    a "Ah, like the quiz... That should do. Though I will be dissapointed if you get everything wrong."
    a "Let's see. Just any silly little quiz would be boring so..."
    a "How about we raise the stakes."
    a "I'll let you go completely unscarthed, as long as you answer the majority correct."
    mc "I'm not sure I like the sound of that..."
    a "Well unfortunately you don't have much of a choice now, do you?"

label quiz anglerfish

#Q1
a "There are obviously many species of AnglerFish..."
a "Over 200 actually."
a "What is my species?"
menu:
    "What species of AnglerFish are they?"
    "Footballfishes 1":
        a "I do hope you turn out to be a meal worth savouring..."
        a "Though I'm not too convinced."
        a "Footballfishes are name for their round and bulky shape..."
        a "I hope your're aware of how that comes across, hm?"
        a "..."
        a "I'm a Black Seadevil."
        a "it would be in your best interest to remember that."
    "Wolftrap Anglers":
        a "Hmm..."
        a "Getting the first question wrong... you're going to be a difficult one, aren't you?"
        a "Let's hope you don't get every question wrong, because then I really will get upset."
        a "Wolftrap anglers are... rather strange in appearance. If I am to put it nicely."
        a "Their jaws are more built like a trap and act as a cage. But enough about those things."
        a "I'm a Black Seadevil. I do hope you won't forget."
        a "Unless you do intend to get eaten?"
    "Krøyer's deep-sea angler":
        a "Well I'll give it to you, it's a close one. They are often described as a 'warty sea-devil', so..."
        a "Sigh, though unfortunately for you, you're very wrong."
        a "I'm a Black Seadevi."
    "Black Seadevil":
        a "So you aren't stupid? That's reasurring."
        a "Yes, I'm the Black Seadevil"
        a "..."
        a "What?"
        mc "N-nothing..."

#Q2   BTW THE ANSWER IS YES TO ALL OF EM, MEOW. just rephrase dat shid pls n ty ilysm ma handsome boy!! :'DDD
a "Now... what do I eat?"
a "Someone who works here should at least know that much."
menu:
    "What do Anglerfish eat?"
    "Small fish":
        #block of code to run
    "Shrimp":
        #block of code to run
    "Squid":
    "Other Anglerfish":
        a "Well, yes."
        a "If I'm gonna be real, all of them are correct."
        a "I eat small fish, shrimp, squids and... as you have already gathered- Angler fish."
        a "Most things don't deter me, you know?"
        a "Not when we're conveniently able to eat prey twice our size."
        mc "Do you... actually mean that?"
        a "Hm? And what if I did?"
        mc "Nevermind..."
        a "Hmph."
    
#Q3
a "And how often do you think I need to? Eat, that is."
menu:
    "Say Statement"
    "Every day":
        a "I sure as hell hope not."
        a "Unlike lesser creatures of the sea, I would only need to eat every few weeks or months."
        a "Real convenient, don't you think?"
    "A week":
        a "A shabby attempt, really."
        a "Though I suppose it depends on the meal as well..."
        a "Hm. What would've been the right answer is if you had said every few weeks or months."
        a "Since we have slow metabolisms, it only makes sense."
    "Every few weeks":
        a "Correct, yes."
        a "Our metabolisms are slow so we are only required to eat every few weeks or months."
    "For months":
        a "That might've been a little vague, but I technically, yes."
        a "We only need to eat every few weeks or months, so I'll accept that as the right answer."
#Q4
a "Like many, I have a primary symbiotic relationship with a certain... something."
a "Do you have any idea what that might me?"
menu:
    "What is an Anglerfish's primary symbiotic relationship?"
    "Cleaning Symbiosis":
        a "Why would something like me need a cleaner fish? Don't be ridiculous."
        a "We have a symbiotic relationship with Bioluminescent Bacteria. Obviously."
        a ""
    "Isopods and fish":
        a "I can't tell whether you want to get eaten or if you're just that stupid..."
        a "Perhaps, both?"
        a "I'll ignore you said that, yes?"
    "Bioluminescent Bacteria":
        a "A smart one, aren't you?"
        a "Sigh. But yes."
        a "This bacteria live in my 'lure'."
        a "We have a symbiotic relationship with the luminous bacteria that live in the tip of our light."
        a "We provide the bacteria with nutrients and a home and they provide us with the light that attracts prey..."
        a "Prey just like you."
    "Other Anglerfish":
        a "Not primarily, no."
        a "That is an answer that I suppose makes sense but even so..."
        a "It's a little ignorant to think, is it not?"
        a "Do you see any other Anglerfish here?"
        a "Hm. Our primary symbiotic relationship is with Bioluminescent Bacteria."
        a "That's what lives and gives light to the tip of our 'lure.'"
        a "Though most aren't aware that that is how it works. Aren't I humble?"
    
#Q5
a "Now, here's something most aren't aware of."
a "I can't just be giving you the easiest of answers now, can I?"
a "That would hardly be entertaining."
a "Do you have any idea where my sensory organ may be located?"
menu:
    "Where is the sensory organ of the Black Seadevil?"
    "Lateral Line":
        a "I'm impressed. Though I'm sure that was just a lucky guess."
        a "Most don't know what a lateral line even is."
        a "That was intended to be a question to catch you out, just so you were aware."
        a "What a shame."
        a "But yes, the white dots scattered across my skin isn't just for show, you know?"
        a "These sensory organs form part of the lateral line system and are used to detect any tiny movement, vibration and pressure change in the surrounding water."
        mc "Like whiskers on a cat!"
        a "A... a cat..?"
        a "Sure..."
        a "Ahem."
    "Olfactory Organs (Sense of Smell)":
        a "Well, I should've more specific. Male Anglerfish are the ones who possess that kind of sense of smell."
        a "Though you'll find out about that later."
        a "What I was actually referring to was the lateral line."
        a "They are the white dots scattered across an Black Seadevil's skin which act as our sensory organs."
        a "With these we can detect any tiny movement, vibration and any pressure change in the surrounding water."
        a "Get it now?"
        mc "...So, does that still count?"
        a "Of course not."
    "The Butt"
        a "Real funny."
        a "Who's stopping me from eating you now, huh?"
        mc "My bad... it was just a joke... haha..."
        a "You irritable thing..."
        a "Why do I even bother entertaining this. Sigh."
        a "You don't deserve the real answer. Let's move on."
        mc "Wait-"
#Q6
a "Now... I have a secondary symbiotic relationship in a different regard to my lure."
a "I'd say this one is more commonly known so if you do get this wrong..."
a "Hmph."
menu:
    "What is an Anglerfish's secondary symbiotic relationship?"
    "Small fish":
        a "The only thing a small fish is good for to me is being my next meal. This was an easy one."
        a "Whatever."
        a "It's sexual paraitism. Male deep sea anglerfish are much smaller with no lure to attract prey. Making them... well, parasites."
        a "Our symbiotic relationship relies on the fact that they bite to attach themselves to us, merging with us bigger females in order for them too fertilise our eggs."
        a "They get our nutrients while we get... well that."
        a "Honestly, it's much more of nuisance in my opinion. They lose all their senses, their eyes being the first to go. Just for a chance to survive."
        a "Rather embarrassing if you ask me."
    "Sexual Parasitism"
        "That's right. The males of my species are... significantly much smaller."
        "Not to mention their ability to hunt effectively is lacking."
        "With no lure there is no ability to attract prey."
        "What other reason for them other than to end up as a parasite? Nature seems to end up making sense is the best of ways."
        "To put it simply though, the only use they have is their sense of smell. They use that to search for a mate and..."
        "They bite. They bite to permanently fuse with us larger females. Better females."
        a "They allow their tissues and blood vessles to merge with ours and... simply die!"
        a "First they lose their eyes, their finds and internal organs"
        a "Just kidding! They don't exactly die, though they might as well."
        a "In this relationship, he's completely catered for. He doesn't need his eyes, or anything else for that matter when he's just draining our resources..."
        a "But the chance that they can fertilise a females egg... it does technically imply a form of mutualism. I suppose."
        a "Are you scared yet? Pff..."
    "Isopods"
        a "Let's end this here. I'm exhausted."
        mc "Wait, aren't you going to elaborate?"
        a "No. I'm not."

    a "Well, let's leave it at that."
    a "This was a lot more labour than I had imagined...sigh..."
    #depending on the scoring, i'd say if mc gets 4 and more correct she says you pass.
    # though for a lesser score she's more wishful abt having yu as her snack.
   
    "Their eyes drift to the teardropped bracelet that weighed on your wrist."
    a "Oh, her."
    a "So that's who you were loudly chatting too..." 
    a "In the end, she did manage to make a friend huh. How amusing."
    mc "You're talking about... Lilith, aren't you?"
    a "Obviously. Can't you keep up?"
    a "And unfortunately, that changes a lot of things... that's a real shame..."
    mc "I'm not sure I follow... Uh..."
    mc "Aren't you going to eat me?"
    a "You sound as if you were looking forward to it."
    a "To answer your question, it simply would not be worth it. You're not worth it."
    a "I'd rather not deal with the consequences of making a snack out of you."
    a "Especially not from your rather {i}large{/i} jellyfish friend."
    mc "That's... rude."
    mc "You shouldn't say that about people."
    a "Oh silly you. One, we aren't {i}people{/i}."
    a "And two, that would no doubt be a compliment. Especially to someone like her."
    a "You have a whole lot of learning to do, don't you?"
    a "Sadly, I don't care enough to do the teaching."
    a "And let's be real. Who else will bring food down to this dome, if not someone as oblivious and irritable as you?"
    a "..."
    a "...Well? Why are you still here?"
    a "Run along now, I won't bother."

label go back up







    # This ends the game.

    return
