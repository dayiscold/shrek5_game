# Определение персонажей
define a = Character("Андрей")
define s = Character("Сергей")
define b = Character("Босс")
define g = Character("Призраки")

# Загрузка фонов и изображений
image bg_apartment = im.Scale("backgrounds/andrey_apartment.jpeg", 1920, 1080)
image bg_coffee = "backgrounds/coffee.png"
image bg_go_work = "backgrounds/go_work.png"
image bg_main_office = im.Scale("backgrounds/main_office.jpeg", 1920, 1080)
image bg_workplace_main_office = im.Scale("backgrounds/workplace_main_office.jpg", 1920, 1080)
image bg_sergey_and_andrey_office = im.Scale("backgrounds/andrey_and_sergey_going to_office.jpeg", 1920, 1080)
image bg_workplace_andrey = im.Scale("backgrounds/workplace_andrey.jpeg", 1920, 1080)
image bg_andrey_and_pc = im.Scale("backgrounds/andrey_and_pc.jpeg", 1920, 1080)
image bg_laptop_cyberattack = im.Scale("backgrounds/laptop_cyberattack.jpeg", 1920, 1080)
image sms = im.Scale("characters/give_me_rent.png", 600, 400)
image andrey = "characters/andrey.png"
image sergey = im.Scale("characters/sergey.png", 896, 1000)
image angry_sergey = im.Scale("characters/angry_sergey.png", 896, 1000)
image boss = "characters/boss.png"
image bg_online_call_with_boss = im.Scale("backgrounds/call_with_boss.jpg", 1920, 1080)
image bg_andrey_leave_office = im.Scale("backgrounds/andrey_leave_office.png", 1920, 1080)
image bg_andrey_leave_office_flash = im.Scale("backgrounds/andrey_leave_office_2.png", 1920, 1080)
image bg_andrey_datacentre = im.Scale("backgrounds/andrey_datacentre.png", 1920, 1080)
image bg_andrey_servers = im.Scale("backgrounds/andrey_servers.png", 1920, 1080)
image bg_servers = im.Scale("backgrounds/servers.jpg", 1920, 1080)
image old_technica = im.Scale("backgrounds/old_technica.jpg", 1920, 1080)
image andrey_flash = "characters/andrey_flash.png"
image bg_andrey_flash_to_server = im.Scale("backgrounds/andrey_flash_to_server.png", 1920, 1080)
image bg_andrey_walks_data = im.Scale("backgrounds/andrey_walks_data.png", 1920, 1080)
image bg_flash_error = im.Scale("backgrounds/flash_error.png", 1920, 1080)
image bg_andrey_checks_pc = im.Scale("backgrounds/andrey_checks_pc.png", 1920, 1080)
image bg_terminal_pc = im.Scale("backgrounds/terminal.jpg", 1920, 1080)
image bg_andrey_terminal = im.Scale("backgrounds/andrey_terminal.jpg", 1920, 1080)
image sozvon = im.Scale("backgrounds/sozvon.png", 1920, 1080)
image hello_ghosts = im.Scale("backgrounds/hello_ghosts.png", 1920, 1080)
image bg_andrey_ghosts = im.Scale("backgrounds/andrey_ghosts.png", 1920, 1080)
image bg_servers_red = im.Scale("backgrounds/servers_red.png", 1920, 1080)
image ghost = "characters/ghost.png"
image bg_andrey_running = im.Scale("backgrounds/andrey_running.png", 1920, 1080)
image bg_andrey_chill_guy = im.Scale("backgrounds/andrey_chill_guy.png", 1920, 1080)

screen game_hint():
    frame:
        align (0.5, 0.95)
        text "Пропустить с помощью ЛКМ" style "default"


screen block_hint:
    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        background "#000000AA"  # Полупрозрачный фон
        text "Сцену нельзя пропустить." style "block_hint_text"




