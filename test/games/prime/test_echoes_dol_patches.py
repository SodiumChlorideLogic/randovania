import pytest

from randovania.dol_patching.dol_file import DolHeader, Section
from randovania.games.prime2.patcher import echoes_dol_patches, echoes_dol_versions
from randovania.games.prime2.patcher.echoes_dol_patches import StartingBeamVisorAddresses
from randovania.games.prime2.layout.echoes_user_preferences import EchoesUserPreferences

DOLS = [
    (DolHeader(sections=(Section(offset=256, base_address=2147496192, size=1344),
                         Section(offset=1600, base_address=2147498048, size=3808352),
                         Section(offset=3969024, base_address=2147491840, size=352),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=3809952, base_address=2147497536, size=288),
                         Section(offset=3810240, base_address=2147497824, size=224),
                         Section(offset=3810464, base_address=2151306400, size=512),
                         Section(offset=3810976, base_address=2151306912, size=32),
                         Section(offset=3811008, base_address=2151306944, size=46400),
                         Section(offset=3857408, base_address=2151353344, size=85536),
                         Section(offset=3942944, base_address=2151775616, size=4384),
                         Section(offset=3947328, base_address=2151785408, size=21696),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0)),
               bss_address=2151438880, bss_size=368356, entry_point=2147496588),
     echoes_dol_versions.ALL_VERSIONS[0]),
    (DolHeader(sections=(Section(offset=256, base_address=2147496192, size=1344),
                         Section(offset=1600, base_address=2147498048, size=3809312),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=3810912, base_address=2147497536, size=288),
                         Section(offset=3811200, base_address=2147497824, size=224),
                         Section(offset=3811424, base_address=2151307360, size=512),
                         Section(offset=3811936, base_address=2151307872, size=32),
                         Section(offset=3811968, base_address=2151307904, size=50432),
                         Section(offset=3862400, base_address=2151358336, size=85184),
                         Section(offset=3947584, base_address=2151780448, size=4384),
                         Section(offset=3951968, base_address=2151790272, size=21664),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0),
                         Section(offset=0, base_address=0, size=0)),
               bss_address=2151443520, bss_size=368548, entry_point=2147496588),
     echoes_dol_versions.ALL_VERSIONS[1]),
]


