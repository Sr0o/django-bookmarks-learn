import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from actions.models import Action

def create_action(user, verb, target = None):
	now = timezone.now()
	last_time = now - datetime.timedelta(seconds = 60)
	similar_actions = Action.objects.filter(user_id = user.id, verb = verb, created__gte = last_time)
	# user_id = user.id 就是查该user的id的actions,似乎_表示该models下的属性的属性,__而这个是该models下的属性.
	if target:
		target_ct = ContentType.objects.get_for_model(target)
		similar_actions = similar_actions.filter(target_ct = target_ct, target_id = target.id)
	if not similar_actions:
		action = Action(user = user, verb = verb, target = target)
		action.save()
		return True
	return False
