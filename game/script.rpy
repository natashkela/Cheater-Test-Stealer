image bg background1="background.jpg"
image bg campus="campus.jpg"
image bg director_office="Director-lost-game.jpg"
image bg game_introduction="intro.jpg"
image bg proffessor_beginning="Proffessor-at-the-board.jpg"
image bg campus_door="campus_door.jpg"
image bg campus_door_equation="campus_door_equation.jpg"
image bg campus_door_equation_easy_mode="campus_door_equation_easy_mode.jpg"
image bg campus_door_equation_hard_mode="campus_door_equation_hard_mode.jpg"
image bg elevator ="elevator_picture.jpg"
image bg elevator_easy_mode ="elevator_picture_easy_mode.jpg"
image bg elevator_hard_mode ="elevator_picture_hard_mode.jpg"
image bg game_over="Game_over_end_picture.jpg"
image bg game_over_moral_lost="game_over_moral_lost.jpg"
image bg office_door="office_door.jpg"
image bg proffessor_sleeping="Proffessor-at-the-board-sleeping.jpg"
image professor="professor.png"
image bg safe="safe.jpg"
image bg safe_easy="safe_easy.jpg"
image bg safe_hard="safe_hard.jpg"
image bg lost_game_picture="lost_game.jpg"
image mark_and_julie="mark_julie.png"
image bg gun="Gun.jpg"
image bg won="won.jpg"
image bg end="end.jpg"
image bg starter="starter_image.jpg"
image bg uni_inside="uni_inside.jpg"
image second_professor="second_professor.png"
image bg hint1="hint1.jpg"
image bg hint1_easy="hint1_easy.jpg"
image bg hint1_hard="hint1_hard.jpg"
image bg hint2="hint2.jpg"
image bg hint2_easy="hint2_easy.jpg"
image bg hint2_hard="hint2_hard.jpg"
image bg hint3="hint3.jpg"
image bg hint3_easy="hint3_easy.jpg"
image bg hint3_hard="hint3_hard.jpg"
image bg stairs_closed="stairs_closed.jpg"
image bg stairs_red="stairs_red.jpg"
#all the sounds are taken from website www.nardionline.net
#-----------------------------------------------------------------------
init:
    python:

        # This function will run a countdown of the given length. It will
        # be white until 5 seconds are left, and then red until 0 seconds are
        # left, and then will blink 0.0 when time is up. 
        def countdown(st, at, length=0.0):

            remaining = length - st

            if remaining > 2.0:
                return Text("%.1f" % remaining, color="#000", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=72)), None

#-----------------------------------------------------------------------------
    
label start:
play music "music.mp3" 
define P = Character (_("Professor"), color = "black")
define Mark = Character(_("Mark"), color="black")
define narrator = Character(_("Narrator"), color="black")
define MD= Character(_("Assignemt"), color="black")
define Director= Character(_("Director"), color="black")
define Anna = Character(_("Anna"), color="black")
define Maid = Character (_("Maid"), color="black")
scene bg starter
$ player_name = renpy.input("What is your name cheater girl?")
$ player_name = player_name.strip()
if player_name == "" :
     $player_name="Catherine"
label mode:
    scene bg background1
    menu:
        "Easy":
                jump easy
        "Medium":
                jump medium
        "Hard":
                jump hard
label medium:
scene bg proffessor_beginning
show professor at left_to_right
"Professor" "Hello everyone. I hope you all know that we are having a final exam tomorrow.
I have put a sample exam on the course website
as promised, so I hope all of
you have looked over it."
"Professor" "As all of you know, the exam will consist of roots,
exponential functions, and parabolic graphs"
player_name "*Thinks* Oh man!!! How did I forget about that?!
I was thinking about it this 
weekend and it flew out of my head"
"Professor" "Do not forget that you are not allowed to have
any electronic devices during the exam.
You are allowed to bring one sheet of notes,
pencils and erasers, or pens"
player_name "*Thinks* Yeah, right. Cause if I bring those 
I am gonna do well on the exam. 
I can't study everything in one day!"
"Narrator" "As the time went by, she got more and more nervous, 
but apparently she was not the only one"
scene bg campus
transform left_to_right:
    xalign 0.0 yalign 1.0
    linear 2.0 xalign 0.5
show mark_and_julie at left_to_right
    
player_name "OMG! Do you know that I forgot about the exam 
and I am not ready like at all?! I can't do it all today"
"Mark" "I know right?! I also forgot about it. I have no idea 
how I am going to study all the material today. We are so stupid! 
How can anyone forget about the FINAL EXAM?!"
player_name "This is awful- we are going to fail the course!"
"Mark" "Not if we know what is going to be on the test..."
player_name "*Silence*"
player_name "Are you suggesting we steal it?"
"Mark" "I mean, I can't do that, but if you do, 
I won't tell anyone at all. 
I am not pushing you or anything,
but I don't think there is any other way."
player_name "*Thinking to herself* Should I just steal it? 
No,no what if I get caught?! 
But everything would be so much easier if I had that test"
player_name "But how am I going to do that?!"
"Narrator" "After sometime, she remembers that..."
player_name "AH-HA! Mark once told me that tests are kept in a safe in the professor's office"
player_name "But how am I going to steal the tests if everyone is in the building?!
Or should I just wait until everyoneleaves and building is locked?"
player_name "That'll work. I am gonna do that!"

scene bg campus    

"Narrator" "She sits in the campus yard looking 
at professors coming out of the math department building"
player_name "OK! Its time! Everything is going to go perfectly! *I hope* "
"Narrator" "If anything goes wrong alarm will ring and whole school will know that you were trying to break into building. Are you sure you want to do this?"

menu choose:
     "Yes, I need that test!":
        jump go_on
     "No, this is a bad idea":
        jump lost_game_run


label go_on:
$menu_flag=1
scene bg campus_door
player_name "What should I do now? I do not have a key to the door and all of the professors are gone."
player_name "I have no idea how to sneak in"
"Narrator" "After a while one of the professors was passing near math department building"
transform right_to_left:
    xalign 1.0 yalign 1.0
    linear 2.0 xalign 0.5
show second_professor at right_to_left
"Professor" "Hey do you know that the building is closed?"
player_name "Yeah sure"
"Professor" "Then why are you standing here staring at the door? You have been here for 15 minutes"
player_name "OMG! what do I tell him now?"

menu choose_open:
        "I forgot my phone in class today and I need it ASAP":
           jump open_the_door
        "I have project to do in math class and I need a book from class":
           jump open_the_door

label open_the_door:
$menu_flag=1
scene bg campus_door
show second_professor
"Professor" "I can open it for you, but with only one condition"
player_name "What's that?"
"Professor" "You should simplify one function for me"
player_name "Okay I will try my best"
scene bg campus_door_equation
"Assignment" "You have to sipmlify the given function in order to open the main door of math department building."
#---------------------------------------------------------
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))
#---------------------------------------------------------
#timer here in a time limit of 1:30 minute

