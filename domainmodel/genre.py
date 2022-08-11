class Genre:
    def __init__(self, genre_id: int, genre_name: str):
        if not isinstance(genre_id, int) or genre_id < 0:
            raise ValueError
        else:
           self.__genre_id: int = genre_id
        self.__name: str = None
        if isinstance(genre_name, str):
            self.__name = genre_name.rstrip(' ')
            self.__name = self.__name.lstrip(' ')

    @property
    def genre_id(self) -> int:
        return self.__genre_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_full_name):
        if isinstance(new_full_name, str):
            self.__name = new_full_name.rstrip(' ')
            self.__name = self.__name.lstrip(' ')
        else:
            self.__name = None

    def __repr__(self):
        # we use access via the property here
        return f"<Genre {self.__name}, genre id = {self.__genre_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__genre_id == other.genre_id

    def __lt__(self, other):
        return self.__genre_id < other.genre_id

    def __hash__(self):
        return hash(self.__genre_id)
