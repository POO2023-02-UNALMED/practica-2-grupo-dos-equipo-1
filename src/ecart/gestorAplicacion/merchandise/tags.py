from enum import Enum


class Tag(Enum):
    ALIMENTOS = "🍎"
    HOGAR = "🏡"
    LIMPIEZA = "🧹"
    ELECTRODOMESTICOS = "📺"
    JUGUETES = "🎠"

    @classmethod
    def get_tag_list(cls):
        return [tag.value for tag in cls]

    @classmethod
    def get_entry_for_tag(cls, tag_value):
        for tag in cls:
            if tag.value == tag_value:
                return tag
        return None  # Return None if the tag is not found in the enum
