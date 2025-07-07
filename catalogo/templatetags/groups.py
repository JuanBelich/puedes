from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    print(f"Checking if user {user.username} is in group {group_name}")
    return user.groups.filter(name=group_name).exists()