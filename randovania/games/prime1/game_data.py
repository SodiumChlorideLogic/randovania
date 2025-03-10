from randovania.games.game import GameData, GameGenerator, GameGui, GameLayout, GamePresetDescriber
from randovania.games.prime1.layout.prime_configuration import PrimeConfiguration
from randovania.games.prime1.layout.prime_cosmetic_patches import PrimeCosmeticPatches
from randovania.games.prime1.generator.item_pool.pool_creator import prime1_specific_pool
from randovania.games.prime1.patcher.randomprime_patcher import RandomprimePatcher
from randovania.games.prime1.layout.preset_describer import prime_expected_items, prime_unexpected_items, prime_format_params


def _prime_gui():
    from randovania.games.prime1.gui.preset_settings import prime1_preset_tabs
    from randovania.games.prime1.gui.dialog.prime_cosmetic_patches_dialog import PrimeCosmeticPatchesDialog

    return GameGui(
        tab_provider=prime1_preset_tabs,
        cosmetic_dialog=PrimeCosmeticPatchesDialog,
    )


game_data: GameData = GameData(
    short_name="Prime",
    long_name="Metroid Prime",
    experimental=False,

    presets=[
        {
            "path": "starter_preset.rdvpreset"
        },
        {
            "path": "fewest_changes.rdvpreset"
        }
    ],

    layout=GameLayout(
        configuration=PrimeConfiguration,
        cosmetic_patches=PrimeCosmeticPatches,
        preset_describer=GamePresetDescriber(
            expected_items=prime_expected_items,
            unexpected_items=prime_unexpected_items,
            format_params=prime_format_params
        )
    ),

    gui=_prime_gui,

    generator=GameGenerator(
        item_pool_creator=prime1_specific_pool
    ),

    patcher=RandomprimePatcher()
)
