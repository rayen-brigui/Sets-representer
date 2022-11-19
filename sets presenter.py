from cProfile import label
import tkinter as tk

import wx
from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Program Math',size=(800,400))
        panel = wx.Panel(self)
       
        filemenu= wx.MenuBar()
        my_sizer = wx.BoxSizer(wx.VERTICAL) 
        self.SetLabel('set values pls')    
       
        self.text_ctrl = wx.TextCtrl(panel)
        self.text_ctrl2 = wx.TextCtrl(panel)
        self.text_ctrl3 = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 2, wx.ALL | wx.EXPAND, 25)   
        my_sizer.Add(self.text_ctrl2, 2, wx.ALL | wx.EXPAND, 25)   
        my_sizer.Add(self.text_ctrl3, 2, wx.ALL | wx.EXPAND, 25)   
         
           
        my_btn = wx.Button(panel, label='Enter')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 10)        
        panel.SetSizer(my_sizer)        
        self.Show()
    
   
    
    
    def on_press(self, event):
        def serialize(array):
             x = []
             for i in array:
                if (i ==' '):
                  print("test")
                else: x.append(i)
             print(x)
             return x
        value1 = self.text_ctrl.GetValue()
        value2 = self.text_ctrl2.GetValue()
        value3 = self.text_ctrl3.GetValue()
        if not value1:
            print("You didn't enter anything!")
           
        else:
            self.Close()
            fig =plt.figure(figsize=(10,10))
            set_a = set(str(value1))
            set_b = set(str(value2))
            set_c = set(str(value3))
            v=venn3((set_a,set_b,set_c),('A', 'B', 'C'))
            plt.title("Sets presentation")
           
            
            aInterb = [value for value in value1 if value in value2]
            bInterc = [value for value in value2 if value in value3]
            aInterc = [value for value in value1 if value in value3]
            inter = [value for value in aInterb if value in bInterc ]
            aInterb =serialize(aInterb)
            bInterc =serialize(bInterc)
            aInterc=serialize(aInterc)
            inter=serialize(inter)
            print(value1)
            print(value2)
            print(value3)
            
            v.get_label_by_id('100').set_text(str(value1))
            if (aInterb != []):
             v.get_label_by_id('110').set_text(aInterb)
            else: v.get_label_by_id('110').set_text("Ø")
            
            if (aInterc != []):
             v.get_label_by_id('101').set_text(aInterc)
            else: v.get_label_by_id('101').set_text("Ø")
            
            if (inter != []):
             v.get_label_by_id('111').set_text(inter)
            else: v.get_label_by_id('111').set_text("Ø")

            v.get_label_by_id('010').set_text(str(value2))
            if (bInterc != []):
             v.get_label_by_id('011').set_text(bInterc)
            else: v.get_label_by_id('011').set_text("Ø")

            v.get_label_by_id('001').set_text(str(value3))
            print('A ∩ B =' ,aInterb)
            print('B ∩ C = ', bInterc)
            print('A ∩ C = ',aInterc)
            fig
            plt.show()
            
    
    
    
            

if __name__ == '__main__':
    app = wx.App()
    frame =MyFrame()
    app.MainLoop()
    input() 
    

