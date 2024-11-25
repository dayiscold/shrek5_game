# Определение персонажей
define a = Character("Андрей")
define s = Character("Сергей")
define b = Character("Босс")

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
image sms = im.Scale("characters/арендодатель.jpg", 600, 400)
image andrey = "characters/andrey.png"
image sergey = im.Scale("characters/sergey.png", 896, 1000)
image boss = "characters/boss.png"
image bg_online_call_with_boss = im.Scale("backgrounds/call_with_boss.jpg", 1920, 1080)




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
    a "{i}*про себя*{/i}\n
    Утро не бывает добрым..."
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
    pause 1.5
    scene bg_workplace_main_office with fade
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
    scene bg_online_call_with_boss with fade
    "Сергей и Андрей должны созвонится с боссом для получения задания, но задание, которое должен был получить Сергей отдают Андрею, а Сергею поручают другое дело."
    show sergey at left
    show andrey at center
    show boss at right
    b "Здравствуйте, коллеги. Сегодня у Андрея первый рабочий день."
    b "Андрей, как тебе обстановка?"
    a "{i}*неуверенно отвечает*{/i}\n
    Обстановка хорошая, мне все нравится."
    b "Отлично, тогда давайте начнем обсуждение."
    s "Босс, я сегодня планирую сходить по вашему поручению, а Андрея оставить в офисе"
    b "Нет, сегодня приезжают наши партнёры, ты должен будешь с ними встретиться. Вместо тебя пойдет Андрей"
    s "{i}*раздраженно*{/i}\n
    Но у него сегодня первый рабочий день! Лучше не доверять ему такое серьезное дело."
    b "{i}*Строго*{/i}\n
    Там всего лишь надо вставить флэшку, а вести переговоры с партнерами он не сможет. Не обсуждается! Сергей, введи Андрея в курс дела."
    s "На листе все подробно описано, дело легкое, разберёшься."