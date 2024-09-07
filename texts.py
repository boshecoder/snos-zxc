import random

def get(user, link):
	ran = random.randint(1, 2)
	if ran == 1 and link != "None":
		return f"Hello dear support, this user - {user} is engaged in spam, doxing and illegal activities. Link to violation: {link}. We would be glad if he is blocked on the platform"
	else:
		return f"Hello dear support, this user - {user} is engaged in spam, doxing and illegal activities. We would be glad if he is blocked on the platform"
	if ran == 2 and link != "None":
		return f"Good day, a person ({user}) has appeared in Telegram who is engaged in spam and so-called deanon, a link to one of the violations: {link}. Please block him in Telegram"
	else:
		return f"Good day, a person ({user}) has appeared in Telegram who is engaged in spam and so-called deanon. Please block him in Telegram"