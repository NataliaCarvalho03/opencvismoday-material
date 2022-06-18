import open3d as o3d
import numpy as np


def view_cloud(point_cloud):
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(point_cloud)
    ctr = vis.get_view_control()
    vis.run()
    vis.destroy_window()


def custom_draw_geometry_with_rotation(point_cloud):

    def rotate_view(vis):
        ctr = vis.get_view_control()
        ctr.rotate(10.0, 0.0)
        return False

    o3d.visualization.draw_geometries_with_animation_callback([point_cloud],
                                                              rotate_view)



def remove_outliers():
    pass

cloud = o3d.io.read_point_cloud("dados/room.pcd")
#print(type(cloud))
print(np.asarray(cloud.points))

#view_cloud(cloud)
voxel_rep = cloud.voxel_down_sample( voxel_size =0.30)
cloud.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([voxel_rep],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[5.0, 2.8, -1.18],
                                  up=[-0.0694, -0.9768, 0.2024])