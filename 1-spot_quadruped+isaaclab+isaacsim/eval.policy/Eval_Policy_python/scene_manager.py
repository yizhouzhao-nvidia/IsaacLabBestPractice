# Scene Manager

import asyncio
import os
from pxr import Usd, UsdGeom, Gf, PhysicsSchemaTools

import omni.usd
from isaacsim.storage.native import get_assets_root_path_async
from isaacsim.core.utils.stage import add_reference_to_stage, create_new_stage_async, update_stage_async
from isaacsim.core.api import World
from isaacsim.core.prims import Articulation

class SceneManager:
    _my_world: World = None

    @staticmethod
    def new_scene():
        async def new_scene_async():
            World.clear_instance()
            await create_new_stage_async()
            await update_stage_async()
            stage = omni.usd.get_context().get_stage()
            # SceneManager._my_world = World(stage_units_in_meters=1.0, backend="torch")
            # await SceneManager._my_world.initialize_simulation_context_async()
            # SceneManager._my_world.scene.add_default_ground_plane()
            PhysicsSchemaTools.addGroundPlane(stage, "/World/groundPlane", "Z", 10, Gf.Vec3f(0, 0, 0), Gf.Vec3f(0.5))

        asyncio.ensure_future(new_scene_async())
            
    @staticmethod
    def save_scene(scene_path):
        pass
    
    @staticmethod
    def add_robot(robot_path = "/Isaac/Robots/BostonDynamics/spot/spot.usd"):
        async def add_robot_async():
            asset_root = await get_assets_root_path_async()
            asset_path = asset_root + robot_path
            print("asset_path: ", asset_path)
            add_reference_to_stage(usd_path=asset_path, prim_path="/World/Spot")
            stage = omni.usd.get_context().get_stage()
            spot_prim = stage.GetPrimAtPath("/World/Spot")
            spot_prim.GetAttribute("xformOp:translate").Set(Gf.Vec3d(0, 0, 0.7))
            # robot_view = Articulation(
            #     prim_paths_expr="/World/Spot",
            #     name="spot_view",
            #     positions=[0, 0, 0],
            # )
            # SceneManager._my_world.scene.add(robot_view)
            # await SceneManager._my_world.reset_async()
        asyncio.ensure_future(add_robot_async())

    @staticmethod
    def remove_robot(robot_path):
        pass
    