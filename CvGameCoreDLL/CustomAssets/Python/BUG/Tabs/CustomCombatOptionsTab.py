## CustomCombatOptionsTab
##
## Author: Freaky

import BugOptionsTab

class CustomCombatOptionsTab(BugOptionsTab.BugOptionsTab):
	"Custom Combat Options Screen Tab"
	
	def __init__(self, screen):
		BugOptionsTab.BugOptionsTab.__init__(self, "CustomCombat", "Custom Combat")

	def create(self, screen):
		tab = self.createTab(screen)
		panel = self.createMainPanel(screen)

		column = self.addOneColumnLayout(screen, panel)
		
		columnL, columnR = self.addTwoColumnLayout(screen, column, "Damage")

		self.addCheckbox(screen, columnL, "CustomCombat__Enabled")
		self.addSpacer(screen, columnR, "CombatDamage")
		self.addTextEdit(screen, columnL, columnR, "CustomCombat__MaxCombatRounds")
		self.addTextEdit(screen, columnL, columnR, "CustomCombat__DamageMultiplier")
		
		self.addCheckbox(screen, columnL, "CustomCombat__NoMetalRequirements")
		self.addSpacer(screen, columnR, "Metal")
		self.addTextEdit(screen, columnL, columnR, "CustomCombat__CopperCombatBonus")
		self.addTextEdit(screen, columnL, columnR, "CustomCombat__IronCombatBonus")
		
		self.addCheckbox(screen, columnL, "CustomCombat__UseMaxStackSize")
		self.addSpacer(screen, columnR, "MaxStackSize")
		self.addTextEdit(screen, columnL, columnR, "CustomCombat__MaxOpenStackSize")
		self.addTextEdit(screen, columnL, columnR, "CustomCombat__MaxCityStackSize")
