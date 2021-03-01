#file picker code adapted from https://sinestesia.co/blog/tutorials/using-blenders-filebrowser-with-python/

import bpy
import os

from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator


class OT_TestOpenFilebrowser(Operator, ImportHelper):

    bl_idname = "test.open_filebrowser"
    bl_label = "Open Template File"
    
    filter_glob: StringProperty(
        default='*.blend',
        options={'HIDDEN'}
    )
    
    some_boolean: BoolProperty(
        name='Do a thing',
        description='Do a thing with the file you\'ve selected',
        default=True,
    )

    def execute(self, context):
        """Do something with the selected file(s)."""

        #Clean material list
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.material_slot_remove_unused()
        
        #import all material templates
        filepath = self.filepath
        innerpath = 'Material'
        templateList = ['Template Body', 'Template Body Outline', 'Template Eye (hitomi)', 'Template Eyebrows (mayuge)', 'Template Eyeline down', 'Template Eyeline up', 'Template Eyewhites (sirome)', 'Template Face', 'Template General', 'Template Hair', 'Template Mixed Metal or Shiny', 'Template Nose', 'Template Shadowcast (Standard)', 'Template Teeth (tooth)']

        for template in templateList:
            bpy.ops.wm.append(
                filepath=os.path.join(filepath, innerpath, template),
                directory=os.path.join(filepath, innerpath),
                filename=template,
                #set_fake=True
                )
        
        #Replace all materials on the body with templates
        body = bpy.data.objects['Body']
        def bodySwap(original, template):
            try:
                body.material_slots[original].material = bpy.data.materials[template]
            except:
                print('material or template wasn\'t found: ' + original + ' / ' + template)

        bodySwap('cf_m_face_00','Template Face')
        bodySwap('cf_m_mayuge_00','Template Eyebrows (mayuge)')
        bodySwap('cf_m_noseline_00','Template Nose')
        bodySwap('cf_m_eyeline_00_up','Template Eyeline up')
        bodySwap('cf_m_eyeline_down','Template Eyeline down')
        bodySwap('cf_m_sirome_00','Template Eyewhites (sirome)')
        bodySwap('cf_m_sirome_00.001','Template Eyewhites (sirome)')
        bodySwap('cf_m_hitomi_00','Template Eye (hitomi)')
        bodySwap('cf_m_hitomi_00.001','Template Eye (hitomi)')
        bodySwap('cf_m_body','Template Body')
        bodySwap('cf_m_tooth','Template Teeth (tooth)')
        bodySwap('cf_m_tang','Template General')
        
        #Replace all of the Hair materials with hair templates and name accordingly
        hair = bpy.data.objects['Hair']
        for original in hair.material_slots:
            template = bpy.data.materials['Template Hair'].copy()
            template.name = 'Template ' + original.name
            original.material = bpy.data.materials[template.name]
        
        #Replace all other materials with the general template and name accordingly
        for ob in bpy.context.view_layer.objects:
            if ob.type == 'MESH' and ('Body' not in ob.name and 'Hair' not in ob.name):
                for original in ob.material_slots:
                    template = bpy.data.materials['Template General'].copy()
                    template.name = 'Template ' + original.name
                    original.material = bpy.data.materials[template.name]
        
        # Get rid of the duplicate node groups cause there's a lot
        def eliminate(node):
            node_groups = bpy.data.node_groups

            # Get the node group name as 3-tuple (base, separator, extension)
            (base, sep, ext) = node.node_tree.name.rpartition('.')

            # Replace the numeric duplicate
            if ext.isnumeric():
                if base in node_groups:
                    print("  Replace '%s' with '%s'" % (node.node_tree.name, base))
                    node.node_tree.use_fake_user = False
                    node.node_tree = node_groups.get(base)
                            
        #stolen from somwhere
        print("\nEliminate Node Group Duplicates:")

        #--- Search for duplicates in actual node groups
        node_groups = bpy.data.node_groups

        for group in node_groups:
            for node in group.nodes:
                if node.type == 'GROUP':
                    eliminate(node)

        #--- Search for duplicates in materials
        mats = list(bpy.data.materials)
        worlds = list(bpy.data.worlds)

        for mat in mats + worlds:
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'GROUP':
                        eliminate(node)

        return {'FINISHED'}

if __name__ == "__main__":
    bpy.utils.register_class(OT_TestOpenFilebrowser)

    # test call
    print((bpy.ops.test.open_filebrowser('INVOKE_DEFAULT')))
    