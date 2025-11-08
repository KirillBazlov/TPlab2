class Logger:
    # Приватное статическое поле для хранения единственного экземпляра
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
