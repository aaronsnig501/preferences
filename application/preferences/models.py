from tortoise import Model
from tortoise.fields import CharField, IntField


class Preferences(Model):

    id = IntField(primary_key=True)
    part_of_speech_tagger = CharField(max_length=15)
    to_language = CharField(max_length=5)
    from_language = CharField(max_length=5)
    client_id = CharField(max_length=50)

    def __str__(self) -> str:
        return (
            f"{self.id}: {self.part_of_speech_tagger}: "
            f"{self.from_language} -> {self.to_language}"
        )
