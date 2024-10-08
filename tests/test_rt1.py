import unittest
import time
from engine import Engine
from timer import Timer
from pulser import Pulser
from generic_test import gate_door_test, gate_dib_test
import logic
import logging

class RT1TestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.logic = [logic.rt1_search_timer, logic.rt1_preset_1, logic.rt1_preset_2, logic.rt1_preset_2_led, 
					logic.rt1_gate_closed_interlock, logic.rt1a_gate_closed_latch, logic.rt1b_gate_closed_latch, logic.rt1_all_gates_closed,logic.rt1_search_set, logic.rt1_search_led]
	
	def setUp(self):
		rt1_initial_state = logic.RSYState(
			RS1_SRCH_SET_LAT = False,
			RS1_SRCH_TMR_ACTV = False,
			RS1A_GT_CLS_ILCK = False,
			RS1_PR1_KSW_RT = False,
			RS1_PR1_TESTBTN_RT = False,
			PERMITTED_ACCESS = True,
			RS1_PR1_LED = False,
			RS1_PR1_LAT = False,
			RS1_PR2_KSW_RT = False,
			RS1_PR2_TESTBTN_RT = False,
			RS1_PR2_LAT = False,
			RS1_DIB_ACTIVE = False,
			RS1A_GT_CLS_RT = False,
			RS1_PR2_LED = False,
			ACR_HW_EN_RT = False,
			EPICS_ILCK_SET_BTN = False,
			RS1A_GT_CLS_LAT = False,
			RS1_SRCH_SET_KSW_RT = False,
			RS1_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS1_SRCH_SET_BTN = False,
			RS1_SRCH_SET_LED = False,

			RS2_406_PR1_KSW_RT = False,
			RS2_406_PR1_TESTBTN_RT = False,
			RS2_406_PR1_LAT = False,
			RS2_406_PR1_LED = False,
			RS2_406_PRSVD_SRCH = False,
			RS2_SRCH_TMR_ACTV = False,
			RS2_406_SDR_CLS_ILCK = False,
			RS2_406_WDR_CLS_RT = False,
			RS2_406_RUDR_CLS_RT = False,
			RS2_406_PR2_LAT = False,
			RS2_406_PR2_KSW_RT = False,
			RS2_406_PR2_TESTBTN_RT = False,
			RS2_406_DIB_ACTIVE = False,
			RS2_406_PR2_LED = False,
			RS2_406_SDR_CLS_RT = False,
			RS2_406_WDR_CLS_LAT = False,
			RS2_406_RUDR_CLS_LAT = False,
			RS2_406_ALL_DRS_CLS_LAT = False,
			RS2_406_PRSVD_SRCH_LED = False,

			RS2_407_PR1_LAT = False,
			RS2_407_PR1_KSW_RT = False,
			RS2_407_PR1_TESTBTN_RT = False,
			RS2_407_PRSVD_SRCH = False,
			RS2_406_SDR_CLS_LAT = False,
			RS2_407_SDR_CLS_ILCK = False,
			RS2_407_NDR_CLS_RT = False,
			RS2_407_EDR_CLS_RT = False,
			RS2_407_PR1_LED = False,
			RS2_407_PR2_LAT = False,
			RS2_407_PR2_KSW_RT = False,
			RS2_407_PR2_TESTBTN_RT = False,
			RS2_407_DIB_ACTIVE = False,
			RS2_407_PR2_LED = False,
			RS2_407_SDR_CLS_RT = False,
			RS2_407_NDR_CLS_LAT = False,
			RS2_407_SDR_CLS_LAT = False,
			RS2_407_EDR_CLS_LAT = False,
			RS2_407_ALL_DRS_CLS_LAT = False,
			RS2_407_PRSVD_SRCH_LED = False,

			RS2_PR1_LAT = False,
			RS2_PR1_KSW_RT = False,
			RS2_PR1_TESTBTN_RT = False,
			RS2_SRCH_SET_LAT = False,
			RS2A_GT_CLS_ILCK = False,
			RS2_PR1_LED = False,
			RS2_PR2_LAT = False,
			RS2_PR2_KSW_RT = False,
			RS2_PR2_TESTBTN_RT = False,
			RS2_DIB_ACTIVE = False,
			RS2_PR2_LED = False,
			RS2A_GT_CLS_RT = False,
			RS2A_GT_CLS_LAT = False,
			RS2_ALL_GTS_DRS_CLS_LAT = False,
			RS2_SRCH_SET_KSW_RT = False,
			RS2_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS2_SRCH_SET_BTN = False,
			RS2_SRCH_SET_LED = False,

			RS3_911_PR1_KSW_RT = False,
			RS3_911_PR1_TESTBTN_RT = False,
			RS3_911_PR1_LAT = False,
			RS3_911_PR1_LED = False,
			RS3_911_EDR_CLS_ILCK = False,
			RS3_911_PRSVD_SRCH_LAT = False,
			RS3_911_PR2_LAT = False,
			RS3_911_PR2_KSW_RT = False,
			RS3_911_PR2_TESTBTN_RT = False,
			RS3_911_PR2_LED = False,
			RS3_911_DIB_ACTIVE = False,
			RS3_911_EDR_CLS_RT = False,
			RS3_911_EDR_CLS_LAT = False,
			RS3_911_PRSVD_SRCH_LED = False,
			RS3_SRCH_TMR_ACTV = False,
			RS3_PR1_LAT = False,
			RS3_PR1_LED = False,
			RS3_PR1_KSW_RT = False,
			RS3_PR1_TESTBTN_RT = False,
			RS3_SRCH_SET_LAT = False,
			RS3A_GT_CLS_ILCK = False,
			RS3B_GT_CLS_RT = False,
			RS3C_GT_CLS_RT = False,
			RS3_PR2_LAT = False,
			RS3_PR2_LED = False,
			RS3_DIB_ACTIVE = False,
			RS3_PR2_KSW_RT = False,
			RS3_PR2_TESTBTN_RT = False,
			RS3A_GT_CLS_RT = False,
			RS3A_GT_CLS_LAT = False,
			RS3B_GT_CLS_LAT = False,
			RS3C_GT_CLS_LAT = False,
			RS3_ALL_GTS_CLS_LAT = False,
			RS3_SRCH_SET_KSW_RT = False,
			RS3_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS3_SRCH_SET_BTN = False,
			RS3_ALL_GTS_DRS_CLS_LAT = False,
			RS3_SRCH_SET_LED = False,

			RS4_912_PR1_KSW_RT = False,
			RS4_912_PR1_TESTBTN_RT = False,
			RS4_SRCH_TMR_ACTV = False,
			RS4_912_WDR_CLS_ILCK = False,
			RS4_912_PR1_LED = False,
			RS4_912_PR1_LAT = False,
			RS4_912_PR2_KSW_RT = False,
			RS4_912_PR2_TESTBTN_RT = False,
			RS4_912_PRSVD_SRCH_LAT = False,
			RS4_912_PR2_LAT = False,	
			RS4_PR1_LAT = False,
			RS4_PR1_KSW_RT = False,
			RS4_PR1_TESTBTN_RT = False,
			RS4_SRCH_SET_LAT = False,
			RS4_912_DIB_ACTIVE = False,
			RS4_912_PR2_LED = False,
			RS4_912_WDR_CLS_RT = False,
			RS4_912_WDR_CLS_LAT = False,
			RS4_912_PRSVD_SRCH_LED = False,			
			RS4A_GT_CLS_ILCK = False,
			RS4B_GT_CLS_RT = False,
			RS4C_GT_CLS_RT = False,
			RS4_DIB_ACTIVE = False,
			RS4_PR2_LAT = False,
			RS4_PR2_LED = False,
			RS4_PR2_KSW_RT = False,
			RS4_PR2_TESTBTN_RT = False,
			RS4A_GT_CLS_RT = False,
			RS4A_GT_CLS_LAT = False,
			RS4B_GT_CLS_LAT = False,
			RS4C_GT_CLS_LAT = False,
			RS4_ALL_GTS_CLS_LAT = False,
			RS4_SRCH_SET_KSW_RT = False,
			RS4_SRCH_SET_TESTBTN_RT = False,
			EPICS_RS4_SRCH_SET_BTN = False,
			RS4_ALL_GTS_DRS_CLS_LAT = False,
			RS4_SRCH_SET_LED = False,

			RS5_913_PR1_KSW_RT = False,
			RS5_913_PR1_TESTBTN_RT = False,
			RS5_913_PRSVD_SRCH_LAT = False,
			RS5_SRCH_TMR_ACTV = False,
			RS5_913_SDR_CLS_RT = False,
			RS5_913_SDR_CLS_LAT = False,
			RS5_913_WDR_CLS_ILCK = False,
			RS5_913_PR1_LED = False,
			RS5_913_PR1_LAT = False,
			RS5_913_PR2_KSW_RT = False,
			RS5_913_PR2_TESTBTN_RT = False,
			RS5_913_PR2_LAT = False,
			RS5_913_DIB_ACTIVE = False,
			RS5_913_PR2_LED = False,
			RS5_PR1_LAT = False,
			RS5_PR1_KSW_RT = False,
			RS5_SRCH_SET_LAT = False,
			RS5_913_WDR_CLS_RT = False,
			RS5_913_WDR_CLS_LAT = False,
			RS5_913_PRSVD_SRCH_LED = False,
			EPICS_RS5_SRCH_SET_BTN = False,
			RS5_PR1_TESTBTN_RT = False,
			RS5A_GT_CLS_ILCK = False,
			RS5B_GT_CLS_RT = False,
			RS5C_GT_CLS_RT = False,
			RS5DE_GT_CLS_RT = False,
			RS5_DIB_ACTIVE = False,
			RS5_PR2_LAT = False,
			RS5_PR2_LED = False,
			RS5_PR2_KSW_RT = False,
			RS5_PR2_TESTBTN_RT = False,
			RS5A_GT_CLS_RT = False,
			RS5A_GT_CLS_LAT = False,
			RS5B_GT_CLS_LAT = False,
			RS5C_GT_CLS_LAT = False,
			RS5DE_GT_CLS_LAT = False,
			RS5_ALL_GTS_CLS_LAT = False,
			RS5_SRCH_SET_KSW_RT = False,
			RS5_SRCH_SET_TESTBTN_RT = False,
			RS5_ALL_GTS_DRS_CLS_LAT = False,
			RS5_SRCH_SET_LED = False,
			RS5_913_ALL_DRS_CLS_LAT = False,

			RT1_PR1_KSW_RT = False,
			RT1_PR1_TESTBTN_RT = False,
			RT1_PR2_KSW_RT = False,
			RT1_PR2_TESTBTN_RT = False,
			RT1_SRCH_SET_KSW_RT = False,
			EPICS_RT1_SRCH_SET_BTN = False, 
			RT1_PR1_LED = False,
			RT1_PR2_LED = False,
			RT1_SRCH_SET_LED = False,
			RT1_PR1_LAT = False,
			RT1_SRCH_SET_LAT = False,
			RT1_SRCH_TMR_ACTV = False,
			RT1A_GT_CLS_ILCK = False,
			RT1B_GT_CLS_RT = False,
			RT1_PR2_LAT = False,
			RT1_DIB_ACTIVE = False,
			RT1A_GT_CLS_RT = False,
			RT1A_GT_CLS_LAT = False,
			RT1B_GT_CLS_LAT = False,
			RT1_ALL_GTS_CLS_LAT = False,

			KYBNK_N_REL_EPICS_BTN = False,
			KYBNK_N_REL = False,
			KYBNK_S_REL_EPICS_BTN = False,
			KYBNK_S_REL = False,
			KYBNK_N_COMPLETE_RT = False,
			KYBNK_N_CMPLT_LAT = False,
			KYBNK_S_COMPLETE_RT = False,
			KYBNK_S_CMPLT_LAT = False,
			ALL_KYBNK_CMPLT_LAT = False,
			RSY_ZN_CLS_LAT = False,
			ILCKS_CMPLT = False,
			RSY_SRCHD = False,
			RSY_SECURITY_VIOLATION = False,
			EPICS_NO_ACCESS_BTN = False,
			EPICS_PERMITTED_ACCESS_BTN = False,
			NO_ACCESS = False,
			AV_WARN_CMPLT = False,
			AV_WARN = False,
			RSY_SECURE = False,
		)
		timer_fast_forward_factor = 10
		rt1_timers = logic.RSYTimers(
			RS1_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS1_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS1_DIB_PULSER =  Pulser(1),
			RS1_SEARCH_LED_PULSER = Pulser(1),

			RS2_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS2_406_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS2_406_DIB_PULSER =  Pulser(1),
			RS2_406_SEARCH_LED_PULSER = Pulser(1),

			RS2_407_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS2_407_DIB_PULSER =  Pulser(1),
			RS2_407_SEARCH_LED_PULSER = Pulser(1),

			RS2_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS2_DIB_PULSER =  Pulser(1),
			RS2_SEARCH_LED_PULSER = Pulser(1),

			RS3_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS3_911_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS3_911_DIB_PULSER =  Pulser(1),
			RS3_911_SEARCH_LED_PULSER = Pulser(1),

			RS3_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS3_DIB_PULSER =  Pulser(1),
			RS3_SEARCH_LED_PULSER = Pulser(1),

			RS4_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS4_912_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS4_912_DIB_PULSER =  Pulser(1),
			RS4_912_SEARCH_LED_PULSER = Pulser(1),

			RS4_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS4_DIB_PULSER =  Pulser(1),
			RS4_SEARCH_LED_PULSER = Pulser(1),

			RS5_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RS5_913_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS5_913_DIB_PULSER =  Pulser(1),
			RS5_913_SEARCH_LED_PULSER = Pulser(1),

			RS5_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RS5_DIB_PULSER =  Pulser(1),
			RS5_SEARCH_LED_PULSER = Pulser(1),

			RT1_SRCH_TMR = Timer(10/timer_fast_forward_factor),
			RT1_DIB_TMR = Timer(15/timer_fast_forward_factor),
			RT1_DIB_PULSER =  Pulser(1),
			RT1_SEARCH_LED_PULSER = Pulser(1),

			AV_WARN_TMR = Timer(10/timer_fast_forward_factor),

		)
		self.engine = Engine(rt1_initial_state, self.logic, timers=rt1_timers)
		self.engine.process() #Do one round of initial processing.
	
	def test_01_gateA_rt1(self):
		gate_door_test(self, 'RT1A_GT_CLS_RT', 'RT1A_GT_CLS_LAT', 'RT1A Gate')
		gate_door_test(self, 'RT1B_GT_CLS_RT', 'RT1B_GT_CLS_LAT', 'RT1B Gate')

	def test_02_gate_rt1a_dib(self):
		gate_dib_test(self, gate_rt_name='RT1A_GT_CLS_RT', gate_interlock_name='RT1A_GT_CLS_ILCK', dib_timer_name='RT1_DIB_TMR', 
					dib_active_name='RT1_DIB_ACTIVE', preset_1_name='RT1_PR1_LAT', preset_2_led_name='RT1_PR2_LED', preset_2_ksw_name='RT1_PR2_KSW_RT', 
					gate_list=['RT1B_GT_CLS_RT'], zone_name='RT1')

	# def test_gate(self):
	# 	# Close gate
	# 	self.engine.state.RT1A_GT_CLS_RT = True
	# 	self.engine.process()
	# 	self.assertTrue(self.engine.state.RT1A_GT_CLS_RT, "RS1 Gate didn't stay closed.")
	# 	self.assertFalse(self.engine.state.RT1A_GT_CLS_LAT, "RS1 Gate latched without pressing interlock reset.")
		
	# 	# Latch
	# 	with self.engine.momentary_press(['EPICS_ILCK_SET_BTN']):
	# 		self.assertFalse(self.engine.state.RT1A_GT_CLS_LAT, "Gate latched without hardware enable.")
	# 		with self.engine.momentary_press(['ACR_HW_EN_RT']):
	# 			self.assertTrue(self.engine.state.RT1A_GT_CLS_LAT, "RS1 Gate not latched with harware enable and interlock reset held.")
	# 		self.assertTrue(self.engine.state.RT1A_GT_CLS_LAT, "RS1 Gate didn't stay latched after releasing hardware enable.")
	# 	self.assertTrue(self.engine.state.RT1A_GT_CLS_LAT, "RS1 Gate didn't stay latched after releasing interlock reset.")			
		
	# 	# Open again
	# 	self.engine.state.RT1A_GT_CLS_RT = False
	# 	self.engine.process()
	# 	self.assertFalse(self.engine.state.RT1A_GT_CLS_RT, "RS1 Gate didn't stay open.")
	# 	self.assertFalse(self.engine.state.RT1A_GT_CLS_LAT, "RS1 Gate remained latched after opening.")
	
	# def test_gate_dib(self):
	# 	self.assertFalse(self.engine.state.RT1A_GT_CLS_ILCK, "RT1 Gate interlock true without gate closed.")
	# 	# Close both RT1A and RT1B gates
	# 	self.engine.state.RT1A_GT_CLS_RT = True
	# 	self.engine.state.RT1B_GT_CLS_RT = True

	# 	self.engine.process()
	# 	self.assertTrue(self.engine.state.RT1A_GT_CLS_ILCK, "RT1 gate interlock not active in P/A with gate closed.")
	# 	self.engine.state.RT1_PR1_LAT = True
	# 	logging.debug("___________________", self.engine.state.RT1_PR1_LAT)
	# 	self.engine.process()

	# 	self.assertFalse(self.engine.timers.RT1_DIB_TMR.running(), "RT1 DIB timer running before turning RT1 PR2 Keyswitch.")
	# 	with self.engine.momentary_press("RT1_PR2_KSW_RT"):
	# 		self.assertTrue(self.engine.timers.RT1_DIB_TMR.running(), "RT1 DIB timer not running after turning RT1 PR2 Keyswitch.")
	# 	self.assertTrue(self.engine.timers.RT1_DIB_TMR.running(), "RT1 DIB timer not running after releasing RS1 PR2 Keyswitch.")
	# 	self.assertTrue(self.engine.state.RT1_DIB_ACTIVE, "RT1 DIB is not active while timer running.")
	# 	self.assertTrue(self.engine.state.RT1A_GT_CLS_ILCK, "RT1 Gate Closed Interlock is not True while RS1 DIB Active.")
	# 	self.engine.state.RT1A_GT_CLS_RT = False

	# 	self.engine.process()
	# 	self.assertTrue(self.engine.state.RT1A_GT_CLS_ILCK, "RT1 Gate Closed Interlock is not True with gate open and RS1 DIB Active.")
	# 	with self.subTest(msg="RT1 Preset 2 LED Tests"):
	# 		preset_2_led_values = []
	# 		while (time.time() - self.engine.timers.RT1_DIB_TMR.time_started()) < self.engine.timers.RT1_DIB_TMR.duration():
	# 			self.engine.process()
	# 			preset_2_led_values.append(self.engine.state.RT1_PR2_LED)
	# 			time.sleep(self.engine.timers.RS1_DIB_TMR.duration() / 10)
	# 		self.assertFalse(all(preset_2_led_values), "RT1 Preset 2 LED is not flashing (always on).")
	# 		self.assertFalse(not any(preset_2_led_values), "RT1 Preset 2 LED is not flashing (always off).")
	# 	# Leave the gate open and let the DIB expire.
	# 	self.engine.process()
	# 	self.assertFalse(self.engine.state.RT1A_GT_CLS_ILCK, "RT1 Gate Closed Interlock still True even after DIB timer expired.")
	
	def test_search_logic(self):
		# Searcher enters zone.
		self.engine.state.RT1A_GT_CLS_RT = True
		self.engine.state.RT1B_GT_CLS_RT = True
		self.engine.process()
		self.assertFalse(self.engine.state.RT1_SRCH_TMR_ACTV, "RS1 Search Timer active before turning PR1 key.")

		# Searcher turns preset 1 key.
		with self.engine.momentary_press("RT1_PR1_KSW_RT"):
			self.assertTrue(self.engine.state.RT1_SRCH_TMR_ACTV, "RT1 Search Timer didn't start after PR1 key turned.")
			self.assertTrue(self.engine.state.RT1_PR1_LAT, "RT1 PR1 did not latch after turning key.")
		self.assertTrue(self.engine.state.RT1_PR1_LAT, "RT1 PR1 didn't stay latched after releasing PR1 key.")
		
		# Attempt to get search reset now.
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_RT1_SRCH_SET_BTN"]):
			self.assertFalse(self.engine.state.RT1_SRCH_SET_LAT, "RT1 Search Set without both preset 2.")
		
		# Searcher turns preset 2 key.
		with self.engine.momentary_press("RT1_PR2_KSW_RT"):
			self.assertTrue(self.engine.state.RT1_PR2_LAT, "RT1 PR2 did not latch after turning key.")
		self.assertTrue(self.engine.state.RT1_PR2_LAT, "RT1 PR2 did not stay latched after releasing PR2 key.")
		
		# Searcher opens gate B to exit.
		self.engine.state.RT1A_GT_CLS_RT = False
		self.engine.process()
		time.sleep(self.engine.timers.RT1_DIB_TMR.duration()/5) #Take some non-zero amount of time to exit
		self.engine.state.RT1A_GT_CLS_RT = True #Close gate on the way out
		self.engine.process()
		
		# Get interlock reset to latch gate
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_ILCK_SET_BTN"]):
			pass
		
		# Get RT1 search set
		with self.engine.momentary_press(["ACR_HW_EN_RT", "EPICS_RT1_SRCH_SET_BTN"]):
			with self.engine.momentary_press("RT1_SRCH_SET_KSW_RT"):
				pass
		self.assertTrue(self.engine.state.RT1_SRCH_SET_LAT, "RT1 search not set with all conditions met.")