# Сцена 1: Начало пути…
label start:
    scene bg_apartment with fade

    # Звук будильника
    play sound "budilnik.mp3"
    "Утро началось с пронзительного звука будильника, заполняющего маленькую комнату сталинки."
    "Андрей протянул руку к телефону, чтобы выключить раздражающий звонок."
    "На экране замигала иконка нового сообщения."

    # Показываем СМС
    window hide
    show sms
    pause 7
    hide sms
    window show

    # Реплика Андрея
    show andrey at center
    a "Утро не бывает добрым..."
    a "Надеюсь, сегодня первый рабочий день пройдёт без потрясений."

    # Выбор игрока
    menu:
        "Пойти попить кофе":
            a "Ладно, начну день с кофе, хоть немного взбодрюсь."
            scene bg_coffee with fade
            "Андрей выпил кофе, но замечает, что уже опаздывает, смотря на часы."
            jump work_scene

        "Пойти сразу на работу":
            a "Лучше сразу отправлюсь на работу, и так много долгов."
            scene bg_go_work with fade
            "Андрей отправился на работу."
            jump work_scene


# Сцена 2: Первый день на работе 
label work_scene:
    # Переход в офис
    window hide
    scene bg_main_office with fade
    show screen game_hint
    pause 3
    scene bg_workplace_main_office with fade
    hide screen game_hint
    window show

    # Встреча с Сергеем
    show andrey at left
    show sergey at right
    "Андрей приходит в офис, где его встречает Сергей, который старается держаться спокойно, но в его поведении заметна нервозность."
    s "Андрей, здравствуй. Рад, что ты решил у нас поработать. Пошли за мной, я покажу тебе офис."
    hide sergey
    hide andrey

    # Прогулка по офису
    scene bg_sergey_and_andrey_office with fade
    "Сергей ведёт по офису Андрея к его рабочему месту."

    # У рабочего места
    scene bg_workplace_andrey with fade
    show sergey at right
    show andrey at left
    s "Здесь наше с тобой рабочее место. Можешь начать осваиваться."
    hide sergey
    hide andrey
    # Работа Андрея
    scene bg_andrey_and_pc with fade
    "Андрей садится за компьютер осмотрительно. Сергей оставил его одного."
    "Когда Андрей садился за свой рабочий стол, он вспоминал, что пентестер — это не просто охотник за уязвимостями. Это тот, кто мыслит как хакер, чтобы защитить систему."
    # Начало работы
    scene bg_laptop_cyberattack with fade
    "«Тестируй так, будто хочешь разрушить, но защищай, как будто жизнь компании зависит от тебя», — вспоминал он слова одного из преподавателей на курсе."
    "В комнате витала тишина, нарушаемая лишь шумом систем охлаждения. Андрей открыл ноутбук и приступил к настройке тестового окружения."
    "Ему предстояло изучить инструменты и освоить платформу, которую компания использовала для симуляции кибератак."
    "Легкое волнение смешивалось с предвкушением."

# Сцена 3: Завязка
label the_intrigue:
    scene sozvon with fade
    "Сергей и Андрей должны созвонится с боссом для получения задания, но задание, которое должен был получить Сергей отдают Андрею, а Сергею поручают другое дело."
    window hide
    menu:
        "Зайти в голосовой чат":
            window show
            b "Здравствуйте, коллеги. Сегодня у Андрея первый рабочий день."
            b "Андрей, как тебе обстановка?"
            "Андрей почувствовал себя неуверенно"
            a "Обстановка хорошая, мне все нравится."
            b "Отлично, тогда давайте начнем обсуждение."
            s "Босс, я сегодня планирую сходить по вашему поручению, а Андрея оставить в офисе"
            b "Нет, сегодня приезжают наши партнёры, ты должен будешь с ними встретиться. Вместо тебя пойдет Андрей"
            "Сергей стал еще более раздражен"
            s "Но у него сегодня первый рабочий день! Лучше не доверять ему такое серьезное дело."
            b "Там всего лишь надо вставить флэшку, а вести переговоры с партнерами он не сможет. Не обсуждается! Сергей, введи Андрея в курс дела."
            s "На листе все подробно описано, дело легкое, разберёшься."
            jump first_task

# Сцена 4: Первое задание
label first_task:
    scene bg_andrey_leave_office_flash with fade
    "Андрей выходит из офиса с флешкой, листком, переданным Сергеем, и краткими, но настороженными наставлениями."
    scene bg_andrey_leave_office with fade
    "Он чувствует неуверенность, ведь ответственность в первый же день оказывается выше, чем он ожидал."
    scene bg_main_office with fade
    show andrey at center:
        zoom 0.7
    a "Ну и начало... Ещё вчера я мечтал, чтобы всё прошло гладко, а сегодня уже бегаю с флешкой. Ладно, справлюсь."

