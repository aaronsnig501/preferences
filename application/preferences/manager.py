from application.preferences.models import Preferences
from application.preferences.validators import PreferencesRequestBody


class PreferencesManager:
    async def set_preferences(self, preferences_body: PreferencesRequestBody) -> None:
        """Set preferences

        Save the preferences

        Args:
            preferences_body (PreferencesRequestBody): The preferences
        """
        preferences = Preferences(
            to_language=preferences_body.to_language,
            from_language=preferences_body.from_language,
            part_of_speech_tagger=preferences_body.part_of_speech_tagger,
            client_id=preferences_body.client_id
        )
        await preferences.save()
