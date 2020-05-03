class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):

	queue = []

	queue.append(group)

	while queue:
		current_group = queue.pop(0)

		for each_user in current_group.users:
			if each_user == user:
				return True

		for each_group in current_group.groups:
			queue.append(each_group)

	return False

print(is_user_in_group("sub_child_user", parent))