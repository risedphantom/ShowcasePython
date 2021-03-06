from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'
    friend_ans = [
        'Спасибо, что снова зашли!',
        'Смотрите сколько угодно.',
        'Рад вас видеть.',
        'Добро пожаловать!'
    ]
    enemy_ans = [
        'Уходите, вы никому не нравитесь.',
        'Неудачного вам дня.',
        'И зачем вы пришли?',
        'Я не в восторге от вас.'
    ]
    anon_ans = [
        'Не очень то и хотелось.',
        'Вы уже уходите?',
        'Не тратьте свое время.',
        'Нажмите Alt+F4.'
    ]
    soon_ans = [
        'Жду встречи.',
        'Так когда встретимся?',
        'Скоро увидимся.',
        'Мы уже назначили встречу?'
    ]