menu choose1:
       "(x-8)(x+11)(x+16)":
            jump choice1_wrong
       "(x-8)(x+16)(x+11)":
            jump choice1_wrong
       "(x+8)(x-11)(x+16)":
            jump choice1_wrong
       "(x-8)(x-11)(x-16)":
            jump choice1_wrong
       "(x+8)(x-11)(x-16)":
            jump choice1_right
       "I need a hint here":
            jump hint1

label out_of_time:
    scene bg game_over
    play sound  "game_lost.wav"
    "Narrator" "Sorry you are out of time"
    return
label hint1:
    scene bg hint1
    "Professor" "Here you go, now you can try to solve it again"
scene bg campus_door_equation
#------------------------------------------------------
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))
#-----------------------------------------------------
menu choose_1:
    "(x-8)(x+11)(x+16)":
        jump choice1_wrong
    "(x-8)(x+16)(x+11)":
        jump choice1_wrong
    "(x+8)(x-11)(x+16)":
        jump choice1_wrong
    "(x-8)(x-11)(x-16)":
        jump choice1_wrong
    "(x+8)(x-11)(x-16)":
        jump choice1_right
label choice1_wrong:
scene bg campus_door_equation
"Professor" "It is okay, do not be sad because many of my students today could not solve this problem too."
player_name "So, will you open the door for me?"
"Professor" "Yeah, sure do not worry about it."
$menu_flag=0
jump game_continues
label choice1_right:
scene bg campus_door_equation
$menu_flag=1
#gaxarebuli
"Professor" "Well done! Many of my students today could not solve this problem on exam and I was just wondering if you could do it!"
"Professor" "Good for you! You should be one of the best students in class"
player_name "I'm best in worst students, but thank you for being nice"
"Professor" "Okay you can go in there now I have another class to take care of."
"Professor" "When you come out make sure that door closes automatically or call help desk"
player_name "Sure I will do that"

jump game_continues

label lost_game:
scene bg lost_game_picture
"Professor" "How dare you try stealing the test? We are going to go straight to the directors office!"
player_name "Please, don't do that! I am so sorry!"
"Professor" "I am sorry too, but you should have thought about this before you tried stealing the exam"

scene bg director_office
"Director" "You have violated school policy number 3.4, which results in expulsion. I have never encountered a problem like this before"
"Director" "I am sorry but you brought this upon yourself. Unfortunately you are expelled from our university"
scene bg game_over
"Narrator" "GAME OVER"
play sound "game_lost.wav"
scene bg game_over_moral_lost
"Narrator" "Remember this!!"
return

label game_continues:
scene bg uni_inside
"Maid" "Hey! Hey you!!! What are you doing here the building is supposed to be closed!"
player_name "Oh! Hi! I just..."
menu:
          "left my phone in the class":
                  jump cleaner_scene
          "wanted to check if my book was in the class":
                  jump cleaner_scene
label cleaner_scene:
"Maid" "Oh! I am so sorry dear! I was just told that no one could get in here at this time"
player_name "Yeah I know. I could not get in and a professor let me in"
"Maid" "Okay dear do what you have to do. I do not want to disturb you"
player_name "Its okay. Thanks!"
#elevator picture form outside without any equations
"Narrator" "After some time she realizes that an elavator works with ID card, which will not work now"
player_name "What do I do now?"
menu:
           "ask a cleaning lady to let you go up with her ID card":
                jump ask_elevator
           "Try to sneak in with emergency stairs":
                jump emergency_stairs
label ask_elevator:
$menu_flag=1
player_name "Excuse me miss I am sorry that I am bothering you, but would you please be so kind to let me on 8th floor with your ID?"
player_name "Mine would not work now"
"Maid" "Of course dear, but you will have to do one favor for me also"
player_name "Okay, how can I help you?"
"Maid" "My son studies here and he told me that he could not solve one equation. 
If you will solve it for me I will let you up, if not you will have to leave the building"
player_name "Sure, I will try my best to help your son. What is the equation?"
jump inside_elevator
label emergency_stairs:
scene bg stairs_closed
$menu_flag=0
player_name "I think this should work"
scene bg stairs_red
"Narrator" "You just tried to go up with emergency stairs. Alarm started, therefore everyone is released from the building"
jump game_lost_emergency_door
label game_lost_emergency_door:
scene bg campus
player_name "This was my only chance! How did I not think about alarm sound! UGHH, I will fail the exam tomorrow"
scene bg game_over
play sound "game_lost.wav"
"Narrator" "Game Over"
return
label inside_elevator:    
scene bg elevator
"Assignment" "Solve this problem to make the lady give you ID card"
#------------------------------------------------
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=210.0)
$ ui.timer(210.0, ui.jumps("out_of_time"))
#---------------------------------------------------
menu :
        "(-1,-2)":
            jump choice2_wrong
        "(-2,-1)":
            jump choice2_wrong
        "(1,2)":
            jump choice2_wrong
        "(1,-2)":
            jump choice2_right
        "(2,1)":
            jump choice2_wrong
        "I need a hint here":
            jump hint2
label hint2:

    scene bg hint2
    "Maid" "My son said that he tried to do it with these formulas, maybe you can try it out too."
    scene bg elevator
#--------------------------------------------------------------------
    show countdown at Position(xalign=.1, yalign=.9)
    image countdown = DynamicDisplayable(countdown, length=210.0)
    $ ui.timer(210.0, ui.jumps("out_of_time"))
#-----------------------------------------------------------------------
    menu:
        "(-1,-2)":
               jump choice2_wrong
        "(-2,-1)":
               jump choice2_wrong
        "(1,2)":
               jump choice2_wrong
        "(1,-2)":
               jump choice2_right
        "(2,1)":
               jump choice2_wrong
label choice2_wrong:
$menu_flag=0
jump lost_game_ID
label lost_game_ID:
scene bg uni_inside
player_name "I tried, but I could not solve it sorry. So will you let me go up?"
"Maid" "I am so sorry dear, but things do not work this way, we had an agreement remember"
"Maid" "You will have to leave the building now"
player_name "Okay..."
play sound "game_lost.wav"
scene bg game_over
"Narrator" "Game Over"
return

label choice2_right:
scene bg uni_inside
$menu_flag=1
"Maid" "Thank you so much dear, you are more then welcome to use my card now"
player_name "Thank you so much!"
jump game_continues1

