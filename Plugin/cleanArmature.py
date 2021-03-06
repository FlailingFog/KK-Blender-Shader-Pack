'''
AFTER CATS (CLEAN ARMATURE) SCRIPT
- Hides all bones that aren't in the bonelist
- Connects the finger bones that CATS sometimes misses for koikatsu imports
Usage:
- Make sure the Fix Model button has already been used in CATS
- Run the script
'''

import bpy

class clean_Armature(bpy.types.Operator):
    bl_idname = "kkb.cleanarmature"
    bl_label = "Clean armature"
    bl_description = "Makes the armature less of an eyesore"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):

        ########################
        import bpy
        
        #Select the armature and make it active
        bpy.ops.object.select_all(action='DESELECT')
        armature = bpy.data.objects['Armature']
        armature.hide = False
        armature.select_set(True)
        bpy.context.view_layer.objects.active=armature
        bpy.ops.object.mode_set(mode='POSE')
        
        #main bone list
        coreList = ['Cf_Pv_Knee_L', 'MiddleFinger1_L', 'LittleFinger3_R', 'Left ankle', 'Left wrist', 'AH1_R', 'Eyesx', 'Right knee', 'LittleFinger1_L', 'Right elbow', 'Cf_Pv_Foot_R', 'LittleFinger3_L', 'ToeTipIK_R', 'IndexFinger2_R', 'MiddleFinger2_L', 'IndexFinger1_L', 'Left arm', 'IndexFinger3_R', 'MiddleFinger2_R', 'MiddleFinger1_R', 'IndexFinger1_R', 'Right ankle', 'Thumb2_R', 'Cf_Pv_Elbo_L', 'Left leg', 'Cf_D_Siri_L', 'Spine', 'Sk_04_04', 'Sk_05_03', 'Kokan', 'Right leg', 'RingFinger3_L', 'MiddleFinger3_L', 'Sk_07_02', 'Neck', 'Thumb1_L', 'MiddleFinger3_R', 'RingFinger1_R', 'Thumb0_L', 'IndexFinger2_L', 'Thumb1_R', 'RingFinger2_R', 'Thumb0_R', 'Left elbow', 'IndexFinger3_L', 'Left shoulder', 'Cf_Pv_Hand_R', 'Right wrist', 'RingFinger3_R', 'Thumb2_L', 'Cf_Pv_Knee_R', 'Cf_Pv_Hand_L', 'Head', 'Left knee', 'Hips', 'Cf_Pv_Foot_L', 'LittleFinger1_R', 'LittleFinger2_L', 'RingFinger1_L', 'Cf_Pv_Elbo_R', 'LittleFinger2_R', 'ToeTipIK_L', 'Right shoulder', 'Right arm', 'Chest', 'Cf_D_Bust00', 'RingFinger2_L', 'AH1_L', 'Right toe', 'Left toe']
        
        #IK bone list
        nonIK = ['Left elbow', 'Right elbow', 'Left arm', 'Right arm', 'Left leg', 'Right leg', 'Left knee', 'Right knee', 'Right ankle', 'Left ankle']

        skirtList = ['Cf_D_Sk_00_00', 'Sk_00_00', 'Sk_00_01', 'Sk_00_02', 'Sk_00_03', 'Sk_00_04', 'Cf_D_Sk_01_00', 'Sk_01_00', 'Sk_01_01', 'Sk_01_02', 'Sk_01_03', 'Sk_01_04', 'Cf_D_Sk_02_00', 'Sk_02_00', 'Sk_02_01', 'Sk_02_02', 'Sk_02_03', 'Sk_02_04', 'Cf_D_Sk_03_00', 'Sk_03_00', 'Sk_03_01', 'Sk_03_02', 'Sk_03_03', 'Sk_03_04', 'Cf_D_Sk_04_00', 'Sk_04_00', 'Sk_04_01', 'Sk_04_02', 'Sk_04_03', 'Sk_04_04', 'Cf_D_Sk_05_00', 'Sk_05_00', 'Sk_05_01', 'Sk_05_02', 'Sk_05_03', 'Sk_05_04', 'Cf_D_Sk_06_00', 'Sk_06_00', 'Sk_06_01', 'Sk_06_02', 'Sk_06_03', 'Sk_06_04', 'Cf_D_Sk_07_00', 'Sk_07_00', 'Sk_07_01', 'Sk_07_02', 'Sk_07_03', 'Sk_07_04']
        
        faceList = ['Eye01_S_L', 'Eye01_S_R', 'Eye02_S_L', 'Eye02_S_R', 'Eye03_S_L', 'Eye03_S_R', 'Eye04_S_L', 'Eye04_S_R', 'Eye05_S_L', 'Eye05_S_R', 'Eye06_S_L', 'Eye06_S_R', 'Eye07_S_L', 'Eye07_S_R', 'Eye08_S_L', 'Eye08_S_R', 'Mayu_R', 'MayuMid_S_R', 'MayuTip_S_R', 'Mayu_L', 'MayuMid_S_L', 'MayuTip_S_L', 'Mouth_R', 'Mouth_L', 'Mouthup', 'MouthLow', 'MouthMove', 'MouthCavity']
        
        #joint correction bone lists
        #cf_j_ bones are merged into cf_s_ bones. cf_s_ bones have their prefix removed by CATS
        upperJointList = ['Elboback_L_Twist', 'Elboback_R_Twist', 'Forearm01_L_Twist', 'Forearm01_R_Twist', 'Shoulder_L_Twist', 'Shoulder_R_Twist', 'Shoulder02_L_Twist', 'Shoulder02_R_Twist', 'Wrist_L_Twist', 'Wrist_R_Twist', 'Cf_D_Wrist_L_Twist', 'Cf_D_Wrist_R_Twist', 'Cf_D_Hand_L_Twist', 'Cf_D_Hand_R_Twist', 'Elbo_L_Twist', 'Elbo_R_Twist', 'Arm01_R_Twist', 'Arm01_L_Twist', 'Cf_D_Arm01_L_Twist', 'Cf_D_Arm01_R_Twist']
        lowerJointList = ['KneeB_R_Twist', 'KneeB_L_Twist', 'Leg_L_Twist', 'Leg_R_Twist', 'Cf_D_Siri_L_Twist', 'Cf_D_Siri_R_Twist', 'Cf_D_Siri01_L_Twist', 'Cf_D_Siri01_R_Twist', 'Waist02_Twist', 'Waist02_Twist_001']

        allLayers = (True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False)
        layer2 =    (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
        layer17 =   (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
        layer18 =   (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
        layer19 =   (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False)

        for armature in [ob for ob in bpy.data.objects if ob.type == 'ARMATURE']:
            for bone in armature.data.bones:
                bone.hide=True
                if bone.name in coreList:
                    #Make core list bones visible on layer 1
                    bone.hide = False
                if bone.name in skirtList or bone.name in faceList:
                    #Make secondary bones visible on layer 2
                    bone.hide = False
                    bpy.ops.pose.select_all(action='DESELECT')
                    bone.select = True
                    bpy.ops.pose.bone_layers(layers=layer2)
                if bone.name in nonIK:
                    #Move bones that don't need to be visible for IK on layer 17
                    bone.hide = False
                    bpy.ops.pose.select_all(action='DESELECT')
                    bone.select = True
                    bpy.ops.pose.bone_layers(layers=layer17)                   
                if bone.name in upperJointList:
                    bone.hide = False
                    #select and move to layer 18
                    bpy.ops.pose.select_all(action='DESELECT')
                    bone.select = True
                    bpy.ops.pose.bone_layers(layers=layer18)
                if bone.name in lowerJointList:
                    bone.hide = False
                    #select and move to layer 19
                    bpy.ops.pose.select_all(action='DESELECT')
                    bone.select = True
                    bpy.ops.pose.bone_layers(layers=layer19)
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        #Make all bone layers visible for now
        bpy.ops.armature.armature_layers(layers=allLayers)
        bpy.context.object.data.display_type = 'STICK'
        
        # Make sure finger bones on the armature are visually connected (ignores A_N_ finger bones)
        bpy.ops.object.mode_set(mode='EDIT')

        armature.data.edit_bones['IndexFinger1_L'].tail = bpy.data.objects['Armature'].data.edit_bones['IndexFinger2_L'].head
        armature.data.edit_bones['MiddleFinger1_L'].tail = bpy.data.objects['Armature'].data.edit_bones['MiddleFinger2_L'].head
        armature.data.edit_bones['RingFinger1_L'].tail = bpy.data.objects['Armature'].data.edit_bones['RingFinger2_L'].head

        armature.data.edit_bones['IndexFinger1_R'].tail = bpy.data.objects['Armature'].data.edit_bones['IndexFinger2_R'].head
        armature.data.edit_bones['MiddleFinger1_R'].tail = bpy.data.objects['Armature'].data.edit_bones['MiddleFinger2_R'].head
        armature.data.edit_bones['RingFinger1_R'].tail = bpy.data.objects['Armature'].data.edit_bones['RingFinger2_R'].head

        bpy.ops.object.mode_set(mode='OBJECT')
                    
        return {'FINISHED'}


if __name__ == "__main__":
    bpy.utils.register_class(clean_Armature)

    # test call
    print((bpy.ops.kkb.cleanarmature('INVOKE_DEFAULT')))
