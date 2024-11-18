# Определение персонажей
define a = Character("Андрей")
define s = Character("Сергей")
# Загрузка фонов и изображений
image bg go_work = "backgrounds/go_work.png"
image bg apartment = im.Scale("backgrounds/andrey_apartment.jpeg", 1920, 1080)
image andrey = "characters/andrey.png"
image sergey = im.Scale("characters/sergey.png", 896, 1000)
image sms = im.Scale("characters/арендодатель.jpg", 600, 400)
image bg coffee = "backgrounds/coffee.png"
image bg main_office = im.Scale("backgrounds/main_office.jpeg", 1920, 1080)
image bg workplace_main_office = im.Scale("backgrounds/workplace_main_office.jpg", 1920, 1080)
image bg sergey_and_andrey_office = im.Scale("backgrounds/andrey_and_sergey_going to_office.jpeg", 1920, 1080)
image bg workplace_andrey = im.Scale("backgrounds/workplace_andrey.jpeg", 1920, 1080)
image bg andrey_and_pc = im.Scale("backgrounds/andrey_and_pc.jpeg", 1920, 1080)
image bg laptop_cyberattack = im.Scale("backgrounds/laptop_cyberattack.jpeg", 1920, 1080)


# Сцена 1: Начало пути...
label start:
    scene bg apartment
    
    # Звук будильника
    play sound "будильник.mp3"
    "Утро началось с пронзительного звука будильника, заполняющего маленькую комнату сталинки."
    "Андрей протянул руку к телефону, чтобы выключить раздражающий звонок."
    "На экране замигала иконка нового сообщения."
    # Показываем текст СМС от арендодателя
    window hide
    show sms
    pause 7
    hide sms 
    window show
    # Андрей реагирует на СМС
    show andrey
    a "*про себя* Утро добрым не бывает…"
    a "Надеюсь, сегодня первый рабочий день пройдёт без потрясений."

    # Выбор игрока
    menu:
        "Пойти попить кофе":
            a "Ладно, начну день с кофе, хоть немного взбодрюсь."
            scene coffee with fade
            "Андрей выпил кофе, но замечает, что уже опаздывает, смотря на часы."
            jump work_scene

        "Пойти сразу на работу":
            a "Лучше сразу отправлюсь на работу, и так много долгов."
            scene go_work with fade
            "Андрей отправился на работу."
            jump work_scene

#Сцена 2: Первый день на работе

label work_scene:
    window hide
    scene bg main_office with fade
    pause 1.5
    scene bg workplace_main_office with fade
    window show
    "Андрей приходит в офис, где его встречает Сергей, который старается держаться спокойно, но в его поведении заметна нервозность."
    show sergey
    s "Андрей, здравствуй. Рад что ты решил у нас поработать. Пошли за мной я покажу тебе офис."
    hide sergey
    scene bg sergey_and_andrey_office with fade
    "Сергей ведет по офису Андрея к его рабочему месту."
    scene bg workplace_andrey with fade
    show sergey
    s "Здесь наше с тобой рабочее место, можешь начать осваивается."
    hide sergey
    scene bg andrey_and_pc with fade
    "Андрей садится за компьютер осмотрительно. Сергей оставил его одного." 
    "Когда Андрей садился за свой рабочий стол, он вглядывался в мониторы, напоминая себе, что пентестер — это не просто охотник за уязвимостями. 
    Это тот, кто мыслит как хакер, чтобы защитить систему."
    scene bg laptop_cyberattack with fade
    "«Тестируй так, будто хочешь разрушить, но защищай, как будто жизнь компании зависит от тебя», — вспоминал он слова одного из преподавателей на курсе."
    "В комнате витала тишина, нарушаемая лишь шумом систем охлаждения. Андрей открыл ноутбук и приступил к настройке тестового окружения."
    "Ему предстояло изучить инструменты и освоить платформу, которую компания использовала для симуляции кибератак."
    "Легкое волнение смешивалось с предвкушением."
    

    