label game_continues1:
#picture of office door without equation
"Narrator" "She went up on the 8th floor and saw class door"
player_name "Finally! I cannot believe that I got here! Only thing left to do is go in there and open the safe!"
"Narrator" "She tried to open the door several times, though she could not"
player_name "I should think of something right now!"
"Narrator" "After sometime she remembers that offices' security system is really well designed and even professors have to solve some random problems to get in there when door is locked."
player_name "Okay, I should be able to do it, but if I don't everything will go to waste."
"Narrator" "Deciding to solve office door problem, she risked expulsion from university. If she did not do it correctly the alarm would start in whole university"
scene bg office_door
#---------------------------------------------------
show countdown at Position(xalign=.0001, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))
#---------------------------------------------------
menu :
      "0":
         jump choice3_wrong
      "21":
         jump choice3_wrong
      "23":
         jump choice3_right
      "22":
         jump choice3_wrong
      "13":
         jump choice3_wrong

label choice3_wrong:
$menu_flag=0
jump lost_game

label choice3_right:
$menu_flag=1
jump game_continues2

label game_continues2:
scene bg proffessor_sleeping
player_name "OMG!!! What is he still doing here??? What am I gonna do now???"

menu :
       "Run you idiot run!!!":
            jump choice4_wrong

       "Stay in the room and take the risk":
            jump choice4_right

       "I don't know what to do":
            jump choice4_no

label choice4_no:
$menu_flag=2
"Narrator" "You've come this far already- don't give up now! Decide what you need to do before the professor wakes up!"
jump figure_out_what_to_do

label choice4_wrong:
$menu_flag=0
jump lost_game_run

label choice4_right:
$menu_flag=1
jump game_continues3

label lost_game_run:
scene bg game_over
"Narrator" "If you started something then finish it!"
play sound "game_lost.wav"
return
label figure_out_what_to_do:
menu:
            "Stealing a test is crazy! I should not have come here":
               jump lost_game_run
            "I'm gonna steal the test and rock the exam!!!":
               jump game_continues3

label game_continues3:
player_name "I cannot believe that I am here! Though, how do I open the safe if I do not know the code?"

menu :
                "Take out a gun and make the professor tell you the code":
                     jump choice5_wrong
                "Try it yourself":
                     jump choice5_right

label choice5_wrong:
$menu_flag=0
jump lost_game1

label lost_game1:
player_name "Wake up and tell me the code of your safe right now!!!"
scene bg proffessor_beginning
"Professor" "What are you doing and why are you pointing a gun at me??"
scene bg gun
player_name "Because I have to steal your tests you idiot. I do not know anything about the exam tomorrow"
"Professor" "That test is not that important- you would kill me if I didn't give you the passcode for the safe??"
player_name "*Looks away and thinks about it for a minute*"
"Professor" "*Runs*"
jump lost_game_gun


label lost_game_gun:
scene bg director_office
"Narrator" "Professor went in director's office and told him the whole story, which resulted in this..."
"Director" "You have violated almost everything in the school's policy. I am really disappointed that we did not see the real you when we were admitting you. I have never encountered a problem like this before!"
"Director" "You are expelled from our University!"
scene bg game_over
"Narrator" "GAME OVER"
play sound "game_lost.wav"
scene bg game_over_moral_lost
"Narrator" "Remember this!!"
return
label choice5_right:
$menu_flag=1
"Assignment" "If you want to open the safe by your own go ahead, but that means that you should think of the code too"
jump game_continues4

label game_continues4:
player_name "What should I do right now?? From where the hell should I know the safe code?!"

menu:
            "Call a friend and ask her for help":
                 jump choice6_wrong
            "NO! I said I will solve it myself!!!":
                 jump choice6_right
            "Not sure what to do - I am getting out of here!":
                 jump lost_game_run

label choice6_wrong:
$menu_flag=0
jump lost_game_call
label lost_game_call:
#I should have picture of Anna here
player_name "Hey Anna, I know that I am calling you really late, but I have to tell you something and you cannot tell anyone else"
"Anna" "Are you okay?? What happened?"
player_name "Just swear that you are not going to tell anyone!!"
"Anna" "Okay, okay I swear!!"
player_name "So, you know about the test we are having tomorrow in math?"
"Anna" "Yes, why?"
player_name "So, I am trying to steal it and its in a safe and you have to help me unlock it"
"Anna" "Okay, that means that you are not okay! I am not going to help you do that!! Sorry bye!!"
player_name "At least promise you won't tell anyone that I called you okay?"
"Anna" "Okay, no problem!"
"Anna" "*thinks* Nah! I am calling the director"
"Anna" "*Rings*"
"Director" "Hello?"
"Anna" "Hi, its Anna. I am so sorry that I am calling this late, but someone is trying to steal a math exam and I thought it was important for me to tell someone"
"Director" "Are you sure? Because the math department is locked right now."
"Anna" "I am pretty sure. That's all I can tell you. Bye"
"Director" "Okay, thanks for calling. Bye"
jump lost_game
label choice6_right:
scene bg safe
"Assigment" "What you have to do know is solve an arithmetic progression problem. Hurry up- its your last step!!!"
#----------------------------------------------------
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=180.0)
$ ui.timer(180.0, ui.jumps("out_of_time"))
#----------------------------------------------------
menu :
             "Password is: 1369":
                  jump choice7_wrong
             "Password is: 1359":
                  jump choice7_wrong
             "Password is: 14710":
                  jump choice7_right
             "Password is: 14711":
                  jump choice7_wrong
             "Password is: 15711":
                  jump choice7_wrong
             "Password is: 14912":
                  jump choice7_wrong
             "I really need a hint here!!!":
                  jump hint3
label hint3:
    scene bg hint3
    "Assignment" "This is the last step. Try using this formula, but figure out what n should be by yourself"
    scene bg safe
#------------------------------------------------------
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=180.0)
$ ui.timer(180.0, ui.jumps("out_of_time"))
#----------------------------------------------------------
menu :
     "Password is: 1369":
         jump choice7_wrong
     "Password is: 1359":
         jump choice7_wrong
     "Password is: 14710":
         jump choice7_right
     "Password is: 14711":
         jump choice7_wrong
     "Password is: 15711":
         jump choice7_wrong
     "Password is: 14912":
         jump choice7_wrong


label choice7_wrong:
$menu_flag=0
jump lost_game

label choice7_right:
scene bg proffessor_beginning
"Professor" "So, many of the people did not get good grades on this exam, but one student recieved a 100."
"Professor" "Apparanetly you studied hard- when you do that your work speaks for itself!"
player_name "Thanks professor! You cannot even imagine what I went through yesterday to get this grade"
"Professor" "Believe me- I've heard stories like this 1000 times"
player_name "I bet not (thinks to herself)"
scene bg won
play sound "game_won.mp3"
"Narrator" "Congratulations!!!"
scene bg end
"Narrator" "Remember!"
return




#---------------------------------------------------------------------------------------------------------------------------------------------



