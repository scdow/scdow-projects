import unittest
from Room import Room
from Player import Player
from Recipe import Recipe
from GameGUI import GameGUI
import tkinter as tk

class TestRoom(unittest.TestCase):
    # self.assertEqual(True, False)  # add assertion here
    def setUp(self):
        self.r1 = Room('room1')
        self.r2 = Room('room2')
        self.r3 = Room('room3')
    def tearDown(self):
        self.r1.exits.clear()
        self.r1.items.clear()
        self.r2.exits.clear()
        self.r2.items.clear()
        self.r3.exits.clear()
        self.r3.items.clear()
    def test_setExit_getExit_getExits(self):
        self.r1.setExit('east',self.r2)
        self.r1.setExit('north',self.r3)
        self.r2.setExit('west',self.r1)
        self.assertTrue(self.r3.setExit('south',self.r1))
        self.assertEqual(self.r1.getExit('east'),self.r2)
        self.assertEqual(self.r1.getExits(),['east','north'])
    def test_setItem_getItems(self):
        self.assertTrue(self.r1.setItem('item1'))
        self.assertTrue(self.r1.setItem('item2'))
        self.assertEqual(self.r1.getItems(),['item1','item2'])
    def test_removeItem_addItem(self):
        self.assertTrue(self.r1.addItem('item3'))
        self.assertTrue(self.r1.addItem('item4'))
        self.assertEqual(self.r1.getItems(),['item3','item4'])
        self.assertTrue(self.r1.removeItem('item3'))
        self.assertEqual(self.r1.getItems(),['item4'])

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.p1 = Player()
    def tearDown(self):
        self.p1.backpack.clear()
        self.p1.recipe.clear()
    def test_pickItem_dropItem(self):
        self.assertTrue(self.p1.pickItem('item1'))
        self.assertTrue(self.p1.pickItem('item2'))
        self.assertTrue(self.p1.pickItem('item3'))
        self.assertEqual(self.p1.backpack,['item1','item2','item3'])
        self.assertTrue(self.p1.dropItem('item2'))
        self.assertEqual(self.p1.backpack,['item1','item3'])
        self.assertTrue(self.p1.dropItem('item3'))
        self.assertEqual(self.p1.backpack, ['item1'])
    def test_checkPackSize(self):
        self.p1.pickItem('item1')
        self.p1.pickItem('item2')
        self.p1.pickItem('item3')
        self.assertTrue(self.p1.checkPackSize())
        self.p1.pickItem('item4')
        self.p1.pickItem('item5')
        self.p1.pickItem('item6')
        self.p1.pickItem('item7')
        self.assertFalse(self.p1.checkPackSize())

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.r1 = Recipe()
    def tearDown(self):
        self.r1.recipes.clear()
    def test_setRecipe(self):
        self.r1.setRecipe(('m1','m2','m3'),'r1','r1 description')
        self.assertTrue(self.r1.recipes == {('m1','m2','m3'):('r1','r1 description')})
    def test_getAllMaterials(self):
        self.r1.setRecipe(('m1','m2','m3'),'r1','r1 description')
        self.r1.setRecipe(('m4',),'r2','r2 description')
        self.r1.setRecipe(('m5','m6','m7','m8','m9'),'r3','r3 description')
        self.assertTrue(list(self.r1.getAllMaterials()) == [('m1','m2','m3'),('m4',),('m5','m6','m7','m8','m9')])
    def test_getProduct(self):
        self.r1.setRecipe(('m1', 'm2', 'm3'), 'r1', 'r1 description')
        self.r1.setRecipe(('m4',), 'r2', 'r2 description')
        self.assertEqual(self.r1.getProduct(('m4',)),('r2','r2 description'))

class TestGameGUI(unittest.TestCase):
    def setUp(self):
        win = tk.Tk()  # Create a window
        self.g1 = GameGUI(win)
    def tearDown(self):
        del(self.g1)
    def test_doGo(self):
        self.g1.game.currentRoom=self.g1.game.tunnel
        self.g1.doGo('down')
        self.assertTrue(self.g1.game.currentRoom==self.g1.game.s1)
    def test_doPick(self):
        self.g1.doPick('m7',btn=tk.Button)
        self.assertTrue( self.g1.pickMsg == self.g1.game.doPickCommand(['m7']) )
    def test_doDrop(self):
        self.g1.doDrop('m7',btn=tk.Button)
        self.assertTrue( self.g1.dropMsg == self.g1.game.doDropCommand(['m7']) )

if __name__ == '__main__':
    unittest.main()
