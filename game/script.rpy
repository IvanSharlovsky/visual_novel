# Declare characters used by this game.
define Te = Character("Такахаси Елизавета Евгеньевна", who_color = "#fa2bfafe", what_color = "#f079f0")
define Uka = Character("Юка", who_color = "#2791fb", what_color = "#65b0f5")
define Hi = Character("Хина", who_color = "#bbf449", what_color = "#8bdb8b")
define K = Character("Коля", who_color = "#F4A460", what_color = "#FFDEAD")
define narrator = Character(what_color = "#f4eeed")
define H = Character("[name]", what_color = "#AFEEEE")
define Inc = Character("???", who_color = "#4b3030", what_color = "#725858")
define SB = Character("Незнакомая ученица", who_color = "#FFFFFF", what_color = "#FFFFFF")

# Some defines
define slowestdissolve = Dissolve(2)

transform rightest:
    xalign 1.1
    yalign 1.0

transform nearright:
    xalign 0.8
    yalign 1.0

# The game starts here.
label start:

    $ K_rel = 5
    $ Uka_rel = 5
    $ Sus = 0

    python:

        import random
        mood = random.randint(0,1)

    if mood:

        scene bg school outside cloud
        with fade

        "{i}Сегодня ты снова пришел в школу. Снова. Ты занимаешься этим каждое утро.
        Как и сотни других людей.{/i}"

        "{i}Вы повторяете это ритуал ежедневно, лишь чтобы добавить несколько оттеноков
        в этот один бесконечный серый поток рутины.{/i}"

        Inc "\"Изо дня в день... Происходит одно и тоже...\""

        Inc "\"Сплошная скука... Изо дня в день...\""

        Inc "\"Этот мир...\""

        Inc "\"Гниет на глазах...\""

        "{i}Однако, погода решила удивить.{/i}"

        scene bg school outside day

        play music "illurock.opus"

        "{i}Выглянуло весеннее солнцо, на улице задул нежный ветерок, полетели лепестки
        сакуры и появилась небольшая надежда на то, что этот день чем-то удивит и дальше.{/i}"

    else:

        # Start by playing some music.
        play music "illurock.opus"

        scene bg school outside day
        with fade

        "{i}Весенний солнечный день, на улице дует нежный ветерок, падают лепестки
        сакуры и все вокруг говорит о том, что этот день будет прекрасным.{/i}"

    scene bg school hall day
    with fade

    "{i}Чей-то женский голос окрикнул тебя.{/i}"

    SB "Привет, ... "

    python:

        name = renpy.input("{i}{color=#FFE4E1}Как тебя зовут?{/color}{/i}")
        while (not name):
            name = renpy.input("Как тебя зовут?")

    SB "Привет, Миха, как дела? Ты сделал то задание... "

    H "\"Вот Я дурак, у меня же нет друзей среди девочек.\""

    scene bg school classroom day
    with fade

    "{i}Первый урок закончился и пока все шло как обычно.{/i}"

    #TODO поменять имя картинки
    show mikola happy

    K "Здарова, [name]! Прекрасная сегодня погодка, не правда ли?"

    "Коля - двоечник-одноклассник. О нем ходит много разных слухов.
    Но ты с ним в хороших отношениях."

    menu:

        "Неужели снова свалить хочешь?":
            jump want_go_away

        "Ага, нечасто такая бывает.":
            jump good_weather

        "Qiuq exit":
            jump exit

########################################################################################################

label want_go_away:

    K "Нуу..."

    #show mikola nod - not working
    #TODO animation without text

    show mikola look around

    K "Конечно нет, о чем ты... не ори так, ну че, идешь?"

    jump answer_go_away

########################################################################################################

label good_weather:

    K "Ха-ха, жалко такие деньки проводить в тесной бетонной коробке,
    понимаешь намек?"

    menu:

        "Еще бы! У тебя только одно на уме":
            jump girls_appearance

        "Кажется, не очень":
            Mi "Ну я имею ввиду, очень уж сейчас хочется развеяться…
            ПОНИМАЕШЬ?"

            $ Mi_rel -= 1

            menu:

                "Да понял, понял":
                    jump question_go_away

                "Окно открыть предлагаешь?":
                    Mi "..."

                    H "..."

                    Mi "... Ты конченый?"

                    $ Mi_rel -= 2

                    jump joke

########################################################################################################

label question_go_away:

    K "Ну, что думаешь? Пойдем?"

    jump answer_go_away

########################################################################################################

label answer_go_away:

    menu:

        "Не, слишком мы в последнее время пропускаем, может завяжем уже?":
            $ Mi_rel -= 3

            show mikola angry

            jump girls_appearance

        "Не, я не собираюсь на 1 урок в месяц ходить":
            $ Mi_rel -= 2

            jump girls_appearance

        "*Молча кивнуть*":
            $ Mi_rel += 1

            Mi "Тогда валим скорее, меня тошнит от местного зоопарка"

            jump girls_appearance

########################################################################################################

label joke:

    menu:

        "Да шучу я успокойся":
            jump d222

        "Нет":
            $ Mi_rel -= 1

            jump girls_appearance

        "Да пошел ты!":
            $ Mi_rel = 0

            jump exit

########################################################################################################

label girls_appearance:

    show yuka angry at nearright

    Uka "Боже, опять эти двое страдают фигней. Вы хоть слышали,
    что на этом уроке будет контрольная по математике?"

    "Юка - строгая староста. Ответственная, всегда следит за порядком."

    show mikola surprised

    K "Что?! Впервые слышу!"

    Uka "Тсц, а вот ходили бы вы на уроки, знали бы об этом заранее!
    И даже не думайте о побеге, я все доложу мисс Такахаси."

    show hina frown at rightest

    Hi "Будет тебе Юка, [name] не заслуживает такой строгости..."

    "Хина - застенчивая девочка. Часто пялится на тебя без
    какой-либо причины."

    show hina frown blush at rightest

    Hi "Всмысле они оба, мы же одноклассники и
    должны помогать друг другу!"

    show hina frown at rightest

    K "Забей на эту дурочку, валим отсюда пока не поздно"

    menu:

        "Пойти":
            jump go

        "Остаться":
            jump notgo

########################################################################################################

label go:

    play sound "run.mp3"

    scene bg school corridor day
    with slowestdissolve

    stop sound

    show teacher

    Te "И куда вы бежите? Урок уже скоро начнется."

    menu:

        "Да так, просто гуляем":
            Te "Вот как..."

            $ Sus += 3

        "...":

            $ Sus += 2

    play sound "bell.mp3"

    Te "Урок начинается, идите в класс"

    jump notgo_after_bell

########################################################################################################

label notgo:

    play sound "bell.mp3"

    jump notgo_after_bell

########################################################################################################

label notgo_after_bell:

    show bg school classroom desks
    #???
    #show mikola back
    #show hina back
    #show yuka back
    #TODO: add images and positioning

    "..."

    return

########################################################################################################

label exit:

    return