label easy:
scene bg proffessor_beginning
show professor at left_to_right
"Professor" "Hello everyone. I hope you all know that we are having a final exam tomorrow.
I have put a sample exam on the course website
as promised, so I hope all of
you have looked over it."
"Professor" "As all of you know, the exam will consist of sum and differences and
equations"
player_name "*Thinks* Oh man!!! How did I forget about that?!
I was thinking about it this 
weekend and it flew out of my head"
"Professor" "Do not forget that you are not allowed to have
any electronic devices during the exam.
You are allowed to bring one sheet of notes,
pencils and erasers, or pens"
player_name "*Thinks* Yeah, right. Cause if I bring those 
I am gonna do well on the exam. 
I can't study everything in one day!"
"Narrator" "As the time went by, she got more and more nervous, 
but apparently she was not the only one"
scene bg campus
show mark_and_julie at left_to_right

player_name "OMG! Do you know that I forgot about the exam 
and I am not ready like at all?! I can't do it all today"
"Mark" "I know right?! I also forgot about it. I have no idea 
how I am going to study all the material today. We are so stupid! 
How can anyone forget about the FINAL EXAM?!"
player_name "This is awful- we are going to fail the course!"
"Mark" "Not if we know what is going to be on the test..."
player_name "*Silence*"
player_name "Are you suggesting we steal it?"
"Mark" "I mean, I can't do that, but if you do, 
I won't tell anyone at all. 
I am not pushing you or anything,
but I don't think there is any other way."
player_name "*Thinking to herself* Should I just steal it? 
No,no what if I get caught?! 
But everything would be so much easier if I had that test"
player_name "But how am I going to do that?!"
"Narrator" "After sometime, she remembers that..."
player_name "AH-HA! Mark once told me that tests are kept in a safe in the professor's office"
player_name "But how am I going to steal the tests if everyone is in the building?!
Or should I just wait until everyoneleaves and building is locked?"
player_name "That'll work. I am gonna do that!"

scene bg campus    

"Narrator" "She sits in the campus yard looking 
at professors coming out of the math department building"
player_name "OK! Its time! Everything is going to go perfectly! *I hope* "
"Narrator" "If anything goes wrong alarm will ring and whole school will know that you were trying to break into building. Are you sure you want to do this?"

menu choose_easy:
     "Yes, I need that test!":
        jump go_on_easy
     "No, this is a bad idea":
        jump lost_game_run_easy


label go_on_easy:
$menu_flag=1
scene bg campus_door
player_name "What should I do now? I do not have a key to the door and all of the professors are gone."
player_name "I have no idea how to sneak in"
"Narrator" "After a while one of the professors was passing near math department building"
transform right_to_left:
    xalign 1.0 yalign 1.0
    linear 2.0 xalign 0.5
show second_professor at right_to_left
"Professor" "Hey do you know that the building is closed?"
player_name "Yeah sure"
"Professor" "Then why are you standing here staring at the door? You have been here for 15 minutes"
player_name "OMG! what do I tell him now?"

menu choose_open_easy:
        "I forgot my phone in class today and I need it ASAP":
           jump open_the_door_easy
        "I have project to do in math class and I need a book from class":
           jump open_the_door_easy

label open_the_door_easy:
$menu_flag=1
scene bg campus_door
show second_professor
"Professor" "I can open it for you, but with only one condition"
player_name "What's that?"
"Professor" "You should simplify one function for me"
player_name "Okay I will try my best"
scene bg campus_door_equation_easy_mode
"Assignment" "You have to sipmlify the given function in order to open the main door of math department building."

#timer here in a time limit of 1:30 minute
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))
menu choose1_easy:
       "-24":
            jump choice1_wrong_easy
       "24":
            jump choice1_wrong_easy
       "16":
            jump choice1_wrong_easy
       "-28":
            jump choice1_right_easy
       "28":
            jump choice1_wrong_easy
       "I need a hint here":
            jump hint1_easy

label hint1_easy:
    scene bg hint1_easy
    "Professor" "Here you go, now you can try to solve it again"
    scene bg campus_door_equation_easy_mode
    show countdown at Position(xalign=.1, yalign=.9)
    image countdown = DynamicDisplayable(countdown, length=90.0)
    $ ui.timer(90.0, ui.jumps("out_of_time"))

menu choose_1_easy:
       "-24":
           jump choice1_wrong_easy
       "24":
           jump choice1_wrong_easy
       "16":
           jump choice1_wrong_easy
       "-28":
           jump choice1_right_easy
       "28":
           jump choice1_wrong_easy

label choice1_wrong_easy:
scene bg campus_door
"Professor" "It is okay, do not be sad because many of my students today could not solve this problem too."
player_name "So, will you open the door for me?"
"Professor" "Yeah, sure do not worry about it."
$menu_flag=0
jump game_continues_easy
label choice1_right_easy:
scene bg campus_door
$menu_flag=1
#gaxarebuli
"Professor" "Well done! Many of my students today could not solve this problem on exam and I was just wondering if you could do it!"
"Professor" "Good for you! You should be one of the best students in class"
player_name "I'm best in worst students, but thank you for being nice"
"Professor" "Okay you can go in there now I have another class to take care of."
"Professor" "When you come out make sure that door closes automatically or call help desk"
player_name "Sure I will do that"

jump game_continues_easy

label lost_game_easy:
scene bg lost_game_picture
"Professor" "How dare you try stealing the test? We are going to go straight to the directors office!"
player_name "Please, don't do that! I am so sorry!"
"Professor" "I am sorry too, but you should have thought about this before you tried stealing the exam"

scene bg director_office
"Director" "You have violated school policy number 3.4, which results in expulsion. I have never encountered a problem like this before"
"Director" "I am sorry but you brought this upon yourself. Unfortunately you are expelled from our university"
scene bg game_over
"Narrator" "GAME OVER"
play sound "game_lost.wav"
scene bg game_over_moral_lost
"Narrator" "Remember this!!"
return

label game_continues_easy:
scene bg uni_inside
"Maid" "Hey! Hey you!!! What are you doing here the building is supposed to be closed!"
player_name "Oh! Hi! I just..."
menu:
          "left my phone in the class":
                  jump cleaner_scene_easy
          "wanted to check if my book was in the class":
                  jump cleaner_scene_easy
label cleaner_scene_easy:
"Maid" "Oh! I am so sorry dear! I was just told that no one could get in here at this time"
player_name "Yeah I know. I could not get in and a professor let me in"
"Maid" "Okay dear do what you have to do. I do not want to disturb you"
player_name "Its okay. Thanks!"
#elevator picture form outside without any equations
"Narrator" "After some time she realizes that an elavator works with ID card, which will not work now"
player_name "What do I do now?"
menu:
           "ask a cleaning lady to let you go up with her ID card":
                jump ask_elevator_easy
           "Try to sneak in with emergency stairs":
                jump emergency_stairs_easy
