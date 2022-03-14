define Te = Character("Романченко Єлизавета Євгеніївна", who_color = "#FF00FF", what_color = "#D8BFD8")
define Uka = Character("Юка", who_color = "#1E90FF", what_color = "#7B68EE")
define Hi = Character("Хина", who_color = "#9ACD32", what_color = "#98FB98")
define Mi = Character("Микола", who_color = "#F4A460", what_color = "#FFDEAD")
define narrator = Character(what_color = "#FFE4E1")
define H = Character("[name]", what_color = "#AFEEEE")


define slowestdissolve = Dissolve(2)

transform rightest:
    xalign 1.1
    yalign 1.0

transform nearright:
    xalign 0.8
    yalign 1.0

label start:

    scene bg outside day

    $ Mi_rel = 5
    $ Uka_rel = 5
    $ Sus = 0

    "{i}{size=+5}Весенний солнечный день, на улице дует нежный ветерок, падают лепестки
    сала и все вокруг говорит о том, что этот день будет прекрасным.{/size}{/i}"

    python:
        name = renpy.input("{i}{color=#FFE4E1}Как тебя зовут?{/color}{/i}")
        while (not name):
            name = renpy.input("Как тебя зовут?")

    H "\"Вот бы запалить сегодня чьи-нибудь трусы...\""

    scene bg classroom day

    show mikola happy

    Mi "Здарова, [name]! Прекрасная сегодня погодка, не правда ли?"

    menu:
        "Опять свалить хочешь?":
            jump d1
        "Да":
            jump d2
        "Qiuq exit":
            jump d3

label d1:

    Mi "Нуу..."

    #show mikola nod - not working

    show mikola look around

    Mi "Конечно нет, о чем ты... не ори так, ну че, идешь?"

    jump d111

label d111:

    menu:
        "Не слишком мы в последнее время пропускаем, как твои родители случайно
        не миллионеры, может завяжем уже?":
            $ Mi_rel -= 3
            show Mikola_angry
            jump d1_15

        "Не, я не собираюсь на 1 урок в месяц ходить":
            $ Mi_rel -= 2
            jump d1_15

        "*Молча кивнуть*":
            $ Mi_rel += 1
            Mi "Тогда валим скорее, меня тошнит от местного зоопарка"
            jump d1_15

label d2:

    Mi "Ха-ха, жалко такие деньки проводить в тесной бетонной коробке,
    понимаешь намек?"

    menu:
        "Да":
            jump d222

        "Нет":
            Mi "Ну я имею ввиду, очень уж сейчас хочется развеяться…
            ПОНИМАЕШЬ?"
            $ Mi_rel -= 1
            menu:
                "Да":
                    jump d222
                "Нет":
                    Mi "..."
                    "..."
                    Mi "... Ты конченый?"
                    $ Mi_rel -= 2
                    jump fucknumbers

label d222:
    Mi "Ну, что думаешь? Пойдем?"
    jump d111

label fucknumbers:
    menu:
        "Да шучу я успокойся":
            jump d222
        "Нет":
            $ Mi_rel -= 1
            jump d1_15
        "Да пошел ты!":
            $ Mi_rel = 0
            jump d3

label d3:
    return

label d1_15:
    show yuka angry small at nearright

    Uka "Боже, опять эти двое страдают фигней. Вы хоть слышали,
    что на этом уроке будет контрольная по математике?"

    show mikola surprised

    Mi "Что?! Впервые слышу!"

    Uka "Тсц, а вот ходили бы вы на уроки, знали бы об этом заранее!
    И даже не думайте о побеге, я все доложу мисс Такахаси."

    show hina frown small at rightest

    Hi "Будет тебе Юка, [name] не заслуживает такой строгости..."

    show hina blush small at rightest

    Hi "всмысле c ними обоими, мы же одноклассники и
    должны помогать друг другу!"

    show hina frown small at rightest

    Mi "Забей на эту дурочку, валим отсюда пока не поздно"

    menu:
        "Пойти":
            jump go
        "Остаться":
            jump notgo

label go:
    scene bg hall
    play sound "run.mp3"
    scene bg hall
    with slowestdissolve
    stop sound
    show teacher
    Te "И куда вы бежите? Урок уже скоро начнется."
    menu:
        "Да так просто гуляем":
            Te "Вот как..."
            $ Sus += 3
        "...":
            $ Sus += 2
    play sound "bell.mp3"
    Te "Ну ладно, пройдемте в класс"
    jump notgo

label notgo:
    return



    return
