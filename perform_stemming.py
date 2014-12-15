from stemming import *

def perform_stemming(word):
	refined_word_step_1a = check_step_1a(word)
	refined_word_step_1b = check_step_1b(refined_word_step_1a)
	if STEP1B_EXT:
		refined_word_step_1b = check_step_1b_ext(refined_word_step_1b)
	refined_word_step_1c = check_step_1c(refined_word_step_1b)
	refined_word_step_2 = check_step2(refined_word_step_1c)
	refined_word_step_3 = check_step3(refined_word_step_2)
	refined_word_step_4 = check_step4(refined_word_step_3)
	refined_word_step_5a = check_step_5a(refined_word_step_4)
	refined_word_step_5b = check_step_5b(refined_word_step_5a)
	return refined_word_step_5b

"""
print perform_stemming("relational")
print perform_stemming("conditional")
print perform_stemming("education")

"""