label ask_elevator_easy:
$menu_flag=1
player_name "Excuse me miss I am sorry that I am bothering you, but would you please be so kind to let me on 8th floor with your ID?"
player_name "Mine would not work now"
"Maid" "Of course dear, but you will have to do one favor for me also"
player_name "Okay, how can I help you?"
"Maid" "My son studies here and he told me that he could not solve one equation. 
If you will solve it for me I will let you up, if not you will have to leave the building"
player_name "Sure, I will try my best to help your son. What is the equation?"
jump inside_elevator_easy
label emergency_stairs_easy:
scene bg stairs_closed
$menu_flag=0
player_name "I think this should work"
scene bg stairs_red
"Narrator" "You just tried to go up with emergency stairs. Alarm started, therefore everyone is released from the building"
jump game_lost_emergency_door_easy
label game_lost_emergency_door_easy:
scene bg campus
player_name "This was my only chance! How did I not think about alarm sound! UGHH, I will fail the exam tomorrow"
scene bg game_over
play sound "game_lost.wav"
"Narrator" "Game Over"
return
label inside_elevator_easy:    
scene bg elevator_easy_mode
"Assignment" "Solve this problem to make the lady give you ID card"
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=210.0)
$ ui.timer(210.0, ui.jumps("out_of_time"))
menu :
        "6":
            jump choice2_wrong_easy
        "-6":
            jump choice2_wrong_easy
        "8":
            jump choice2_right_easy
        "-8":
            jump choice2_wrong_easy
        "4":
            jump choice2_wrong_easy
        "I need a hint here":
            jump hint2_easy
label hint2_easy:
    scene bg hint2_easy
    "Maid" "My son said that he went up to this point and then could not go on, maybe you can try it out too and finish it."
    scene bg elevator_easy_mode
    show countdown at Position(xalign=.1, yalign=.9)
    image countdown = DynamicDisplayable(countdown, length=210.0)
    $ ui.timer(210.0, ui.jumps("out_of_time"))
    menu:
        "6":
            jump choice2_wrong_easy
        "-6":
            jump choice2_wrong_easy
        "8":
            jump choice2_right_easy
        "-8":
            jump choice2_wrong_easy
        "4":
            jump choice2_wrong_easy
label choice2_wrong_easy:
$menu_flag=0
jump lost_game_ID_easy
label lost_game_ID_easy:
scene bg uni_inside
player_name "I tried, but I could not solve it sorry. So will you let me go up?"
"Maid" "I am so sorry dear, but things do not work this way, we had an agreement remember"
"Maid" "You will have to leave the building now"
player_name "Okay..."
play sound "game_lost.wav"
scene bg game_over
"Narrator" "Game Over"
return

label choice2_right_easy:
scene bg uni_inside
$menu_flag=1
"Maid" "Thank you so much dear, you are more then welcome to use my card now"
player_name "Thank you so much!"
jump game_continues1_easy

label game_continues1_easy:
"Narrator" "She went up on the 8th floor and saw class door"
player_name "Finally! I cannot believe that I got here! Only thing left to do is go in there and open the safe!"
"Narrator" "She tried to open the door several times, though she could not"
player_name "I should think of something right now!"
"Narrator" "After sometime she remembers that offices' security system is really well designed and even professors have to solve some random problems to get in there when door is locked."
player_name "Okay, I should be able to do it, but if I don't everything will go to waste."
"Narrator" "Deciding to solve office door problem, she risked expulsion from university. If she did not do it correctly the alarm would start in whole university"
scene bg office_door
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))
menu :
      "0":
         jump choice3_wrong_easy
      "21":
         jump choice3_wrong_easy
      "23":
         jump choice3_right_easy
      "22":
         jump choice3_wrong_easy
      "13":
         jump choice3_wrong_easy

label choice3_wrong_easy:
$menu_flag=0
jump lost_game_easy

label choice3_right_easy:
$menu_flag=1
jump game_continues2_easy

label game_continues2_easy:
scene bg proffessor_sleeping
player_name "OMG!!! What is he still doing here??? What am I gonna do now???"

menu :
       "Run you idiot run!!!":
            jump choice4_wrong_easy

       "Stay in the room and take the risk":
            jump choice4_right_easy

       "I don't know what to do":
            jump choice4_no_easy

label choice4_no_easy:
$menu_flag=2
"Narrator" "You've come this far already- don't give up now! Decide what you need to do before the professor wakes up!"
jump figure_out_what_to_do_easy

label choice4_wrong_easy:
$menu_flag=0
jump lost_game_run_easy

label choice4_right_easy:
$menu_flag=1
jump game_continues3_easy

label lost_game_run_easy:
scene bg game_over
"Narrator" "If you started something then finish it!"
play sound "game_lost.wav"
return
label figure_out_what_to_do_easy:
menu:
            "Stealing a test is crazy! I should not have come here":
               jump lost_game_run_easy
            "I'm gonna steal the test and rock the exam!!!":
               jump game_continues3_easy

label game_continues3_easy:
player_name "I cannot believe that I am here! Though, how do I open the safe if I do not know the code?"

menu :
                "Take out a gun and make the professor tell you the code":
                     jump choice5_wrong_easy
                "Try it yourself":
                     jump choice5_right_easy

label choice5_wrong_easy:
$menu_flag=0
jump lost_game1_easy

label lost_game1_easy:
player_name "Wake up and tell me the code of your safe right now!!!"
scene bg proffessor_beginning
"Professor" "What are you doing and why are you pointing a gun at me??"
scene bg gun
player_name "Because I have to steal your tests you idiot. I do not know anything about the exam tomorrow"
"Professor" "That test is not that important- you would kill me if I didn't give you the passcode for the safe??"
player_name "*Looks away and thinks about it for a minute*"
"Professor" "*Runs*"
jump lost_game_gun_easy


label lost_game_gun_easy:
scene bg director_office
"Narrator" "Professor went in director's office and told him the whole story, which resulted in this..."
"Director" "You have violated almost everything in the school's policy. I am really disappointed that we did not see the real you when we were admitting you. I have never encountered a problem like this before!"
"Director" "You are expelled from our University!"
scene bg game_over
"Narrator" "GAME OVER"
play sound "game_lost.wav"
scene bg game_over_moral_lost
"Narrator" "Remember this!!"
return
label choice5_right_easy:
$menu_flag=1
"Assignment" "If you want to open the safe by your own go ahead, but that means that you should think of the code too"
jump game_continues4_easy

label game_continues4_easy:
player_name "What should I do right now?? From where the hell should I know the safe code?!"

menu:
            "Call a friend and ask her for help":
                 jump choice6_wrong_easy
            "NO! I said I will solve it myself!!!":
                 jump choice6_right_easy
            "Not sure what to do - I am getting out of here!":
                 jump lost_game_run_easy

