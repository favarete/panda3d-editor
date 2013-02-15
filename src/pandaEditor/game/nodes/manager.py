from constants import *


class Manager( object ):
    
    def __init__( self ):
        from sceneRoot import SceneRoot
        
        from nodePath import NodePath
        from render import Render
        from actor import Actor
        from pandaNode import PandaNode
        from collisionNode import CollisionNode
        from camera import Camera
        from baseCam import BaseCam
        from modelNode import ModelNode
        from baseCamera import BaseCamera
        from modelRoot import ModelRoot

        from light import Light
        from ambientLight import AmbientLight
        from pointLight import PointLight
        from directionalLight import DirectionalLight
        from spotlight import Spotlight
        
        from texture import Texture
        from textureStage import TextureStage
        
        from bulletWorld import BulletWorld
        from bulletDebugNode import BulletDebugNode
        from bulletRigidBodyNode import BulletRigidBodyNode
        from bulletBoxShape import BulletBoxShape
        
        self.nodeWrappers = {
            'SceneRoot':SceneRoot,
            
            'NodePath':NodePath,
            'Render':Render,
            'PandaNode':PandaNode,
            'Actor':Actor,
            'CollisionNode':CollisionNode,
            'Camera':Camera,
            'BaseCam':BaseCam,
            'ModelNode':ModelNode,
            'BaseCamera':BaseCamera,
            'ModelRoot':ModelRoot,
            
            'Light':Light,
            'AmbientLight':AmbientLight,
            'PointLight':PointLight,
            'DirectionalLight':DirectionalLight,
            'Spotlight':Spotlight,
            
            'Texture':Texture,
            'TextureStage':TextureStage,
            
            'BulletWorld':BulletWorld,
            'BulletDebugNode':BulletDebugNode,
            'BulletRigidBodyNode':BulletRigidBodyNode,
            'BulletBoxShape':BulletBoxShape
        }
        
        self.pyTagWrappers = {}
        
    def Create( self, nTypeStr, *args ):
        wrprCls = self.nodeWrappers[nTypeStr]
        wrpr = wrprCls()
        return wrpr.Create( *args )
    
    def Wrap( self, comp ):
        wrprCls = self.GetWrapper( comp )
        if wrprCls is not None:
            return wrprCls( comp )
        
        return None
        
    def GetWrapper( self, comp ):
        typeStr = self.GetTypeString( comp )
        if typeStr in self.nodeWrappers:
            return self.nodeWrappers[typeStr]
        
        return None
    
    def GetWrapperByName( self, cType ):
        if cType in self.nodeWrappers:
            return self.nodeWrappers[cType]
        elif cType in self.pyTagWrappers:
            return self.pyTagWrappers[cType]
        
        return None
        
    def GetTypeString( self, comp ):
        """Return the type of the component as a string."""
        typeStr = type( comp ).__name__
        if typeStr == 'NodePath':
            typeStr = comp.node().getTag( TAG_NODE_TYPE )
            if not typeStr:
                typeStr = type( comp.node() ).__name__
        elif comp is base.scene:
            typeStr = 'SceneRoot'
        
        return typeStr