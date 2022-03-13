define Te = Character("Романченко Єлизавета Євгеніївна")
define Uka = Character("Юка")
define Hi = Character("Хина")
define Mi = Character("Микола")      # TODO: add colors


label start:

    scene bg outide

    $ Mi_rel = 5
    $ Uka_rel = 5
    $ Sus = 0

    "Весенний солнечный день, за окном дует нежный ветерок, падают лепестки
    сала и все вокруг говорит о том, что этот день будет прекрасным."

    python:
        name = renpy.input("Как тебя зовут?")
        while (not name):
            name = renpy.input("Как тебя зовут?")

    scene bg classroom

    show Mikola_happy

    Mi "Здарова, [name]! Прекрасная сегодня погодка, не правда ли?"

    menu:
        "Опять свалить хочешь?":
            jump d1
        "Да":
            jump d2
        "...":
            jump d3

label d1:

    Mi "Нуу..."

    show Mikola_nod

    show Mikola_look_around

    Mi "Конечно нет, о чем ты... не ори так, ну че идешь?"

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
    "сценарий 3.???" #TODO
    return

label d1_15:
    "сценарий 1.15" #продолжение
    return

    return