label choice6_wrong_easy:
$menu_flag=0
jump lost_game_call_easy
label lost_game_call_easy:
#I should have picture of Anna here
player_name "Hey Anna, I know that I am calling you really late, but I have to tell you something and you cannot tell anyone else"
"Anna" "Are you okay?? What happened?"
player_name "Just swear that you are not going to tell anyone!!"
"Anna" "Okay, okay I swear!!"
player_name "So, you know about the test we are having tomorrow in math?"
"Anna" "Yes, why?"
player_name "So, I am trying to steal it and its in a safe and you have to help me unlock it"
"Anna" "Okay, that means that you are not okay! I am not going to help you do that!! Sorry bye!!"
player_name "At least promise you won't tell anyone that I called you okay?"
"Anna" "Okay, no problem!"
"Anna" "*thinks* Nah! I am calling the director"
"Anna" "*Rings*"
"Director" "Hello?"
"Anna" "Hi, its Anna. I am so sorry that I am calling this late, but someone is trying to steal a math exam and I thought it was important for me to tell someone"
"Director" "Are you sure? Because the math department is locked right now."
"Anna" "I am pretty sure. That's all I can tell you. Bye"
"Director" "Okay, thanks for calling. Bye"
jump lost_game_easy
label choice6_right_easy:
scene bg safe_easy
"Assigment" "What you have to do know is solve three equations and aswers to them will be password for the safe. Hurry up- its your last step!!!"
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=180.0)
$ ui.timer(180.0, ui.jumps("out_of_time"))
menu :
             "Password is: 2040":
                  jump choice7_right_easy
             "Password is: 200":
                  jump choice7_wrong_easy
             "Password is: 2042":
                  jump choice7_wrong_easy
             "Password is: 2041":
                  jump choice7_wrong_easy
             "Password is: 2140":
                  jump choice7_wrong_easy
             "Password is: 2240":
                  jump choice7_wrong_easy
             "I really need a hint here!!!":
                  jump hint3_easy
label hint3_easy:
    scene bg hint3_easy
    "Assignment" "This is the last step. Try using this equality, but figure out what the answers by yourself"
    scene bg safe_easy
    show countdown at Position(xalign=.1, yalign=.9)
    image countdown = DynamicDisplayable(countdown, length=180.0)
    $ ui.timer(180.0, ui.jumps("out_of_time"))
menu :
            "Password is: 2040":
                  jump choice7_right_easy
            "Password is: 200":
                  jump choice7_wrong_easy
            "Password is: 2042":
                  jump choice7_wrong_easy
            "Password is: 2041":
                  jump choice7_wrong_easy
            "Password is: 2140":
                  jump choice7_wrong_easy
            "Password is: 2240":
                  jump choice7_wrong_easy


label choice7_wrong_easy:
$menu_flag=0
jump lost_game_easy

label choice7_right_easy:
scene bg proffessor_beginning
"Professor" "So, many of the people did not get good grades on this exam, but one student recieved a 100."
"Professor" "Apparanetly you studied hard- when you do that your work speaks for itself!"
player_name "Thanks professor! You cannot even imagine what I went through yesterday to get this grade"
"Professor" "Believe me- I've heard stories like this 1000 times"
player_name "I bet not (thinks to herself)"
scene bg won
play sound "game_won.mp3"
"Narrator" "Congratulations!!!"
scene bg end
"Narrator" "Remember!"
return



#--------------------------------------------------------------------------------------------------------------------------------





label hard:
scene bg proffessor_beginning
show professor at left_to_right
"Professor" "Hello everyone. I hope you all know that we are having a final exam tomorrow.
I have put a sample exam on the course website
as promised, so I hope all of
you have looked over it."
"Professor" "As all of you know, the exam will consist of derivatives,
trigonometric equations and critical points"
player_name "*Thinks* Oh man!!! How did I forget about that?!
I was thinking about it this 
weekend and it flew out of my head"
"Professor" "Do not forget that you are not allowed to have
any electronic devices during the exam.
You are allowed to bring one sheet of notes,
pencils and erasers, or pens"
player_name "*Thinks* Yeah, right. Cause if I bring those 
I am gonna do well on the exam. 
I can't study everything in one day!"
"Narrator" "As the time went by, she got more and more nervous, 
but apparently she was not the only one"
scene bg campus
show mark_and_julie at left_to_right
player_name "OMG! Do you know that I forgot about the exam 
and I am not ready like at all?! I can't do it all today"
"Mark" "I know right?! I also forgot about it. I have no idea 
how I am going to study all the material today. We are so stupid! 
How can anyone forget about the FINAL EXAM?!"
player_name "This is awful- we are going to fail the course!"
"Mark" "Not if we know what is going to be on the test..."
player_name "*Silence*"
player_name "Are you suggesting we steal it?"
"Mark" "I mean, I can't do that, but if you do, 
I won't tell anyone at all. 
I am not pushing you or anything,
but I don't think there is any other way."
player_name "*Thinking to herself* Should I just steal it? 
No,no what if I get caught?! 
But everything would be so much easier if I had that test"
player_name "But how am I going to do that?!"
"Narrator" "After sometime, she remembers that..."
player_name "AH-HA! Mark once told me that tests are kept in a safe in the professor's office"
player_name "But how am I going to steal the tests if everyone is in the building?!
Or should I just wait until everyoneleaves and building is locked?"
player_name "That'll work. I am gonna do that!"

scene bg campus    

"Narrator" "She sits in the campus yard looking 
at professors coming out of the math department building"
player_name "OK! Its time! Everything is going to go perfectly! *I hope* "
"Narrator" "If anything goes wrong alarm will ring and whole school will know that you were trying to break into building. Are you sure you want to do this?"

menu choose_hard:
     "Yes, I need that test!":
        jump go_on_hard
     "No, this is a bad idea":
        jump lost_game_run_hard


label go_on_hard:
$menu_flag=1
scene bg campus_door
player_name "What should I do now? I do not have a key to the door and all of the professors are gone."
player_name "I have no idea how to sneak in"
"Narrator" "After a while one of the professors was passing near math department building"
transform right_to_left:
    xalign 1.0 yalign 1.0
    linear 2.0 xalign 0.5
show second_professor at right_to_left
"Professor" "Hey do you know that the building is closed?"
player_name "Yeah sure"
"Professor" "Then why are you standing here staring at the door? You have been here for 15 minutes"
player_name "OMG! what do I tell him now?"

menu choose_open_hard:
        "I forgot my phone in class today and I need it ASAP":
           jump open_the_door_hard
        "I have project to do in math class and I need a book from class":
           jump open_the_door_hard

label open_the_door_hard:
$menu_flag=1
scene bg campus_door
show second_professor
"Professor" "I can open it for you, but with only one condition"
player_name "What's that?"
"Professor" "You should simplify one function for me"
player_name "Okay I will try my best"
scene bg campus_door_equation_hard_mode
"Assignment" "You have to sipmlify the given function in order to open the main door of math department building."
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))


menu choose1_hard:
       "cos(2x)+2":
            jump choice1_wrong_hard
       "sin(2x)+1":
            jump choice1_right_hard
       "cos(2x)+1":
            jump choice1_wrong_hard
       "sin(2x)-1":
            jump choice1_wrong_hard
       "sin(2x)":
            jump choice1_wrong_hard
       "I need a hint here":
            jump hint1_hard

