import uuid


class Player(object):
    """ Игрок """
    def __init__(self, name, player_id, chat_id):
        self.name = name
        self.role = 0
        self.player_id = player_id
        self.chat_id = chat_id
        self.master = 0
        self.status = 0

    # Назначить роль игрока
    def set_role(self, role):
        self.role = role

    # Получить роль игрока
    def get_role(self):
        return self.role

    # Получить имя игрока
    def get_name(self):
        return self.name

    # Получить id игрока
    def get_id(self):
        return  self.player_id

    # Получить chat_id
    def get_chat_id(self):
        return self.chat_id

    # Назначить статус
    def set_status(self, status):
        self.status = status


class Room(object):
    """Комната игроков"""
    def __init__(self, room_name):
        self.room_id = uuid.uuid4()
        self.room_name = room_name
        self.room_status = 0
        self.players = []

    # Добавить игрока в комнату
    def set_player(self, player):
        self.players.append(player)

    # Получить игроков комнаты
    def get_players(self):
        return self.players

    # Изменить статус комнаты
    def set_status(self, status):
        self.room_status = status

    # Получить текущий статус комнаты
    def get_status(self):
        return self.room_status

    # Получить имя команты
    def get_name(self):
        return self.room_name

    # Получить id комнаты
    def get_id(self):
        return self.room_status

