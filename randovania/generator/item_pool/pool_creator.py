import typing
from typing import Tuple, Callable, Dict

from randovania.game_description import default_database
from randovania.game_description.resources.resource_database import ResourceDatabase
from randovania.game_description.resources.resource_info import add_resources_into_another
from randovania.generator.item_pool import PoolResults
from randovania.generator.item_pool.ammo import add_ammo
from randovania.generator.item_pool.major_items import add_major_items
from randovania.layout.base.base_configuration import BaseConfiguration


def _extend_pool_results(base_results: PoolResults, extension: PoolResults):
    base_results.pickups.extend(extension.pickups)
    base_results.assignment.update(extension.assignment)
    add_resources_into_another(base_results.initial_resources, extension.initial_resources)

def calculate_pool_results(layout_configuration: BaseConfiguration,
                           resource_database: ResourceDatabase,
                           ) -> PoolResults:
    """
    Creates a PoolResults with all starting items and pickups in fixed locations, as well as a list of
    pickups we should shuffle.
    :param layout_configuration:
    :param resource_database:
    :return:
    """
    base_results = PoolResults([], {}, {})

    # Adding major items to the pool
    _extend_pool_results(base_results, add_major_items(resource_database,
                                                       layout_configuration.major_items_configuration,
                                                       layout_configuration.ammo_configuration))

    # Adding ammo to the pool
    base_results.pickups.extend(add_ammo(resource_database,
                                         layout_configuration.ammo_configuration))

    layout_configuration.game.data.generator.item_pool_creator(base_results, layout_configuration, resource_database)

    return base_results


def calculate_pool_item_count(layout: BaseConfiguration) -> Tuple[int, int]:
    """
    Calculate how many pickups are needed for given layout, with how many spots are there.
    :param layout:
    :return:
    """
    game_description = default_database.game_description_for(layout.game)
    num_pickup_nodes = game_description.world_list.num_pickup_nodes

    pool_pickups, pool_assignment, _ = calculate_pool_results(layout, game_description.resource_database)
    min_starting_items = layout.major_items_configuration.minimum_random_starting_items

    pool_count = len(pool_pickups) + len(pool_assignment)
    maximum_size = num_pickup_nodes + min_starting_items

    return pool_count, maximum_size