label hint1_hard:
    scene bg hint1_hard
    "Professor" "Here you go, now you can try to solve it again"
scene bg campus_door_equation_hard_mode
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))
menu choose_1_hard:
       "cos(2x)+2":
            jump choice1_wrong_hard
       "sin(2x)+1":
            jump choice1_right_hard
       "cos(2x)+1":
            jump choice1_wrong_hard
       "sin(2x)-1":
            jump choice1_wrong_hard
       "sin(2x)":
            jump choice1_wrong_hard

label choice1_wrong_hard:
scene bg campus_door_equation_hard_mode
"Professor" "It is okay, do not be sad because many of my students today could not solve this problem too."
player_name "So, will you open the door for me?"
"Professor" "Yeah, sure do not worry about it."
$menu_flag=0
jump game_continues_hard
label choice1_right_hard:
scene bg campus_door
$menu_flag=1
#gaxarebuli
"Professor" "Well done! Many of my students today could not solve this problem on exam and I was just wondering if you could do it!"
"Professor" "Good for you! You should be one of the best students in class"
player_name "I'm best in worst students, but thank you for being nice"
"Professor" "Okay you can go in there now I have another class to take care of."
"Professor" "When you come out make sure that door closes automatically or call help desk"
player_name "Sure I will do that"

jump game_continues_hard

label lost_game_hard:
scene bg lost_game_picture
"Professor" "How dare you try stealing the test? We are going to go straight to the directors office!"
player_name "Please, don't do that! I am so sorry!"
"Professor" "I am sorry too, but you should have thought about this before you tried stealing the exam"

scene bg director_office
"Director" "You have violated school policy number 3.4, which results in expulsion. I have never encountered a problem like this before"
"Director" "I am sorry but you brought this upon yourself. Unfortunately you are expelled from our university"
scene bg game_over
"Narrator" "GAME OVER"
play sound "game_lost.wav"
scene bg game_over_moral_lost
"Narrator" "Remember this!!"
return

label game_continues_hard:
scene bg uni_inside
"Maid" "Hey! Hey you!!! What are you doing here the building is supposed to be closed!"
player_name "Oh! Hi! I just..."
menu:
          "left my phone in the class":
                  jump cleaner_scene_hard
          "wanted to check if my book was in the class":
                  jump cleaner_scene_hard
label cleaner_scene_hard:
"Maid" "Oh! I am so sorry dear! I was just told that no one could get in here at this time"
player_name "Yeah I know. I could not get in and a professor let me in"
"Maid" "Okay dear do what you have to do. I do not want to disturb you"
player_name "Its okay. Thanks!"
#elevator picture form outside without any equations
"Narrator" "After some time she realizes that an elavator works with ID card, which will not work now"
player_name "What do I do now?"
menu:
           "ask a cleaning lady to let you go up with her ID card":
                jump ask_elevator_hard
           "Try to sneak in with emergency stairs":
                jump emergency_stairs_hard
label ask_elevator_hard:
$menu_flag=1
player_name "Excuse me miss I am sorry that I am bothering you, but would you please be so kind to let me on 8th floor with your ID?"
player_name "Mine would not work now"
"Maid" "Of course dear, but you will have to do one favor for me also"
player_name "Okay, how can I help you?"
"Maid" "My son studies here and he told me that he could not solve one equation. 
If you will solve it for me I will let you up, if not you will have to leave the building"
player_name "Sure, I will try my best to help your son. What is the equation?"
jump inside_elevator_hard
label emergency_stairs_hard:
scene bg stairs_closed
$menu_flag=0
player_name "I think this should work"
scene bg stairs_red
"Narrator" "You just tried to go up with emergency stairs. Alarm started, therefore everyone is released from the building"
jump game_lost_emergency_door_hard
label game_lost_emergency_door_hard:
scene bg campus
player_name "This was my only chance! How did I not think about alarm sound! UGHH, I will fail the exam tomorrow"
scene bg game_over
play sound "game_lost.wav"
"Narrator" "Game Over"
return
label inside_elevator_hard:    
scene bg elevator_hard_mode
"Assignment" "Derive this function to make the lady give you her ID card"
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=180.0)
$ ui.timer(180.0, ui.jumps("out_of_time"))
menu :
        "12x^4+21x^3+24x^2+56x+5":
            jump choice2_wrong_hard
        "12x^3+21x^2+24x+56":
            jump choice2_right_hard
        "12x^3-21x^2+24x+56":
            jump choice2_wrong_hard
        "12x^3+21x^2+24x+56+5":
            jump choice2_wrong_hard
        "12x^3+21x^2+24+56":
            jump choice2_wrong_hard
        "I need a hint here":
            jump hint2_hard
label hint2_hard:
    scene bg hint2_hard
    "Maid" "My son said that he tried to do it with these formulas, maybe you can try it out too."
    scene bg elevator_hard_mode
    show countdown at Position(xalign=.1, yalign=.9)
    image countdown = DynamicDisplayable(countdown, length=180.0)
    $ ui.timer(180.0, ui.jumps("out_of_time"))
    menu:
        "12x^4+21x^3+24x^2+56x+5":
            jump choice2_wrong_hard
        "12x^3+21x^2+24x+56":
            jump choice2_right_hard
        "12x^3-21x^2+24x+56":
            jump choice2_wrong_hard
        "12x^3+21x^2+24x+56+5":
            jump choice2_wrong_hard
        "12x^3+21x^2+24+56":
            jump choice2_wrong_hard

label choice2_wrong_hard:
$menu_flag=0
jump lost_game_ID_hard
label lost_game_ID_hard:
scene bg uni_inside
player_name "I tried, but I could not solve it sorry. So will you let me go up?"
"Maid" "I am so sorry dear, but things do not work this way, we had an agreement remember"
"Maid" "You will have to leave the building now"
player_name "Okay..."
play sound "game_lost.wav"
scene bg game_over
"Narrator" "Game Over"
return

label choice2_right_hard:
scene bg uni_inside
$menu_flag=1
"Maid" "Thank you so much dear, you are more then welcome to use my card now"
player_name "Thank you so much!"
jump game_continues1_hard

label game_continues1_hard:
#picture of office door without equation
"Narrator" "She went up on the 8th floor and saw class door"
player_name "Finally! I cannot believe that I got here! Only thing left to do is go in there and open the safe!"
"Narrator" "She tried to open the door several times, though she could not"
player_name "I should think of something right now!"
"Narrator" "After sometime she remembers that offices' security system is really well designed and even professors have to solve some random problems to get in there when door is locked."
player_name "Okay, I should be able to do it, but if I don't everything will go to waste."
"Narrator" "Deciding to solve office door problem, she risked expulsion from university. If she did not do it correctly the alarm would start in whole university"
scene bg office_door
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=90.0)
$ ui.timer(90.0, ui.jumps("out_of_time"))
menu :
      "0":
         jump choice3_wrong_hard
      "21":
         jump choice3_wrong_hard
      "23":
         jump choice3_right_hard
      "22":
         jump choice3_wrong_hard
      "13":
         jump choice3_wrong_hard

