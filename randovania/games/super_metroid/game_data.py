from randovania.games.super_metroid.generator.item_pool.pool_creator import super_metroid_specific_pool
from randovania.games.super_metroid.layout.super_metroid_configuration import SuperMetroidConfiguration
from randovania.games.super_metroid.layout.super_metroid_cosmetic_patches import SuperMetroidCosmeticPatches
from randovania.games.game import GameData, GameGenerator, GameGui, GameLayout
from randovania.games.super_metroid.patcher.super_duper_metroid_patcher import SuperDuperMetroidPatcher


def _super_metroid_gui():
    from randovania.games.super_metroid.gui.preset_settings import super_metroid_preset_tabs
    from randovania.gui.dialog.base_cosmetic_patches_dialog import BaseCosmeticPatchesDialog

    return GameGui(
        tab_provider=super_metroid_preset_tabs,
        cosmetic_dialog=BaseCosmeticPatchesDialog,
    )


game_data: GameData = GameData(
    short_name="SM",
    long_name="Super Metroid",
    experimental=True,

    presets=[
        {
            "path": "starter_preset.rdvpreset"
        }
    ],

    layout=GameLayout(
        configuration=SuperMetroidConfiguration,
        cosmetic_patches=SuperMetroidCosmeticPatches
    ),

    gui=_super_metroid_gui,

    generator=GameGenerator(
        item_pool_creator=super_metroid_specific_pool
    ),

    patcher=SuperDuperMetroidPatcher()
)