# Сцена 5: Дата-центр
label data_centre:
    scene bg_andrey_datacentre with fade
    "Следуя инструкциям Сергея, Андрей добирается до заброшенного здания, которое раньше было дата-центром компании."
    window hide
    scene old_technica with fade
    show screen game_hint
    pause 2.5 
    hide screen game_hint
    scene bg_andrey_servers with fade
    window show
    "Внутри царит полумрак, обстановка мрачная, по помещению разбросана старая техника."
    scene bg_servers with fade
    show andrey_flash at center
    a "Что ж..."
    window hide
    menu:
        "Продолжить осмотр помещения перед работой.":
            scene andrey_walks_data with fade
            "Андрей осторожно идёт между рядами серверов, слыша отдалённые скрипы и стуки."
            play sound "walks_in_center.mp3"
            window hide
            show screen block_hint 
            show andrey_walks_data at Transform(zoom=1.1) with fade
            $ renpy.pause(5.5, hard=True)
            pause 0.7
            play sound "skrip.mp3"
            show andrey_walks_data at Transform(zoom=1.2) with fade
            pause 2
            hide screen block_hint
            jump flash_to_server
        "Сразу вставить флэшку в основной сервер.":
            jump flash_to_server

label flash_to_server:
    scene bg_andrey_flash_to_server with fade
    a "Поехали… Надеюсь, это того стоит."
    "Андрей подходит к серверу, находит подходящий порт и подключает флешку."


#Сцена 6: Активация вируса
label activation_virus:
    window show
    scene bg_flash_error with fade
    "После того как Андрей вставляет флешку, на экране компьютера появляется предупреждающее сообщение: «Ошибка доступа. Подключение к сети недоступно»."
    scene andrey_checks_pc with fade
    "Андрей пытается разобраться с ошибкой, проверяя кабели и настройки, но его попытки ни к чему не приводят."
    scene bg_terminal_pc with fade
    "Внезапно терминал начинает заполняться странными строками кода."
    scene andrey_terminal with fade 
    "Андрей нервно глотнул, увидев строки кода, хаотично заполняющие экран."
    "Они менялись слишком быстро, словно система сама ожила и начала действовать наперекор всем правилам."
    "Его руки слегка дрожали, когда он попытался закрыть окна с предупреждениями."
    scene hello_ghosts with fade
    "И тут он заметил первое движение в помещении. В тени серверных стоек мелькнуло что-то еле уловимое. Андрей замер, сердце забилось быстрее."
    "Тонкая грань между логикой и паникой начала рушиться, когда тени обрели формы — призраки сотрудников прошлого."
    scene bg_andrey_ghosts with fade
    "На экране компьютера предупреждения сменились хаотичными красными символами, отражающимися на лице Андрея."
    "Призраки начали обступать его, их полупрозрачные фигуры зловеще следили за каждым его движением."
    scene bg_servers_red with fade
    show ghost at right
    show andrey at left
    g "Ты такой же, как и мы… Тебя тоже обманули…"
    a "Что?! Кто вы?"
    g "Мы — жертвы этой компании. Оставь флешку и уходи, пока можешь. Иначе ты станешь следующим…"
    hide ghost
    hide andrey
    window hide
    menu:
        "Попытаться выйти из здания.":
            scene andrey_running with fade
            window show
            "Андрей быстро направляется к выходу, но дверь оказывается заперта."
            "Он судорожно тянет за ручку, но та не двигается. За спиной слышатся тихие шепоты призраков, которые кажутся всё ближе."
            jump sinister_twist
        "Продолжить попытки работать с сервером, игнорируя призраков.":
            scene bg_andrey_chill_guy with fade
            window show
            "Андрей сосредоточенно работает за компьютером, пытаясь закрыть предупреждающие окна, но коды продолжают появляться, а тени, как будто сговорившись, начинают двигаться вокруг него, сжимая пространство."
            jump sinister_twist

#Сцена 7: Зловещий поворот
label sinister_twist:
    pass
