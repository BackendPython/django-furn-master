import pkg_resources
import random

_wordlists = {}

def _load_wordlist(list_reference, filename):
	global _wordlists
	unparsed_list = pkg_resources.resource_string(__name__, filename)
	_wordlists[list_reference] = unparsed_list.decode().replace("\r\n","\n").strip().split('\n')

def _load_wordlists():
	_load_wordlist("insulting_adjectives", "wordlists/insulting_adjectives.txt")
	_load_wordlist("nouns", "wordlists/nouns.txt")
	_load_wordlist("past_tense_verbs", "wordlists/past_tense_verbs.txt")

def _get_random_word(list):
	return random.choice(_wordlists[list])

def get_insulting_adjective():
	return _get_random_word("insulting_adjectives")
def get_noun():
	return _get_random_word("nouns")
def get_past_tense_verb():
	return _get_random_word("past_tense_verbs")

_load_wordlists()