label choice3_wrong_hard:
$menu_flag=0
jump lost_game_hard

label choice3_right_hard:
$menu_flag=1
jump game_continues2_hard

label game_continues2_hard:
scene bg proffessor_sleeping
player_name "OMG!!! What is he still doing here??? What am I gonna do now???"

menu :
       "Run you idiot run!!!":
            jump choice4_wrong_hard

       "Stay in the room and take the risk":
            jump choice4_right_hard

       "I don't know what to do":
            jump choice4_no_hard

label choice4_no_hard:
$menu_flag=2
"Narrator" "You've come this far already- don't give up now! Decide what you need to do before the professor wakes up!"
jump figure_out_what_to_do_hard

label choice4_wrong_hard:
$menu_flag=0
jump lost_game_run_hard

label choice4_right_hard:
$menu_flag=1
jump game_continues3_hard

label lost_game_run_hard:
scene bg game_over
"Narrator" "If you started something then finish it!"
play sound "game_lost.wav"
return
label figure_out_what_to_do_hard:
menu:
            "Stealing a test is crazy! I should not have come here":
               jump lost_game_run_hard
            "I'm gonna steal the test and rock the exam!!!":
               jump game_continues3_hard

label game_continues3_hard:
player_name "I cannot believe that I am here! Though, how do I open the safe if I do not know the code?"

menu :
                "Take out a gun and make the professor tell you the code":
                     jump choice5_wrong_hard
                "Try it yourself":
                     jump choice5_right_hard

label choice5_wrong_hard:
$menu_flag=0
jump lost_game1_hard

label lost_game1_hard:
player_name "Wake up and tell me the code of your safe right now!!!"
scene bg proffessor_beginning
"Professor" "What are you doing and why are you pointing a gun at me??"
scene bg gun
player_name "Because I have to steal your tests you idiot. I do not know anything about the exam tomorrow"
"Professor" "That test is not that important- you would kill me if I didn't give you the passcode for the safe??"
player_name "*Looks away and thinks about it for a minute*"
"Professor" "*Runs*"
jump lost_game_gun_hard


label lost_game_gun_hard:
scene bg director_office
"Narrator" "Professor went in director's office and told him the whole story, which resulted in this..."
"Director" "You have violated almost everything in the school's policy. I am really disappointed that we did not see the real you when we were admitting you. I have never encountered a problem like this before!"
"Director" "You are expelled from our University!"
scene bg game_hard
"Narrator" "GAME OVER"
play sound "game_lost.wav"
scene bg game_over_moral_lost
"Narrator" "Remember this!!"
return
label choice5_right_hard:
$menu_flag=1
"Assignment" "If you want to open the safe by your own go ahead, but that means that you should think of the code too"
jump game_continues4_hard

label game_continues4_hard:
player_name "What should I do right now?? From where the hell should I know the safe code?!"

menu:
            "Call a friend and ask her for help":
                 jump choice6_wrong_hard
            "NO! I said I will solve it myself!!!":
                 jump choice6_right_hard
            "Not sure what to do - I am getting out of here!":
                 jump lost_game_run_hard

label choice6_wrong_hard:
$menu_flag=0
jump lost_game_call_hard
label lost_game_call_hard:
#I should have picture of Anna here
player_name "Hey Anna, I know that I am calling you really late, but I have to tell you something and you cannot tell anyone else"
"Anna" "Are you okay?? What happened?"
player_name "Just swear that you are not going to tell anyone!!"
"Anna" "Okay, okay I swear!!"
player_name "So, you know about the test we are having tomorrow in math?"
"Anna" "Yes, why?"
player_name "So, I am trying to steal it and its in a safe and you have to help me unlock it"
"Anna" "Okay, that means that you are not okay! I am not going to help you do that!! Sorry bye!!"
player_name "At least promise you won't tell anyone that I called you okay?"
"Anna" "Okay, no problem!"
"Anna" "*thinks* Nah! I am calling the director"
"Anna" "*Rings*"
"Director" "Hello?"
"Anna" "Hi, its Anna. I am so sorry that I am calling this late, but someone is trying to steal a math exam and I thought it was important for me to tell someone"
"Director" "Are you sure? Because the math department is locked right now."
"Anna" "I am pretty sure. That's all I can tell you. Bye"
"Director" "Okay, thanks for calling. Bye"
jump lost_game_hard
label choice6_right_hard:
scene bg safe_hard
"Assigment" "Now you have to find critical points of the function round the number which won't be integers and consider negative answers as positive (ex. -2 1.5 2 -> 2 2 2)"
show countdown at Position(xalign=.1, yalign=.9)
image countdown = DynamicDisplayable(countdown, length=180.0)
$ ui.timer(180.0, ui.jumps("out_of_time"))
menu :
             "Password is: 012":
                  jump choice7_wrong_hard
             "Password is: 015":
                  jump choice7_right_hard
             "Password is: 014":
                  jump choice7_wrong_hard
             "Password is: 024":
                  jump choice7_wrong_hard
             "Password is: 034":
                  jump choice7_wrong_hard
             "Password is: 013":
                  jump choice7_wrong_hard
             "I really need a hint here!!!":
                  jump hint3_hard
label hint3_hard:
    scene bg hint3_hard
    "Assignment" "This is the last step. Try using this equality, but figure out what the answers by yourself"
    scene bg safe_hard
    show countdown at Position(xalign=.1, yalign=.9)
    image countdown = DynamicDisplayable(countdown, length=180.0)
    $ ui.timer(180.0, ui.jumps("out_of_time"))
menu :
             "Password is: 012":
                    jump choice7_wrong_hard
             "Password is: 015":
                    jump choice7_right_hard
             "Password is: 014":
                    jump choice7_wrong_hard
             "Password is: 024":
                    jump choice7_wrong_hard
             "Password is: 034":
                    jump choice7_wrong_hard
             "Password is: 013":
                    jump choice7_wrong_hard


label choice7_wrong_hard:
$menu_flag=0
jump lost_game_hard

label choice7_right_hard:
scene bg proffessor_beginning
"Professor" "So, many of the people did not get good grades on this exam, but one student recieved a 100."
"Professor" "Apparanetly you studied hard- when you do that your work speaks for itself!"
player_name "Thanks professor! You cannot even imagine what I went through yesterday to get this grade"
"Professor" "Believe me- I've heard stories like this 1000 times"
player_name "I bet not (thinks to herself)"
scene bg won
play sound "game_won.mp3"
"Narrator" "Congratulations!!!"
scene bg end
"Narrator" "Remember!"
return