def test_apply_game_options_patch(dol_file):
    user_preferences = EchoesUserPreferences()
    offset = 0x2000

    # Run
    dol_file.set_editable(True)
    with dol_file:
        echoes_dol_patches.apply_game_options_patch(offset, user_preferences, dol_file)

    # Assert
    results = dol_file.dol_path.read_bytes()[0x100:]
    assert results == (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x93\xe1\x00\x1c\x7c\x7f\x1b\x78'
                       b'\x38\x61\x00\x08\x38\x00\x00\x01\x90\x1f\x00\x00\x38\x00\x00\x04\x90\x1f\x00\x04'
                       b'\x38\x00\x00\x00\x90\x1f\x00\x08\x38\x00\x00\x00\x90\x1f\x00\x0c\x38\x00\x00\x00'
                       b'\x90\x1f\x00\x10\x38\x00\x00\x69\x90\x1f\x00\x14\x38\x00\x00\x4f\x90\x1f\x00\x18'
                       b'\x38\x00\x00\xff\x90\x1f\x00\x1c\x38\x00\x00\xff\x90\x1f\x00\x20\x38\x00\x00\xa0'
                       b'\x98\x1f\x00\x24\x38\x00\x00\x00\x90\x1f\x00\x2c\x90\x1f\x00\x30\x90\x1f\x00\x34'
                       b'\x60\x00\x00\x00\x60\x00\x00\x00\x60\x00\x00\x00\x60\x00\x00\x00\x60\x00\x00\x00'
                       b'\x60\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       )


def test_apply_beam_cost_patch(dol_file, default_echoes_preset):
    patch_addresses = echoes_dol_patches.BeamCostAddresses(
        uncharged_cost=0x2000,
        charged_cost=0x2010,
        charge_combo_ammo_cost=0x2020,
        charge_combo_missile_cost=0x2030,
        get_beam_ammo_type_and_costs=0x2040,
        is_out_of_ammo_to_shoot=0x2100,
        gun_get_player=0x4000,
        get_item_amount=0x5000,
    )
    beam_configuration = default_echoes_preset.configuration.beam_configuration

    # Run
    dol_file.set_editable(True)
    with dol_file:
        echoes_dol_patches.apply_beam_cost_patch(patch_addresses, beam_configuration, dol_file)

    # Assert
    results = dol_file.dol_path.read_bytes()[0x100:]

    # print("")
    # for i in range(40):
    #     a = i * 20
    #     print("b'" + "".join([f"\\x{i:02x}" for i in results[a:a + 20]]) + "'")

    assert results == (b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00'
                       b'\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x1e'
                       b'\x00\x00\x00\x1e\x00\x00\x00\x1e\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x00\x05'
                       b'\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x81\x59\x07\x74\x55\x4a\x10\x3a\x7c\x03\x50\x2e'
                       b'\x90\x1d\x00\x00\x81\x59\x07\x74\x39\x4a\x00\x01\x7d\x49\x03\xa6\x42\x00\x00\x10'
                       b'\x38\x60\xff\xff\x39\x20\xff\xff\x48\x00\x00\x2c\x42\x00\x00\x10\x38\x60\x00\x2d'
                       b'\x39\x20\xff\xff\x48\x00\x00\x1c\x42\x00\x00\x10\x38\x60\x00\x2e\x39\x20\xff\xff'
                       b'\x48\x00\x00\x0c\x38\x60\x00\x2e\x39\x20\x00\x2d\x90\x7b\x00\x00\x91\x3c\x00\x00'
                       b'\x48\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x94\x21\xff\xf0'
                       b'\x7c\x08\x02\xa6\x90\x01\x00\x14\x93\xe1\x00\x0c\x93\xc1\x00\x08\x7c\x7e\x1b\x78'
                       b'\x48\x00\x1e\xe9\x83\xe3\x13\x14\x80\xbe\x07\x74\x38\xa5\x00\x01\x7c\xa9\x03\xa6'
                       b'\x42\x00\x00\x0c\x38\x60\x00\x00\x48\x00\x00\xc4\x42\x00\x00\x0c\x38\x80\x00\x2d'
                       b'\x48\x00\x00\x18\x42\x00\x00\x0c\x38\x80\x00\x2e\x48\x00\x00\x0c\x38\x80\x00\x2e'
                       b'\x48\x00\x00\x04\x7f\xe3\xfb\x78\x38\xa0\x00\x01\x48\x00\x2e\xa1\x3c\x80\x00\x00'
                       b'\x60\x84\x20\x00\x80\xbe\x07\x74\x54\xa5\x10\x3a\x7c\x84\x28\x2e\x7c\x03\x20\x00'
                       b'\x40\x80\x00\x0c\x38\x60\x00\x01\x48\x00\x00\x74\x80\xbe\x07\x74\x38\xa5\x00\x01'
                       b'\x7c\xa9\x03\xa6\x42\x00\x00\x0c\x38\x60\x00\x00\x48\x00\x00\x5c\x42\x00\x00\x0c'
                       b'\x38\x60\x00\x00\x48\x00\x00\x50\x42\x00\x00\x0c\x38\x60\x00\x00\x48\x00\x00\x44'
                       b'\x38\x80\x00\x2d\x48\x00\x00\x04\x7f\xe3\xfb\x78\x38\xa0\x00\x01\x48\x00\x2e\x39'
                       b'\x3c\x80\x00\x00\x60\x84\x20\x00\x80\xbe\x07\x74\x54\xa5\x10\x3a\x7c\x84\x28\x2e'
                       b'\x7c\x03\x20\x00\x40\x80\x00\x0c\x38\x60\x00\x01\x48\x00\x00\x0c\x38\x60\x00\x00'
                       b'\x48\x00\x00\x04\x80\x01\x00\x14\x83\xe1\x00\x0c\x83\xc1\x00\x08\x7c\x08\x03\xa6'
                       b'\x38\x21\x00\x10\x4e\x80\x00\x20'
                       )


_bytes_for_item = {
    "Combat Visor": b'\x00',
    "Echo Visor": b'\x01',
    "Dark Visor": b'\x03',
    "Power Beam": b'\x00',
    "Light Beam": b'\x02',
}


@pytest.mark.parametrize("starting_visor", ["Combat Visor", "Dark Visor", "Echo Visor"])
@pytest.mark.parametrize("starting_beam", ["Power Beam", "Light Beam"])
def test_apply_starting_visor_patch(dol_file, starting_beam, starting_visor):
    addresses = StartingBeamVisorAddresses(
        player_state_constructor_clean=0x1FB0,
        player_state_constructor_decode=0x20B0,
        health_info_constructor=0x5000,
        enter_morph_ball_state=0x20B0,
        start_transition_to_visor=0x6100,
        reset_visor=0x2100,
    )
    default_items = {
        "visor": starting_visor,
        "beam": starting_beam,
    }
    # Run
    dol_file.set_editable(True)
    with dol_file:
        echoes_dol_patches.apply_starting_visor_patch(addresses, default_items, dol_file)

    # Assert
    results = dol_file.dol_path.read_bytes()[0x100:]
    # print("")
    # for i in range(40):
    #     a = i * 20
    #     print("b'" + "".join([f"\\x{i:02x}" for i in results[a:a + 20]]) + "'")

    expected = (
        b'\x00\x00\x00\x00\x48\x00\x2f\xfd\x38\x00\x00{be}\x90\x1e\x00\x0c\x38\x00\x00{vi}'
        b'\x90\x1e\x00\x30\x90\x1e\x00\x34\x38\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x00{vi}'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x00{vi}\x90\x1e\x00\x30\x90\x1e\x00\x34'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x80\x00{vi}\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    ).replace(b"{vi}", _bytes_for_item[starting_visor]
              ).replace(b"{be}", _bytes_for_item[starting_beam])

    assert results == expected


def test_apply_safe_zone_heal_patch(dol_file, echoes_game_description):
    addresses = echoes_dol_patches.SafeZoneAddresses(
        heal_per_frame_constant=0x2000,
        increment_health_fmr=0x2030,
    )
    sda2_base = 0x10B0

    # Run
    dol_file.set_editable(True)
    with dol_file:
        echoes_dol_patches.apply_safe_zone_heal_patch(addresses, sda2_base, 1.0,
                                                      dol_file)

    # Assert
    results = dol_file.dol_path.read_bytes()[0x100:]
    expected = (b'\x3c\x88\x88\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x22\x0f\x50\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                )

    assert results == expected


@pytest.mark.parametrize(["header", "version"], DOLS)
def test_apply_fixes(dol_file, header, version):
    dol_file.header = header

    # Run
    dol_file.set_editable(True)
    with dol_file:
        echoes_dol_patches.apply_fixes(version, dol_file)


@pytest.mark.parametrize(["header", "version"], DOLS)
@pytest.mark.parametrize("enabled", [False, True])
def test_apply_unvisited_room_names(dol_file, header, version, enabled):
    dol_file.header = header

    # Run
    dol_file.set_editable(True)
    with dol_file:
        echoes_dol_patches.apply_unvisited_room_names(version, dol_file, enabled)


@pytest.mark.parametrize(["header", "version"], DOLS)
@pytest.mark.parametrize("enabled", [False, True])
def test_apply_teleporter_sounds(dol_file, header, version, enabled):
    dol_file.header = header

    # Run
    dol_file.set_editable(True)
    with dol_file:
        echoes_dol_patches.apply_teleporter_sounds(version, dol_file, enabled)
