from dataclasses import dataclass


@dataclass
class PreferencesRequestBody:
    to_language: str
    from_language: str
    part_of_speech_tagger: str
    client_id: str
