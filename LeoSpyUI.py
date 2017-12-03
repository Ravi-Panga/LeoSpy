# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LeoSpy", pos = wx.DefaultPosition, size = wx.Size( 920,538 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu2, u"File" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem4 )
		
		self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem5 )
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem6 )
		
		self.m_menubar1.Append( self.m_menu3, u"Edit" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap21, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_bpButton1 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-new-picture-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer1.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.m_bpButton2 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-edit-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer1.Add( self.m_bpButton2, 0, wx.ALL, 5 )
		
		self.m_bpButton3 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-rotate-left-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer1.Add( self.m_bpButton3, 0, wx.ALL, 5 )
		
		self.m_bpButton4 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-rotate-right-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer1.Add( self.m_bpButton4, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( gSizer1, 0, 0, 5 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_bpButton5 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-search-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer2.Add( self.m_bpButton5, 0, wx.ALL, 5 )
		
		self.m_bpButton6 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-crop-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer2.Add( self.m_bpButton6, 0, wx.ALL, 5 )
		
		self.m_bpButton7 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-refresh-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer2.Add( self.m_bpButton7, 0, wx.ALL, 5 )
		
		self.m_bpButton8 = wx.BitmapButton( self.m_panel1, wx.ID_ANY, wx.Bitmap( u"ai-save-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer2.Add( self.m_bpButton8, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( gSizer2, 0, 0, 5 )
		
		
		bSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Save as :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer11.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_radioBtn2 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Right Profile", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Left Profile", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer4, 0, 0, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_bitmap2, 1, wx.ALL|wx.ALIGN_BOTTOM|wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bitmap21.Bind( wx.EVT_LEFT_DOWN, self.someListener )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.onBrowse )
		self.m_bpButton5.Bind( wx.EVT_BUTTON, self.onZoom )
		self.m_bpButton6.Bind( wx.EVT_BUTTON, self.calculate )
		self.m_bpButton7.Bind( wx.EVT_BUTTON, self.compare )
		self.m_bpButton8.Bind( wx.EVT_BUTTON, self.save_cal )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def someListener( self, event ):
		event.Skip()
	
	def onBrowse( self, event ):
		event.Skip()
	
	def onZoom( self, event ):
		event.Skip()
	
	def calculate( self, event ):
		event.Skip()
	
	def compare( self, event ):
		event.Skip()
	
	def save_cal( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 716,471 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bpButton9 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"ai-crop-txt.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer7.Add( self.m_bpButton9, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7, 0, 0, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"SaveZoom", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem7 )
		
		self.m_menubar2.Append( self.m_menu3, u"File" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bpButton9.Bind( wx.EVT_BUTTON, self.OnSavePNG )
		self.Bind( wx.EVT_MENU, self.OnSavePNG, id = self.m_menuItem7.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSavePNG( self, event ):
		event.Skip()
	
	

